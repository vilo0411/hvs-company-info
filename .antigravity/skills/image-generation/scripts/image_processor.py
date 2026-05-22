import os
import argparse
from PIL import Image, ImageDraw, ImageOps, ImageFilter

def create_rounded_mask(size, radius):
    """Create a high-quality anti-aliased rounded mask."""
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), size], radius, fill=255)
    return mask

def process_and_overlay_logo(input_path, logo_path, output_path, position="bottom_right", quality=85):
    try:
        # 1. Open background image
        bg = Image.open(input_path).convert("RGBA")
        bg_w, bg_h = bg.size
        
        # 2. Open logo image
        logo = Image.open(logo_path).convert("RGBA")
        
        # 3. Calculate target logo size (12% of background width)
        logo_w = int(bg_w * 0.12)
        logo_aspect = logo.height / logo.width
        logo_h = int(logo_w * logo_aspect)
        logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
        
        # 4. Create a glassmorphic/white container card around the logo to make it stand out beautifully
        padding = int(logo_w * 0.08)
        card_w = logo_w + (padding * 2)
        card_h = logo_h + (padding * 2)
        
        # Create card background (semi-transparent white card with a border)
        card = Image.new("RGBA", (card_w, card_h), (255, 255, 255, 220)) # 85% opaque white
        
        # Draw a subtle border
        draw = ImageDraw.Draw(card)
        draw.rounded_rectangle([(0, 0), (card_w-1, card_h-1)], radius=8, outline=(123, 87, 224, 60), width=1) # HVS primary purple border with 23% opacity
        
        # Paste logo on card
        card.paste(logo, (padding, padding), logo)
        
        # Crop card to be rounded
        mask = create_rounded_mask((card_w, card_h), radius=8)
        
        # 5. Determine coordinates based on position
        margin = int(bg_w * 0.02) # 2% margin
        
        if position == "bottom_right":
            x = bg_w - card_w - margin
            y = bg_h - card_h - margin
        elif position == "top_left":
            x = margin
            y = margin
        elif position == "bottom_center":
            x = (bg_w - card_w) // 2
            y = bg_h - card_h - margin
        else: # Default to bottom_right
            x = bg_w - card_w - margin
            y = bg_h - card_h - margin
            
        # 6. Composite the card onto the background
        bg.paste(card, (x, y), mask)
        
        # 7. Convert back to RGB for WebP compression and save
        final_img = bg.convert("RGB")
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        final_img.save(output_path, "WEBP", quality=quality, method=6)
        print(f"SUCCESS: Image processed, logo overlayed at {position}, and saved as WebP to {output_path}")
        print(f"File size optimized to: {os.path.getsize(output_path) // 1024} KB")
        return True
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="HVS Securities Image Post-Processor (WebP + Logo Overlay)")
    parser.add_argument("--input", required=True, help="Path to raw input image")
    parser.add_argument("--logo", required=True, help="Path to logo image")
    parser.add_argument("--output", required=True, help="Path to save optimized WebP image")
    parser.add_argument("--position", default="bottom_right", choices=["bottom_right", "top_left", "bottom_center"], help="Logo position")
    parser.add_argument("--quality", type=int, default=85, help="WebP quality (default: 85)")
    
    args = parser.parse_args()
    process_and_overlay_logo(args.input, args.logo, args.output, args.position, args.quality)
