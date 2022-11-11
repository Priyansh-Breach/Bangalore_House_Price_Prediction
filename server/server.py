from flask import Flask, request, jsonify, request
import util

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():

    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    bhk = int(request.form['bhk'])
    location = request.form['location']
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    response = jsonify({
        'locations': util.get_estimates_price(location, total_sqft, bath, balcony, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print('Starting python flask server for home price prediction...')
    app.run(debug=True)
