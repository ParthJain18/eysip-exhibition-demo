from flask import render_template, Blueprint
import pandas as pd
# from main import app

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('home.html')

@routes.route('/activity')
def activity():
    return render_template('activity1.html')
@routes.route('/ocr')
def ocr():
    return render_template('ocr.html')


@routes.route('/main5')
def main5():
    return render_template('main5.html')

@routes.route('/edit_csv')
def edit_csv():
    data = pd.read_csv('static/data/csv-file.csv')
    return render_template('edit_csv.html', data = data.to_dict(orient='records'))

@routes.route('/game')
def game():
    return render_template('game.html')

@routes.route('/game1')
def game1():
    return render_template('game1.html')