import requests
from flask import Flask, render_template,request

api_key='NNmLnS0p097GAVedJjOzMu4SoxTUuD90'



url = "https://api.ai21.com/studio/v1/j1-grande/complete"
app = Flask(__name__)


def get_data(text):
    
    payload={
            "prompt": str("Q:"+text),
            "numResults": 1,
            "maxTokens": 40,
            "temperature": 0,
            "topKReturn": 0,
            "topP":1,
            "countPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "frequencyPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "presencePenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
        },
        "stopSequences":["Q:"]
        }
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer NNmLnS0p097GAVedJjOzMu4SoxTUuD90"
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    print(data)
    return data['completions'][0]['data']['text']
@app.route('/',methods=['GET','POST'])
def index():
    data=''
    #  print(response.text)
    if request.method == 'POST':
        print("text =", request.form['user_text'])
        text=request.form['user_text']
        data=get_data(text)
        
    
    return render_template('index.html',data=data)




if __name__ == '__main__':
     app.run()
     
 