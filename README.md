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

### 🗂️ Project Structure
```
Hybrid-Recommendation-System/
│
├── .dvc/                        # DVC metadata
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

## 📦 Setup Instructions
