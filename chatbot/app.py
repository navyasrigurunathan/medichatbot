from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import speech_recognition as sr

app = Flask(__name__)
app.secret_key = "your_secret_key"

# ✅ Expanded Simple Home Remedies
disease_data = {
    "fever": "Drink plenty of water, rest in a cool place, and use a wet cloth on the forehead. If it doesn’t improve, see a doctor.",
    "cold": "Stay warm, drink warm water, and inhale steam. If symptoms persist, see a doctor.",
    "diabetes": "Eat balanced meals, exercise daily, and manage stress. Always follow your doctor’s advice.",
    "hypertension": "Reduce salt intake, stay active, and practice deep breathing. If BP stays high, see a doctor.",
    "migraine": "Rest in a quiet, dark room, apply a cold cloth to your head, and breathe deeply. If it keeps happening, see a doctor.",
    "flu": "Drink warm fluids, rest well, and stay hydrated. If it gets worse, see a doctor.",
    "food poisoning": "Drink plenty of fluids, eat light meals, and rest. If vomiting continues, see a doctor.",
    "pneumonia": "Rest, drink warm fluids, and use a humidifier. If breathing is difficult, see a doctor.",
    "anemia": "Eat iron-rich foods like leafy greens, nuts, and red meat. If weakness continues, see a doctor.",
    "arthritis": "Do light stretching, use warm compresses, and avoid overuse of joints. If pain stays, see a doctor.",
    "dehydration": "Drink small sips of water frequently and rest. If feeling dizzy, see a doctor.",
    "covid-19": "Isolate, drink warm liquids, and rest. If breathing gets hard, see a doctor.",
    "malaria": "Rest, use mosquito nets, and drink fluids. If fever stays high, see a doctor.",
    "dengue": "Rest, drink coconut water or juices, and avoid mosquito bites. If bleeding starts, see a doctor.",
    "chickenpox": "Stay in a cool environment, wear loose clothes, and avoid scratching. If symptoms worsen, see a doctor.",
    "depression": "Talk to someone, go for a walk, and listen to calming music. If it persists, see a doctor.",
    "obesity": "Eat home-cooked meals, stay active, and sleep well. If weight gain continues, see a doctor.",
    "thyroid disorder": "Eat a balanced diet, manage stress, and stay active. Regular check-ups are necessary.",
    "kidney stones": "Drink plenty of water, avoid salty foods, and stay active. If pain is severe, see a doctor.",
    "ulcer": "Eat small, frequent meals, avoid spicy food, and stay stress-free. If pain continues, see a doctor.",
    "asthma": "Sit upright, take deep breaths, and avoid dust. If breathing worsens, see a doctor.",
    "sinusitis": "Use steam inhalation, drink warm liquids, and rest. If pain increases, see a doctor.",
    "eczema": "Keep skin moisturized, avoid harsh soaps, and wear cotton clothes. If itching worsens, see a doctor.",
    "constipation": "Eat fiber-rich food, drink warm water, and walk daily. If it continues, see a doctor.",
    "acidity": "Drink warm water, eat on time, and avoid lying down right after eating. If pain stays, see a doctor.",
    "heartburn": "Avoid spicy and fried foods, eat small meals, and don't lie down immediately after eating.",
    "stomach ache": "Drink warm water, rest, and avoid spicy food. If pain continues, see a doctor.",
    "insomnia": "Follow a bedtime routine, avoid caffeine, and reduce screen time before bed.",
    "cough": "Drink warm honey-lemon water, inhale steam, and avoid cold drinks.",
    "bronchitis": "Rest, stay hydrated, and use a humidifier. If symptoms worsen, see a doctor.",
    "back pain": "Use a hot or cold compress, practice light stretching, and maintain good posture.",
    "high cholesterol": "Eat a diet rich in fiber, avoid processed foods, and exercise regularly.",
    "toothache": "Rinse with warm salt water, apply a cold compress, and avoid very hot or cold foods.",
    "allergies": "Avoid allergens, take antihistamines, and drink plenty of water.",
    "ear infection": "Apply a warm compress to relieve pain. Avoid inserting anything into the ear. See a doctor if it worsens.",
    "sore throat": "Gargle with warm salt water, drink herbal tea with honey, and avoid cold drinks.",
    "eye strain": "Rest your eyes, use eye drops, and follow the 20-20-20 rule (look away every 20 minutes for 20 seconds).",
    "skin rash": "Apply aloe vera or coconut oil, avoid scratching, and wear breathable clothing.",
    "motion sickness": "Breathe deeply, avoid looking at moving objects, and eat ginger or peppermint candy.",
    "sunburn": "Apply aloe vera gel, stay hydrated, and avoid sun exposure until healed.",
    "cold sores": "Apply ice to reduce swelling, and use lip balm with lysine.",
    "menstrual cramps": "Use a heating pad, drink herbal tea, and do light stretching.",
    "headache": "Drink water, rest in a quiet dark room, and massage your temples.",
    "fatigue": "Get enough sleep, eat a balanced diet, and take short breaks from screen time.",
    "dizziness": "Sit or lie down immediately, drink water, and take deep breaths.",
}

# ✅ Set Dashboard as Homepage
@app.route('/')
def home():
    return render_template('dash.html')  # ✅ Now, dashboard is the homepage


# ✅ Get Response API (Includes Disclaimer)
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input', '').strip().lower()
    response = disease_data.get(user_input, "Sorry, I don't understand. Please consult a doctor for proper advice.")
    
    
    
    
    return jsonify({'response': response})

# ✅ Speech Recognition API (Includes Disclaimer)
@app.route('/speech', methods=['POST'])
def speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio).lower().strip()
            response = disease_data.get(user_input, "Sorry, I don't understand. Please consult a doctor for proper advice.")

            # ✅ Add disclaimer to speech responses
            response += " | Disclaimer: The chatbot may make mistakes. Always consult a doctor for any health problems."

            return jsonify({'user_input': user_input, 'response': response})
        except sr.UnknownValueError:
            return jsonify({'response': "Sorry, I couldn't understand that. Please try again."})
        except sr.RequestError:
            return jsonify({'response': "Speech service unavailable at the moment. Please try later."})

if __name__ == '__main__':
    app.run(debug=True)
