from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index2.html')


@app.route("/toyproject", methods=["POST"])
def toyproject_post(): #제목, 내용, 닉네임, 비밀번호
    title_receive = request.form['post_title_give']
    contents_receive = request.form['contents_give']
    nickname_receive = request.form['nickname_give']
    password_receive = request.form['post_password_give']
    category_receive = request.form['category_give']
    #post_num_receive = request.form['post_num_give']
    postingnumber = list(db.toyproject.find({}, {'_id': False}))
    post_num = len(postingnumber) + 1
    doc = {
        'title' : title_receive,
        'contents' : contents_receive,
        'nickname': nickname_receive,
        'password': password_receive,
        'category': category_receive,
        'post_num': post_num
    }
    db.toyproject.insert_one(doc)
    return jsonify({'msg':'저장되었습니다.'})

@app.route("/toyproject", methods=["GET"])
def toyproject_get():
    post_list = list(db.toyproject.find({},{'_id':False}))
    return jsonify({'post_list': post_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)