from flask import Flask
import random

app = Flask(__name__)

@app.route('/temperature')
def temperature():
    # Returns a fake temperature as a plain string for easy Grafana parsing
    return str(round(random.uniform(20.0, 30.0), 2))

@app.route('/status')
def status():
    return "OK"

@app.route('/health')
def health():
    return "healthy"

if __name__ == '__main__':
    # Listen on all network interfaces
    app.run(host='0.0.0.0', port=5000)
    