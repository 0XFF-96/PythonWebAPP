#Make another app.route() decorator here that takes in an integer id in the URI 

@app.route('/puppies/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def puppiesFunctionId(id):

    if reqeust.method == 'GET':
        return getPuppy(id)
    elif reqeust.method == 'PUT':
        name = reqeust.args.get('name')
        description = request.args.get('description', '')
        return updatePuppy(id, name, description)
    elif reqeust.method == 'DELETE':
        return deletePuppy(id)

    
#Call the method to edit a specific puppy 

def getAllPuppies():

    puppies = session.query(Puppy).all()
    return jsonify(Puppies=[i.serialize for i in puppies])

def getPuppy(id):

    puppy = session.query(Puppy).filter_by(id=id).one()
    return jsonify(puppy=puppy.serialize)

def makANewPuppy(name, description):
    puppy = Puppy(name=name, description = description)
    session.add(puppy)
    session.commit()
    return jsonfy(Puppy=puppy.serialize)

def updatePuppy(id, name, description):
    puppy - session.query(Puppy).filter_by(id=id).one()

    if not name:
        puppy.name = name
    if not description:
        puppy.description = description
    session.add(puppy)
    session.commit()

    return 'Updated a Puppy with id %s '%id 

def deletePuppy(id):

    puppy = session.query(Puppy).filter_by(id=id).one()
    session.delete(puppy)
    session.commit()

    return "Removed Puppy with id %s"%id 

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)


from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask.ext.httpauth import HTTpBasicAuth

auth = HTTPBasicAuth()
engine = create_engine('sqlite:///bagelShop.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()
app = Flask(__name__)

#ADD @auth.verify_passwrod here 
 
@app.route('/bagels', methods=['GET', 'POST'])
#protect this route with a required login 
def showALlBagels():
    if reqeust.method =='GET':
        bagels = session.query(Bagel).all()
        return jsonify(bagels = [bagel.serialize for bagel in bagels])
    elif reqeust.method == 'POST':
        name = request.json.get('description')
        picture = reqeust.json('picture')
        price = request.json.get('price')
        newBagel = Bagel(name=name, description = description, picture=picturee, price=price)
        session.add(newBagel)
        session.commit()

        return jsonify(newBagel.serialize)

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)



