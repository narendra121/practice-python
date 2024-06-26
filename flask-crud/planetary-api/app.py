from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Float
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager,jwt_required,create_access_token
from flask_mail import Mail,Message

app=Flask(__name__)



@app.route('/health')
def statusCheck():
    return jsonify(message='Server is Up!')

@app.errorhandler(404)
def not_found(error):
    return jsonify(message="that resource not found"),200

# http://localhost:5000/parameters?name=narend&age=13
@app.route("/parameters")
def parameters():
    # name= request.args.get('name')
    age= int(request.args.get('age'))
    if age<18:
        return jsonify(message='you child guy'),401
    else:
        return jsonify(message='you big guy'),200
    
# http://localhost:5000/url_variables/narend/13  
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str,age:int):
    # name= request.args.get('name')
    # age= request.args.get('age')
    if age<18:
        return jsonify(message='you child guy'),401
    else:
        return jsonify(message='you big guy'),200
    

@app.route('/planets',methods=['GET'])
def planets():
    planets_list=Planet.query.all()
    result=planets_schema.dump(planets_list)
    return jsonify(result)

########################### DataBASE ##################
    
basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'planets.db')
db=SQLAlchemy(app)
   
class User(db.Model):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    first_name= Column(String)
    last_name= Column(String)
    email= Column(String,unique=True)
    password= Column(String)

class Planet(db.Model):
    __tablename__='planets'
    planet_id=Column(Integer,primary_key=True)
    planet_name=Column(String)
    planet_type=Column(String)
    home_star= Column(String)
    mass= Column(Float)
    radius=Column(Float)
        
@app.cli.command('db_create')
def db_created():
    db.create_all()
    print('Database created!')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped')

@app.cli.command('db_seed')
def db_seed():
    mercury=Planet(planet_name='Mercury',
                   planet_type='Class D',
                   home_star='Sun',
                   mass=3.222,
                   radius=1543
                   )
    
    venus=Planet(planet_name='Venus',
                   planet_type='Class K',
                   home_star='Sun',
                   mass=4.222,
                   radius=1343
                   )
    
    earth=Planet(planet_name='Earth',
                   planet_type='Class M',
                   home_star='Sun',
                   mass=5.222,
                   radius=2343
                   )
    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)

    test_user = User(first_name='Narendra',
                     
                     last_name='Y',
                     email='ynd@aha.com',
                     password='12345'
                     )
    db.session.add(test_user)

    db.session.commit()
    print('Database seeded!')


#for jason conversion
ma=Marshmallow(app)
class UserSchema(ma.Schema):
    class Meta:
        fields= ('id','first_name','last_name','email','password')

class PlanetSchema(ma.Schema):
    class Meta:
        fields=('planet_id','planet_name','planet_type','home_star','mass','radius')


user_schema=UserSchema() #single
users_schema=UserSchema(many=True) #multiple objects

planet_schema=PlanetSchema()
planets_schema=PlanetSchema(many=True)

#authentication

app.config['JWT_SECRET_KEY']='super-secret'
jwt=JWTManager(app)

@app.route('/register',methods=['POST'])
def register():
    email=request.form['email']
    test=User.query.filter_by(email=email).first()
    if test:
        return jsonify(message='that email already exists')
    else:
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        password=request.form['password']
        user=User(first_name=first_name,last_name=last_name,email=email,password= password)
        db.session.add(user)
        db.session.commit()
        return jsonify(message='User created successfully'),201
    
@app.route('/login',methods=['POST'])
def login():
    if request.is_json:
        email=request.json['email']
        password= request.json['password']
    else:
        email=request.form['email']
        password=request.form['password']
    
    test=User.query.filter_by(email=email,password=password).first()
    if test:
        access_token=create_access_token(identity=email)
        return jsonify(message='Login succeeded',access_token=access_token)
    else:
        return jsonify(message="Bad email or password !"),401
    


#Email
app.config['MAIL_SERVER']='live.smtp.mailtrap.io'
app.config['MAIL_USERNAME']=os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD']=os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
app.config['MAIL_PORT']=587
mail=Mail(app)

@app.route('/reset_pass/<string:email>',methods=['GET'])
def resetPassword(email: str):
    user=User.query.filter_by(email=email).first()
    if user:
        msg=Message("your planetary api password is "+user.password,
                    sender='mailtrap@demomailtrap.com',
                    recipients=[email]
                    )
        mail.send(msg)
        return jsonify(messaage="password sent to "+email)
    else:
        return jsonify(message="that email doesn't exist")
    
#crud
    
# localhost:5000/planet/1
@app.route('/planet/<int:planet_id>',methods=['GET'])
def planet_details(planet_id: int):
    planet =Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        result=planet_schema.dump(planet)
        return jsonify(result)
    else:
        return jsonify(message='That planet not exists!')
    
@app.route('/add_planet',methods=['POST'])
@jwt_required()
def add_planet():
    planet_name=request.form['planet_name']
    test=Planet.query.filter_by(planet_name=planet_name).first()
    if test:
        return jsonify("there is already a planet by that name"),409
    else:
        planet_type= request.form['planet_type']
        home_star=request.form['home_star']
        mass=float(request.form['mass'])
        radius=float(request.form['radius'])
        new_planet=Planet(planet_name=planet_name,planet_type=planet_type,home_star=home_star,mass=mass,radius=radius)

        db.session.add(new_planet)
        db.session.commit()

        return jsonify(message="you added the planet")
    
@app.route('/update_planet',methods=["PUT"])
@jwt_required()
def update_planet():
    planet_id=int(request.form['planet_id'])
    planet= Planet.query.filter_by(planet_id=planet_id).first()
    
    if planet:
        planet.planet_name=request.form['planet_name']
        planet.planet_type=request.form['planet_type']
        planet.home_star =request.form['home_star']
        planet.radius=float(request.form['radius'])
        planet.mass=float(request.form['mass'])
        db.session.commit()
        return jsonify(message="You updated a planet"),202
    else:
        return jsonify(message="That planet doesnt exist")
    

@app.route('/remove/<int:planet_id>',methods=['DELETE'])
@jwt_required()
def remove_planet(planet_id: int):
    planet=Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return jsonify(message="You have deleted the record"),202
    else:
        return jsonify(message="Record not found")