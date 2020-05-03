from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        name = data['idi_name']
        email = data['idi_mail']
        message = data['idi_text']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/contact.php', methods=['POST', 'GET'])
def submit_form(): 
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('contact_submitted.html')
        except:
            return 'Did not save to database'
