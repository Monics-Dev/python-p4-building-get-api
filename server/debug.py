from flask import Flask
from models import Game,db
import ipdb;
from faker import Faker
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
@app.route('/debug')
def debug():
    faker = Faker()
    with app.app_context():  # Set up the application context
        
         game = Game.query.first()
         ipdb.set_trace()

         game.to_dict()


if __name__ == '__main__':
    app.run(debug= True)
 
 
    
          
 