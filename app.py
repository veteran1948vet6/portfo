from flask import Flask, render_template,request,redirect
import csv


app = Flask(__name__)
print(app)


@app.route('/')
def index0():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/work.html')
def work():
    return render_template('work.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/thankyou.html')
def thankyou():
    return render_template('thankyou.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'

    else:
        return 'something went wrong'


def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data["email"]
        subject= data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database,delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])