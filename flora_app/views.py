from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
import numpy as np
import tensorflow as tf
import os
import requests
from django.conf import settings
from .recommendations import get_recommendation  # Import your recommendation function
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from flask import render_template

# Load the trained model
model_path = os.path.join(settings.BASE_DIR, 'models', 'model.h5')
model = tf.keras.models.load_model(model_path)

# Define class names
CLASS_NAMES = ['Apple__Apple_scab', 'Apple_Black_rot', 'Apple_Cedar_apple_rust', 'Apple_healthy', 
               'Blueberry_healthy', 'Cherry(including_sour)__healthy', 'Cherry(including_sour)__Powdery_mildew', 
               'Corn(maize)__Cercospora_leaf_spot Gray_leaf_spot', 'Corn(maize)__Common_rust', 'Corn_(maize)__healthy', 
               'Corn(maize)__Northern_Leaf_Blight', 'Grape_Black_rot', 'Grape_Esca(Black_Measles)', 'Grape__healthy', 
               'Grape_Leaf_blight(Isariopsis_Leaf_Spot)', 'Orange__Haunglongbing(Citrus_greening)', 'Peach__Bacterial_spot', 
               'Peach_healthy', 'Pepper,_bell_Bacterial_spot', 'Pepper,_bell_healthy', 'Potato_Early_blight', 
               'Potato_healthy', 'Potato_Late_blight', 'Raspberry_healthy', 'Soybean_healthy', 'Squash_Powdery_mildew', 
               'Strawberry_healthy', 'Strawberry_Leaf_scorch', 'Tomato_Bacterial_spot', 'Tomato_Early_blight', 
               'Tomato_healthy', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 
               'Tomato_Spider_mites Two-spotted_spider_mite', 'Tomato_Target_Spot', 'Tomato_Tomato_mosaic_virus', 
               'Tomato__Tomato_Yellow_Leaf_Curl_Virus']

# flora_app/news

NEWS_API_KEY = '3833c3d9d0984c03bb6613e581edadec'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

def latest_news(request):
    params = {
        'apiKey': NEWS_API_KEY,
        'q': 'plantation OR farming OR agriculture OR gardening NOT company NOT offers NOT sports NOT film',
        'sortBy': 'publishedAt',
        'pageSize': 25,
    }
    response = requests.get(NEWS_API_URL, params=params)
    news_data = response.json().get('articles', [])
    return render(request, 'pages/news.html', {'news_data': news_data})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after signin
    return render(request, 'pages/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'pages/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

@login_required
def ask(request):
    if request.method == 'POST':
        disease = request.POST.get('disease', '')
        # Get recommendations for the provided disease
        recommendations = get_recommendation(disease)
        return render(request, 'pages/response.html', {'disease': disease, 'recommendations': recommendations})
    
    return render(request, 'pages/ask.html')

def predict(request):
    if request.method == 'POST':
        plant_image = request.FILES.get('plant_image')
        
        #J-G
        # if plant_image.name.lower() == 'bbee.png':
        #     return render(request, 'pages/predict.html', {'message': 'Not a Plant'})

        # Save the uploaded image to the server
        file_path = default_storage.save(plant_image.name, ContentFile(plant_image.read()))
        img_path = default_storage.path(file_path)
        
        # Load and preprocess the image
        img = Image.open(img_path).resize((150, 150))  # Resize to 150x150 instead of 224x224
        img_array = np.array(img) / 255.0  # Normalize the image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Predict the disease
        predictions = model.predict(img_array)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]

        # Store predicted disease in session
        request.session['predicted_disease'] = predicted_class
        
        # Redirect to a new page to display recommendations
        # return redirect('recommendation') 
        return render(request, 'pages/predict.html', {'disease': predicted_class})  # Render the same page with the disease   
    
    return render(request, 'pages/predict.html')

def recommendation(request):
    # Retrieve predicted disease from session
    predicted_disease = request.session.get('predicted_disease', None)
    
    if predicted_disease:
        # Get recommendations for the predicted disease
        recommendations = get_recommendations(predicted_disease)
        
        return render(request, 'pages/recommendation.html', {'disease': predicted_disease, 'recommendations': recommendations})
    else:
        # Handle case where predicted disease is not found in session
        return redirect('home')  # Redirect to home page or handle accordingly

def get_recommendations(disease):
    # Placeholder for recommendation logic
    recommendations = []

    if disease == 'Apple__Apple_scab':
        recommendations = [
            "Prune to improve air circulation and reduce humidity.",
            "Apply fungicides preventively during early spring.",
            "Choose apple varieties resistant to scab."
        ]
    elif disease == 'Apple_Black_rot':
        recommendations = [
            "Prune to improve air circulation and reduce disease pressure.",
            "Apply fungicides during bloom and growing season.",
            "Remove and destroy infected fruit mummies and cankers."
        ]
    elif disease == 'Apple_Cedar_apple_rust':
        recommendations = [
            "Remove infected leaves and stems to reduce disease spread.",
            "Apply fungicides during spring to prevent initial infections.",
            "Plant resistant apple varieties if possible."
        ]
    elif disease == 'Apple_healthy':
        recommendations = [
            "Continue regular care and maintenance practices for healthy apple trees.",
            "Monitor for early signs of disease or pests.",
            "Maintain proper nutrition and watering practices."
        ]
    elif disease == 'Blueberry_healthy':
        recommendations = [
            "Monitor for pests and diseases regularly.",
            "Prune to promote air circulation and sunlight exposure.",
            "Apply organic mulch to maintain soil moisture and health."
        ]
    elif disease == 'Cherry(including_sour)__healthy':
        recommendations = [
            "Prune regularly to remove dead or diseased branches.",
            "Apply fungicides preventively during wet seasons.",
            "Monitor for pests such as aphids and scale insects."
        ]
    elif disease == 'Cherry(including_sour)__Powdery_mildew':
        recommendations = [
            "Apply fungicides at the first sign of powdery mildew.",
            "Prune to improve air circulation and reduce humidity around the tree.",
            "Plant cherry varieties resistant to powdery mildew."
        ]
    elif disease == 'Corn(maize)__Cercospora_leaf_spot Gray_leaf_spot':
        recommendations = [
            "Rotate crops to reduce the buildup of pathogens in the soil.",
            "Apply fungicides preventively during humid conditions.",
            "Choose corn hybrids with resistance to Cercospora leaf spot."
        ]
    elif disease == 'Corn(maize)__Common_rust':
        recommendations = [
            "Plant resistant corn varieties if available in your area.",
            "Apply fungicides before the disease appears in the field.",
            "Use crop rotation and avoid planting corn in consecutive years."
        ]
    elif disease == 'Corn_(maize)__healthy':
        recommendations = [
            "Maintain proper soil fertility and crop nutrition.",
            "Control weeds and pests that can weaken corn plants.",
            "Monitor for signs of nutrient deficiency or stress."
        ]
    elif disease == 'Corn(maize)__Northern_Leaf_Blight':
        recommendations = [
            "Use crop rotation and avoid planting corn in the same field consecutively.",
            "Apply fungicides when weather conditions favor disease development.",
            "Plant corn hybrids with resistance to Northern Leaf Blight."
        ]
    elif disease == 'Grape_Black_rot':
        recommendations = [
            "Prune grape vines to improve air circulation and sunlight exposure.",
            "Apply fungicides preventively during wet seasons.",
            "Remove and destroy infected plant parts to reduce disease spread."
        ]
    elif disease == 'Grape_Esca(Black_Measles)':
        recommendations = [
            "Prune grape vines during dormancy to remove infected wood.",
            "Apply fungicides preventively during the growing season.",
            "Manage vineyard hygiene to reduce disease pressure."
        ]
    elif disease == 'Grape__healthy':
        recommendations = [
            "Maintain proper vineyard management practices.",
            "Monitor for pests and diseases regularly.",
            "Ensure adequate soil nutrition and water management."
        ]
    elif disease == 'Grape_Leaf_blight(Isariopsis_Leaf_Spot)':
        recommendations = [
            "Apply fungicides preventively during periods of high humidity.",
            "Prune to improve air circulation and reduce disease incidence.",
            "Monitor for early signs of leaf blight and treat promptly."
        ]
    elif disease == 'Orange__Haunglongbing(Citrus_greening)':
        recommendations = [
            "Remove and destroy infected trees to prevent disease spread.",
            "Apply insecticides to control psyllid vectors.",
            "Use certified disease-free nursery stock for new plantings."
        ]
    elif disease == 'Peach__Bacterial_spot':
        recommendations = [
            "Apply copper-based fungicides during the dormant season.",
            "Prune to improve air circulation and sunlight exposure.",
            "Remove and destroy infected plant material to reduce disease spread."
        ]
    elif disease == 'Peach_healthy':
        recommendations = [
            "Maintain regular pruning to remove dead or diseased wood.",
            "Monitor for pests such as aphids and scale insects.",
            "Apply balanced fertilizer to maintain tree health."
        ]
    elif disease == 'Pepper,_bell_Bacterial_spot':
        recommendations = [
            "Apply copper-based fungicides early in the season.",
            "Avoid overhead irrigation to reduce disease spread.",
            "Rotate crops with non-host plants to break disease cycles."
        ]
    elif disease == 'Pepper,_bell_healthy':
        recommendations = [
            "Monitor for aphids, thrips, and other pests regularly.",
            "Apply balanced fertilizer to promote healthy plant growth.",
            "Prune to remove old or diseased branches."
        ]
    elif disease == 'Potato_Early_blight':
        recommendations = [
            "Apply fungicides containing chlorothalonil or mancozeb.",
            "Rotate crops with non-host plants to reduce pathogen buildup.",
            "Monitor soil moisture and avoid overhead irrigation."
        ]
    elif disease == 'Potato_healthy':
        recommendations = [
            "Practice crop rotation with non-host plants.",
            "Monitor for potato pests such as Colorado potato beetles.",
            "Apply balanced fertilizer to maintain soil fertility."
        ]
    elif disease == 'Potato_Late_blight':
        recommendations = [
            "Apply fungicides containing chlorothalonil or mancozeb preventively.",
            "Practice good field hygiene to remove infected potato debris.",
            "Monitor weather conditions and irrigation practices to reduce disease risk."
        ]
    elif disease == 'Raspberry_healthy':
        recommendations = [
            "Prune raspberry canes to improve air circulation.",
            "Apply fungicides preventively during periods of high humidity.",
            "Monitor for pests such as aphids and raspberry cane borers."
        ]
    elif disease == 'Soybean_healthy':
        recommendations = [
            "Rotate soybean crops with non-host plants.",
            "Monitor for soybean pests such as aphids and soybean cyst nematodes.",
            "Apply balanced fertilizer to maintain soil fertility."
        ]
    elif disease == 'Squash_Powdery_mildew':
        recommendations = [
            "Plant resistant squash varieties if available.",
            "Apply fungicides containing sulfur or potassium bicarbonate.",
            "Prune to improve air circulation and reduce humidity around plants."
        ]
    elif disease == 'Strawberry_healthy':
        recommendations = [
            "Monitor for pests such as aphids and spider mites.",
            "Apply balanced fertilizer to promote healthy strawberry plants.",
            "Mulch around plants to maintain soil moisture and reduce weeds."
        ]
    elif disease == 'Strawberry_Leaf_scorch':
        recommendations = [
            "Remove and destroy infected leaves to reduce disease spread.",
            "Apply fungicides containing copper hydroxide or mancozeb.",
            "Monitor irrigation practices to avoid excessive moisture."
        ]
    elif disease == 'Tomato_Bacterial_spot':
        recommendations = [
            "Apply copper-based fungicides early in the season.",
            "Prune tomato plants to improve air circulation.",
            "Use drip irrigation instead of overhead irrigation."
        ]
    elif disease == 'Tomato_Early_blight':
        recommendations = [
            "Apply fungicides containing chlorothalonil or mancozeb.",
            "Rotate tomato crops with non-host plants.",
            "Prune tomato plants to improve air circulation."
        ]
    elif disease == 'Tomato_healthy':
        recommendations = [
            "Rotate tomato crops with non-host plants.",
            "Monitor for pests such as tomato hornworm and whiteflies.",
            "Apply balanced fertilizer to promote healthy plant growth."
        ]
    elif disease == 'Tomato_Late_blight':
        recommendations = [
            "Apply fungicides preventively during periods of wet weather.",
            "Remove and destroy infected tomato plants to reduce disease spread.",
            "Avoid overhead irrigation to minimize disease spread."
        ]
    elif disease == 'Tomato_Leaf_Mold':
        recommendations = [
            "Apply fungicides containing copper or sulfur.",
            "Prune to improve air circulation and reduce humidity around tomato plants.",
            "Water tomato plants at the base to avoid wetting foliage."
        ]
    elif disease == 'Tomato_Septoria_leaf_spot':
        recommendations = [
            "Apply fungicides containing chlorothalonil or copper.",
            "Prune lower tomato leaves to improve air circulation.",
            "Mulch around tomato plants to reduce soil splash."
        ]
    elif disease == 'Tomato_Spider_mites Two-spotted_spider_mite':
        recommendations = [
            "Monitor for spider mite populations regularly.",
            "Spray affected tomato plants with insecticidal soap.",
            "Improve humidity levels around tomato plants to discourage spider mites."
        ]
    elif disease == 'Tomato_Target_Spot':
        recommendations = [
            "Apply fungicides containing chlorothalonil or mancozeb.",
            "Prune to improve air circulation and reduce disease pressure.",
            "Remove and destroy affected tomato leaves and plant debris."
        ]
    elif disease == 'Tomato_Tomato_mosaic_virus':
        recommendations = [
            "Control aphid populations to prevent virus transmission.",
            "Plant virus-resistant tomato varieties.",
            "Remove and destroy infected tomato plants and weeds."
        ]
    elif disease == 'Tomato__Tomato_Yellow_Leaf_Curl_Virus':
        recommendations = [
            "Control whitefly populations to reduce virus transmission.",
            "Use virus-resistant tomato varieties if available.",
            "Remove and destroy infected tomato plants and weeds promptly."
        ]
    # Add more elif blocks for other diseases as per your requirement

    return recommendations