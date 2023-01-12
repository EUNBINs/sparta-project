from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority',  tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('메인화면.html')

@app.route('/posting')
def mainHome():
   return render_template('boardCreate.html')

@app.route('/board')
def board():
   return render_template('board.html')

@app.route("/toyproject", methods=["POST"])
def toyproject_post(): #제목, 내용, 닉네임, 비밀번호
    title_receive = request.form['post_title_give']
    contents_receive = request.form['contents_give']
    nickname_receive = request.form['nickname_give']
    password_receive = request.form['post_password_give']
    category_receive = request.form['category_give']
    #post_num_receive = request.form['post_num_give']
    toyproject_list = list(db.toyproject.find({}, {'_id': False}))
    mx = 0 # mx라는 변수를 만들고 0으로 초기화 함(이름은 임의로 지정함) (초기화하지 않는경우 에러발생)
    for user in toyproject_list:
        mx = max(mx, user['post_num'])#max(a,b) 함수를 사용하여 반복문동안 mx와 [post_num]중 큰 숫자를 다시 mx에 넣음
        #max(1,3) = 3
        #괄호 안의 숫자들 중 가장 큰 수를 구하는 함수
    post_num = mx + 1 #이부분이 없으면 마지막 post_num과 같은 숫자가 되기 때문에 1을 더해주어야함
    doc = {
        'title' : title_receive,
        'contents' : contents_receive,
        'nickname': nickname_receive,
        'password': password_receive,
        'post_num': post_num,
    }
    db.toyproject.insert_one(doc)
    return jsonify({'msg':'게시물 등록이 완료되었습니다.'})

@app.route("/toyproject", methods=["GET"])
def toyproject_get():
    toyproject_list = list(db.toyproject.find({}, {'_id': False}))
    return jsonify({'toyproject':toyproject_list})

@app.route("/toyproject", methods=["DELETE"])

def toyproject_get():
    post_num_receive = request.form['post_num_give']
    db.toyproject.delete.one({'post_num': int(post_num_receive)})
    return jsonify({'msg':'삭제 완료'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

