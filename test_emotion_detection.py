def emotion_detector(text_to_analyze):
    # ... [code existant] ...

    if response.status_code == 200:
        try:
            response_data = response.json()
            emotion_predictions = response_data.get('emotionPredictions', [])
            if emotion_predictions:
                emotions = emotion_predictions[0].get('emotion', {})
                
                # Extraire les scores des émotions
                anger_score = emotions.get('anger', 0)
                disgust_score = emotions.get('disgust', 0)
                fear_score = emotions.get('fear', 0)
                joy_score = emotions.get('joy', 0)
                sadness_score = emotions.get('sadness', 0)
                
                # Appliquer un seuil pour disgust
                if disgust_score > 0.3:  # Ajustez le seuil selon vos besoins
                    dominant_emotion = 'disgust'
                else:
                    dominant_emotion = max(emotions, key=emotions.get) if emotions else 'No emotion detected'
                
                result = {
                    'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score,
                    'dominant_emotion': dominant_emotion
                }
                
                return result
            else:
                return {'error': 'No emotion predictions found'}
        except Exception as e:
            return {'error': f"Error processing response: {str(e)}"}
    else:
        return {'error': f"Request failed with status code {response.status_code}: {response.text}"}