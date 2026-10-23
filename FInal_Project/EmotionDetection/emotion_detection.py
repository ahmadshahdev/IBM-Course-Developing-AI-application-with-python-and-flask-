

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
    
    # Returning the text format of the response as per initial task requirements
    return response.text