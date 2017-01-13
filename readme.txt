使用backref的效果
posts = db.relationship('Post', backref='users', lazy='subquery')
posts 决定了在父表访问子表的使用用user.posts
backref='users'决定了子表访问父表的时候用post.users 而是不是post.user
第一 父表读取子表
user=User('yoyo3')
post=Post('post1')
user.posts.append(post)
db.session.add(user)
db.session.commit()
User.query.all()

第二 子表读取父表
post=Post.query.filter_by(title='post1').first()
post.users