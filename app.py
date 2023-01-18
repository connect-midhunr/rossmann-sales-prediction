from flask import Flask, request, app, jsonify, render_template
from helper import get_total_sales

# initializing app
app = Flask(__name__)

# defining index page
@app.route('/')
def index():
    return render_template('index.html')

# defining an api for predicting sales
@app.route('/predict_api', methods=['POST'])
def predict_api():
    dates = request.json['data']
    store = list(dates.values())[0]
    from_date = list(dates.values())[1]
    to_date = list(dates.values())[2]

    total_sales = get_total_sales(store, from_date, to_date)
    return jsonify(total_sales)

if __name__ == "__main__":
    app.run(debug=True)