from flask import Flask, render_template, jsonify
app = Flask(__name__)
from pymongo import MongoClient
import certifi
client = MongoClient('mongodb+srv://test:sparta@cluster0.citdv.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enter')
def enter():
    return render_template('nav_bar.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route("/mbti", methods=["GET"])
def user_get():
    user_list = list(db.prac.find({}, {'_id': False}))
    # print(user_list)
    return jsonify({'user_list': user_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)