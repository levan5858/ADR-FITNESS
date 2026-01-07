# Quick Image Setup Guide - 50 Andrei Deiu Images

## ✅ HTML Files Are Ready!
All HTML files are already configured to use local images. Just add the image files!

## 📥 How to Add 50 Images:

### Option 1: Manual Download (Fastest)
1. **Download from Instagram** (@andreideiu_):
   - Use a tool like: https://downloadgram.org/ or similar
   - Or right-click and save images directly from browser

2. **Save images in `assets/images/` folder with these exact names:**
   - `andrei-1.jpg` (homepage hero)
   - `andrei-2.jpg` through `andrei-50.jpg` (gallery images)
   - Use `.jpg` or `.png` - both work!

3. **Image assignments:**
   - `andrei-1.jpg` → Homepage hero image
   - `andrei-2.jpg` to `andrei-4.jpg` → Homepage gallery
   - `andrei-5.jpg` → About page hero + Contact page
   - `andrei-6.jpg` to `andrei-15.jpg` → Video thumbnails (10 videos)
   - `andrei-16.jpg` to `andrei-50.jpg` → Photo gallery (35 photos)

### Option 2: Bulk Download Script
If you have direct image URLs, create a file `image_urls.txt` with one URL per line, then run:
```bash
python3 download_images_bulk.py
```

### Option 3: Drag & Drop
1. Download all 50 images to your computer
2. Rename them to `andrei-1.jpg` through `andrei-50.jpg`
3. Drag all 50 files into `assets/images/` folder

## 🎥 For Videos (10 YouTube embeds):

1. Go to Andrei's YouTube: https://www.youtube.com/@AndreiDeiu
2. Find 10 videos you want to feature
3. Get video IDs from URLs (the part after `?v=`)
4. Replace in HTML files:
   - `YOUTUBE_VIDEO_ID_1` through `YOUTUBE_VIDEO_ID_10`
   - See `VIDEO_IDS.md` for detailed instructions

## ⚡ Quick Start:
1. Download 50 images from @andreideiu_ Instagram
2. Rename: `andrei-1.jpg`, `andrei-2.jpg`, ... `andrei-50.jpg`
3. Copy to: `assets/images/` folder
4. Done! Images will automatically appear on the site.

## 📝 Notes:
- Images fall back to placeholder if file not found
- Supported formats: .jpg, .jpeg, .png, .webp
- Recommended size: 1200x800px or larger for best quality
- All images should be of Andrei Deiu (you have rights to use them)
