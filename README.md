# 🌍 EcoTrack – AI-Powered Personalized Environmental Impact Tracker and Advisor

*Track • Understand • Reduce Your Carbon Footprint*

EcoTrack is a full-stack web application prototype designed to help individuals quantify their personal carbon footprint and receive personalized, data-driven recommendations for reducing their environmental impact. This project addresses the need for dynamic, engaging tools in the fight against climate change, directly supporting *Sustainable Development Goal 13: Climate Action*.

## 💡 Problem Solved

Most existing carbon footprint calculators are *generic and static, failing to provide the **personalized, dynamic guidance* necessary to drive sustainable behavioral changes. EcoTrack overcomes this limitation by combining structured user data with intelligent estimation to deliver real-time, actionable insights.

## ✨ Key Features (Proof-of-Concept)

The core functionality demonstrated in this prototype aligns directly with the project's research objectives:

| Feature | Research Objective | Description |
| :--- | :--- | :--- |
| *Data Collection* | Objective 1 | Interactive forms for capturing key lifestyle data (energy, transport, water, waste). |
| *ML/AI Estimation* | Objective 2 | A calculation engine (mock ML/AI) using industry-standard emission factors to accurately estimate the user's monthly CO₂ footprint. |
| *Visualization Dashboard* | Objective 3 | Real-time, categorized results displayed using custom progress bars to show the percentage breakdown of the total footprint. |
| *Personalized Feedback* | Objective 3 | Provides the necessary data foundation to generate tailored recommendations based on the user's highest-impact areas. |

## 🛠️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| *Frontend/UI* | Python (Streamlit), HTML/CSS | Rapid prototyping, interactive forms, and data visualization. |
| *Backend/Logic* | Python | Core logic for the calculation engine and data handling. |
| *ML Artifacts* | carbon_pipeline.joblib, label_encoder.joblib | Evidence of planned/initial Machine Learning pipeline and data preprocessing implementation (e.g., standard scaling, one-hot encoding). |
| *Visual Elements* | Streamlit Lottie | Integration of animated graphics for enhanced user engagement. |

## ⚙️ Installation and Setup

To run the EcoTrack prototype locally, follow these steps:

### Prerequisites

  * Python 3.8+
  * The necessary project files (app.py, .joblib files).

### 1\. Clone the Repository (or unzip files)

bash
# Assuming a repository structure
git clone https://github.com/nitharshana31/ECO-Track-SteamlitApp.git
cd ECO-Track-SteamlitApp


### 2\. Install Dependencies

You will need streamlit, streamlit-lottie, and requests. Since the joblib files are present, it is also recommended to install the scikit-learn library they were created with.

bash
pip install streamlit streamlit-lottie requests scikit-learn


### 3\. Run the Application

Execute the Streamlit script from your terminal:

bash
streamlit run app.py


The application will automatically open in your default web browser (usually at http://localhost:8501).

## 🚀 Usage

1.  Navigate to the *🏠 Home* page to view the project overview.
2.  Switch to the *🧮 Calculator* page via the sidebar navigation.
3.  Input your monthly, daily, and yearly consumption data (Electricity, Car distance, Air travel, etc.).
4.  Click the "*🌱 Calculate Footprint*" button.
5.  Review the *Total Monthly Footprint* and the *Detailed Breakdown* to understand your highest-impact categories.

## 📁 Project Files

| File | Description | Role in Project |
| :--- | :--- | :--- |
| app.py | Main application script (Python Streamlit). | Contains all UI logic, the calculation engine, and the navigation structure. |
| carbon_pipeline.joblib | Machine Learning Preprocessing Pipeline. | Stores the fitted scikit-learn pipeline for transforming raw input data (scaling, encoding) for a future ML model. |
| label_encoder.joblib | Label Encoder artifact. | Stores fitted encoders for categorical features, supporting the pipeline. |
| Final Year Project Research Proposal.pdf | Project Documentation. | Outlines the problem statement, objectives, architecture, and project plan. |

"# poc-Final" 
"# poc" 
"# proof_of_Concept"
