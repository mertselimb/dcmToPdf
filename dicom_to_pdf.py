import os
import pydicom
import numpy as np
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def merge_dicom_images_from_directory(directory):
    images = []
    for filename in sorted(os.listdir(directory)):
        if filename.lower().endswith('.dcm'):
            file_path = os.path.join(directory, filename)
            try:
                # Read the DICOM file
                dicom_data = pydicom.dcmread(file_path)
                # Convert DICOM data to a PIL image
                image_data = dicom_data.pixel_array
                # Normalize the pixel array (to ensure the data is in range [0, 255])
                if np.max(image_data) > 255:
                    image_data = (image_data / np.max(image_data)) * 255
                image_data = image_data.astype(np.uint8)

                # Convert to grayscale PIL image
                image = Image.fromarray(image_data)
                
                # Convert to RGB if necessary
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                
                images.append(image)
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")
    return images

def images_to_pdf(images, output_pdf_path):
    # Create a PDF file with ReportLab
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter
    for index, image in enumerate(images):
        # Scale image to fit PDF size
        img_width, img_height = image.size
        aspect = img_width / float(img_height)
        if img_width > width or img_height > height:
            if aspect > 1:
                # Landscape orientation
                img_width = width
                img_height = width / aspect
            else:
                # Portrait orientation
                img_height = height
                img_width = height * aspect
        image = image.resize((int(img_width), int(img_height)))
        temp_image_path = 'temp_image' + str(index) + '.jpg'
        image.save(temp_image_path)
        c.drawImage(temp_image_path, 0, 0, width, height)
        c.showPage()  # Create a new page in the PDF for each image
        os.remove(temp_image_path)  # Remove the temporary image file
    c.save()

def dicom_dir_to_pdf(dicom_directory, output_pdf_path):
    # Merge DICOM files from the directory
    merged_images = merge_dicom_images_from_directory(dicom_directory)
    if merged_images:
        # Convert merged images to a single PDF file
        images_to_pdf(merged_images, output_pdf_path)
        print(f"PDF created successfully at {output_pdf_path}")
    else:
        print("No valid DICOM images found in the directory.")

# Specify the directory containing DICOM files and the output PDF path
dicom_directory = 'data'
output_pdf_path = 'output.pdf'

# Convert DICOM directory to PDF
dicom_dir_to_pdf(dicom_directory, output_pdf_path)
