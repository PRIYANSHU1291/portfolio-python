from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

projects = [
    {"title": "Student Placement and Salary Prediction System", "desc": "Built a Random Forest model to predict student placement status and salary from a custom dataset, deployed via a Streamlit web app with real-time input. Implemented data preprocessing, feature engineering, model training, evaluation, and deployment using Python, pandas, and scikit-learn.", "link": "#"},
    {"title": "Automated Youtube Video Slide Conversion Tool", "desc": "Developed a Python tool to extract slides from YouTube videos at set intervals using OpenCV for frame processing and duplicate detection, with PDF export for easy sharing. Designed with a virtual environment for portability and reproducibility.", "link": "#"}
]

@app.route("/")
def home():
    return render_template("index.html", name="Priyanshu Raj",
                           role="Developer",
                           projects=projects,
                           contact_email=os.getenv("CONTACT_EMAIL", "yourname@example.com"))

if __name__ == "__main__":
    app.run(debug=True)
