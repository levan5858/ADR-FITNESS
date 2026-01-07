#!/usr/bin/env python3
"""
Helper script to rename images in assets/images/ to andrei-1.jpg through andrei-50.jpg
Run this after you've downloaded images to the assets/images/ folder
"""

import os
import shutil
from pathlib import Path

images_dir = Path('assets/images')

if not images_dir.exists():
    print("❌ assets/images/ folder not found!")
    print("Create it first: mkdir -p assets/images")
    exit(1)

# Get all image files
image_files = []
for ext in ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']:
    image_files.extend(list(images_dir.glob(ext)))

# Filter out already renamed files
image_files = [f for f in image_files if not f.name.startswith('andrei-')]

if not image_files:
    print("✅ No images to rename (or all already renamed)")
    print(f"Found {len(list(images_dir.glob('andrei-*.jpg')))} already named images")
    exit(0)

print(f"Found {len(image_files)} images to rename")
print("Renaming to: andrei-1.jpg, andrei-2.jpg, etc.\n")

# Sort by modification time (newest first) or name
image_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)

# Rename them
for i, img_file in enumerate(image_files[:50], 1):  # Limit to 50
    new_name = images_dir / f"andrei-{i}.jpg"
    
    # If target exists, skip
    if new_name.exists():
        print(f"⚠️  {new_name.name} already exists, skipping {img_file.name}")
        continue
    
    # Rename (convert to jpg if needed)
    try:
        if img_file.suffix.lower() != '.jpg':
            # For non-jpg files, we'd need PIL to convert, so just rename extension
            shutil.move(str(img_file), str(new_name))
            print(f"✓ Renamed: {img_file.name} → {new_name.name}")
        else:
            shutil.move(str(img_file), str(new_name))
            print(f"✓ Renamed: {img_file.name} → {new_name.name}")
    except Exception as e:
        print(f"✗ Error renaming {img_file.name}: {e}")

print(f"\n✅ Done! Renamed {min(len(image_files), 50)} images")
print("Next step: git add assets/images/ && git commit -m 'Add images' && git push")
