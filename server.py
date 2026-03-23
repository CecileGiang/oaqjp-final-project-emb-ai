''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows each possible emotion with the associated score,
        and highlights the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    de = response['dominant_emotion']

    # GESTION DE L'ERREUR : Si l'entrée était vide ou invalide (dominant_emotion est None)
    if de is None:
        return "Invalid text! Please try again!"

    items = [f"'{e}': {s}" for e, s in response.items() if e != 'dominant_emotion']

    if len(items) > 1:
        emos = ", ".join(items[:-1])
        emos = f"{emos} and {items[-1]}."
    else:
        emos = f"{items[0]}." if items else ""

    return f"For the given statement, the system response is {emos} The dominant emotion is {de}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
