from django.shortcuts import render
import pickle
import numpy as np
import os

# Load model from flightproject/flightproject folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = pickle.load(open(os.path.join(BASE_DIR, "flightproject", "flight_model.pkl"), "rb"))

def predict(request):
    price_usd = None
    price_inr = None

    if request.method == "POST":
        airline = request.POST['airline']
        source = request.POST['source']
        departure_time = request.POST['departure_time']
        stops = int(request.POST['stops'])
        arrival_time = request.POST['arrival_time']
        destination = request.POST['destination']
        flight_class = request.POST['class']
        departure_date = request.POST['departure_date']

        # Airline: 
        airline_map = {'AirAsia': 0, 'Air Asia': 0, 'IndiGo': 1, 'Indigo': 1, 'GO_FIRST': 2, 'GoAir': 2, 
                       'SpiceJet': 3, 'Air_India': 4, 'Air India': 4, 'Vistara': 5}
        airline_encoded = airline_map.get(airline, 0)
        
        # Source: 
        source_map = {'Delhi': 0, 'Hyderabad': 1, 'Bangalore': 2, 'Mumbai': 3, 'Kolkata': 4, 'Chennai': 5}
        source_encoded = source_map.get(source, 0)
        
        # Destination:
        dest_map = {'Delhi': 0, 'Hyderabad': 1, 'Mumbai': 2, 'Bangalore': 3, 'Chennai': 4, 'Kolkata': 5}
        destination_encoded = dest_map.get(destination, 0)
        
        # Time:
        time_map = {'Early Morning': 0, 'Morning': 1, 'Afternoon': 2, 'Evening': 3, 'Night': 4, 'Late Night': 5}
        dep_time_encoded = time_map.get(departure_time, 0)
        arrival_time_encoded = time_map.get(arrival_time, 0)
        
        # Class
        class_encoded = 1 if flight_class == 'Business' else 0
        
        # Calculate days_left (days between today and departure)
        from datetime import datetime
        today = datetime.now().date()
        dep_date = datetime.strptime(departure_date, '%Y-%m-%d').date()
        days_left = (dep_date - today).days
        
        # Feature order: airline, source_city, destination_city, departure_time, arrival_time, stops, class, days_left
        features = np.array([[airline_encoded, source_encoded, destination_encoded, dep_time_encoded, 
                            arrival_time_encoded, stops, class_encoded, days_left]])

        price_inr = model.predict(features)[0]
        # Convert INR to USD
        price_usd = price_inr / 90.71

    return render(request, "predict.html", {
        "price_usd": price_usd,
        "price_inr": price_inr,
        "show_result": price_usd is not None
    })
