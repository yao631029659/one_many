from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
# 就只针对一对多

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # 下面这个列是不存在的 是虚拟的 我为什么知道因为我运行了一下 用sqlite Expert 查看的
    #这个小写的user就是当前表 backref 相当于你在Post表里面建立的虚拟列名 这里用users 那么如果你先用Post来访问user 就应该写出Post.users 而不是Post.user
    posts = db.relationship('Post', backref='users', lazy='subquery')

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        # formats what is shown in the shell when print is
        # called on it
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    # post有个是实在的user_id列 就是说外键是真实存在的
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)


@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()
