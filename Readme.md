# Resume Parser Application

This application is a resume parser built using Streamlit and Google Generative AI. It extracts key details from resumes in PDF format and presents them in a user-friendly interface.

## Table of Contents

## Live

[Live Demo](https://factorykaam.streamlit.app/)

## Features

- Upload PDF resumes to extract details such as:
  - Full Name
  - Contact Number
  - Email Address
  - Location
  - Skills (Technical & Non-Technical)
  - Education
  - Work Experience
  - Certifications
  - Languages Spoken
  - Social Links (LinkedIn, GitHub, LeetCode)

## Prerequisites

- Python 3.7 or higher
- Basic knowledge of using the command line

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   cd resume-parser-app

## Add your own API

I have used gemini to parse the resume. To run this project create a `.env` file and add your own API in this format:
`GOOGLE_API_KEY=<your API>`
