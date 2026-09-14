import os
from PIL import Image

image_files = ["Diego1.jpeg", "Diego3.jpeg", "Diego4.jpeg", "Diego6.JPG", "Diego7.jpeg"]
# Find them
paths = []
for root, dirs, files in os.walk("."):
    for f in files:
        if f in image_files:
            paths.append(os.path.join(root, f))

for path in paths:
    orig_size = os.path.getsize(path)
    if orig_size < 1_000_000:
        continue
    img = Image.open(path)
    # Convert to RGB if needed
    if img.mode != "RGB":
        img = img.convert("RGB")
    # Resize if extremely huge (e.g., width > 2000)
    if img.width > 2000:
        ratio = 2000 / img.width
        img = img.resize((2000, int(img.height * ratio)), Image.Resampling.LANCZOS)
    img.save(path, "JPEG", quality=75, optimize=True)
    new_size = os.path.getsize(path)
    print(f"Compressed {path}: {orig_size/1024/1024:.2f}MB -> {new_size/1024/1024:.2f}MB")
