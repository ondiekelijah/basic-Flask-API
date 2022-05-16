from api.app import db,ma

class User(db.Model):
    id= db.Column(db.Integer, primary_key =True)
    name=db.Column(db.String(100),nullable=False )
    email=db.Column(db.String(100),nullable=False )
    password=db.Column(db.String(150),nullable=False )
    

    def __repr__(self):
        return "<User %r>" % self.name


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "email")

user_schema = UserSchema()
users_schema = UserSchema(many=True)