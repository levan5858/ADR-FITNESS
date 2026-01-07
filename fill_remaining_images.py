#!/usr/bin/env python3
"""
Fill remaining image slots by copying best images to missing numbers
"""
import shutil
from pathlib import Path

images_dir = Path('assets/images')
existing = sorted([f for f in images_dir.glob('andrei-*')])

# Find missing numbers
all_nums = set(range(1, 51))
existing_nums = set()
for f in existing:
    try:
        num = int(f.stem.split('-')[1])
        existing_nums.add(num)
    except:
        pass

missing = sorted(all_nums - existing_nums)
print(f"Missing image numbers: {missing}")

if missing:
    # Get best quality images to duplicate
    best_images = sorted(existing, key=lambda x: x.stat().st_size, reverse=True)[:len(missing)]
    
    for i, missing_num in enumerate(missing):
        if i < len(best_images):
            source = best_images[i]
            ext = source.suffix
            dest = images_dir / f"andrei-{missing_num}{ext}"
            shutil.copy2(source, dest)
            print(f"✓ Created: {dest.name} (from {source.name})")

total = len(list(images_dir.glob('andrei-*')))
print(f"\n✓ Total images now: {total}/50")
