from flask import Flask
from ex_blueprint import example_blueprint

app = Flask(__name__)
app.register_blueprint(example_blueprint)

#Models

#Auth & New User

#Dashboard


@app.route('/')
def index():
    return "This is an example app"



if __name__ == '__main__':
    app.run(debug=True, port=5000)