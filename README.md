
# DICOM to PDF Converter
This project provides a Python script to convert all DICOM (.dcm) files in a specified directory into a single PDF file. Each DICOM image will be added as a separate page in the PDF. This can be particularly useful for medical professionals and researchers who need to consolidate and share DICOM images in a more accessible format.

## Features

* Converts multiple DICOM images into a single PDF file.
* Handles grayscale DICOM images and converts them to RGB format for better compatibility.
* Automatically resizes images to fit within the PDF page.


## Requirements

Python 3.10

Virtual environment (optional but recommended)


## Setup Instructions


### Clone or Download the Repository

First, clone this repository or download the script files to your local machine.
```
git clone https://github.com/yourusername/dicom-to-pdf-converter.git
cd dicom-to-pdf-converter
```

### Create and Activate a Virtual Environment

Creating a virtual environment is recommended to manage dependencies in isolation:

Create a virtual environment:
```
python -m venv venv
```

Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```
On macOS/Linux:
```
source venv/bin/activate
```


### Install Required Packages

Install the necessary Python packages using pip:
```
pip install -r requirements.txt
```
## Prepare Your DICOM Files

Place your DICOM files (.dcm format) in the 'data' directory, which is inside the main project folder. If your DICOM files are stored in a different directory, update the dicom_directory variable in the script dicom_to_pdf.py:

Change 'data' to your directory path
```
dicom_directory = 'data'
```
## Run the Script

Run the script to convert DICOM files to a PDF:
```
python dicom_to_pdf.py
```
By default, the script will look for DICOM files in the 'data' directory and create an output.pdf file in the main folder.

## Output

The generated PDF file (output.pdf) will be created in the main project directory. Each page of the PDF will contain one DICOM image.

Script Details in dicom_to_pdf.py

### This script performs the following steps:

Reads DICOM Files: It reads all .dcm files from the specified directory (data).
Converts to PIL Images: Each DICOM file is converted into a PIL image, handling grayscale images by converting them to RGB.

Image Resizing: Images are resized to fit the standard letter-sized PDF pages while maintaining the aspect ratio.

Generates a PDF: All images are combined into a single PDF file with each image on a separate page.

requirements.txt
```
This file lists the necessary Python packages and their versions:
pydicom==2.4.1
Pillow==9.2.0
reportlab==3.6.12
numpy==1.21.2
```

## Troubleshooting

Empty Images in PDF: Ensure that your DICOM files contain valid pixel data. You can verify this by opening the DICOM files in a DICOM viewer.

Error Reading DICOM Files: Some DICOM files might be corrupted or lack image data. The script will skip these files and print a warning.

## Customization

Change Output Directory: Modify the output_pdf_path variable in dicom_to_pdf.py to change where the PDF is saved.

Change Page Size: Update the letter size in images_to_pdf function to use different page sizes, like A4.

## License
This project is open-source and free to use. Feel free to modify and distribute it as needed.