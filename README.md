# 🔍 Visual Product Matcher

A web application that finds visually similar products based on uploaded images using AI-powered image embeddings and similarity search.

## 📋 Overview
This project allows users to upload an image or paste an image URL, and the system will find the most visually similar products from a database of 50+ items across categories like flowers, humans, pets, anime, and scenery.

## ✨ Features
- ✅ Dual input methods (file upload & URL)
- ✅ AI-powered visual similarity search using CLIP model
- ✅ Similarity scoring with adjustable threshold
- ✅ Support for multiple image formats (JPG, PNG, AVIF, base64)
- ✅ Real-time results with top 5 matches
- ✅ Mobile-responsive design

## 🛠️ Technical Stack
- **Frontend:** Streamlit  
- **ML Model:** CLIP (ViT-B-32) via `sentence-transformers`  
- **Similarity Search:** Cosine similarity (`scikit-learn`)  
- **Image Processing:** Pillow, pillow-avif-plugin  
- **Data Storage:** JSON  

## 🧠 Approach / Methodology
- Generate feature embeddings for the uploaded image and all stored product images using the **CLIP model**.  
- Compute **cosine similarity** between the uploaded image embedding and each product embedding to find visual matches.  
- Filter results based on a **user-defined similarity threshold** and display the **top 5 matches** with image, name, category, and similarity score.  
- Handle both **local file uploads** and **image URLs** with proper error checking to ensure robust operation.

## 🌐 Live Demo
Try it out here: [Visual Product Matcher](https://manishpoudel-7-unthinkable-solutions-assig-visualmatcher-s72wan.streamlit.app/)
