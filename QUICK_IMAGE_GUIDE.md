# ⚡ QUICK GUIDE: Add 50 Andrei Deiu Images NOW

## The Problem:
The HTML files are updated but showing placeholder images because the actual image files don't exist yet.

## The Solution - 3 Options:

### Option 1: Manual Upload via GitHub (EASIEST - 5 minutes)
1. Go to: https://github.com/levan5858/ADR-FITNESS/tree/main/assets/images
2. Click "Add file" → "Upload files"
3. Download 50 images from Instagram @andreideiu_ (use any Instagram downloader)
4. Rename them: `andrei-1.jpg`, `andrei-2.jpg`, ... `andrei-50.jpg`
5. Drag all 50 files into the upload area
6. Click "Commit changes"
7. Done! Site will update in 1-2 minutes

### Option 2: Use Terminal (if you have images locally)
```bash
cd "/Users/work1/Desktop/ANDREI DEIU/assets/images"
# Copy your 50 images here, named andrei-1.jpg through andrei-50.jpg
cd "/Users/work1/Desktop/ANDREI DEIU"
git add assets/images/
git commit -m "Add 50 Andrei Deiu images"
git push origin main
```

### Option 3: Use Instagram Downloader Tool
1. Install: `pip install instaloader` (or use any Instagram downloader)
2. Download from @andreideiu_:
   ```bash
   instaloader andreideiu_ --no-videos --no-captions
   ```
3. Rename and move to `assets/images/` folder
4. Commit and push

## Image Requirements:
- **Format**: .jpg or .png
- **Names**: Must be exactly `andrei-1.jpg` through `andrei-50.jpg`
- **Location**: `assets/images/` folder
- **Size**: Any size works, but 1200x800px+ recommended

## Current Status:
✅ HTML files updated and pushed to GitHub
❌ Image files missing (that's why you see placeholders)
⏳ Waiting for you to add the 50 images

## After Adding Images:
The site will automatically update on GitHub Pages within 1-2 minutes!
