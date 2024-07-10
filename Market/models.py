from Market import db, login_manager
from Market import bcrypt

from flask_login import UserMixin





class example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email_address = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(70), nullable=False, unique=False)
    budget =    db.Column(db.Integer, nullable=True, unique=False)
    items = db.relationship("Item", backref="Owned_users", lazy= True)


    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db. Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(80), nullable=False, unique=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))


    # def __repr__(self):

    #     return f'Item{id} {self.name} {price} {barcode} {description} {owner} '
    



class PetType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family = db.Column(db.String( 30), nullable=False)
    pets = db.relationship('Pet', backref='pet_family', lazy = True)
    

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String( 50), nullable=False)    
    # type = db.Column(db.String( 30), nullable=False)
    breed_name = db.Column(db.String(30), nullable=True)
    cost = db.Column(db.Integer, nullable=False)
    belongs_to = db.Column(db.Integer, db.ForeignKey('pet_type.id'))



    def __repr__(self):
        return f"Pet('{self.name}', '{self.type}', '{self.breed}', '{self.cost}')"
    
        



