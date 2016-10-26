#db model
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self): #property has a misleading name. In general this method should just return True unless the object represents a user that should not be allowed to authenticate for some reason.
        return True

    @property
    def is_active(self): #property should return True for users unless they are inactive, for example because they have been banned.
        return True

    @property
    def is_anonymous(self):#property should return True only for fake users that are not supposed to log in to the system.
        return False

    def get_id(self): #method should return a unique identifier for the user, in unicode format. We use the unique id generated by the database layer for this.
        try:
            return unicode(self.id) #for Python2
        except NameError:
            return str(self.id) #for Python3

    def __repr__(self):
        return "<User %r>" % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Post %r'% (self.body)