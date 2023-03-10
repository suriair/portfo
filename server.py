from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def main_html():
    return render_template('index.html')

@app.route('/<inp_get>')
def main_page_opt(inp_get):
  return render_template(f'{inp_get}')

def write_to_file(data):
  with open('database.csv', 'a', newline='') as database:
    email = data['email']
    subject = data['subject']
    message = data['message']
    database_writer = csv.writer(database, delimiter= ',', quotechar= '|', quoting= csv.QUOTE_MINIMAL)
    database_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
     data = request.form.to_dict()
     write_to_file(data)
     return render_template('thankyou.html')
  else:
     return 'Oops! something went worng.'
