import flask

app = flask.Flask(__name__)

app.config["DEBUG"] = True

@app.route('/', methods=['GET'])

def home():
    return "<h1>The 4th Generation Warfare Archive</h1><p>This site is a prototype API for accessing historical information on 4th Generation warefare.</p>"

app.run(host='0.0.0.0')
