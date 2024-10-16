from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_band_name():
    city = request.form['city']
    pet = request.form['pet']
    band_name = city + " " + pet
    return f'Your band name could be: {band_name}'

if __name__ == '__main__':
    app.run(debug=True)
