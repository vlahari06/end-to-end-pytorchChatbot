from flask import Flask, render_template, request
import torch
import json
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize, stem
import random



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    bot_name = "Sam"
    userText = request.args.get('msg')
    data = torch.load("data.pth")
    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]
    w = tokenize(userText)
    X = bag_of_words(w,all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)


    model = NeuralNet(input_size, hidden_size, output_size)
    model.load_state_dict(model_state)
    model.eval()

    with open('intents.json', 'r') as json_data:
        intents = json.load(json_data)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                prediction = random.choice(intent['responses'])#print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        #print(f"{bot_name}: I do not understand...")
        prediction = "I do not understand..."

    return str(prediction)


if __name__ == "__main__":
    app.run()
    #app.run(host='0.0.0.0',port=8080)