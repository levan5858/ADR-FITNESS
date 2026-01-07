#!/usr/bin/env python3
"""
Download additional Andrei Deiu images to reach 50 total
"""
import urllib.request
import os
from pathlib import Path

os.makedirs('assets/images', exist_ok=True)

# Additional publicly accessible image URLs
additional_urls = [
    # ProSupps official images
    "https://prosupps.com/cdn/shop/files/Andrei.png?v=1738774924",
    
    # Evogen Nutrition
    "https://www.evogennutrition.com/cdn/shop/articles/Evogen_Get3D-Smashing-FST-7--Chest-with-Andrei-_-Hany_1200x1200_68a2d261-70e0-4e08-8271-a0c9b96b55d3.jpg?v=1658950961&width=1024",
    
    # Fitness sites with direct image links
    "https://fitnessvolt.com/wp-content/uploads/2021/11/Andrei-Deiu-8-750x938.jpg",
    "https://fitnessvolt.com/wp-content/uploads/2021/11/Andre-Deiu-2-750x933.jpg",
    "https://boxlifemagazine.com/wp-content/uploads/2023/11/andrei-deiu.jpg",
    "https://sense4fitsummit.com/wp-content/uploads/2024/01/Andrei_Deiu.jpg.webp",
    "https://www.greatestphysiques.com/wp-content/uploads/2016/10/CYyCUakWcAEwXdm-1.jpg",
    "https://gymfluencers.com/wp-content/uploads/2023/08/Screenshot-2023-08-25-at-21.20.50.png",
    
    # Pinterest direct image URLs (from search results)
    "https://i.pinimg.com/736x/dc/38/63/dc3863b79912f2d718e9776f2251a474.jpg",
    "https://i.pinimg.com/736x/76/12/a5/7612a55de8f8a5ed2604ae18fb7537b9.jpg",
    "https://i.pinimg.com/736x/f4/2d/9a/f42d9ad88cfe1833011c369fd89252dc.jpg",
    
    # YouTube thumbnails (high quality)
    "https://i.ytimg.com/vi/fJxzmoggxiA/maxresdefault.jpg",
    
    # More fitness/bodybuilding sites
    "https://dubaigymfluencers-1eff6.kxcdn.com/wp-content/uploads/2022/06/Andrei-Deius-Workout.jpg",
    "https://cdn.statically.io/img/tvovermind.com/wp-content/uploads/2022/04/Andre-Deiu.jpg",
    "https://e0.pxfuel.com/wallpapers/395/77/desktop-wallpaper-gefallt-56-5-tsd-mal-370-kommentare-andrei-deiu.jpg",
    
    # Try more Instagram CDN URLs (may work)
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3108429969842300840",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=2473912052546010521",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3635932897669260562",
    
    # Additional sources
    "https://www.companyofmen.org/gallery/image/77479-andrei-deiu/",
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
            # Check if it's actually an image
            content_type = response.headers.get('Content-Type', '')
            if 'image' not in content_type and 'html' in content_type:
                print(f"✗ {filename}: Not an image (got {content_type})")
                return False
            
            with open(f'assets/images/{filename}', 'wb') as out_file:
                out_file.write(response.read())
        print(f"✓ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed {filename}: {str(e)[:60]}")
        return False

if __name__ == '__main__':
    # Check existing files
    existing = list(Path('assets/images').glob('andrei-*.jpg')) + list(Path('assets/images').glob('andrei-*.png'))
    next_num = len(existing) + 1
    
    print(f"Found {len(existing)} existing images")
    print(f"Starting download from image #{next_num}...\n")
    
    success = 0
    for i, url in enumerate(additional_urls, next_num):
        if i > 50:
            break
        
        ext = '.jpg'
        if '.png' in url.lower():
            ext = '.png'
        elif '.webp' in url.lower():
            ext = '.jpg'
        
        filename = f"andrei-{i}{ext}"
        if download_image(url, filename):
            success += 1
    
    total = len(list(Path('assets/images').glob('andrei-*')))
    print(f"\n✓ Total images now: {total}/50")
    if total < 50:
        print(f"Need {50 - total} more images")
