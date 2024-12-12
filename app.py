from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_instructions', methods=['POST'])
def get_instructions():
    data = request.json
    emergency_type = data.get('emergencyType')

    instructions = {
        "Bleeding": [
            "Apply pressure to the wound with a clean cloth.",
            "Elevate the injured area above heart level.",
            "Seek medical help if bleeding does not stop."
        ],
        "Nose Bleed": [
            "Sit upright and lean forward.",
            "Pinch the nostrils together for 10 minutes.",
            "Apply a cold compress to the bridge of the nose."
        ],
        "Minor burns": [
            "Cool the burn with running water for 10-15 minutes.",
            "Cover with a clean, non-stick dressing.",
            "Avoid applying ice directly to the burn."
        ],
        "Severe burns": [
            "Call emergency services immediately.",
            "Do not remove clothing stuck to the burn.",
            "Cover with a sterile dressing."
        ],
        "Asthma Attack": [
            "Assist the person with their inhaler (2 puffs, 1 minute apart).",
            "Keep them calm and upright.",
            "Call emergency services if breathing does not improve."
        ],
        "Choking": [
            "Perform the Heimlich maneuver if the person cannot breathe.",
            "Encourage coughing if they can still breathe.",
            "Call emergency services if choking persists."
        ],
        "Heart Attack": [
            "Call emergency services immediately.",
            "Have the person sit or lie down comfortably.",
            "Offer aspirin if not allergic, and help them chew it.",
            "Perform CPR if necessary."
        ],
        "Cardiac Arrest": [
            "Call emergency services immediately.",
            "Begin CPR (30 chest compressions followed by 2 rescue breaths).",
            "Use an Automated External Defibrillator (AED) if available."
        ],
        "Bone Fracture": [
            "Immobilize the injured area using a splint or padding.",
            "Do not attempt to realign the bone.",
            "Apply ice packs to reduce swelling."
        ],
        "Sprain": [
            "Rest the injured area.",
            "Apply ice to reduce swelling.",
            "Compress the area with an elastic bandage.",
            "Elevate the injured limb above heart level."
        ],
        "Ingestion of Poison": [
            "Identify the substance ingested and call poison control or emergency services.",
            "Do not induce vomiting unless instructed to do so.",
            "Monitor their breathing and provide CPR if necessary."
        ],
        "Heat Stroke": [
            "Move the person to a cool, shaded area.",
            "Remove excess clothing and cool them with wet cloths or cold packs.",
            "Call emergency services immediately."
        ],
        "Hypothermia": [
            "Move the person to a warm, dry area.",
            "Cover them with blankets or warm clothing.",
            "Avoid direct heat sources or rubbing the skin."
        ],
        "Epileptic Seizure": [
            "Protect the person from injury by moving objects away.",
            "Do not restrain them or place anything in their mouth.",
            "Turn them onto their side to keep the airway clear."
        ],
        "Anaphylaxis": [
            "Administer an epinephrine injection if available.",
            "Call emergency services immediately.",
            "Keep the person lying down and elevate their legs."
        ],
        "General Shock Symptoms": [
            "Lay the person flat on their back.",
            "Elevate their legs slightly unless there is an injury.",
            "Keep them warm and comfortable.",
            "Call emergency services immediately."
        ],
        "Fainting": [
            "Lay the person flat and elevate their legs.",
            "Loosen tight clothing.",
            "Check for breathing and pulse."
        ],
        "Headache": [
            "Encourage the person to rest in a quiet, dark place.",
            "Apply a cool compress to their forehead.",
            "Offer over-the-counter pain relievers like ibuprofen."
        ],
        "Body Pain": [
            "Encourage rest and relaxation.",
            "Apply heat or cold packs to the affected area.",
            "Offer over-the-counter pain relievers."
        ],
        "Dry Tongue": [
            "Encourage the person to drink plenty of water.",
            "Avoid caffeine and alcohol.",
            "Seek medical advice if the dryness persists."
        ],
        "Stomach Pain": [
            "Have the person rest in a comfortable position.",
            "Offer small sips of water or clear fluids.",
            "Avoid solid foods until the pain subsides."
        ],
        "Low BP": [
            "Lay the person flat and elevate their legs.",
            "Keep them warm and comfortable.",
            "Offer small sips of water or electrolyte drinks."
        ],
        "High BP": [
            "Encourage the person to sit down and relax.",
            "Help them take prescribed medications if available.",
            "Avoid caffeine and salty foods."
        ],
        "Low Sugar": [
            "Offer a sugary drink, candy, or glucose tablets immediately.",
            "Encourage the person to rest until symptoms improve.",
            "Seek medical attention if symptoms persist."
        ],
        "High Sugar": [
            "Encourage hydration with water to reduce sugar concentration.",
            "Help the person take prescribed insulin or medications.",
            "Seek medical attention if symptoms worsen."
        ],
        "Pregnancy Pain": [
            "Encourage rest in a comfortable position.",
            "Apply a warm compress to the back or lower abdomen.",
            "Seek medical advice if pain is severe."
        ],
        "Menstrual Cycle": [
            "Encourage rest and relaxation.",
            "Apply a hot water bottle or heating pad to the lower abdomen.",
            "Offer over-the-counter pain relievers like ibuprofen."
        ]
    }
    return jsonify({
        "instructions": instructions.get(emergency_type, ["No instructions available for this emergency type."])
    })

@app.route('/find_hospitals')
def find_hospitals():
    # Get lat and lon from query parameters
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    if not latitude or not longitude:
        return jsonify({"error": "Location not provided"}), 400

    # Simulated hospital data (In a real application, this would be fetched from a database or external API)
    hospitals = [
        {"name": "City Central Hospital", "distance": "2.3 km"},
        {"name": "Emergency Medical Center", "distance": "5.1 km"},
        {"name": "Urban Trauma Unit", "distance": "7.6 km"}
    ]

    return jsonify({"hospitals": hospitals})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_hospitals')
def find_hospitals():
    # Get lat and lon from query parameters
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    logger.debug(f"Received location - Latitude: {latitude}, Longitude: {longitude}")

    if not latitude or not longitude:
        logger.error("Location parameters missing")
        return jsonify({"error": "Location not provided"}), 400

    try:
        # SIMULATED HOSPITAL DATA 
        # In a real application, this would be fetched from a database or external API
        hospitals = [
            {
                "name": "Nanjappa Life Care, Shivamogga", 
                "distance": "3.4 km",
                "mapUrl": "https://maps.app.goo.gl/WvBmsx4TcHB212Bi9"
            },
            {
                "name": "MC Gann Hospital, Shivamogga", 
                "distance": "6.9 km",
                "mapUrl": "https://maps.app.goo.gl/1yC4Bd3DEkTBGFMX6"
            },
            {
                "name": "Metro Hospital, Shivamogga", 
                "distance": "7.6 km",
                "mapUrl": "https://maps.app.goo.gl/yEeUEf2sk66K3L9q8"
            }
        ]

        logger.debug(f"Returning hospitals: {hospitals}")
        return jsonify({"hospitals": hospitals})

    except Exception as e:
        logger.error(f"Error in find_hospitals: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)