## 🎧 Hybrid Recommendation System
A modular and scalable Hybrid Recommendation System that combines Content-Based Filtering and Collaborative Filtering using Spotify and Last.fm data. This project demonstrates a full pipeline from raw data processing to deploying the model with DVC and Docker integration.

### 🚀 Features
* 📊 Data Cleaning and Transformation using Pandas and Dask

* 🧠 Content-Based Filtering based on song features like genre, artist, tempo, and more

* 👥 Collaborative Filtering using user-item interactions (Matrix Factorization with Surprise/Dask)

* 🔀 Hybrid System combining both methods for robust recommendations

* 📁 Modular structure with separate scripts and notebooks

* 🛠️ ML Pipelines with DVC for versioned data processing

* 🐳 Docker Support for easy containerization and deployment

* 📈 Jupyter Notebooks for EDA and experiments

* ✅ CI/CD workflow for automated testing and deployment

--
### 🗂️ Project Structure
```
Hybrid-Recommendation-System/
│
├── .dvc/                       # DVC metadata
├── .github/workflows/          # CI/CD pipeline
├── notebooks/                  # EDA & model notebooks
├── recsys-env/                 # Python virtual environment (optional)
│
├── app.py                      # Main app runner
├── collaborative_filtering.py  # Collaborative filtering model
├── content_based_filtering.py  # Content-based filtering model
├── data_cleaning.py            # Data pre-processing script
├── transform_filtered_data.py  # Final data transformation
│
├── hybrid_recommendations.py   # Hybrid recommender logic
├── dvc.yaml / dvc.lock         # DVC pipeline stages
├── Dockerfile                  # Docker configuration
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── ...

```

--
### 📦 Setup Instructions

#### 1️⃣ Clone the repository
```
git clone https://github.com/netra212/Hybrid-Recommendation-System.git
cd Hybrid-Recommendation-System
```

#### 2️⃣ Create and activate virtual environment
```
python -m venv recsys-env
source recsys-env/bin/activate  # On Windows: recsys-env\Scripts\activate
```

#### 3️⃣ Install dependencies
```
pip install -r requirements.txt
OR
conda create --name recsys-env python=3.12
conda activate recsys-env
pip install -r requirements.txt
```
--
### ⚙️ Running the Pipeline
* Make sure DVC is installed:
```pip install dvc```

* Run the full pipeline:
```dvc repro```
--
### 🧪 Notebooks
* **Hybrid_Recomment_System_Content_Based_Recommendation.ipynb** – Analysis and model building for content-based recommendations.

* **Spotify_Collaborative_Filtering.ipynb** – Exploratory analysis and collaborative filtering.
--
### 🐳 Docker Support
Build and run the app in a container:
```
docker build -t hybrid-recsys .
docker run -p 8501:8501 hybrid-recsys
```
--
### 🧠 How the Hybrid Model Works
The hybrid system combines:

* **Similarity Score** from **content-based filtering** (e.g., cosine similarity on features like genre, tempo)

* **Latent Factors** from **collaborative filtering** (e.g., matrix factorization)

Both scores are **normalized and weighted** to produce the final recommendations.
--
### ✅ Use Cases
* Music streaming platforms

* Personalized content feeds

* E-commerce recommendation systems

* Social media content suggestions
--
### 📌 TODOs / Improvements
* Add Streamlit-based front-end for real-time user interaction

* Tune weighting strategy in hybrid fusion

* Deploy to cloud (AWS/GCP/Azure) with Docker or FastAPI

* Add unit testing for all modules
--
### 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.
--
### 📄 License
MIT
--
### 📬 Contact
Created by Netra KC – Feel free to reach out with questions or suggestions!
