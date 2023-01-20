import requests
from flask import Flask, render_template,request

api_key='NNmLnS0p097GAVedJjOzMu4SoxTUuD90'



url = "https://api.ai21.com/studio/v1/j1-grande/complete"
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    response = requests.post(url, json=payload, headers=headers)
    #  print(response.text)
    if request.method == 'POST':
        print("text =", request.form['user_text'])
    data = response.text
    return render_template('index.html',data=data)


payload = {"prompt": 'what is life?',
    "numResults": 1,
    "maxTokens": 16,
    "minTokens": 0,
    "temperature": 0.7,
    "topP": 1,
    "topKReturn": 0,
    "frequencyPenalty": {
        "scale": 1,
        "applyToWhitespaces": True,
        "applyToPunctuations": True,
        "applyToNumbers": True,
        "applyToStopwords": True,
        "applyToEmojis": True
    },
    "presencePenalty": {
        "scale": 0,
        "applyToWhitespaces": True,
        "applyToPunctuations": True,
        "applyToNumbers": True,
        "applyToStopwords": True,
        "applyToEmojis": True
    },
    "countPenalty": {
        "scale": 0,
        "applyToWhitespaces": True,
        "applyToPunctuations": True,
        "applyToNumbers": True,
        "applyToStopwords": True,
        "applyToEmojis": True
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer NNmLnS0p097GAVedJjOzMu4SoxTUuD90"
}

if __name__ == '__main__':
     app.run()