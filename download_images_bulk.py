#!/usr/bin/env python3
"""
Bulk download script for Andrei Deiu images.
Add image URLs to image_urls.txt (one URL per line), then run this script.
"""

import urllib.request
import os
import sys

# Create images directory
os.makedirs('assets/images', exist_ok=True)

def download_image(url, filename):
    """Download an image from a URL"""
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, f'assets/images/{filename}')
        print(f"✓ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def main():
    # Check if image_urls.txt exists
    if not os.path.exists('image_urls.txt'):
        print("Creating image_urls.txt template...")
        with open('image_urls.txt', 'w') as f:
            f.write("# Add one image URL per line\n")
            f.write("# Example:\n")
            f.write("# https://example.com/image1.jpg\n")
            f.write("# https://example.com/image2.jpg\n")
        print("Please add image URLs to image_urls.txt and run again.")
        return
    
    # Read URLs from file
    with open('image_urls.txt', 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    if not urls:
        print("No URLs found in image_urls.txt")
        return
    
    print(f"Found {len(urls)} URLs to download")
    print(f"Will save as andrei-1.jpg through andrei-{len(urls)}.jpg\n")
    
    # Download each image
    success_count = 0
    for i, url in enumerate(urls, 1):
        filename = f"andrei-{i}.jpg"
        if download_image(url, filename):
            success_count += 1
    
    print(f"\n✓ Successfully downloaded {success_count}/{len(urls)} images")
    print(f"Images saved to: assets/images/")

if __name__ == '__main__':
    main()
