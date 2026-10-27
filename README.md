# 🏋️ Big Data Platform for Fitness Recommendation System

A big data engineering project that builds an end-to-end, multi-source data platform to power personalized fitness recommendations.  
The system integrates structured, semi-structured, and unstructured data through Kafka, Hadoop, Spark, Cassandra, and MySQL, running on a 7-container Docker network.

---

## 📌 Overview

Developed for a business case with **REVIVO Wellness Center**, whose client data was scattered across separate systems and processed manually, making personalized recommendations and real-time insights difficult.

This project designs a big data platform that centralizes this data, applies a data governance layer, and delivers fitness insights through an interactive dashboard based on a client's age, BMI, gender, and goals.

---

## 🎯 Objectives

- Centralize fragmented fitness and client data into a single platform  
- Build a pipeline that handles structured, semi-structured, and unstructured data  
- Apply distributed processing (Hadoop, Spark) for analysis and ML modeling  
- Design a data governance layer considering privacy regulations (HIPAA)  
- Provide an interactive dashboard for clients and trainers  

---

## 🧠 Key Features

- **Multi-source pipeline:** CSV (MySQL), JSON & streaming (Kafka), image metadata (Cassandra) → HDFS → Spark → Streamlit  
- **Distributed analysis:** Hadoop MapReduce to count unique exercises by difficulty level  
- **ML modeling:** Spark ML classification of exercise intensity  
- **Data governance:** cataloging, quality checks, and single source of truth design  
- **7-container Docker network** with shared volumes and documented, reproducible setup  

---

## 🗂️ Dataset

| Type | Source | Description |
|---|---|---|
| Structured | `exercise_dataset.csv` | 12 columns: exercise, calories burned, age, gender, BMI, weight, duration, heart rate, weather, intensity (target) |
| Semi-structured | `exercises.json` + Kafka stream | Exercise metadata and streaming event data |
| Unstructured | [free-exercise-db](https://github.com/yuhonas/free-exercise-db) | 800+ exercises with images, target muscles, equipment, level, and instructions |

---

## ⚙️ Methodology

The platform is built through the following steps:

1. Data ingestion  
   - Structured CSV loaded into MySQL with a defined schema  
   - Exercise metadata and image paths loaded into Cassandra  
   - Kafka topics for streaming data  

2. Data storage design  
   - **MySQL** for structured client and exercise records  
   - **Cassandra** for image metadata, using UUID primary keys and `LIST<TEXT>` fields for variable-length muscles and instructions; images stay on the file system and only paths are stored  
   - **HDFS** for distributed batch processing  

3. Distributed processing  
   - **Hadoop MapReduce** (Python streaming): mapper validates difficulty levels, reducer deduplicates exercise IDs and counts unique exercises per level (beginner / intermediate / expert)  
   - **Spark ML**: classification model predicting exercise intensity, trained with stratified splits  

4. Data governance  
   - Data cataloging and metadata management  
   - Data quality pipeline: NULL handling, deduplication, outlier handling  
   - Access control design for sensitive health data (HIPAA)  
   - Master data management for a single view of each client  

5. Visualization  
   - Streamlit dashboard where users enter age, BMI, gender, and goals to get exercise insights  

---

## 📊 Model Evaluation

<!-- Spark ML 모델 성능 수치가 있다면 여기에 추가하세요 (예: Accuracy, F1) -->

- Spark ML intensity classifier evaluated on a stratified hold-out split  
- MapReduce output validated against the full exercise dataset to confirm unique exercise counts per difficulty level  

---

## 🛠️ Tech Stack

- **Languages:** Python, SQL, Bash  
- **Streaming:** Apache Kafka  
- **Storage:** MySQL, Apache Cassandra, HDFS  
- **Processing:** Apache Hadoop (MapReduce), Apache Spark (Spark ML)  
- **ML & Visualization:** Scikit-learn, Streamlit, Matplotlib / Seaborn  
- **Infrastructure:** Docker (7 containers), Ubuntu VM  

---

## 📁 Project Structure

<!-- 실제 저장소 폴더 구조에 맞게 수정하세요 -->

```
Fitness-Recommendation-System/
│
├── data/                # CSV, JSON, image metadata
├── mysql/               # Schema & loading scripts
├── cassandra/           # Schema & load_image.py
├── hadoop/              # mapper.py, reducer.py
├── spark/               # Spark ML model
├── streamlit/           # Dashboard app
├── docs/                # Architecture diagram & business requirements
└── README.md
```

---

## 🚀 Results

- Built an end-to-end pipeline integrating **CSV, JSON, Kafka streaming, and image data** from ingestion to dashboard  
- Classified and analyzed **800+ exercises** by difficulty, target muscle, and equipment to define exercise pools for each user level  
- Ran **Hadoop MapReduce** to count unique exercises per difficulty level, providing the data basis for recommendation logic  
- Deployed a **Streamlit dashboard** returning personalized exercise insights from user inputs  
- Resolved frequent VM crashes by documenting all installation commands and container settings, making the environment **reproducible** for the whole team  

---

## 📌 Limitations

- Ran on a single VM with Docker, not a production-scale cluster  
- Client data was simulated; real wearable or client records were not used  
- Recommendations are based on exercise attributes and user profile rules, not learned from user feedback  

---

## 🔧 Future Work

- Collect user feedback to build learned recommenders (e.g., collaborative filtering, NCF)  
- Migrate to a managed cloud environment for scalability  
- Integrate wearable device data for real-time recommendations  

---

## 👤 Team Members

Park, Eunsoo  
Dessie, Yeabsira S  
Tsegaselassie, Wengel A  

**My role:** Cassandra schema design and data loading, Hadoop MapReduce implementation, ML modeling, and Docker container network setup

---

## ✔️ Summary

> An end-to-end big data platform that integrates multi-source fitness data through Kafka, Hadoop, Spark, Cassandra, and MySQL on Docker, delivering personalized exercise insights via a Streamlit dashboard
