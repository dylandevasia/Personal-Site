# Theme & Design Guide

## Project Vision

This website serves as my professional portfolio and central hub for showcasing my experience, projects, and technical interests. The design emphasizes clarity, professionalism, and simplicity while remaining modern and visually engaging.

Rather than functioning as a résumé replacement, the website expands upon my experiences through detailed project case studies and highlights the engineering process behind my work.

---

# Design Principles

- Professional over flashy
- Content first
- Mobile responsive
- Fast loading
- Accessible
- Consistent spacing
- Minimal animations
- Easy navigation

Every section should have a clear purpose. Decorative elements should support the content rather than distract from it.

---

# Overall Style

The website follows a clean, scroll-based layout inspired by modern software engineering portfolios.

Avoid:

- Dashboard layouts
- Excessive whitespace
- Large gradients
- Glassmorphism
- Neon colors
- Overly animated components

Prioritize readability and strong typography.

---

# Color Palette

Primary Background
- White

Secondary Background
- Light Gray

Primary Text
- Slate / Charcoal

Accent Color
- Blue

Success
- Green

Warning
- Amber

Danger
- Red

Colors should primarily come from the DaisyUI theme.

---

# Typography

Primary Font

Inter

Fallback

sans-serif

Hierarchy

H1
Large, bold

H2
Section titles

H3
Project titles

Body
16–18px equivalent

Captions
Small uppercase labels

---

# Layout Philosophy

The website should tell a story from top to bottom.

Navigation

↓

Introduction

↓

Career Goals

↓

Technical Skills

↓

Featured Projects

↓

Contact

Avoid placing multiple unrelated sections side-by-side.

Vertical scrolling should feel natural.

---

# Components

Reusable components live inside

css/components/

Current components:

- navbar
- buttons
- cards
- badges
- footer
- timeline

Each component should be reusable across multiple pages.

---

# Icons

Icon Library

Lucide Icons

Use icons sparingly.

Examples:

- GitHub
- LinkedIn
- Email
- Download
- External Link
- Arrow Right

Avoid decorative icons that do not communicate information.

---

# Buttons

Primary

Filled accent button

Secondary

Outlined button

Text

Simple inline links

Buttons should have subtle hover animations.

---

# Cards

Project cards should be compact previews.

The homepage only contains summaries.

The Projects page contains complete engineering write-ups.

Cards should have:

- Title
- Description
- Technologies
- Read More button

---

# Badges

Use DaisyUI badge components.

Examples:

Python

AWS

C++

Java

Verilog

PyTorch

Docker

Git

PostgreSQL

Azure

Badges communicate technologies quickly without adding visual clutter.

---

# Animations

Animations should enhance—not distract.

Allowed:

- Fade-in on scroll
- Slight hover lift
- Smooth scrolling
- Button hover effects
- Card elevation

Avoid:

- Bounce animations
- Spinning elements
- Continuous movement
- Long transitions

---

# Images

Images should support the content.

Examples:

- Professional portrait
- Architecture diagrams
- Screenshots
- Hardware photos
- Simulation outputs

Avoid decorative stock photography.

---

# Navigation

Sticky navigation bar.

Pages:

- Home
- Projects
- Experience

External Links:

- Resume
- GitHub
- LinkedIn

The current page should always be visually highlighted.

---

# Homepage

Purpose

Introduce who I am in under 30 seconds.

Sections

1. Hero
2. Career Objectives
3. Technology Badges
4. Featured Projects
5. Contact

---

# Projects Page

Purpose

Provide detailed engineering case studies.

Each project should include:

- Overview
- Problem
- Solution
- Technologies
- Challenges
- Results
- Images
- GitHub (if public)

---

# Experience Page

Purpose

Expand upon my résumé.

Sections

- Professional Experience
- Research
- Education
- Skills
- Leadership
- Resume Download

---

# Code Style

Prefer semantic HTML.

Keep Tailwind classes readable.

Extract repeated styling into component CSS.

Avoid unnecessary JavaScript.

Favor maintainability over cleverness.

---

# Future Improvements

Potential additions:

- Dark mode
- Blog
- Project filtering
- Search
- Interactive project demos
- Animations using GSAP
- Visitor analytics
- Contact form backend

---

# Guiding Principle

Every design decision should answer one question:

**Does this make it easier for a recruiter to understand who I am and what I build?**

If the answer is no, it probably does not belong on the website.