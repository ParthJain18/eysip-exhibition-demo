# from flask import render_template, request, jsonify, make_response, send_from_directory, Blueprint, redirect, url_for, send_file
# import pandas as pd
# import os
# from process_model.main import create_process_model
# # from ocr.ocr import perform_ocr
# from werkzeug.utils import secure_filename

# # apis = Blueprint('apis', __name__)

# # Api
# @apis.route('/api/process-model', methods=['POST'])
# def process_model():

#     if 'csv-file' in request.files and request.files:
#         file = request.files['csv-file']
#         file.save('static/data/csv-file-upload.csv')
#         data = pd.read_csv('data/csv-file-upload.csv')
#     else:
#         data = pd.read_csv('static/data/csv-file.csv')

#     columns = ['timestamp', 'activity', 'user_id']
#     missing = [col for col in columns if col not in data.columns]

#     if missing:
#         response = jsonify({'error': 'Missing required columns', 'missing_columns': columns})
#         return make_response(response, 400)

#     if data[columns].isnull().any().any():
#         response = jsonify({'error': 'Null values found in required columns'})
#         return make_response(response, 400)
    
#     create_process_model(data)

#     return send_from_directory('process_model', 'ocr_result.png')

# @apis.route('/upload', methods=['POST'])
# def upload_file():
#     if 'csvFile' in request.files:
#         file = request.files['csvFile']
#         if file.filename != '':
#             filename = 'edit-csv.csv'
#             file.save(os.path.join('static/data', filename))
#     return redirect(url_for('edit_csv'))


# @apis.route('/edit-csv')
# def edit_csv():
#     # Load the CSV file from static/data/edit-csv.csv
#     # Convert it to the format expected by the template
#     # For example, read the CSV into a list of dictionaries
#     data = pd.read_csv('static/data/edit-csv.csv')
#     return render_template('edit_csv.html', data=data)

# @apis.route('/edit', methods= ['GET', 'POST'])
# def edit():
#     if request.method == 'POST':
#         print(request.form.to_dict(flat=False))
#         updated_data = request.form.to_dict(flat=False)
#         # Find the max length of any list in the dictionary
#         max_length = max(len(lst) for lst in updated_data.values())
#         # Ensure all lists have the same length, padding with None if necessary
#         for key in updated_data:
#             updated_data[key] += [None] * (max_length - len(updated_data[key]))
        
#         df = pd.DataFrame(updated_data)
#         df.to_csv('static/data/csv-file.csv', index=False)
#         # print(df.head())
#         # return redirect(url_for('edit_csv'))
#         return jsonify({"success": True, "message": "Data saved!"})
#     else:
#         data = pd.read_csv('static/data/csv-file.csv')
#         # print(data.head())
#         return render_template('edit_csv.html', data=data.to_dict(orient='records'))


# # @apis.route('/api/ocr', methods= ['POST'])
# # def get_ocr():
# #     data = request.get_json()
# #     print(data)
# #     text = perform_ocr(data['imagePath'])
# #     return make_response(jsonify({"text": text}), 200)

# # @apis.route('/api/ocr-from-file', methods=['POST'])
# # def ocr_from_file():
# #     print(request.files)
# #     if 'file' not in request.files:
# #         return jsonify({'error': 'No file part'}), 400

# #     file = request.files['file']
# #     if file.filename == '':
# #         return jsonify({'error': 'No selected file'}), 400

#     if file:
#         filepath = os.path.join('temporary_directory', secure_filename(file.filename))
#         file.save(filepath)

#         print(filepath)
#         # Replace 'perform_activity' with the actual function that processes the file
#         text = perform_ocr(filepath)
#         print(text)

#         return make_response(jsonify({'text': text}), 200)
