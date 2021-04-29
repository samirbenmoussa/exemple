from app import db
class User(db.Model):
    __tablename__ = 'utlisateur' 
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False, unique=True)
    prenom = db.Column(db.String, nullable=False, unique=True)
    cin = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=True)
    job = db.Column(db.String, nullable=False, unique=True)
    adresse = db.Column(db.String, nullable=False, unique=True)
    ville = db.Column(db.String, nullable=False, unique=True)

    
    

        

