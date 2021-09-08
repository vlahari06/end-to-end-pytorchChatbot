# Implementation of a Contextual Chatbot in PyTorch and Flask.  
Simple chatbot 2 layer implementation with PyTorch and Flask. 

- Customization for your own use case is super easy. Just modify `intents.json` with possible patterns and responses and re-run the training (see below for more info).
- The Pytorch model is taken from the repo [https://github.com/python-engineer/pytorch-chatbot](https://github.com/python-engineer/pytorch-chatbot)
- The frontend application is created using following [https://dev.to/sahilrajput/build-a-chatbot-using-flask-in-5-minutes-574i](https://dev.to/sahilrajput/build-a-chatbot-using-flask-in-5-minutes-574i)
- The flask implementation is inspired from this tutorial [https://towardsdatascience.com/model-deployment-using-flask-c5dcbb6499c9] (https://towardsdatascience.com/model-deployment-using-flask-c5dcbb6499c9) 
- The approach is inspired by this article and ported to PyTorch: [https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077).

## Followed to video tutorial to create the pytorch model
[![Alt text](https://img.youtube.com/vi/RpWeNzfSUHw/hqdefault.jpg)](https://www.youtube.com/watch?v=RpWeNzfSUHw&list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg)

## Installation

### Create an environment
Whatever you prefer (e.g. `conda` or `venv`)
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### Activate it
Mac / Linux:
```console
. venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
```
### Install PyTorch and dependencies

For Installation of PyTorch see [official website](https://pytorch.org/).

You also need `nltk`:
 ```console
pip install nltk
 ```

If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Pytorch model Usage
Run
```console
python train.py
```
This will dump `data.pth` file. And then run
```console
python chat.py
```
## Customize
Have a look at [intents.json](intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the chat bot. You have to re-run the training whenever this file is modified.
```console
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hello, thanks for visiting",
        "Hi there, what can I do for you?",
        "Hi there, how can I help?"
      ]
    },
    ...
  ]
}
```

## Create a web Application using Flask

- install flask 
 ```console
pip install flask
 ```
- Index.html file in templates has the html and Javascript code for frontend. Detailed explanation of html file is given in [https://dev.to/sahilrajput/build-a-chatbot-using-flask-in-5-minutes-574i](https://dev.to/sahilrajput/build-a-chatbot-using-flask-in-5-minutes-574i)
- Run app.py that directs to a URL and chat with the bot
- The chat.py consists the code that takes saved model and returns the predicted sentence.

