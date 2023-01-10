from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('DB주소')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('boardCreate.html')

@app.route("/toyproject", methods=["POST"])
# 제목, 내용, 닉네임, 비밀번호
def toyproject_post():
    nick_name_receive = request.form['nickname_give']
    post_password_receive = request.form['post_password_give']
    post_title_receive = request.form['post_title_give']
    contents_receive = request.form['contents_give']
    category_receive = request.form['category_give']
    post_num_receive = request.form['post_num_give']

    doc = {
        'nick_name': nick_name_receive,
        'post_paswword': post_password_receive,
        'post_title': post_title_receive,
        'contents': contents_receive,
        'category': category_receive,
        'post_num': post_num_receive
    }
    db.toyproject.insert_one(doc)

    return jsonify({'msg':'게시물 등록이 완료되었습니다'})

@app.route("/homework", methods=["GET"])
def homework_get():
    comment_list = list(db.homework.find({},{'_id':False}))
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=8000, debug=True)