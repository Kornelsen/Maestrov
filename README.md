# Maestrov
Maestrov is a web application that utilizes the Markov Process to analyze and produce songs based on probabilities and predictions generated using the structure of inputted note sequences. This project was originally built for McHacks 2017, an annual hackathon put on at McGill University in Montreal, Quebec.

[Winner of the "Smartest X Prize" @McHacks 2017](https://devpost.com/software/maestrov)

### Installation
```
pip install flask
pip install markovify
pip install pysynth
```
### Deployment
```
FLASK_APP='Maestrov'
flask run
```
App runs at http://127.0.0.1:5000
### Technology
Maestrov was built using the following:

| Tech |  |
| ------ | ------ |
| Flask | http://flask.pocoo.org |
| Markovify | https://github.com/jsvine/markovify/blob/master/README.md |
| PySynth | https://github.com/mdoege/PySynth/blob/master/README.md |
