from flask import Flask, jsonify
from flask_restful import Api
from resources.user import  User, UserRegister, UserLogin, UserLogout, DateExtend
from resources.food import Food,FoodResgister,FoodSearch
from resources.meal_template import MealTemplate,MealTemplateRegister,MealTemplateSearch
from flask_jwt_extended import JWTManager
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=3600)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(seconds=3600)
#app.config['JWT_BLACKLIST_ENABLED'] = True
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/user/register')
api.add_resource(UserLogin, '/user/login')
api.add_resource(UserLogout, '/user/logout')
api.add_resource(DateExtend, '/user/date_extend/<int:user_id>')
api.add_resource(Food, '/food/<int:food_id>')
api.add_resource(FoodSearch,'/food')
api.add_resource(FoodResgister, '/food')
api.add_resource(MealTemplate, '/meal_template/<int:meal_template_id>')
api.add_resource(MealTemplateRegister, '/meal_template/register')
api.add_resource(MealTemplateSearch, '/meal_template')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)