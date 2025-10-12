import streamlit as st
from PIL import Image ,ImageOps
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from io import BytesIO
import json


with open('data/products.json' , 'r') as f:
    allProducts = json.load(f)


st.set_page_config(page_title="Visual Product Matcher", layout="wide")

st.title("🔍 Visual Product Matcher")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    uploadedImage = st.file_uploader(
        "📤 Upload an image", 
        type=['jpg', 'jpeg', 'png', 'avif']
    )

with col2:
    picture = st.text_input("🔗 Or paste image URL")


if uploadedImage or picture:
    st.markdown("### Your Image")
    col_img = st.columns([1, 2, 1])

    with col_img[1]:
        if uploadedImage:
            img = Image.open(uploadedImage)
            img_resized = img.resize((300, 300))
            st.image(img_resized, width=300)
            image_to_encode = img
        elif picture:
            response = requests.get(picture)
            img = Image.open(BytesIO(response.content))
            img_resized = img.resize((300, 300))
            st.image(img_resized, width=300)
            image_to_encode = img

    st.markdown("---")

    value = st.slider("Minimum Similarity Score (%)"  , min_value=0 , max_value=100)

    if st.button("Find Similar Products", type="primary"):
        with st.spinner("Searching for similar products..."):
            model = SentenceTransformer('clip-ViT-B-32')
            vector = model.encode(image_to_encode)

            # Results
            results = []
            for product in allProducts:
                similarity = cosine_similarity([vector] , [product['vector']])[0][0]
                product['similarityScore'] = similarity * 100
                results.append(product)

            results.sort(key = lambda x:x['similarityScore'] , reverse=True)
            topMatches =  results[:5]

            filtered = []
            for m in topMatches:
                if m['similarityScore'] >= value:
                    filtered.append(m)
    
        if filtered:
            st.markdown("### 🎯 Similar Products Found")
            st.markdown("---")

            # Display 3 per row
            for i in range(0, len(filtered), 3):
                cols = st.columns(3)
                for idx, match in enumerate(filtered[i:i+3]):
                    with cols[idx]:
                        # Check if image_path is a URL or local file
                        if match['image_path'].startswith('http'):
                            # It's a URL - fetch it
                            response = requests.get(match['image_path'])
                            product_img = Image.open(BytesIO(response.content))
                        else:
                            # It's a local file
                            product_img = Image.open(match['image_path'])
                        
                        product_img = ImageOps.exif_transpose(product_img)
                        product_img_resized = product_img.resize((300, 300))
                        st.image(product_img_resized, use_container_width=True)
                        st.write(f"**{match['name']}**")
                        st.write(f"Category: {match['category']}")
                        st.write(f"Similarity: {match['similarityScore']:.2f}%")
        else:
            st.warning("⚠️ No products match your similarity threshold. Try lowering it!")
else:
    st.info("👆 Please upload an image or paste a URL to get started")  