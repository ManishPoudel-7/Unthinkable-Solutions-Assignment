🔍 Visual Product Matcher
A web application that finds visually similar products based on uploaded images using AI-powered image embeddings and similarity search.
📋 Overview
This project allows users to upload an image or paste an image URL, and the system will find the most visually similar products from a database of 50+ items across categories like flowers, humans, pets, anime, and scenery.
✨ Features

Dual input methods (file upload & URL)
AI-powered visual similarity search using CLIP model
Similarity scoring with adjustable threshold
Support for multiple image formats (JPG, PNG, AVIF, base64)
Real-time results with top 5 matches
Mobile-responsive design

🛠️ Technical Stack

Frontend: Streamlit
ML Model: CLIP (ViT-B-32) via sentence-transformers
Similarity Search: Cosine similarity (scikit-learn)
Image Processing: Pillow, pillow-avif-plugin
Data Storage: JSON
