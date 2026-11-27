# Personal Portfolio Website

My personal portfolio website showcasing my experience, projects, technical skills, and resume. The site is built as a lightweight static website and deployed on AWS using a fully automated CI/CD pipeline.

**Live Website:** https://dylandevasia.info

---

## About

I'm **Dylan Devasia**, a Computer Engineering (EE-CS) student at **Texas A&M University** with interests in software engineering, machine learning, cloud infrastructure, embedded systems, and computer architecture. My experience includes internships at **Q2 Software** and **Schneider Electric**, hardware security research at Texas A&M, and several full-stack and systems projects.

This website serves as a central location for my:

- Resume
- Professional experience
- Technical projects
- Technical skills
- Volunteer work
- Contact information

---

## Features

- Responsive design for desktop and mobile
- Clean, modern single-theme interface
- Portfolio, Resume, Qualifications, and Service pages
- Downloadable resume
- Custom 404 page
- Automated AWS deployment
- Global content delivery with Amazon CloudFront
- HTTPS using AWS Certificate Manager
- Automated Python-based deployment validation tests
- Automatic CloudFront cache invalidation after successful deployments

---

## Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Cloud Infrastructure

- Amazon S3
- Amazon CloudFront
- AWS Certificate Manager
- AWS CodePipeline
- AWS CodeBuild
- IAM

### Testing

- Python
- Automated deployment verification

---

## CI/CD Pipeline

Every push to the `main` branch automatically triggers deployment.

```text
GitHub
   │
   ▼
CodePipeline
   │
   ▼
CodeBuild
   │
   ├── Run Python validation tests
   ├── Verify website structure
   ├── Validate HTML assets
   ├── Upload website to Amazon S3
   └── Create CloudFront invalidation
   │
   ▼
CloudFront
   │
   ▼
https://dylandevasia.info
```

The pipeline ensures that every deployment passes automated validation before publishing the latest version of the website. Once deployment completes, a CloudFront invalidation refreshes cached content so visitors immediately receive the newest version.

---

## Project Structure

```text
.
├── README.md
├── buildspec.yml
├── css
│   └── style1.css
├── images
│   ├── ...
│   └── portfolio images
├── javascript
│   └── scripts.js
├── resume
│   └── Dylan_Resume.pdf
├── tests
│   ├── __init__.py
│   └── run_tests.py
├── index.html
├── portfolio.html
├── qualifications.html
└── service.html
```

---

## Deployment

The production website is hosted using Amazon S3 and Amazon CloudFront.

Deployment workflow:

1. Push changes to the GitHub repository.
2. AWS CodePipeline detects the new commit.
3. AWS CodeBuild executes automated Python validation tests.
4. If all tests pass, the updated website is uploaded to Amazon S3.
5. A CloudFront invalidation clears cached files.
6. CloudFront distributes the latest version globally over HTTPS.

---

## About Me

I'm currently pursuing a **B.S. in Computer Engineering (EE-CS)** at **Texas A&M University** with a **3.94 GPA**. My experience includes:

- Software Engineering Intern at Q2 Software
- Hardware Security Research Assistant at Texas A&M
- R&D Engineering Intern at Schneider Electric
- Software Engineer (Machine Learning) at ArchivePicks

I'm interested in software engineering, cloud computing, embedded systems, machine learning, hardware security, and computer architecture.

---

## Selected Projects

- Personal Portfolio Website
- Restaurant POS System
- ARMv8 CPU Implementation
- Hardware Security Fuzzing Research

Additional project information is available throughout the portfolio website and in my resume.

---

## Contact

**Dylan Devasia**

Website: https://dylandevasia.info

Email: dylandevasia@gmail.com

LinkedIn: https://www.linkedin.com/in/dylan-devasia/

GitHub: https://github.com/dylandevasia

---

## License

This project is intended as a personal portfolio showcasing my professional experience and technical projects. The source code is available for educational purposes, but please do not copy personal content such as my resume, biography, project descriptions, or images without permission.