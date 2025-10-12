import json
from sentence_transformers import SentenceTransformer
from PIL import Image
import os

# Model for converting Images to Vectors
model = SentenceTransformer('clip-ViT-B-32')

# Category of the Image
def getCategory(filename):
    prefix = filename[0].lower()

    allCategories = {
        'f': 'flowers',
        'h': 'humans',
        'a': 'pets',
        'c': 'anime',
        's': 'scenery'
    }

    return allCategories.get(prefix , 'unknown')

# Array for all the Images
allImages = []
imagesFolder = 'data/Images'

for index , filename in enumerate(os.listdir(imagesFolder)):
    if not filename.lower().endswith(('.jpg', '.png', '.jpeg' , '.avif')):
        continue

    imagePath = os.path.join(imagesFolder , filename)
    image = Image.open(imagePath)

    # Making Vector of the image
    vector = model.encode(image).tolist()

    # Getting the Category
    category = getCategory(filename)

    # Single Product Entry
    singleImage = {
        "id": index + 1,
        "name": filename.split('.')[0].upper(), 
        "category": category,
        "image_path": imagePath,
        "vector": vector
    }

    allImages.append(singleImage)

# Saving to JSON
with open('data/products.json' , 'w') as f:
    json.dump(allImages , f , indent=2)


print(f"Processed {len(allImages)} products!")
