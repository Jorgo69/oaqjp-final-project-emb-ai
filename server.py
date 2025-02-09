"""
Module principal de l'application Flask pour analyser les émotions dans un texte.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

# Initialiser l'application Flask
APP = Flask(__name__)

@APP.route('/')
def home():
    """
    Route par défaut pour afficher un message d'accueil.
    """
    return (
        "Bienvenue dans l'API d'analyse des émotions ! "
        "Envoyez une requête POST à /emotionDetector avec un texte JSON."
    )

@APP.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Route pour détecter les émotions dans un texte fourni via une requête POST.
    """
    input_text = request.json.get('text', '')

    result = emotion_detector(input_text)

    if result['dominant_emotion'] is None:
        # Si dominant_emotion est None, retourner un message d'erreur
        return jsonify({
            "error": "Texte invalide ! Veuillez réessayer !"
        }), 400

    # Formater la réponse
    response = {
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }

    return jsonify(response)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000)
    