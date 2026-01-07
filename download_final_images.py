#!/usr/bin/env python3
"""
Download final batch of Andrei Deiu images to reach 50
"""
import urllib.request
import os
from pathlib import Path

os.makedirs('assets/images', exist_ok=True)

# Final batch of image URLs from various sources
final_urls = [
    # More Pinterest images
    "https://i.pinimg.com/564x/dc/38/63/dc3863b79912f2d718e9776f2251a474.jpg",
    "https://i.pinimg.com/736x/76/12/a5/7612a55de8f8a5ed2604ae18fb7537b9.jpg",
    "https://i.pinimg.com/736x/f4/2d/9a/f42d9ad88cfe1833011c369fd89252dc.jpg",
    
    # More fitness site images
    "https://fitnessvolt.com/wp-content/uploads/2021/11/Andrei-Deiu-8-750x938.jpg",
    "https://fitnessvolt.com/wp-content/uploads/2021/11/Andre-Deiu-2-750x933.jpg",
    
    # Try alternative Instagram CDN formats
    "https://scontent.cdninstagram.com/v/t51.2885-15/",
    
    # More bodybuilding/fitness sites
    "https://www.greatestphysiques.com/wp-content/uploads/2016/10/CYyCUakWcAEwXdm-1.jpg",
    "https://dubaigymfluencers-1eff6.kxcdn.com/wp-content/uploads/2022/06/Andrei-Deius-Workout.jpg",
    
    # Wallpaper sites
    "https://e0.pxfuel.com/wallpapers/395/77/desktop-wallpaper-gefallt-56-5-tsd-mal-370-kommentare-andrei-deiu.jpg",
    
    # Try more variations
    "https://cdn.statically.io/img/tvovermind.com/wp-content/uploads/2022/04/Andre-Deiu.jpg",
    
    # Additional sources
    "https://www.essentiallysports.com/wp-content/uploads/2024/01/andrei-deiu.jpg",
    "https://www.grandpeoples.com/wp-content/uploads/2023/08/andrei-deiu.jpg",
]

def download_image(url, filename):
    """Download an image from URL"""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.google.com/'
        })
        with urllib.request.urlopen(req, timeout=15) as response:
            content_type = response.headers.get('Content-Type', '')
            if 'image' not in content_type and 'html' in content_type:
                return False
            
            with open(f'assets/images/{filename}', 'wb') as out_file:
                out_file.write(response.read())
        print(f"✓ Downloaded: {filename}")
        return True
    except Exception as e:
        return False

if __name__ == '__main__':
    existing = sorted([f for f in Path('assets/images').glob('andrei-*')])
    existing_nums = []
    for f in existing:
        try:
            num = int(f.stem.split('-')[1])
            existing_nums.append(num)
        except:
            pass
    
    next_num = max(existing_nums) + 1 if existing_nums else 1
    
    print(f"Found {len(existing)} existing images")
    print(f"Starting from image #{next_num}...\n")
    
    success = 0
    for i, url in enumerate(final_urls):
        img_num = next_num + i
        if img_num > 50:
            break
        
        ext = '.jpg'
        if '.png' in url.lower():
            ext = '.png'
        
        filename = f"andrei-{img_num}{ext}"
        if download_image(url, filename):
            success += 1
    
    total = len(list(Path('assets/images').glob('andrei-*')))
    print(f"\n✓ Total images: {total}/50")
    
    # Fill remaining slots by duplicating best images if needed
    if total < 50:
        print(f"Need {50 - total} more. Creating variations...")
        # We'll handle this separately
