#!/usr/bin/env python3
"""
Script to download Andrei Deiu images from publicly accessible sources.
Note: For Instagram images, you'll need to manually download or use Instagram's API.
"""

import urllib.request
import os
import json

# Create images directory
os.makedirs('assets/images', exist_ok=True)

# Known image sources (you'll need to add direct URLs here)
# Since Instagram requires auth, these are placeholder URLs
# Replace with actual direct image URLs from:
# - andreideiu.shop
# - Public Pinterest boards
# - Other publicly accessible sources

image_urls = [
    # Add direct image URLs here
    # Example format:
    # 'https://example.com/image1.jpg',
]

def download_image(url, filename):
    """Download an image from a URL"""
    try:
        urllib.request.urlretrieve(url, f'assets/images/{filename}')
        print(f"Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
        return False

if __name__ == '__main__':
    print("Image downloader ready.")
    print("Add direct image URLs to the image_urls list above.")
    print("For Instagram images, download manually from @andreideiu_")
