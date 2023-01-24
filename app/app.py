from flask import Flask, request, app, jsonify, render_template
from helper import get_total_sales

# initializing app
app = Flask(__name__)

# defining index page
@app.route('/')
def index():
    return render_template('./pages/index.html')

# defining an api for predicting sales
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    store = int(list(data.values())[0])
    from_date = str(list(data.values())[1])
    to_date = str(list(data.values())[2])

    total_sales = jsonify(get_total_sales(store, from_date, to_date))
    total_sales.headers.add('Access-Control-Allow-Origin', '*')
    return total_sales

if __name__ == "__main__":
    app.run(debug=True)