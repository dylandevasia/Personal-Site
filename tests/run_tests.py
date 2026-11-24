#!/usr/bin/env python3

from pathlib import Path
import re
import sys


SITE_DIR = Path(".")


def require(condition: bool, message: str):
    if condition:
        print(f"[PASS] {message}")
    else:
        print(f"[FAIL] {message}")
        raise AssertionError(message)


def read_file(relative_path: str) -> str:
    path = SITE_DIR / relative_path

    require(
        path.exists(),
        f"{relative_path} exists",
    )

    return path.read_text(
        encoding="utf-8"
    )


# ==========================================================
# Deterministic Tests
# ==========================================================


def test_required_pages():

    required = [
        "index.html",
        "portfolio.html",
        "qualifications.html",
        "service.html",
        "genai.html",
    ]

    for page in required:

        require(
            (SITE_DIR / page).exists(),
            f"Required page '{page}' exists",
        )


def test_required_assets():

    assets = [
        "css/style1.css",
        "javascript/scripts.js",
        "resume/Dylan_Resume.pdf",
    ]

    for asset in assets:

        require(
            (SITE_DIR / asset).exists(),
            f"Required asset '{asset}' exists",
        )


def test_navigation():

    pages = [
        "index.html",
        "portfolio.html",
        "qualifications.html",
        "service.html",
        "genai.html",
    ]

    for page in pages:

        html = read_file(page)

        links = re.findall(
            r'href\s*=\s*["\']([^"\']+)["\']',
            html,
            flags=re.IGNORECASE,
        )

        for link in links:

            if (
                link.startswith("http")
                or link.startswith("#")
                or link.startswith("mailto:")
                or link.startswith("javascript:")
                or not link
            ):
                continue

            target = SITE_DIR / link

            require(
                target.exists(),
                f"{page} -> {link} exists",
            )


def test_css_links():

    for page in SITE_DIR.glob("*.html"):

        html = page.read_text(
            encoding="utf-8"
        )

        css_links = re.findall(
            r'<link[^>]*href\s*=\s*["\']([^"\']+)["\']',
            html,
            flags=re.IGNORECASE,
        )

        for css in css_links:

            if css.startswith("http"):

                continue

            require(
                (SITE_DIR / css).exists(),
                f"{page.name} references existing CSS '{css}'",
            )


def test_javascript_links():

    for page in SITE_DIR.glob("*.html"):

        html = page.read_text(
            encoding="utf-8"
        )

        scripts = re.findall(
            r'<script[^>]*src\s*=\s*["\']([^"\']+)["\']',
            html,
            flags=re.IGNORECASE,
        )

        for script in scripts:

            if script.startswith("http"):

                continue

            require(
                (SITE_DIR / script).exists(),
                f"{page.name} references existing JavaScript '{script}'",
            )


def test_image_assets():

    for page in SITE_DIR.glob("*.html"):

        html = page.read_text(
            encoding="utf-8"
        )

        images = re.findall(
            r'<img[^>]*src\s*=\s*["\']([^"\']+)["\']',
            html,
            flags=re.IGNORECASE,
        )

        for image in images:

            if (
                image.startswith("http")
                or image.startswith("data:")
            ):
                continue

            require(
                (SITE_DIR / image).exists(),
                f"{page.name} references existing image '{image}'",
            )


def test_page_titles():

    for page in SITE_DIR.glob("*.html"):

        html = page.read_text(
            encoding="utf-8"
        )

        require(
            "<title>" in html.lower(),
            f"{page.name} contains a title tag",
        )


def test_image_alt_text():

    for page in SITE_DIR.glob("*.html"):

        html = page.read_text(
            encoding="utf-8"
        )

        imgs = re.findall(
            r"<img[^>]*>",
            html,
            flags=re.IGNORECASE,
        )

        for img in imgs:

            require(
                re.search(
                    r'alt\s*=\s*["\'][^"\']+["\']',
                    img,
                    flags=re.IGNORECASE,
                ) is not None,
                f"{page.name} image contains alt text",
            )


# ==========================================================
# Main
# ==========================================================


def main():

    print("=" * 60)
    print("Running deterministic website tests...")
    print("=" * 60)

    test_required_pages()

    test_required_assets()

    test_navigation()

    test_css_links()

    test_javascript_links()

    test_image_assets()

    test_page_titles()

    test_image_alt_text()

    # ----------------------------------------------
    # Optional AI-generated tests
    # ----------------------------------------------

    try:

        from tests.ai_generated_tests import run_ai_tests

        print(
            "\nRunning AI-generated tests...\n"
        )

        run_ai_tests()

    except ImportError:

        print(
            "\nNo AI-generated tests found. Skipping."
        )

    print(
        "\nAll tests passed."
    )


if __name__ == "__main__":

    try:

        main()

    except Exception as exc:

        print(
            f"\nTEST FAILURE: {exc}"
        )

        sys.exit(1)