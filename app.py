from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Live presentation 2025 '

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
