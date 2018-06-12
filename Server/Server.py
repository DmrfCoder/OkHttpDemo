#-*-coding:utf-8-*-
from flask import Flask
from flask import request
import os

app = Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

@app.route('/')
def test():
    return '服务器正常运行'



#此方法处理用户注册
@app.route('/register',methods=['POST'])
def register():
    username=request.form['username']
    password=request.form['password']

    print('username:'+username)
    print('password:'+password)
    return '注册成功'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

