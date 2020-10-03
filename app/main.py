from flask import Flask
app = Flask(__name__)

@app.route('/')
def test_app():
    return 'App is working!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')