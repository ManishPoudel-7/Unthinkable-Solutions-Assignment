import json

# Read the JSON file
with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print(f"Found {len(products)} products")
print(f"\nBefore: {products[0]['image_path']}")

# Simply change .avif to .jpg in all paths
changed_count = 0
for product in products:
    old_path = product['image_path']
    new_path = old_path.replace('.avif', '.jpg').replace('.AVIF', '.jpg')
    if old_path != new_path:
        changed_count += 1
    product['image_path'] = new_path

print(f"After: {products[0]['image_path']}")

# Save updated JSON (vectors stay the same!)
with open('data/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2)

print(f"\n✅ Updated {len(products)} products!")
print(f"✅ Changed {changed_count} paths from .avif to .jpg")
print("✅ Vectors unchanged - saved tons of time!")
print("\nFirst 3 sample paths:")
for i in range(min(3, len(products))):
    print(f"  {products[i]['name']}: {products[i]['image_path']}")