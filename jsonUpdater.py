import json

# Read the JSON file
with open('data/products.json', 'r') as f:
    products = json.load(f)

# GitHub details
GITHUB_USERNAME = "ManishPoudel-7"
REPO_NAME = "Unthinkable-Solutions-Assignment"
BRANCH = "master"

# Update all paths WITHOUT changing vectors
for product in products:
    old_path = product['image_path']
    
    # Extract filename from old path (handles both / and \)
    filename = old_path.replace('data/Images\\', '').replace('data/Images/', '').replace('data\\Images\\', '')
    
    # Create GitHub URL
    product['image_path'] = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/data/Images/{filename}"

# Save updated JSON (vectors stay the same!)
with open('data/products.json', 'w') as f:
    json.dump(products, f, indent=2)

print(f"✅ Updated {len(products)} products!")
print("✅ Vectors unchanged - only paths updated")
print("\nSample paths:")
for i in range(min(3, len(products))):
    print(f"{products[i]['name']}: {products[i]['image_path']}")