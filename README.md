# Florafend: Plant Leaf Disease Detection System
Florafend is a web-based application designed to help farmers and plant enthusiasts detect and manage plant leaf diseases. The application uses a Convolutional Neural Network (CNN) model to predict the type of disease affecting a plant based on leaf images. It also provides tailored recommendations for disease management and offers the latest news about plant diseases.

Features
Disease Prediction: Upload a leaf image, and Florafend will predict the disease affecting the plant using a trained CNN model.
Recommendations: Receive personalized recommendations for managing the detected disease.
Latest News: Stay updated with the latest news on plant diseases, sourced from NewsAPI.
Blog Section: Read articles and insights related to plant health and disease management.
Installation
To set up the Florafend project locally, follow these steps:

Clone the repository:
git clone https://github.com/yourusername/florafend.git
cd florafend

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Access the application:
Open your browser and go to http://127.0.0.1:8000/
