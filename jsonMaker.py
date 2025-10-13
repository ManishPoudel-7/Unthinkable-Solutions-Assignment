import json
from sentence_transformers import SentenceTransformer
from PIL import Image
import os

# Model for converting Images to Vectors
model = SentenceTransformer('clip-ViT-B-32')

# Category of the Image
def getCategory(filename):
    # Extract the prefix before the hyphen
    if '-' in filename:
        prefix = filename.split('-')[0].lower()
    else:
        prefix = filename.split('.')[0].lower()
    
    allCategories = {
        'book': 'Books',
        'doll': 'Dolls',
        'fan': 'Fans',
        'laptop': 'Laptops',
        'refrigerator': 'Refrigerators',
        'scenery': 'Scenery',
        'shirt': 'Shirts',
        'smartphone': 'Smartphones',
        'teddybear': 'Teddy Bears',
        'toycar': 'Toy Cars',
        'tshirt': 'T-Shirts',
        'washingmachine': 'Washing Machines',
        'watch': 'Watches'
    }
    
    return allCategories.get(prefix, 'Unknown')

# Array for all the Images
allImages = []
imagesFolder = 'data/Images'

for index, filename in enumerate(os.listdir(imagesFolder)):
    if not filename.lower().endswith(('.jpg', '.png', '.jpeg')):
        continue

    imagePath = os.path.join(imagesFolder, filename)
    image = Image.open(imagePath)

    # Making Vector of the image
    vector = model.encode(image).tolist()

    # Getting the Category
    category = getCategory(filename)

    # Single Product Entry
    singleImage = {
        "id": index + 1,
        "name": filename.split('.')[0].replace('-', ' ').title(), 
        "category": category,
        "image_path": imagePath,
        "vector": vector
    }

    allImages.append(singleImage)

# Saving to JSON
with open('data/products.json', 'w') as f:
    json.dump(allImages, f, indent=2)

print(f"Processed {len(allImages)} products!")