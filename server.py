from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template ('index.html')


@app.route('/components')
def components():
    return render_template ('components.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a',  newline='') as databasecsv:
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(databasecsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return 'form submitted'
        except:
            return 'did not save to database' 
    else:
        return 'try again'



