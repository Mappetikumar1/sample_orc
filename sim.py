from pathlib import Path
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import traceback  # For error logging

# Path to your folder (can contain images + PDFs)
directory = Path(r"C:/Users/Kumar/OneDrive\Desktop\sample")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Common default path on Windows

print(f"Scanning directory: {directory.absolute()}")
print(f"Found files: {[f.name for f in directory.iterdir()]}")  # Debug: List all files

for file in directory.iterdir():
    try:
        ext = file.suffix.lower()
        print(f"\nProcessing file: {file.name} (extension: {ext})")

        # If it's an image
        if ext in [".jpg", ".jpeg", ".png", ".webp"]:
            print(f"--- Text from {file.name} ---")
            img = Image.open(file)
            text = pytesseract.image_to_string(img, lang="eng")
            print(text if text.strip() else "No text detected")

        # If it's a PDF
        elif ext == ".pdf":
            print(f"--- Text from {file.name} ---")
            pages = convert_from_path(file, 300, poppler_path=r"C:/Users/Kumar\Downloads/poppler/poppler-25.07.0/Library\bin")
            for i, page in enumerate(pages, start=1):
                text = pytesseract.image_to_string(page, lang="eng")
                print(f"\n(Page {i})")
                print(text if text.strip() else "No text detected")

        else:
            print(f"Skipping unsupported file: {file.name}")

    except Exception as e:
        print(f"Error processing {file.name}: {str(e)}")
        traceback.print_exc()  # Prints full error details