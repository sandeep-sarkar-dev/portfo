from flask import Flask,render_template,request,redirect
import csv

app=Flask(__name__)

print(__name__)

@app.route('/')
def my_homepage():
	return render_template('index.html')

@app.route('/<string:page_name>')
def page_nm(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		try:
			data=request.form.to_dict()
			write_to_csv(data)
			return redirect('thankyou.html')
		except:
			return "did not save to database"
	else:
		return 'Something went wrong..Please try again !!!!!'

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_writer=csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
		
    #return 'Thanks for submitting the form'

#@app.route('/works.html')
#def hello_works():
#	return render_template('works.html')

#@app.route('/about.html')
#def hello_about():
#	return render_template('about.html')

#@app.route('/contact.html')
#def hello_contact():
#	return render_template('contact.html')

#@app.route('/components.html')
#def hello_components():
#	return render_template('components.html')

@app.route('/index.html')
def my_homeindex():
	return render_template('index.html')

@app.route('/work.html')
def hello_work():
	return render_template('work.html')
