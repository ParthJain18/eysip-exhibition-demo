from flask import Flask, render_template, jsonify, request, send_from_directory, make_response
from process_model.main import create_process_model
import pandas as pd

app = Flask(__name__)
# Pages
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/main2')
def main2():
    return render_template('main2.html')

@app.route('/main3')
def main3():
    return render_template('main3.html')
@app.route('/main5')
def main5():
    return render_template('main5.html')


# Api
@app.route('/api/process-model', methods=['POST'])
def process_model():
    file = request.files['csv-file']
    if file:
        file.save('data/csv-file.csv')
    
    data = pd.read_csv('data/csv-file.csv')

    columns = ['timestamp', 'activity', 'user_id']
    missing = [col for col in columns if col not in data.columns]

    if missing:
        response = jsonify({'error': 'Missing required columns', 'missing_columns': columns})
        return make_response(response, 400)

    if data[columns].isnull().any():
        response = jsonify({'error': 'Null values found in required columns'})
        return make_response(response, 400)
    
    create_process_model(data)

    return send_from_directory('process_model', 'ocr_result.png')

@app.route('/api/ocr', methods= ['POST'])
def get_ocr():
    return 

if __name__ == '__main__':
    app.run(port=5000, debug=True)
