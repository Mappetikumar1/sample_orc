from pathlib import Path
from PIL import Image
import pytesseract 

# Path to your folder (NOT a single image)
directory = Path("C:/Users/Kumar/OneDrive/Desktop/sample")

# Loop through all files in the folder
for file in directory.iterdir():
    if file.suffix.lower() in [".jpg", ".jpeg", ".png",".webp"]:   # check extension
        print(f"\n--- Text from {file.name} ---")
        print(pytesseract.image_to_string(Image.open(file)))
