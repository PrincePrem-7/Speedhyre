from flask import Flask, render_template, request, redirect, url_for
import os
import database

app = Flask(__name__)

# Folder Path Configuration
UPLOAD_FOLDER = '/Users/prince/Workspace/SpeedHire_Project/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/candidates')
def candidates():
    connection = database.get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Candidates")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('candidates.html', candidates=data)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['cv']
        if file.filename == '':
            return "No file selected"
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return f"File Uploaded Successfully: {file.filename}"
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
