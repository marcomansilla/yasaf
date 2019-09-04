from flask import Flask
from routes import short

app  = Flask(__name__)
app.register_blueprint(short)

app.run(debug=True)
