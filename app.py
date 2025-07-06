from flask import Flask, request, jsonify
from recommendation import Recommender

app = Flask(__name__)
recommender = Recommender()


@app.route('/')
def home():
    return "👋 Welcome to the Product Recommendation API. Use /recommend?customer_id=Cust_2"



@app.route('/recommend', methods=['GET'])
def recommend():
    customer_id = request.args.get('customer_id')
    if not customer_id:
        return jsonify({"error": "Please provide a customer_id query parameter."}), 400

    recommendations = recommender.recommend(customer_id)
    if isinstance(recommendations, str):
        return jsonify({"error": recommendations}), 404

    return jsonify({"customer_id": customer_id, "recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
