#!/usr/bin/env python3
"""
Download Andrei Deiu images from various sources
"""
import urllib.request
import os
import re
from pathlib import Path

os.makedirs('assets/images', exist_ok=True)

# Extract direct image URLs from the provided Google search URLs
image_urls = [
    # Instagram images (may need authentication, but trying direct CDN)
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3580219698271046428",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3243869622598139858",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3462874708103637061",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3505581225944534913",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3327116706977985368",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3379433812904982058",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3772997574769746963",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3698436155922670095",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3108429969842300840",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=2473912052546010521",
    "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3635932897669260562",
    
    # Pinterest
    "https://i.pinimg.com/736x/dc/38/63/dc3863b79912f2d718e9776f2251a474.jpg",
    
    # ProSupps official
    "https://prosupps.com/cdn/shop/files/Andrei.png?v=1738774924",
    
    # Evogen Nutrition
    "https://www.evogennutrition.com/cdn/shop/articles/Evogen_Get3D-Smashing-FST-7--Chest-with-Andrei-_-Hany_1200x1200_68a2d261-70e0-4e08-8271-a0c9b96b55d3.jpg?v=1658950961&width=1024",
    
    # YouTube thumbnail
    "https://i.ytimg.com/vi/fJxzmoggxiA/maxresdefault.jpg",
    
    # Fitness sites
    "https://gymfluencers.com/wp-content/uploads/2023/08/Screenshot-2023-08-25-at-21.20.50.png",
    "https://fitnessvolt.com/wp-content/uploads/2021/11/Andrei-Deiu-8-750x938.jpg",
    "https://boxlifemagazine.com/wp-content/uploads/2023/11/andrei-deiu.jpg",
    "https://sense4fitsummit.com/wp-content/uploads/2024/01/Andrei_Deiu.jpg.webp",
    "https://www.greatestphysiques.com/wp-content/uploads/2016/10/CYyCUakWcAEwXdm-1.jpg",
    
    # Facebook (may need auth)
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=1312835803538008",
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=1377103510444570",
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=1415239466630974",
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=1252704832884439",
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=1252704846217771",
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=1352107632944158",
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=249446306543635",
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=2552971015013002",
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=985301446291447",
]

def download_image(url, filename):
    """Download an image from URL"""
    try:
        # Set user agent to avoid blocking
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(f'assets/images/{filename}', 'wb') as out_file:
                out_file.write(response.read())
        print(f"✓ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed {filename}: {str(e)[:50]}")
        return False

if __name__ == '__main__':
    print(f"Downloading {len(image_urls)} images...\n")
    success = 0
    for i, url in enumerate(image_urls, 1):
        ext = '.jpg'
        if '.png' in url.lower():
            ext = '.png'
        elif '.webp' in url.lower():
            ext = '.jpg'  # Convert webp to jpg name
        
        filename = f"andrei-{i}{ext}"
        if download_image(url, filename):
            success += 1
    
    print(f"\n✓ Successfully downloaded {success}/{len(image_urls)} images")
    print(f"Need {50 - success} more images to reach 50 total")
