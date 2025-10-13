from PIL import Image
import pillow_avif
import os

input_folder = "data/Images"
output_folder = "data/Images_JPG"

# Create output folder
os.makedirs(output_folder, exist_ok=True)

converted_count = 0

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.avif'):
        try:
            input_path = os.path.join(input_folder, filename)
            
            # Open AVIF image
            img = Image.open(input_path)
            
            # Convert to RGB
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # Create new filename with .jpg extension
            new_filename = filename.replace('.avif', '.jpg')
            output_path = os.path.join(output_folder, new_filename)
            
            # Save as JPG
            img.save(output_path, 'JPEG', quality=95)
            print(f"✅ Converted: {filename} -> {new_filename}")
            converted_count += 1
            
        except Exception as e:
            print(f"❌ Error converting {filename}: {e}")

print(f"\n✅ Converted {converted_count} images!")
print(f"📁 JPG images are in: {output_folder}")