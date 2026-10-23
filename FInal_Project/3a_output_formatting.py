import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required by the Watson API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # The JSON payload containing the text to analyze
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Sending a POST request to the API
    response = requests.post(url, json=payload, headers=headers)
    
    # Parse the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extract the dictionary of emotions from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extract individual emotion scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Determine the dominant emotion by finding the key with the highest value
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the beautifully formatted dictionary as required by the final project
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }