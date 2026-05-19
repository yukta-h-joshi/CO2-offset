from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__, static_folder='.', template_folder='.')

# 1. Core Carbon Calculation Logic (Your Python Engine)
def calculate_carbon_sequestration(species, count=1, age=5):
    # Standard baseline sequestration metrics (kg of CO2 per tree per year)
    species_database = {
        "neem": 20.0,
        "ashoka": 15.0,
        "peepal": 22.5,
        "banyan": 25.0
    }
    
    # Clean and match the user input species
    species_key = str(species).strip().lower()
    base_rate = species_database.get(species_key, 15.0) # Default to 15 if unknown
    
    # Scale based on tree age and quantity
    total_sequestration = base_rate * count * (age / 5)
    return round(total_sequestration, 2)

# 2. Route to Serve Your Frontend Layout
@app.route('/')
def home():
    # This renders your index.html file directly from your folder
    return render_template('index.html')

# 3. Route to Process Data Sent From Frontend
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    # Safely extract values from the incoming frontend request
    species = data.get('species', 'neem')
    try:
        count = int(data.get('count', 1))
        age = int(data.get('age', 5))
    except ValueError:
        return jsonify({"error": "Invalid numerical inputs"}), 400
        
    # Run the math engine
    result = calculate_carbon_sequestration(species, count, age)
    
    # Send the answer back to the UI as clean JSON
    return jsonify({
        "status": "success",
        "species_calculated": species,
        "total_co2_sequestered_kg": result
    })

if __name__ == '__main__':
    # Start the local development server
    app.run(debug=True)