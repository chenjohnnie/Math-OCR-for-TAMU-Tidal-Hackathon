# Math-OCR-for-TAMU-Tidal-Hackathon

## Introduction
This project, developed for the TAMU Tidal Hackathon hosted on 11-11-23, harnesses the power of the Mathpix OCR API to convert images containing mathematical expressions and text into LaTeX and decimal formats. It's designed to assist in educational settings, allowing for the easy automated comparison of student and professor answers in LaTeX format.

## Features
- **OCR Conversion**: Converts images of mathematical expressions into LaTeX.
- **Decimal Conversion**: Transforms LaTeX expressions into decimal values.
- **Answer Comparison**: Compares student and professor answers for accuracy.
- **Text Recognition**: Extracts plain text from images for additional processing.

## How It Works
The tool uses the Mathpix OCR API to process images. Here's an overview of the functionality:
1. **Image to Base64 Conversion**: Images are converted to Base64 format for processing.
2. **OCR Processing**: The base64-encoded images are then processed through the Mathpix API to extract LaTeX or text.
3. **LaTeX to Decimal Conversion**: Extracted LaTeX expressions can be converted into decimal format.
4. **Answer Evaluation**: The tool compares LaTeX expressions from student and professor images to determine if they are sufficiently close.
5. **Text Extraction**: Extracts and returns text from images, useful for name recognition or other textual data.

## Requirements
To use this tool, you need:
- A Mathpix API key and App ID. Sign up at [Mathpix](https://mathpix.com/).
- Python environment with required libraries (`requests`, `json`, `base64`, `sympy`).

## Installation and Usage
1. **Clone the Repository**: `git clone [https://github.com/chenjohnnie/Math-OCR-for-TAMU-Tidal-Hackathon/]`.
2. **Install Dependencies**: `pip install requests sympy`.
3. **Set Up API Credentials**: Replace `MATHPIX_APP_ID` and `MATHPIX_APP_KEY` with your Mathpix credentials.
4. **Run the Script**: Use the provided functions in your Python environment to process images. Will need to create your own folder and script to handle batch images
