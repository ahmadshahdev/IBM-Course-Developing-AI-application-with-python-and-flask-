from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint to receive text and return emotion analysis.
    """
    # Retrieve the text to analyze from the GET request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    
    # Extract the emotion scores and dominant emotion from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Check if dominant_emotion is None (which happens if the text is invalid)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
        
    # Return the beautifully formatted string as required by the project specifications
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, "
        f"'joy': {joy_score} and 'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Endpoint to render the main HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on standard host and port
    app.run(host="0.0.0.0", port=5000)