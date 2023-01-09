from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority',  tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/toyproject", methods=["POST"])
def toyproject_post(): #제목, 내용, 닉네임, 비밀번호
    post_title_receive = request.form['post_title_give']
    contents_receive = request.form['contents_give']
    nickname_receive = request.form['nickname_give']
    post_password_receive = request.form['post_password_give']
    category_receive = request.form['category_give']
    post_num_receive = request.form['post_num_give']

    doc = {
        'post_title' : post_title_receive,
        'contents' : contents_receive,
        'nickname': nickname_receive,
        'post_password': post_password_receive,
        'category': category_receive,
        'post_num': post_num_receive
    }
    db.toyproject.insert_one(doc)
    return jsonify({'msg':'저장되었습니다.'})

@app.route("/toyproject", methods=["GET"])
def homework_get():
    toyproject_list = list(db.toyproject.find({}, {'_id': False}))
    return jsonify({'toyproject':toyproject_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)