import os
import json
import sys
from PIL import Image

# Force UTF-8 encoding for standard output to avoid UnicodeEncodeErrors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def optimize_images(manifest_path):
    if not os.path.exists(manifest_path):
        print(f"Error: Manifest not found at {manifest_path}")
        return

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    updated = False
    for img in manifest.get('images', []):
        raw_path = img.get('source')
        output_path = img.get('output')
        
        # Ensure output folder exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        if os.path.exists(raw_path):
            try:
                print(f"Processing: {raw_path} -> {output_path}")
                with Image.open(raw_path) as im:
                    # Convert to RGB if necessary (for JPEG/WebP)
                    if im.mode in ("RGBA", "P"):
                        im = im.convert("RGB")
                    
                    # Target size (Defaults from Visual Brand Framework)
                    target_width = img.get('width', 1000)
                    target_height = img.get('height', 600)
                    
                    # Resize with aspect ratio preservation (Crop to fit)
                    im.thumbnail((target_width * 2, target_height * 2), Image.Resampling.LANCZOS)
                    
                    # Center crop to target size
                    width, height = im.size
                    left = (width - target_width) / 2
                    top = (height - target_height) / 2
                    right = (width + target_width) / 2
                    bottom = (height + target_height) / 2
                    
                    im = im.crop((left, top, right, bottom))
                    
                    # Save as WebP
                    im.save(output_path, "WEBP", quality=85, method=6)
                    
                    # Update manifest info
                    img['status'] = 'ready'
                    img['width'], img['height'] = im.size
                    img['file_size_kb'] = round(os.path.getsize(output_path) / 1024, 2)
                    img['format'] = 'webp'
                    updated = True
                    print(f"Done: {img['file_size_kb']} KB")
            except Exception as e:
                print(f"Failed to process {raw_path}: {e}")
        else:
            print(f"Source file not found: {raw_path}")

    if updated:
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        print("Manifest updated successfully.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        optimize_images(sys.argv[1])
    else:
        print("Usage: python image_optimizer.py <manifest_path>")
