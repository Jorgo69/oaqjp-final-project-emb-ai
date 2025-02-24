# EmotionDetection/emotion_detection.py

import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze:  # Gestion des entrées vides
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        
        if response.status_code == 200:
            response_data = response.json()
            emotion_predictions = response_data.get('emotionPredictions', [])
            if emotion_predictions:
                emotions = emotion_predictions[0].get('emotion', {})
                
                anger_score = emotions.get('anger', 0)
                disgust_score = emotions.get('disgust', 0)
                fear_score = emotions.get('fear', 0)
                joy_score = emotions.get('joy', 0)
                sadness_score = emotions.get('sadness', 0)
                
                dominant_emotion = max(emotions, key=emotions.get) if emotions else None
                
                return {
                    'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score,
                    'dominant_emotion': dominant_emotion
                }
            else:
                return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }
        elif response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }