import os
import sys
import argparse
from PIL import Image

# Force UTF-8 encoding for standard output to avoid UnicodeEncodeErrors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def convert_to_webp(input_path, output_path, quality=85):
    try:
        img = Image.open(input_path).convert("RGB")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, "WEBP", quality=quality, method=6)
        print(f"SUCCESS: Saved WebP to {output_path}")
        print(f"File size: {os.path.getsize(output_path) // 1024} KB")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="HVS PNG → WebP Converter")
    parser.add_argument("--input", required=True, help="Path to raw PNG input")
    parser.add_argument("--output", required=True, help="Path to save WebP output")
    parser.add_argument("--quality", type=int, default=85, help="WebP quality (default: 85)")
    args = parser.parse_args()
    convert_to_webp(args.input, args.output, args.quality)
