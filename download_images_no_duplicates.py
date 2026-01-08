#!/usr/bin/env python3
"""
Download images with duplicate detection - checks both filename and content hash
"""
import os
import hashlib
import urllib.request
import urllib.error
import ssl
from pathlib import Path

# Create SSL context that doesn't verify certificates (for public image downloads)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Image URLs to download
IMAGE_URLS = [
    "https://i.pinimg.com/474x/7c/70/5c/7c705c84c51249a7e07c6eb076b671c8.jpg",
    "https://cdn.shopify.com/s/files/1/0423/8761/files/EBB33238-A523-4246-83AB-4831BBD8CE63_480x480.jpg?v=1708102692",
    "https://gymfluencers.com/wp-content/uploads/2023/08/Screenshot-2023-08-25-at-21.20.50.png",
    "https://fitnessvolt.com/wp-content/uploads/2021/11/Andre-Deiu-1-750x938.jpg",
    "https://gymfluencers.com/wp-content/uploads/2023/08/Screenshot-2023-08-25-at-21.30.46-1024x655.png.webp",
    "https://fitnessvolt.com/wp-content/uploads/2021/11/Andrei-Deiu-3-750x938.jpg",
    "https://sense4fitsummit.com/wp-content/uploads/2024/01/Andrei_Deiu.jpg.webp",
    "https://sense4fitsummit.com/wp-content/uploads/2024/01/Andre_Deiu2-819x1024.jpg.webp",
]

IMAGES_DIR = Path("assets/images")
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def get_file_hash(filepath):
    """Calculate MD5 hash of file content"""
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except:
        return None

def get_existing_hashes():
    """Get hashes of all existing images"""
    hashes = {}
    for img_file in IMAGES_DIR.glob("andrei-*.{jpg,jpeg,png,webp}"):
        file_hash = get_file_hash(img_file)
        if file_hash:
            hashes[file_hash] = img_file.name
    return hashes

def download_image(url, index):
    """Download image with duplicate detection"""
    try:
        # Determine file extension from URL
        if ".webp" in url.lower():
            ext = "webp"
        elif ".png" in url.lower():
            ext = "png"
        else:
            ext = "jpg"
        
        # Find next available number
        existing_files = list(IMAGES_DIR.glob("andrei-*.{jpg,jpeg,png,webp}"))
        existing_numbers = []
        for f in existing_files:
            try:
                num = int(f.stem.split("-")[1])
                existing_numbers.append(num)
            except:
                pass
        
        # Start from highest number + 1, or use index if provided
        if existing_numbers:
            next_num = max(existing_numbers) + 1
        else:
            next_num = 50  # Start from 50 for new images
        
        filename = f"andrei-{next_num}.{ext}"
        filepath = IMAGES_DIR / filename
        
        # Check if filename already exists
        if filepath.exists():
            print(f"⚠️  Skipping {filename} - file already exists")
            return None
        
        # Download image
        print(f"Downloading {url}...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=30, context=ssl_context) as response:
            image_data = response.read()
            
            # Check content hash
            content_hash = hashlib.md5(image_data).hexdigest()
            existing_hashes = get_existing_hashes()
            
            if content_hash in existing_hashes:
                print(f"⚠️  Skipping {url} - duplicate content (matches {existing_hashes[content_hash]})")
                return None
            
            # Save image
            with open(filepath, "wb") as f:
                f.write(image_data)
            
            print(f"✅ Downloaded: {filename}")
            return filename
            
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code} for {url}")
        return None
    except urllib.error.URLError as e:
        print(f"❌ URL Error for {url}: {e.reason}")
        return None
    except Exception as e:
        print(f"❌ Error downloading {url}: {str(e)}")
        return None

def main():
    print("Starting image download with duplicate detection...\n")
    downloaded = []
    
    for i, url in enumerate(IMAGE_URLS, 1):
        result = download_image(url, i)
        if result:
            downloaded.append(result)
    
    print(f"\n✅ Download complete! Downloaded {len(downloaded)} new images.")
    if downloaded:
        print("New images:", ", ".join(downloaded))

if __name__ == "__main__":
    main()
