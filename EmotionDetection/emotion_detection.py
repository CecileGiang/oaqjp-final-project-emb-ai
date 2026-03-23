import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_dict = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = input_dict, headers=headers)
    formatted_response = json.loads(response.text)

    result = formatted_response['emotionPredictions'][0]['emotion']
    result['dominant_emotion'] = max(result, key=result.get)
    
    return result