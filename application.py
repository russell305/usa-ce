# export FLASK_APP=application.py
# set FLASK_APP=application.py
# top/mac bottom/windows
export DATABASE_URL="postgres://ayjxjjxhgpzlnl:f150cc319da46e38a1fb398ee335d98fa5468668d0d8aa3da415aed475d08f9b@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d9prh5mib7dh2p"


# put link on sign-in page to other courses...need to take more courses?

# fix title tags

#p tags need to have font size or make h-tag,for SEO. after all templates done.



#fix wrong password and cancel, there are duplicates

#adminer /

#test stripe black background

#heroku logs --tail
# heroku add ons
# move pa-image into folder do this last

from flask import Flask, render_template, request, session, jsonify, redirect, url_for# Import the class `Flask` from the `flask` module, written by someone else.
from flask_session import Session
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from pandas import read_csv
import json #for Python to Javascript
import requests #for JSON
import stripe
import hashlib #password
import re  #regex
import datetime
import math
import csv
import utils
import ia_courses
import lhv_courses
import health_courses

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

from flask_sslify import SSLify
sslify = SSLify(app)

Session (app)
engine = create_engine("postgres://iykazvclamrzem:140bdec1e446a9119d4fb1c9e20d89fb17716e702de72b7be09f2b2e53b86d36@ec2-50-19-127-115.compute-1.amazonaws.com:5432/d134n6bd1767sd")
#talk to datbase wiTh SQL. Object used to manage connections to database.
#Sending data to and from database.
db = scoped_session(sessionmaker(bind=engine)) # for individual sessions

#0275d8   primary  blue color

# utils.recent_certificates()
# utils.recent_certificates_csv()

# db.execute("CREATE TABLE fl_life_health_agent_1(id SERIAL PRIMARY KEY, name VARCHAR NOT NULL UNIQUE,email VARCHAR NOT NULL, password VARCHAR NOT NULL, address VARCHAR NOT NULL,first VARCHAR NOT NULL,last VARCHAR NOT NULL,license_no VARCHAR NOT NULL,license_state VARCHAR NOT NULL, maiden VARCHAR NOT NULL, color VARCHAR NOT NULL, ethics_paid Boolean, ethics_course  Boolean, ethics_score_date VARCHAR, course_2_paid Boolean, course_2_complete Boolean, course_2_score_date VARCHAR,  course_3_paid Boolean, course_3_complete Boolean, course_3_score_date VARCHAR, course_4_paid Boolean, course_4_complete Boolean, course_4_score_date VARCHAR)")

#relational database
# db.execute("CREATE TABLE ia_results_1(id SERIAL PRIMARY KEY, name VARCHAR NOT NULL UNIQUE,name_id INTEGER REFERENCES fl_public_adjuster_1)")
# db.commit()
# user = db.execute("SELECT fl_public_adjuster_1.name FROM fl_public_adjuster_1 JOIN ia_results_1 ON fl_public_adjuster_1.id = ia_results_1.name_id WHERE ia_results_1.name = 'frank'  ").fetchall()
# now = datetime.datetime.now()
# print("today-date", now)
'''
import pandas as pd

name_dict = {
			'Name': ['a','b','c','d'],
			'Score': [90,80,95,20]
		  }

df = pd.DataFrame(name_dict)

print (df)
df.to_csv('file_name.csv', index = False)

df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
				   'mask': ['red', 'purple'],
				   'weapon': ['sai', 'bo staff']})

df.to_csv('test.csv', index=False)


import pandas as pd
df = pd.DataFrame([['Bob', 'Builder'], ['Sally', 'Baker'], ['Scott', 'Candle Stick Maker']],
columns=['name', 'occupation'])
# df.to_csv('lhv-20-26000-30000.csv', index = False)
'''

'''
df = read_csv("licenses-7-2020.csv")
# newdf = df[(df.License_Desc == "LIFE INCL VAR ANNUITY & HEALTH") & (df.CE_Scenario == "CE, with more than 6 years")]
# newdf.to_csv('newdf.csv', index = False)
# print("total florida licenses",df.count())
df1 = df[df['License TYCL Desc'] == 'HEALTH']
# df1 = df[df['License_Desc'] == 'LIFE INCL VAR ANNUITY & HEALTH']
# df1 = df[df['License_Desc'] == 'SURPLUS LINES']


print("h",df1.count())
# df1.to_csv('test1.csv', index=False, columns=['Full Name','First Name','License_Desc' ])
# df2 = df1[df1['CE_Scenario'] == "CE, with more than 6 years"]


# print("lhv > 6",df2.count())
# df3 = df2.filter(["Email", "CE_Scenario"])
df3 = df1[['Email Address', 'First Name','Last Name']].head(6000).tail(1000)
# df3 = df1['Email Address'].head(5000).tail(2000)

df3.to_csv('h-5000-6000.csv', index = False)
'''


'''
#for end of month deadline
df = read_csv("licenses-7-2020.csv")
print("total florida licenses",df.count())
df1 = df[df['License TYCL Desc'] == 'HEALTH']
# df1 = df[df['License TYCL Desc'] == 'PUBLIC ADJUSTER-ALL LINES']
# df1 = df[df['License_Desc'] == 'LIFE INCL VAR ANNUITY & HEALTH']

print("lhv",df1.count())
df2 = df1[df1['CE Due Date'] == "7/31/2020 12:00:00 AM"]
# print("due july lhv",df2.count())
# df3 = df2[df2['CE_Hours_Required'] == '="20"']
# df3 = df2[df2['CE Hours Applied'] != '="24"']
# df3 = df2[df2['CE Hours Applied'] == '="0"'] &  df2[df2['CE Hours Applied'] != '="20"']
df3 = df2[df2['CE Hours Applied'] != '="24"']
# newdf = df[(df.CE Hours Applied != '="24"') & (df.CE_Scenario == "CE, with more than 6 years")]
print("0 hours",df3.count())
# df4 = df3[['Email Address', 'First Name','Last Name']].head(1500)
df4 = df3[['Email Address', 'First Name','Last Name']]
# df4 = df3['Email Address']
df4.to_csv('240-july-end-1.csv', index = False)
'''

#adds comma
# df3.to_csv('lh-group-1.csv', index=False, header=False, line_terminator=',\n')

# used to force stuff in database
'''
email = "jeffg@fsclaimsadj.com"
ethics_paid = True
flood_paid = True
property_paid = True
# course_3_paid=True

# user =  db.execute("SELECT *  FROM fl_public_adjuster_1 WHERE email = :email ", {"email": email}).fetchall()
# db.execute("UPDATE fl_independent_adjuster_1 SET ethics_paid = :ethics_paid WHERE email = :email", {"ethics_paid": ethics_paid, "email": email})
db.execute("UPDATE fl_public_adjuster_1 SET ethics_paid = :ethics_paid WHERE email = :email", {"ethics_paid": ethics_paid, "email": email})
db.execute("UPDATE fl_public_adjuster_1 SET flood_paid = :flood_paid WHERE email = :email", {"flood_paid": flood_paid, "email": email})
db.execute("UPDATE fl_public_adjuster_1 SET property_paid = :property_paid WHERE email = :email", {"property_paid": property_paid, "email": email})
db.commit()

print("dbchangzes")
'''
# email = "aupds24@hotmail.comBujosa@24"
# db.execute("UPDATE fl_life_health_agent_1 SET course_2_score_date = :course_2_score_date WHERE email = :email", {"course_2_score_date": course_2_score_date, "email": email})
# name = db.execute("SELECT name FROM fl_health_agent_1 WHERE email = :email", {"email": email})
# name = name[0]
# db.commit()
# id = db.execute("SELECT name, password FROM fl_life_health_agent_1 WHERE email = :email" , {"email": email}).fetchall()
# last='Fowler'
# id = db.execute("SELECT * FROM fl_life_health_agent_1 WHERE last = :last" , {"last": last}).fetchall()
# id = id[0]
# print(id)
'''
email="russm305@gmail.com"
db.execute("DELETE FROM fl_public_adjuster_1 WHERE email = :email" , {"email": email})
db.execute("DELETE FROM fl_independent_adjuster_1 WHERE email = :email" , {"email": email})
db.execute("DELETE FROM fl_health_agent_1 WHERE email = :email" , {"email": email})
db.execute("DELETE FROM fl_life_health_agent_1 WHERE email = :email" , {"email": email})
db.commit()

print("dbchange")
'''

def result_chapter():
	wrong_answer = False
	if session.get("admin") is True:
		result_1 = "correct"
		result_2 = "correct"
	else:
		result_1 = request.form.get("1", "")
		if result_1 != "correct":
			wrong_answer = True
			result_1 = "wrong"
		result_2 = request.form.get("2", "")
		if result_2 != "correct":
			wrong_answer = True
			result_2 = "wrong"
	result_data = [wrong_answer, result_1, result_2]
	return result_data

def check_admin():
	if session.get("admin") is True:
		admin_button = True
	else:
		admin_button = False
	return admin_button

def final_results(num_questions):
	num_correct = 0
	exam_pass = False

	for x in range(num_questions):
		result = request.form.get(str(x+1), "")
		print (result)
		if result == "correct":
			num_correct += 1

	if session.get("admin") is True:
		num_correct = num_questions

	final_score = num_correct/num_questions
	final_score = final_score * 100
	final_score = math.trunc(final_score)

	# final_score = 92

	if final_score >= 70:
		exam_pass = True

	final_score = str(final_score)
	now = datetime.datetime.now()
	month = str(now.month)
	day = str(now.day)
	year = str(now.year)
	date_fin = month + "/" + day + "/" + year

	final_score_data = [final_score, exam_pass, date_fin]
	return final_score_data

@app.route("/", methods = ["GET", "POST"])
def index():
	session['admin'] = False #causing errors timing out
	return render_template("main_page.html")

@app.route('/faq/', methods = ["GET", "POST"])
def faq():
	return render_template("faq.html")

@app.route('/contact/', methods = ["GET"])
def contact():
	return render_template("contact.html")

@app.route('/canceled/', methods = ["GET","POST"])
def canceled():
	return "Payment not accepted try again"

@app.route('/wrong_password/', methods = ["GET"])
def wrong_password():
	return render_template("wrong_password.html")

@app.route('/forgot_password/', methods = ["GET","POST"])
def forgot_password():
	return render_template("forgot_password.html")

@app.route('/forgot_password_result/', methods = ["GET","POST"])
def forgot_password_result():
	email_regex = request.form.get("email")
	email = re.sub("[ \s]","", email_regex.lower())
	color_regex = request.form.get("color")
	color = re.sub("[ \s]","",color_regex.lower())

	if db.execute("SELECT id FROM fl_public_adjuster_1 WHERE email = :email AND color = :color", {"email": email, "color": color}).rowcount == 0:
		if db.execute("SELECT id FROM fl_independent_adjuster_1 WHERE email = :email AND color = :color", {"email": email, "color": color}).rowcount == 0:
			if db.execute("SELECT id FROM fl_health_agent_1 WHERE email = :email AND color = :color", {"email": email, "color": color}).rowcount == 0:
				if db.execute("SELECT id FROM fl_life_health_agent_1 WHERE email = :email AND color = :color", {"email": email, "color": color}).rowcount == 0:
					return "Email and Security Answer dont match, contact russell@floridadiscountce.org or call 786-873-7526."

	user =  db.execute("SELECT *  FROM fl_public_adjuster_1 WHERE email = :email AND color = :color", {"email": email, "color": color}).fetchall()
	if user != []:
		name=user[0].name
		password=user[0].password

	user = db.execute("SELECT * FROM fl_life_health_agent_1 WHERE email = :email AND color = :color", {"email": email, "color": color}).fetchall()
	if user != []:
		name=user[0].name
		password=user[0].password

	user = db.execute("SELECT * FROM fl_health_agent_1 WHERE email = :email AND color = :color", {"email": email, "color": color}).fetchall()
	if user != []:
		name=user[0].name
		password=user[0].password

	user = db.execute("SELECT * FROM fl_independent_adjuster_1 WHERE email = :email AND color = :color", {"email": email, "color": color}).fetchall()
	if user != []:
		name=user[0].name
		password=user[0].password

	name = "'" + name + "'"
	password = "'" + password + "'"
	return render_template("forgot_password_result.html", name=name, password=password)

@app.route('/public_adjuster/', methods = ["GET"])
def public_adjuster():
	session['discipline'] = "Public Adjuster"
	# discipline = "public adjuster"
	return render_template("pa/public_adjuster.html")

@app.route('/independent_adjuster/', methods = ["GET"])
def independent_adjuster():
	session['discipline'] = "All-Lines Adjuster"
	return render_template("ia/independent_adjuster.html")

@app.route('/health/', methods = ["GET"])
def health():
	session['discipline'] = "Health Agent"
	return render_template("health/health.html")

@app.route('/life_health/', methods = ["GET"])
def life_health():
	session['discipline'] = "Life Health Agent"
	return render_template("life_health/life_health.html")

@app.route('/sign_up/', methods = ["GET","POST"])
def sign_up():
	return render_template("sign_up.html")

@app.route('/checkout/', methods = ["GET","POST"])
def checkout():
	name_reg = request.form.get("name")
	name = re.sub("[ \s]+$","",name_reg)
	print ("name", "--"+name+"--")
	session['name'] = name
	email_regex = request.form.get("email")
	email = re.sub("[ \s]","", email_regex.lower())
	print (email)
	password1 = request.form.get("password")
	password_regex = re.sub(" $","", password1)
	password = password1 = password_regex
	#hash passwords
	# salt = "6Agz"
	# db_password = password1+salt
	# h = hashlib.md5(db_password.encode())
	# password = h.hexdigest()
	'''
	street = request.form.get("street")
	city = request.form.get("city")
	state = request.form.get("state")
	zip_code = request.form.get("zip_code")
	address = street+", "+city+", "+state+", "+zip_code

	'''
	address = "N/A"
	first = request.form.get("first")
	last = request.form.get("last")
	license_no = request.form.get("license")
	# license_state = request.form.get("license_state")
	license_state = "FL"
	street_regex= request.form.get("street")
	maiden_regex = request.form.get("maiden")
	maiden = re.sub("[ \s]", "",maiden_regex.lower())
	color_regex = request.form.get("color")
	color = re.sub("[ \s]","",color_regex.lower())

	if db.execute("SELECT * FROM fl_public_adjuster_1 WHERE name = :name ", {"name": name}).rowcount > 0:
		return "username taken, go back and choose another"
	elif db.execute("SELECT * FROM fl_independent_adjuster_1 WHERE name = :name ", {"name": name}).rowcount > 0:
		return "username taken, go back and choose another"
	elif db.execute("SELECT * FROM fl_health_agent_1  WHERE name = :name ", {"name": name}).rowcount > 0:
		return "username taken, go back and choose another"
	elif db.execute("SELECT * FROM fl_life_health_agent_1  WHERE name = :name ", {"name": name}).rowcount > 0:
		return "username taken, go back and choose another"

	if session['discipline'] == "Public Adjuster":
		db.execute("INSERT INTO fl_public_adjuster_1(name, email, password, address, first, last, license_no, license_state,  maiden , color) VALUES (:name, :email, :password, :address, :first, :last, :license_no, :license_state,  :maiden, :color)", { "name":name, "email":email, "password":password, "address":address,"first":first, "last":last, "license_no":license_no, "license_state":license_state,  "maiden":maiden, "color":color})
		db.commit()

	elif session['discipline'] == "All-Lines Adjuster":
		db.execute("INSERT INTO fl_independent_adjuster_1(name, email, password, address, first, last, license_no, license_state,  maiden , color) VALUES (:name, :email, :password, :address, :first, :last, :license_no, :license_state,  :maiden, :color)", { "name":name, "email":email, "password":password, "address":address,"first":first, "last":last, "license_no":license_no, "license_state":license_state,  "maiden":maiden, "color":color})
		db.commit()

	elif session['discipline'] == "Health Agent":
		db.execute("INSERT INTO fl_health_agent_1 (name, email, password, address, first, last, license_no, license_state,  maiden , color) VALUES (:name, :email, :password, :address, :first, :last, :license_no, :license_state,  :maiden, :color)", { "name":name, "email":email, "password":password, "address":address,"first":first, "last":last, "license_no":license_no, "license_state":license_state,  "maiden":maiden, "color":color})
		db.commit()

	elif session['discipline'] == "Life Health Agent":
		db.execute("INSERT INTO fl_life_health_agent_1 (name, email, password, address, first, last, license_no, license_state,  maiden , color) VALUES (:name, :email, :password, :address, :first, :last, :license_no, :license_state,  :maiden, :color)", { "name":name, "email":email, "password":password, "address":address,"first":first, "last":last, "license_no":license_no, "license_state":license_state,  "maiden":maiden, "color":color})
		db.commit()
	else:
		return redirect(url_for("index"))

	full_name = first + " " + last
	print(full_name)
	user = {
		"name": name,
		# "address": address,
		"email": email,
		"full_name": full_name,
		"license_no": license_no
	}
	course = session['course']
	discipline = session['discipline']

	return render_template("checkout.html", user=user, course=course, discipline=discipline)

@app.route('/success/', methods = ["GET","POST"])
def success():
	name = session['name']
	print("session['discipline']", session['discipline'])

	print("session['course']", session['course'])
	if session['discipline'] == "Public Adjuster":
		if session['course'] == "pa-ethics":
			ethics_paid = True
			db.execute("UPDATE fl_public_adjuster_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.commit()

		elif session['course'] == "pa-flood":
			flood_paid = True
			db.execute("UPDATE fl_public_adjuster_1 SET flood_paid = :flood_paid WHERE name = :name", {"flood_paid": flood_paid, "name": name})
			db.commit()

		elif session['course'] == "pa-property":
			property_paid = True
			db.execute("UPDATE fl_public_adjuster_1 SET property_paid = :property_paid WHERE name = :name", {"property_paid": property_paid, "name": name})
			db.commit()

		elif session['course'] == "pa-course-4":
			course_4_paid = True
			db.execute("UPDATE fl_public_adjuster_1 SET course_4_paid = :course_4_paid WHERE name = :name", {"course_4_paid": course_4_paid, "name": name})
			db.commit()

		elif session['course'] == "pa-bundle-24":
			ethics_paid = True
			flood_paid = True
			property_paid = True
			db.execute("UPDATE fl_public_adjuster_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.execute("UPDATE fl_public_adjuster_1 SET flood_paid = :flood_paid WHERE name = :name", {"flood_paid": flood_paid, "name": name})
			db.execute("UPDATE fl_public_adjuster_1 SET property_paid = :property_paid WHERE name = :name", {"property_paid": property_paid, "name": name})
			db.commit()

		elif session['course'] == "pa-bundle-20":
			ethics_paid = True
			course_4_paid = True
			property_paid = True
			db.execute("UPDATE fl_public_adjuster_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.execute("UPDATE fl_public_adjuster_1 SET course_4_paid = :course_4_paid WHERE name = :name", {"course_4_paid": course_4_paid, "name": name})
			db.execute("UPDATE fl_public_adjuster_1 SET property_paid = :property_paid WHERE name = :name", {"property_paid": property_paid, "name": name})
			db.commit()


	elif session['discipline'] == "All-Lines Adjuster":
		if session['course'] == "ia-ethics":
			ethics_paid = True
			db.execute("UPDATE fl_independent_adjuster_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.commit()

		elif session['course'] == "ia-homeowners":
			course_2_paid = True
			db.execute("UPDATE fl_independent_adjuster_1 SET course_2_paid = :course_2_paid WHERE name = :name", {"course_2_paid": course_2_paid, "name": name})
			db.commit()

		elif session['course'] == "ia-umbrella":
			course_3_paid = True
			db.execute("UPDATE fl_independent_adjuster_1 SET course_3_paid = :course_3_paid WHERE name = :name", {"course_3_paid": course_3_paid, "name": name})
			db.commit()

		elif session['course'] == "ia-course-4":
			course_4_paid = True
			db.execute("UPDATE fl_independent_adjuster_1 SET course_4_paid = :course_4_paid WHERE name = :name", {"course_4_paid": course_4_paid, "name": name})
			db.commit()

		elif session['course'] == "ia-bundle-24":
			ethics_paid = True
			course_2_paid = True
			course_3_paid = True
			db.execute("UPDATE fl_independent_adjuster_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.execute("UPDATE fl_independent_adjuster_1 SET course_2_paid = :course_2_paid WHERE name = :name", {"course_2_paid": course_2_paid, "name": name})
			db.execute("UPDATE fl_independent_adjuster_1 SET course_3_paid = :course_3_paid WHERE name = :name", {"course_3_paid": course_3_paid, "name": name})
			db.commit()

		elif session['course'] == "ia-bundle-20":
			ethics_paid = True
			course_4_paid = True
			course_3_paid = True
			db.execute("UPDATE fl_independent_adjuster_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.execute("UPDATE fl_independent_adjuster_1 SET course_4_paid = :course_4_paid WHERE name = :name", {"course_4_paid": course_4_paid, "name": name})
			db.execute("UPDATE fl_independent_adjuster_1 SET course_3_paid = :course_3_paid WHERE name = :name", {"course_3_paid": course_3_paid, "name": name})
			db.commit()


	elif session['discipline'] == "Health Agent":
		if session['course'] == "health-ethics":
			ethics_paid = True
			db.execute("UPDATE fl_health_agent_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.commit()

		elif session['course'] == "health-course-2":
			course_2_paid = True
			db.execute("UPDATE fl_health_agent_1 SET course_2_paid = :course_2_paid WHERE name = :name", {"course_2_paid": course_2_paid, "name": name})
			db.commit()
		elif session['course'] == "health-course-3":
			course_3_paid = True
			db.execute("UPDATE fl_health_agent_1 SET course_3_paid = :course_3_paid WHERE name = :name", {"course_3_paid": course_3_paid, "name": name})
			db.commit()
		elif session['course'] == "health-bundle-24":
			ethics_paid = True
			course_2_paid = True
			course_3_paid = True
			db.execute("UPDATE fl_health_agent_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.execute("UPDATE fl_health_agent_1 SET course_2_paid = :course_2_paid WHERE name = :name", {"course_2_paid": course_2_paid, "name": name})
			db.execute("UPDATE fl_health_agent_1 SET course_3_paid = :course_3_paid WHERE name = :name", {"course_3_paid": course_3_paid, "name": name})
			db.commit()

	elif session['discipline'] == "Life Health Agent":
		if session['course'] == "life-health-ethics":
			ethics_paid = True
			db.execute("UPDATE fl_life_health_agent_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.commit()

		elif session['course'] == "life-health-course-2":
			course_2_paid = True
			db.execute("UPDATE fl_life_health_agent_1 SET course_2_paid = :course_2_paid WHERE name = :name", {"course_2_paid": course_2_paid, "name": name})
			db.commit()

		elif session['course'] == "life-health-course-3":
			course_3_paid = True
			db.execute("UPDATE fl_life_health_agent_1 SET course_3_paid = :course_3_paid WHERE name = :name", {"course_3_paid": course_3_paid, "name": name})
			db.commit()

		elif session['course'] == "life-health-course-4":
			course_4_paid = True
			db.execute("UPDATE fl_life_health_agent_1 SET course_4_paid = :course_4_paid WHERE name = :name", {"course_4_paid": course_4_paid, "name": name})
			db.commit()

		elif session['course'] == "life-health-bundle-20":
			ethics_paid = True
			course_2_paid = True
			course_4_paid = True
			db.execute("UPDATE fl_life_health_agent_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.execute("UPDATE fl_life_health_agent_1 SET course_2_paid = :course_2_paid WHERE name = :name", {"course_2_paid": course_2_paid, "name": name})
			db.execute("UPDATE fl_life_health_agent_1 SET course_4_paid = :course_4_paid WHERE name = :name", {"course_4_paid": course_4_paid, "name": name})
			db.commit()

		elif session['course'] == "life-health-bundle-24":
			ethics_paid = True
			course_2_paid = True
			course_3_paid = True
			db.execute("UPDATE fl_life_health_agent_1 SET ethics_paid = :ethics_paid WHERE name = :name", {"ethics_paid": ethics_paid, "name": name})
			db.execute("UPDATE fl_life_health_agent_1 SET course_2_paid = :course_2_paid WHERE name = :name", {"course_2_paid": course_2_paid, "name": name})
			db.execute("UPDATE fl_life_health_agent_1 SET course_3_paid = :course_3_paid WHERE name = :name", {"course_3_paid": course_3_paid, "name": name})
			db.commit()

	paid_message = "Please Sign-In with the username and password you just created."
	return render_template("sign_in_main.html", paid_message = paid_message)

@app.route('/sign_in_main/', methods = ["GET","POST"])
def sign_in_main():
	return render_template("sign_in_main.html")

@app.route('/sign_in_main_result/', methods = ["GET","POST"])
def sign_in_main_result():
	name = request.form.get("name")
	session['name'] = name
	password = request.form.get("password")
	# admin_button = check_admin()  #not used yet
	passed = 'Passed this course'
	nopass = 'Have not finished'

	if name == "admin" and password == "florida123":
		session['admin'] = True
		pa1 = [(True,None)]
		pa2 = [(True,None)]
		pa3 = [(True,None)]
		pa4 = [(True,None)]
		ia1 = [(True,None)]
		ia2 = [(True,None)]
		ia3 = [(True,None)]
		ia4 = [(True,None)]
		h1 = [(True,None)]
		h2 = [(True,None)]
		h3 = [(True,None)]
		h4 = [(True,None)]
		lhv1 = [(True,None)]
		lhv2 = [(True,None)]
		lhv3 = [(True,None)]
		lhv4 = [(True,None)]
		user =   {
		0:{
		'first': 'admin',
		'last': 'admin',
		'name': 'admin',
		'address': 'admin',
		'email': 'admin',
			},
		}

		print("user", user)
		print("pa1", pa1)

		return render_template("sign_in_main_result.html",user=user,
		pa1=pa1, pa2=pa2, pa3=pa3, pa4=pa4, ia1=ia1, ia2=ia2, ia3=ia3, ia4=ia4, h1=h1, h2=h2,
		h3=h3, h4=h4, lhv1=lhv1, lhv2=lhv2, lhv3=lhv3, lhv4=lhv4, passed=passed, nopass=nopass )
	#check if username in system
	if db.execute("SELECT id FROM fl_public_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).rowcount == 0:
		if db.execute("SELECT id FROM fl_independent_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).rowcount == 0:
			if db.execute("SELECT id FROM fl_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).rowcount == 0:
				if db.execute("SELECT id FROM fl_life_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).rowcount == 0:
					return redirect(url_for("wrong_password"))

	if db.execute("SELECT * FROM fl_public_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).rowcount == 1:
		user = db.execute("SELECT * FROM fl_public_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if db.execute("SELECT * FROM fl_independent_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).rowcount == 1:
		user = db.execute("SELECT * FROM fl_independent_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if db.execute("SELECT * FROM fl_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).rowcount == 1:
		user = db.execute("SELECT * FROM fl_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if db.execute("SELECT * FROM fl_life_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).rowcount == 1:
		user = db.execute("SELECT * FROM fl_life_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()

	print("user", user)
	pa1 = db.execute("SELECT ethics_paid, ethics_score_date FROM fl_public_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	print ('pa1', pa1)
	if pa1 != []:
		pa1 = pa1
	else:
		pa1 = [None,None]
		'''
	pa1 [(True, '92/5/21/2020/pa-ethics-5-1112515')]
	pa2 [(None, None)]
	pa3 [(True, None)]
	ia1 []
	'''

	pa2 = db.execute("SELECT flood_paid, flood_score_date FROM fl_public_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if pa2 != []:
		pa2 = pa2
	else:
		pa2 = [None,None]

	pa3 = db.execute("SELECT property_paid, property_score_date FROM fl_public_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if pa3 != []:
		pa3 = pa3
	else:
		pa3 = [None,None]

	pa4 = db.execute("SELECT course_4_paid, course_4_score_date FROM fl_public_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if pa4 != []:
		pa4 = pa4
	else:
		pa4 = [None,None]

	ia1 = db.execute("SELECT ethics_paid, ethics_score_date FROM fl_independent_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if ia1 != []:
		ia1 = ia1
	else:
		ia1 = [None,None]

	ia2 = db.execute("SELECT course_2_paid, course_2_score_date FROM fl_independent_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if ia2 != []:
		ia2 = ia2
	else:
		ia2 = [None,None]

	ia3 = db.execute("SELECT course_3_paid, course_3_score_date FROM fl_independent_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if ia3 != []:
		ia3 = ia3
	else:
		ia3 = [None,None]

	ia4 = db.execute("SELECT course_4_paid, course_4_score_date FROM fl_independent_adjuster_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if ia4 != []:
		ia4 = ia4
	else:
		ia4 = [None,None]

	h1 = db.execute("SELECT ethics_paid, ethics_score_date FROM fl_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if h1 != []:
		h1 = h1
	else:
		h1 = [None,None]

	h2 = db.execute("SELECT course_2_paid, course_2_score_date FROM fl_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	print(h2)
	if h2 != []:
		h2 = h2
	else:
		h2 = [None,None]

	h3 = db.execute("SELECT course_3_paid, course_3_score_date FROM fl_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if h3 != []:
		h3 = h3
	else:
		h3 = [None,None]

	h4 = db.execute("SELECT course_4_paid, course_4_score_date FROM fl_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if h4 != []:
		h4 = h4
	else:
		h4 = [None,None]

	lhv1 = db.execute("SELECT ethics_paid, ethics_score_date FROM fl_life_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if lhv1 != []:
		lhv1 = lhv1
	else:
		lhv1 = [None,None]

	lhv2 = db.execute("SELECT course_2_paid, course_2_score_date FROM fl_life_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if lhv2 != []:
		lhv2 = lhv2
	else:
		lhv2 = [None,None]

	lhv3 = db.execute("SELECT course_3_paid, course_3_score_date FROM fl_life_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if lhv3 != []:
		lhv3 = lhv3
	else:
		lhv3 = [None,None]

	lhv4 = db.execute("SELECT course_4_paid, course_4_score_date FROM fl_life_health_agent_1 WHERE name = :name AND password = :password", {"name": name, "password": password}).fetchall()
	if lhv4 != []:
		lhv4 = lhv4
	else:
		lhv4 = [None,None]

	return render_template("sign_in_main_result.html",  user=user,
	pa1=pa1, pa2=pa2, pa3=pa3, pa4=pa4, ia1=ia1, ia2=ia2, ia3=ia3, ia4=ia4, h1=h1, h2=h2,
	h3=h3, h4=h4, lhv1=lhv1, lhv2=lhv2, lhv3=lhv3, lhv4=lhv4, passed=passed, nopass=nopass )

################################INTRO###########################################

@app.route('/sample_page/', methods = ["GET","POST"])
def sample_page():
	return render_template("sample_page.html")

@app.route('/pa/5_hour_law_ethics/', methods = ["GET"])
def pa_five_hour_law_ethics():
	session['course'] = "pa-ethics"
	return render_template("pa/ethics/5_hour_law_&_ethics.html")

@app.route('/pa/flood/', methods = ["GET"])
def pa_flood():
	session['course'] = "pa-flood"
	return render_template("pa/flood/flood-intro.html")

@app.route('/pa/property/', methods = ["GET"])
def pa_property():
	session['course'] = "pa-property"
	return render_template("pa/property/intro.html")

@app.route('/pa/nfip/', methods = ["GET"])
def pa_course_4():
	session['course'] = "pa-course-4"
	return render_template("pa/course_4/intro.html")

@app.route('/ia/5_hour_law_ethics/', methods = ["GET"])
def ia_five_hour_law_ethics():
	session['course'] = "ia-ethics"
	return render_template("ia/ethics/intro.html")

@app.route('/ia/umbrella/', methods = ["GET"])
def ia_umbrella():
	# return "umbrella"
	session['course'] = "ia-umbrella"
	return render_template("ia/umbrella/intro.html")

@app.route('/ia/homeowners/', methods = ["GET"])
def ia_homeowners():
	session['course'] = "ia-homeowners"
	return render_template("ia/homeowners/intro.html")

@app.route('/health/law_ethics/', methods = ["GET","POST"])
def health_law_ethics():
	session['course'] = "health-ethics"
	return render_template("health/ethics/intro.html")

@app.route('/life_health/law_ethics/', methods = ["GET"])
def life_health_law_ethics():
	session['course'] = "life-health-ethics"
	return render_template("life_health/ethics/intro.html")

@app.route('/life_health/long_term_care/', methods = ["GET"])
def life_health_course_2():
	session['course'] = "life-health-course-2"
	return render_template("life_health/course_2/intro.html")

@app.route('/life_health/medicare/', methods = ["GET"])
def life_health_course_3():
	session['course'] = "life-health-course-3"
	return render_template("life_health/course_3/intro.html")

############################BUNDLE################################################
@app.route('/pa/bundle_20/', methods = ["GET"])
def pa_bundle_20():
	session['course'] = "pa-bundle-20"
	title = "Public Adjuster 20-Hour 3-Course Bundle (5-320)+(3-20)"
	course_1 = "5-Hour Law & Ethics Update for Public Adjusters (5-320)"
	course_2 = "4-Hour National Flood Insurance Program for Public Adjusters (3-20)"
	course_3 = "11-Hour Auto - Personal Property - Umbrella Update for Public Adjusters (3-20)"
	hours = 20
	approval = "20 Public Adjuster Ethics and Electives (5-320)+(3-20)"
	price = "$21.00"

	return render_template("bundle_template.html",  title=title, course_1=course_1,
	course_2=course_2, course_3=course_3, hours=hours, approval=approval, price=price)

@app.route('/pa/bundle_24/', methods = ["GET"])
def pa_bundle():
	session['course'] = "pa-bundle-24"
	title = "Public Adjuster 24-Hour 3-Course Bundle (5-320)+(3-20)"
	course_1 = "5-Hour Law & Ethics Update for Public Adjusters (5-320)"
	course_2 = "8-Hour Flood & Homeowner's Insurance Update for Public Adjusters (3-20)"
	course_3 = "11-Hour Auto - Personal Property - Umbrella Update for Public Adjusters (3-20)"
	hours = 24
	approval = "24 Public Adjuster Ethics and Electives (5-320)+(3-20)"
	price = "$25.00"
	return render_template("bundle_template.html",  title=title, course_1=course_1,
	course_2=course_2, course_3=course_3, hours = hours, approval = approval, price=price)

@app.route('/ia/bundle_20/', methods = ["GET"])
def ia_bundle_20():
	session['course'] = "ia-bundle-20"
	title = "All-Lines Adjuster 20-hour 3-course bundle (5-620)+(5-20 & 6-20)"
	course_1 = "5-Hour Law & Ethics Update for All-Lines Adjusters (5-620) "
	course_2 = "3-Hour NationalFlood Insurance Program for All-Lines Adjusters (5-20 & 6-20)"
	course_3 = "12-Hour Umbrella and Underwriting Insurance Update For All-Lines Adjusters (5-20 & 6-20)"
	hours = 20
	approval = "20 All-Lines Adjuster Ethics and Electives (5-620)+(5-20 & 6-20)"
	price = "$21.00"
	return render_template("bundle_template.html",   title=title, course_1=course_1,
	course_2=course_2, course_3=course_3, hours = hours, approval = approval, price=price)

@app.route('/ia/bundle_24/', methods = ["GET"])
def ia_bundle():
	session['course'] = "ia-bundle-24"
	title = "All-Lines Adjuster 24-hour 3-course bundle (5-620)+(5-20 & 6-20)"
	course_1 = "5-Hour Law & Ethics Update for All-Lines Adjusters (5-620) "
	course_2 = "7-Hour Homeowners, Property and Auto Insurance Update for All-Lines Adjusters (5-20 & 6-20)"
	course_3 = "12-Hour Flood, Umbrella, and Underwriting Insurance Update For All-Lines Adjusters (5-20 & 6-20)"
	hours = 24
	approval = "24 All-Lines Adjuster Ethics and Electives (5-620)+(5-20 & 6-20)"
	price = "$25.00"
	return render_template("bundle_template.html",   title=title, course_1=course_1,
	course_2=course_2, course_3=course_3, hours = hours, approval = approval, price=price)

@app.route('/life_health/bundle_24/', methods = ["GET"])
def life_health_bundle():
	session['course'] = "life-health-bundle-24"
	title = "Life/Health/Annuity Agent 24-Hour 3-Course Bundle (5-215) + (2-15 & 2-18)"
	course_1 = "5-Hour Law & Ethics Update for Life, Health, & Annuity Agents (5-215)"
	course_2 = "10-Hour Long-Term Care & Partnership Programs for Life, Health, & Annuity Agents (2-15 & 2-18) "
	course_3 = "9-Hour Medicare, Medicaid CE Update for Life, Health, & Annuity Agents (2-15 & 2-18)"
	hours = 24
	approval = "24 Life/Health/Annuity Agent Ethics and Electives (5-215) + (2-15 & 2-18)"
	price = "$25.00"

	return render_template("bundle_template.html", title=title, course_1=course_1,
	course_2=course_2, course_3=course_3, hours = hours, approval = approval, price=price)

@app.route('/life_health/bundle_20/', methods = ["GET"])
def life_health_bundle_20():
	session['course'] = "life-health-bundle-20"
	title = "Life/Health/Annuity Agent 20-Hour 3-Course Bundle (5-215) + (2-15 & 2-18)"
	course_1 = "5-Hour Law & Ethics Update for Life, Health, & Annuity Agents (5-215)"
	course_2 = "10-Hour Long-Term Care & Partnership Programs for Life, Health, & Annuity Agents (2-15 & 2-18) "
	course_3 = "5-Insurance Claims Update for Life, Health, & Annuity Agents (2-15 & 2-18)"
	hours = 20
	approval = "20 Life/Health/Annuity Agent Ethics and Electives (5-215) + (2-15 & 2-18)"
	price = "$21.00"

	return render_template("bundle_template.html", title=title, course_1=course_1,
	course_2=course_2, course_3=course_3, hours = hours, approval = approval, price=price)

@app.route('/health/bundle/', methods = ["GET"])
def health_bundle_24():
	session['course'] = "health-bundle-24"
	title = "Health Agent 24-Hour 3-Course Bundle (5-240) + (2-40)"
	course_1 = "5-Hour Law & Ethics Update for Health Agents (5-240)"
	course_2 = "10-Hour Long-Term Care & Partnership Programs for Health Agents (2-40) "
	course_3 = "9-Hour Medicare, Medicaid CE Update for Health Agents (2-40)"
	hours = 24
	approval = "24 Health Agent Ethics and Electives (5-240) + (2-40)"
	price = "$25.00"

	return render_template("bundle_template.html", title=title, course_1=course_1,
	course_2=course_2, course_3=course_3, hours = hours, approval = approval, price=price)

@app.route('/security_question/<string:url>', methods = ["GET","POST"])
def security_question(url):
	print(url)
	return render_template("security_question.html", url=url)

@app.route('/security_question_result/<string:url>', methods = ["GET","POST"])
def security_question_result(url):

	name_reg = request.form.get("name")
	name = re.sub("[ \s]+$","",name_reg)
	color_regex = request.form.get("color")
	maiden = re.sub("[ \s]","",color_regex.lower())

	if name == 'admin':
		return redirect(url_for(url, name = name))


	if db.execute("SELECT id FROM fl_public_adjuster_1 WHERE name = :name AND maiden = :maiden", {"name": name, "maiden": maiden}).rowcount == 0:
		if db.execute("SELECT id FROM fl_independent_adjuster_1 WHERE name = :name AND maiden = :maiden", {"name": name, "maiden": maiden}).rowcount == 0:
			if db.execute("SELECT id FROM fl_health_agent_1 WHERE name = :name AND maiden = :maiden", {"name": name, "maiden": maiden}).rowcount == 0:
				if db.execute("SELECT id FROM fl_life_health_agent_1 WHERE name = :name AND maiden = :maiden", {"name": name, "maiden": maiden}).rowcount == 0:
					return "incorrect username or favorite color, username must be spelled exactly the same as when created, please go back and try again"

	return redirect(url_for(url, name = name))
#################################LAW AND ETHICS##################################



@app.route('/pa/ethics/chapter_1/', methods = ["GET","POST"])
def pa_ethics_chapter_1():
	if session.get("admin") is True:
		admin_button = True
		return render_template("pa/ethics/chapter_1.html", admin_button=admin_button)
	name = session['name']
	ethics_passed = db.execute("SELECT ethics_course FROM fl_public_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
	ethics_passed = ethics_passed[0][0]
	if  ethics_passed == True:
		return redirect(url_for("pa_ethics_final_prep", name=name))
	return render_template("pa/ethics/chapter_1.html")

@app.route('/pa/ethics/chapter_1_results/', methods = ["GET","POST"])
def pa_ethics_chapter_1_results():
	answer_1 = "Consumer Services"
	answer_2 = "Investigative and Forensic Services"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_1_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_2/', methods = ["GET","POST"])
def pa_ethics_chapter_2():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_2.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_2_results/', methods = ["GET","POST"])
def pa_ethics_chapter_2_results():
	wrong_answer = False
	answer_1 = "$50,000"
	answer_2 = "6 months"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_2_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_3/', methods = ["GET","POST"])
def pa_ethics_chapter_3():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_3.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_3_results/', methods = ["GET","POST"])
def pa_ethics_chapter_3_results():
	answer_1 = "30 days"
	answer_2 = "Always True"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_3_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_4/', methods = ["GET","POST"])
def pa_ethics_chapter_4():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_4.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_4_results/', methods = ["GET","POST"])
def pa_ethics_chapter_4_results():
	answer_1 = "2 years"
	answer_2 = "All of the above"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_4_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_5/', methods = ["GET","POST"])
def pa_ethics_chapter_5():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_5.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_5_results/', methods = ["GET","POST"])
def pa_ethics_chapter_5_results():
	answer_1 = "Three"
	answer_2 = "Coffee shop"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_5_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_6/', methods = ["GET","POST"])
def pa_ethics_chapter_6():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_6.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_6_results/', methods = ["GET","POST"])
def pa_ethics_chapter_6_results():
	answer_1 = "Public adjuster account"
	answer_2 = "Participate in the adjustment"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_6_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_7/', methods = ["GET","POST"])
def pa_ethics_chapter_7():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_7.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_7_results/', methods = ["GET","POST"])
def pa_ethics_chapter_7_results():
	answer_1 = "Adjuster lines import eligibility"
	answer_2 = "HB1011"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_7_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_8/', methods = ["GET","POST"])
def pa_ethics_chapter_8():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_8.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_8_results/', methods = ["GET","POST"])
def pa_ethics_chapter_8_results():
	answer_1 = "Return emails within 24 hours"
	answer_2 = "Standard of care"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_8_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_9/', methods = ["GET","POST"])
def pa_ethics_chapter_9():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_9.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_9_results/', methods = ["GET","POST"])
def pa_ethics_chapter_9_results():
	answer_1 = "Right to sue"
	answer_2 = "Unfair claims settlement practices"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_9_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_10/', methods = ["GET","POST"])
def pa_ethics_chapter_10():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_10.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_10_results/', methods = ["GET","POST"])
def pa_ethics_chapter_10_results():
	answer_1 = "MyProfile"
	answer_2 = "Conflict of interest"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_10_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_11/', methods = ["GET","POST"])
def pa_ethics_chapter_11():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_11.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_11_results/', methods = ["GET","POST"])
def pa_ethics_chapter_11_results():
	answer_1 = "Never true"
	answer_2 = "Website of unauthorized insurers"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_11_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/chapter_12/', methods = ["GET","POST"])
def pa_ethics_chapter_12():
	admin_button = check_admin()
	return render_template("pa/ethics/chapter_12.html", admin_button=admin_button)

@app.route('/pa/ethics/chapter_12_results/', methods = ["GET","POST"])
def pa_ethics_chapter_12_results():
	answer_1 = "Insurance Insights"
	answer_2 = "2 years"
	result_data = result_chapter()
	return render_template("pa/ethics/chapter_12_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/ethics/final_prep/<string:name>', methods = ["GET","POST"])
def pa_ethics_final_prep(name):
	print(name)
	name = name
	# return"kk"
	ethics_course = True
	db.execute("UPDATE fl_public_adjuster_1 SET ethics_course = :ethics_course WHERE name = :name", {"ethics_course": ethics_course, "name": name})
	db.commit()
	return render_template("pa/ethics/final_prep.html", name=name)

@app.route('/pa/ethics/review/<string:name>', methods = ["GET","POST"])
def pa_ethics_review(name):
	print(name)
	name=name
	return render_template("pa/ethics/review.html", name=name)

@app.route('/pa/ethics/final_exam/<string:name>', methods = ["GET","POST"])
def pa_ethics_final_exam(name):
	name=name
	admin_button = check_admin()
	return render_template("pa/ethics/final_exam.html", admin_button=admin_button, name=name)

@app.route('/pa/ethics/final_results/<string:name>', methods = ["GET","POST"])
def pa_ethics_final_results(name):
	print(name)
	date_fin = ""
	admin_button = check_admin()
	num_questions=30
	name = name
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		course_complete_data = [name, final_score, date_fin]
		ethics_score_date = "109996-1112515-5-PublicAdj_Ethics" + "-" + final_score  + "-" + "09-08-2020" + "/" + date_fin
		db.execute("UPDATE fl_public_adjuster_1 SET ethics_score_date = :ethics_score_date WHERE name = :name", {"ethics_score_date": ethics_score_date, "name": name})
		db.commit()


	return render_template("pa/ethics/final_results.html", name=name, final_score=final_score, date_fin=date_fin, admin_button=admin_button, percent = final_score, exam_pass = exam_pass, answer_1="Department of Financial Services",answer_2="All of the above",answer_3="Defamation",answer_4=5,answer_5="Assist in reconstruction efforts.",answer_6="Accredited Claims Adjuster (ACA)",answer_7="Not having license on your person at all times.",answer_8="Three",answer_9="Never true",answer_10="All of the above",answer_11="Individuals who hold limited lines licenses for which no exam is required.",answer_12="Always true",answer_13="Stepping in after liquidation to assume financial responsibility for most claims",answer_14="Take such legal action as may be necessary to avoid payment of improper claims",answer_15="Adjusters must report the facts after making a complete investigation in a truthful and unbiased manner.",answer_16="Provide prompt and conscientious service",answer_17="Always false",answer_18="Subject to arrest and may be charged with a third-degree felony.",answer_19="Someone who does all of the above but is also an attorney.",answer_20="Always true",answer_21="All of the above",answer_22="None of the above",answer_23="Be a licensed insurance agent",answer_24="Guaranty association",answer_25="Turn down referrals from a non-licensed adjuster",answer_26="Crop and Hail limited lines",answer_27="Website development",answer_28="Conflicts of interest",answer_29="The public",answer_30="MyProfile")

@app.route('/pa/ethics/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def pa_ethics_course_complete(name, final_score, date_fin):
	print(name, final_score, date_fin)
	name = name
	percent = final_score
	date_complete = date_fin

	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'

	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_public_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		course_no = 109996
		offering_no = 1112515
		user_name = data[0][5]


	course = "Florida 5-Hour Law & Ethics Update for Public Adjusters"

	return render_template("course_complete.html",user_name=user_name, first_name=first_name, last_name = last_name, address = address, course = course, license_no = license_no,
	 license_state = license_state, course_no=course_no, offering_no=offering_no, date_complete=date_complete,  percent=percent)

#*************NFIP********************
@app.route('/pa/nfip/chapter_1/', methods = ["GET","POST"])
def pa_course_4_chapter_1():
	if session.get("admin") is True:
		admin_button = True
		return render_template("pa/course_4/chapter_1.html", admin_button=admin_button)
	name = session['name']
	course_passed = db.execute("SELECT course_4_complete FROM fl_public_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
	course_passed = course_passed[0][0]
	if course_passed == True:
		return redirect(url_for("pa_course_4_final_prep", name=name))
	return render_template("pa/course_4/chapter_1.html")
@app.route('/pa/nfip/chapter_1_results/', methods = ["GET","POST"])
def pa_course_4_chapter_1_results():
	answer_1 = "Single Family"
	answer_2 = "30 days"
	result_data = result_chapter()
	return render_template("pa/course_4/chapter_1_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/nfip/chapter_2/', methods = ["GET","POST"])
def pa_course_4_chapter_2():
	admin_button = check_admin()
	return render_template("pa/course_4/chapter_2.html", admin_button=admin_button)
@app.route('/pa/nfip/chapter_2_results/', methods = ["GET","POST"])
def pa_course_4_chapter_2_results():
	answer_1 = "It contacts FEMA and requests admission to the NFIP"
	answer_2 = "Coastal Barrier Resources Systems"
	result_data = result_chapter()
	return render_template("pa/course_4/chapter_2_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/nfip/chapter_3/', methods = ["GET","POST"])
def pa_course_4_chapter_3():
	admin_button = check_admin()
	return render_template("pa/course_4/chapter_3.html", admin_button=admin_button)
@app.route('/pa/nfip/chapter_3_results/', methods = ["GET","POST"])
def pa_course_4_chapter_3_results():
	answer_1 = "Structured to build a capital surplus"
	answer_2 = "Repetitive Loss Properties"
	result_data = result_chapter()
	return render_template("pa/course_4/chapter_3_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/nfip/chapter_4/', methods = ["GET","POST"])
def pa_course_4_chapter_4():
	admin_button = check_admin()
	return render_template("pa/course_4/chapter_4.html", admin_button=admin_button)
@app.route('/pa/nfip/chapter_4_results/', methods = ["GET","POST"])
def pa_course_4_chapter_4_results():
	answer_1 = "All of the above"
	answer_2 = "Base Flood Elevation"
	result_data = result_chapter()
	return render_template("pa/course_4/chapter_4_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/nfip/chapter_5/', methods = ["GET","POST"])
def pa_course_4_chapter_5():
	admin_button = check_admin()
	return render_template("pa/course_4/chapter_5.html", admin_button=admin_button)
@app.route('/pa/nfip/chapter_5_results/', methods = ["GET","POST"])
def pa_course_4_chapter_5_results():
	answer_1 = "Grandfathering"
	answer_2 = "They were in debt and needed to collect more premiums"
	result_data = result_chapter()
	return render_template("pa/course_4/chapter_5_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/nfip/chapter_6/', methods = ["GET","POST"])
def pa_course_4_chapter_6():
	admin_button = check_admin()
	return render_template("pa/course_4/chapter_6.html", admin_button=admin_button)
@app.route('/pa/nfip/chapter_6_results/', methods = ["GET","POST"])
def pa_course_4_chapter_6_results():
	answer_1 = "Average historical loss"
	answer_2 = "The Homeowner Flood Insurance Affordability Act"
	result_data = result_chapter()
	return render_template("pa/course_4/chapter_6_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/nfip/final_prep/<string:name>', methods = ["GET","POST"])
def pa_course_4_final_prep(name):
	name=name
	course_4_complete = True
	db.execute("UPDATE fl_public_adjuster_1 SET course_4_complete = :course_4_complete WHERE name = :name", {"course_4_complete": course_4_complete, "name": name})
	db.commit()
	return render_template("pa/course_4/final_prep.html", name=name)

@app.route('/pa/nfip/review/<string:name>', methods = ["GET","POST"])
def pa_course_4_review(name):
	name=name
	return render_template("pa/course_4/review.html", name=name)

@app.route('/pa/nfip/final_exam/<string:name>', methods = ["GET","POST"])
def pa_course_4_final_exam(name):
	admin_button = check_admin()
	name=name
	return render_template("pa/course_4/final_exam.html", admin_button=admin_button, name=name)

@app.route('/pa/nfip/final_results/<string:name>', methods = ["GET","POST"])
def pa_course_4_final_results(name):
	date_fin = ''
	num_questions=25
	name = name
	final_score_data=final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		date_fin = date_fin
		course_4_score_date = "112746-1124753-4-PublicAdj_NFIP" + "-" + final_score  + "-" + "11-07-2020" + "/" + date_fin
		db.execute("UPDATE fl_public_adjuster_1 SET course_4_score_date = :course_4_score_date WHERE name = :name", {"course_4_score_date": course_4_score_date, "name": name})
		db.commit()
	return render_template("pa/course_4/final_results.html",  name=name, final_score = final_score, date_fin=date_fin, exam_pass = exam_pass)

@app.route('/pa/nfip/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def pa_course_4_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score

	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'

	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_public_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
		print("data", data)
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = "112746"
		offering_no = "1124753"

	course = "Florida 4-Hour National Flood Insurance Program"
	return render_template("course_complete.html", user_name = user_name, first_name = first_name, last_name = last_name, license_no = license_no, address = address, course = course,  license_state = license_state,  course_no = course_no, offering_no = offering_no,  percent = percent, date_complete=date_complete)

@app.route('/pa/flood/chapter_1/', methods = ["GET","POST"])
def pa_flood_chapter_1():
	if session.get("admin") is True:
		admin_button = True
		return render_template("pa/flood/chapter_1.html", admin_button = admin_button)
	name = session['name']
	flood_passed = db.execute("SELECT flood_course FROM fl_public_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
	print("gut", flood_passed)
	flood_passed = flood_passed[0][0]
	print("gut", flood_passed)
	if flood_passed == True:
		return redirect(url_for("pa_flood_final_prep",name=name))
	return render_template("pa/flood/chapter_1.html")

@app.route('/pa/flood/chapter_1_results/', methods = ["GET","POST"])
def pa_flood_chapter_1_results():
	answer_1 = "Single Family"
	answer_2 = "30 days"
	result_data = result_chapter()
	return render_template("pa/flood/chapter_1_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/flood/chapter_2/', methods = ["GET","POST"])
def pa_flood_chapter_2():
	admin_button = check_admin()
	return render_template("pa/flood/chapter_2.html", admin_button=admin_button)

@app.route('/pa/flood/chapter_2_results/', methods = ["GET","POST"])
def pa_flood_chapter_2_results():
	answer_1 = "It contacts FEMA and requests admission to the NFIP"
	answer_2 = "Coastal Barrier Resources Systems"
	result_data = result_chapter()
	return render_template("pa/flood/chapter_2_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/flood/chapter_3/', methods = ["GET","POST"])
def pa_flood_chapter_3():
	admin_button = check_admin()
	return render_template("pa/flood/chapter_3.html", admin_button=admin_button)

@app.route('/pa/flood/chapter_3_results/', methods = ["GET","POST"])
def pa_flood_chapter_3_results():
	answer_1 = "Structured to build a capital surplus"
	answer_2 = "Repetitive Loss Properties"
	result_data = result_chapter()
	return render_template("pa/flood/chapter_3_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/flood/chapter_4/', methods = ["GET","POST"])
def pa_flood_chapter_4():
	admin_button = check_admin()
	return render_template("pa/flood/chapter_4.html", admin_button=admin_button)
@app.route('/pa/flood/chapter_4_results/', methods = ["GET","POST"])
def pa_flood_chapter_4_results():
	answer_1 = "All of the above"
	answer_2 = "Base Flood Elevation"
	result_data = result_chapter()
	return render_template("pa/flood/chapter_4_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/flood/chapter_5/', methods = ["GET","POST"])
def pa_flood_chapter_5():
	admin_button = check_admin()
	return render_template("pa/flood/chapter_5.html", admin_button=admin_button)
@app.route('/pa/flood/chapter_5_results/', methods = ["GET","POST"])
def pa_flood_chapter_5_results():
	answer_1 = "Grandfathering"
	answer_2 = "They were in debt and needed to collect more premiums"
	result_data = result_chapter()
	return render_template("pa/flood/chapter_5_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/flood/chapter_6/', methods = ["GET","POST"])
def pa_flood_chapter_6():
	admin_button = check_admin()
	return render_template("pa/flood/chapter_6.html", admin_button=admin_button)
@app.route('/pa/flood/chapter_6_results/', methods = ["GET","POST"])
def pa_flood_chapter_6_results():
	answer_1 = "All of the above"
	answer_2 = "School resume"
	result_data = result_chapter()
	return render_template("pa/flood/chapter_6_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/flood/chapter_7/', methods = ["GET","POST"])
def pa_flood_chapter_7():
	admin_button = check_admin()
	return render_template("pa/flood/chapter_7.html", admin_button=admin_button)
@app.route('/pa/flood/chapter_7_results/', methods = ["GET","POST"])
def pa_flood_chapter_7_results():
	answer_1 = "Declaration Page"
	answer_2 = "Indemnity Form"
	result_data = result_chapter()
	return render_template("pa/flood/chapter_7_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/flood/chapter_8/', methods = ["GET","POST"])
def pa_flood_chapter_8():
	admin_button = check_admin()
	return render_template("pa/flood/chapter_8.html", admin_button=admin_button)
@app.route('/pa/flood/chapter_8_results/', methods = ["GET","POST"])
def pa_flood_chapter_8_results():
	answer_1 = "Liability"
	answer_2 = "80%"
	result_data = result_chapter()
	return render_template("pa/flood/chapter_8_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/flood/chapter_9/', methods = ["GET","POST"])
def pa_flood_chapter_9():
	admin_button = check_admin()
	return render_template("pa/flood/chapter_9.html", admin_button=admin_button)
@app.route('/pa/flood/chapter_9_results/', methods = ["GET","POST"])
def pa_flood_chapter_9_results():
	answer_1 = "Substitution"
	answer_2 = "Provides coverage for people who give advice"
	result_data = result_chapter()
	return render_template("pa/flood/chapter_9_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/flood/final_prep/<string:name>', methods = ["GET","POST"])
def pa_flood_final_prep(name):
	print(name)
	flood_course = True
	name = name
	db.execute("UPDATE fl_public_adjuster_1 SET flood_course = :flood_course WHERE name = :name", {"flood_course": flood_course, "name": name})
	db.commit()
	return render_template("pa/flood/final_prep.html", name=name)

@app.route('/pa/flood/final_exam/<string:name>', methods = ["GET","POST"])
def pa_flood_final_exam(name):
	admin_button = check_admin()
	name = name
	return render_template("pa/flood/final_exam.html", admin_button = admin_button, name=name)

@app.route('/pa/flood/review/<string:name>', methods = ["GET","POST"])
def pa_flood_review(name):
	return render_template("pa/flood/review.html", name=name)

@app.route('/pa/flood/final_results/<string:name>', methods = ["GET","POST"])
def pa_flood_final_results(name):
	date_fin = ""
	num_questions=45
	name = name
	final_score_data=final_results(num_questions)
	final_score = final_score_data[0]
	print(final_score)
	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		flood_score_date = "110472-1113898-8-PublicAdj_Flood" + "-" + final_score  + "-" + "10-13-2020" + "/" + date_fin
		db.execute("UPDATE fl_public_adjuster_1 SET flood_score_date = :flood_score_date WHERE name = :name", {"flood_score_date": flood_score_date, "name": name})
		db.commit()
	return render_template("pa/flood/final_results.html", name=name, final_score=final_score, date_fin=date_fin, exam_pass=exam_pass)

@app.route('/pa/flood/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def pa_flood_course_complete(name, final_score, date_fin):
	print(name, final_score, date_fin)
	name = name
	percent = final_score
	date_complete = date_fin
# kkk
	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name='admin'
	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_public_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = 110472
		offering_no = 1113898

	course = "Florida 8-Hour Flood & Homeowner's Insurance Update for Public Adjusters"

	return render_template("course_complete.html",user_name=user_name, first_name = first_name, last_name = last_name, address = address, course = course, license_no = license_no, license_state = license_state,  course_no = course_no, offering_no = offering_no, date_complete = date_complete,  percent = percent)

@app.route('/pa/property/chapter_1/', methods = ["GET","POST"])
def pa_property_chapter_1():
	'''check if course passed, if so send to final exam'''
	if session.get("admin") is True:
		admin_button = True
		return render_template("pa/property/chapter_1.html", admin_button = admin_button)
	name = session['name']
	property_passed = db.execute("SELECT property_course FROM fl_public_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
	print("gut", property_passed)
	property_passed = property_passed[0][0]
	print("gut", property_passed)
	if property_passed == True:
		return redirect(url_for("pa_property_final_prep", name=name))
	return render_template("pa/property/chapter_1.html")
@app.route('/pa/property/chapter_1_results/', methods = ["GET","POST"])
def pa_property_chapter_1_results():
	answer_1 = "The insurance company"
	answer_2 = "50 to 70 percent"
	result_data = result_chapter()
	return render_template("pa/property/chapter_1_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_2/', methods = ["GET","POST"])
def pa_property_chapter_2():
	admin_button = check_admin()
	return render_template("pa/property/chapter_2.html", admin_button = admin_button)
@app.route('/pa/property/chapter_2_results/', methods = ["GET","POST"])
def pa_property_chapter_2_results():
	answer_1 = "Auto Glass Insurance"
	answer_2 = "Marketing Budget"
	result_data = result_chapter()
	return render_template("pa/property/chapter_2_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_3/', methods = ["GET","POST"])
def pa_property_chapter_3():
	admin_button = check_admin()
	return render_template("pa/property/chapter_3.html", admin_button = admin_button)
@app.route('/pa/property/chapter_3_results/', methods = ["GET","POST"])
def pa_property_chapter_3_results():
	answer_1 = "Height"
	answer_2 = "25%"
	result_data = result_chapter()
	return render_template("pa/property/chapter_3_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_4/', methods = ["GET","POST"])
def pa_property_chapter_4():
	admin_button = check_admin()
	return render_template("pa/property/chapter_4.html", admin_button = admin_button)
@app.route('/pa/property/chapter_4_results/', methods = ["GET","POST"])
def pa_property_chapter_4_results():
	answer_1 = "Ocean Marine"
	answer_2 = "Fish"
	result_data = result_chapter()
	return render_template("pa/property/chapter_4_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_5/', methods = ["GET","POST"])
def pa_property_chapter_5():
	admin_button = check_admin()
	return render_template("pa/property/chapter_5.html", admin_button = admin_button)
@app.route('/pa/property/chapter_5_results/', methods = ["GET","POST"])
def pa_property_chapter_5_results():
	answer_1 = "Travelers "
	answer_2 = "All of the above"
	result_data = result_chapter()
	return render_template("pa/property/chapter_5_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_6/', methods = ["GET","POST"])
def pa_property_chapter_6():
	admin_button = check_admin()
	return render_template("pa/property/chapter_6.html", admin_button = admin_button)
@app.route('/pa/property/chapter_6_results/', methods = ["GET","POST"])
def pa_property_chapter_6_results():
	answer_1 = "Protection and Indemnity Insurance"
	answer_2 = "Surgeons"
	result_data = result_chapter()
	return render_template("pa/property/chapter_6_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_7/', methods = ["GET","POST"])
def pa_property_chapter_7():
	admin_button = check_admin()
	return render_template("pa/property/chapter_7.html", admin_button = admin_button)
@app.route('/pa/property/chapter_7_results/', methods = ["GET","POST"])
def pa_property_chapter_7_results():
	answer_1 = "Personal injury losses that may be limited or excluded under most homeowners’ policies"
	answer_2 = "Writing an assessment of the damage"
	result_data = result_chapter()
	return render_template("pa/property/chapter_7_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_8/', methods = ["GET","POST"])
def pa_property_chapter_8():
	admin_button = check_admin()
	return render_template("pa/property/chapter_8.html", admin_button = admin_button)
@app.route('/pa/property/chapter_8_results/', methods = ["GET","POST"])
def pa_property_chapter_8_results():
	answer_1 = "Condition Precedent"
	answer_2 = "Two"
	result_data = result_chapter()
	return render_template("pa/property/chapter_8_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_9/', methods = ["GET","POST"])
def pa_property_chapter_9():
	admin_button = check_admin()
	return render_template("pa/property/chapter_9.html", admin_button = admin_button)
@app.route('/pa/property/chapter_9_results/', methods = ["GET","POST"])
def pa_property_chapter_9_results():
	answer_1 = "Performance depends on the occurrence of an uncertain event"
	answer_2 = "All of the above"
	result_data = result_chapter()
	return render_template("pa/property/chapter_9_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_10/', methods = ["GET","POST"])
def pa_property_chapter_10():
	admin_button = check_admin()
	return render_template("pa/property/chapter_10.html", admin_button = admin_button)
@app.route('/pa/property/chapter_10_results/', methods = ["GET","POST"])
def pa_property_chapter_10_results():
	answer_1 = "Licensed sales"
	answer_2 = "Windowing"
	result_data = result_chapter()
	return render_template("pa/property/chapter_10_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_11/', methods = ["GET","POST"])
def pa_property_chapter_11():
	admin_button = check_admin()
	return render_template("pa/property/chapter_11.html", admin_button = admin_button)
@app.route('/pa/property/chapter_11_results/', methods = ["GET","POST"])
def pa_property_chapter_11_results():
	answer_1 = "Insureds"
	answer_2 = "Insurance Fraud Hall of Shame"
	result_data = result_chapter()
	return render_template("pa/property/chapter_11_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/chapter_12/', methods = ["GET","POST"])
def pa_property_chapter_12():
	admin_button = check_admin()
	return render_template("pa/property/chapter_12.html", admin_button = admin_button)

@app.route('/pa/property/chapter_12_results/', methods = ["GET","POST"])
def pa_property_chapter_12_results():
	answer_1 = "White elephant"
	answer_2 = "Future"

	result_data = result_chapter()
	return render_template("pa/property/chapter_12_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/pa/property/final_prep/<string:name>/', methods = ["GET","POST"])
def pa_property_final_prep(name):
	property_course = True
	name = name
	db.execute("UPDATE fl_public_adjuster_1 SET property_course = :property_course WHERE name = :name", {"property_course": property_course, "name": name})
	db.commit()
	return render_template("pa/property/final_prep.html", name=name)

@app.route('/pa/property/final_exam/<string:name>/', methods = ["GET","POST"])
def pa_property_final_exam(name):
	admin_button = check_admin()
	name=name
	return render_template("pa/property/final_exam.html", admin_button = admin_button, name=name)

@app.route('/pa/property/review/<string:name>/', methods = ["GET","POST"])
def pa_property_review(name):
	name=name
	return render_template("pa/property/review.html", name=name)

@app.route('/pa/property/final_results/<string:name>/', methods = ["GET","POST"])
def pa_property_final_results(name):
	date_fin = ''
	name=name
	num_questions=60
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		date_fin = date_fin
		property_score_date = "110817-1115583-11-PublicAdj_Auto" + "-" + final_score  + "-" + "11-07-2020" + "/" + date_fin
		db.execute("UPDATE fl_public_adjuster_1 SET property_score_date = :property_score_date WHERE name = :name", {"property_score_date": property_score_date, "name": name})
		db.commit()

	return render_template("pa/property/final_results.html",  name=name, date_fin = date_fin, final_score=final_score, exam_pass=exam_pass)

@app.route('/pa/property/course_complete/<string:name>/<int:final_score>/<path:date_fin>/', methods = ["GET","POST"])
def pa_property_course_complete(name, date_fin, final_score):
	name = name
	date_complete = date_fin
	percent = final_score

	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'
	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_public_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data [0][5]
		course_no = 110817
		offering_no = 1115583

	course = "Florida 11-Hour Personal Property & Umbrella Update for Public Adjusters"

	return render_template("course_complete.html", user_name = user_name, first_name = first_name, last_name = last_name, address = address, course = course, license_no = license_no, license_state = license_state,  course_no = course_no, offering_no = offering_no, date_complete = date_complete,  percent = percent)

###################ETHICS##########################


@app.route('/ia/ethics/chapter_1/', methods = ["GET","POST"])
def ia_ethics_chapter_1():
	if session.get("admin") is True:
		admin_button = True
		return render_template("ia/ethics/chapter_1.html", admin_button = admin_button)
	name = session['name']
	ethics_passed = db.execute("SELECT ethics_course FROM fl_independent_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
	ethics_passed=ethics_passed[0][0]
	if  ethics_passed == True:
		return redirect(url_for("ia_ethics_final_prep", name=name))
	return render_template("ia/ethics/chapter_1.html")
@app.route('/ia/ethics/chapter_1_results/', methods = ["GET","POST"])
def ia_ethics_chapter_1_results():
	answer_1 = "Consumer Services"
	answer_2 = "Office of Inspector General"
	result_data = result_chapter()
	return render_template("ia/ethics/chapter_1_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/ethics/chapter_2/', methods = ["GET","POST"])
def ia_ethics_chapter_2():
	admin_button = check_admin()
	return render_template("ia/ethics/chapter_2.html", admin_button=admin_button)
@app.route('/ia/ethics/chapter_2_results/', methods = ["GET","POST"])
def ia_ethics_chapter_2_results():
	answer_1 = "Independent and company adjusters"
	answer_2 = "24 months"
	result_data = result_chapter()
	return render_template("ia/ethics/chapter_2_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/ethics/chapter_3/', methods = ["GET","POST"])
def ia_ethics_chapter_3():
	admin_button = check_admin()
	return render_template("ia/ethics/chapter_3.html", admin_button=admin_button)
@app.route('/ia/ethics/chapter_3_results/', methods = ["GET","POST"])
def ia_ethics_chapter_3_results():
	answer_1 = "Terminate or refuse to renew the adjuster’s appointment"
	answer_2 = "Insurance Insights"
	result_data = result_chapter()
	return render_template("ia/ethics/chapter_3_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/ethics/chapter_4/', methods = ["GET","POST"])
def ia_ethics_chapter_4():
	admin_button = check_admin()
	return render_template("ia/ethics/chapter_4.html", admin_button=admin_button)
@app.route('/ia/ethics/chapter_4_results/', methods = ["GET","POST"])
def ia_ethics_chapter_4_results():
	answer_1 = "Independent adjuster account"
	answer_2 = "Participate in the adjustment"
	result_data = result_chapter()
	return render_template("ia/ethics/chapter_4_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/ethics/chapter_5/', methods = ["GET","POST"])
def ia_ethics_chapter_5():
	admin_button = check_admin()
	return render_template("ia/ethics/chapter_5.html", admin_button=admin_button)
@app.route('/ia/ethics/chapter_5_results/', methods = ["GET","POST"])
def ia_ethics_chapter_5_results():
	answer_1 = "Policyholders shall have the right to a conflict of interest"
	answer_2 = "NAIIA Code of Ethics"
	result_data = result_chapter()
	return render_template("ia/ethics/chapter_5_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/ethics/chapter_6/', methods = ["GET","POST"])
def ia_ethics_chapter_6():
	admin_button = check_admin()
	return render_template("ia/ethics/chapter_6.html", admin_button=admin_button)
@app.route('/ia/ethics/chapter_6_results/', methods = ["GET","POST"])
def ia_ethics_chapter_6_results():
	answer_1 = "Deceptive Use of Name"
	answer_2 = "Churning"
	result_data = result_chapter()
	return render_template("ia/ethics/chapter_6_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/ethics/chapter_7/', methods = ["GET","POST"])
def ia_ethics_chapter_7():
	admin_button = check_admin()
	return render_template("ia/ethics/chapter_7.html", admin_button=admin_button)
@app.route('/ia/ethics/chapter_7_results/', methods = ["GET","POST"])
def ia_ethics_chapter_7_results():
	answer_1 = "$100"
	answer_2 = "Seeing a deceased minor or witnessing the death of a minor"
	result_data = result_chapter()
	return render_template("ia/ethics/chapter_7_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/ethics/chapter_8/', methods = ["GET","POST"])
def ia_ethics_chapter_8():
	admin_button = check_admin()
	return render_template("ia/ethics/chapter_8.html", admin_button=admin_button)
@app.route('/ia/ethics/chapter_8_results/', methods = ["GET","POST"])
def ia_ethics_chapter_8_results():
	answer_1 = "Liable to the insured for the full amount of the claim or loss not paid"
	answer_2 = "Website of unauthorized insurers"
	result_data = result_chapter()
	return render_template("ia/ethics/chapter_8_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/ethics/chapter_9/', methods = ["GET","POST"])
def ia_ethics_chapter_9():
	admin_button = check_admin()
	return render_template("ia/ethics/chapter_9.html", admin_button=admin_button)
@app.route('/ia/ethics/chapter_9_results/', methods = ["GET","POST"])
def ia_ethics_chapter_9_results():
	answer_1 = "Affordability Index"
	answer_2 = "Off-shore operator"

	result_data = result_chapter()
	return render_template("ia/ethics/chapter_9_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/ethics/final_prep/<string:name>/', methods = ["GET","POST"])
def ia_ethics_final_prep(name):
	ethics_course = True
	name = name
	db.execute("UPDATE fl_independent_adjuster_1 SET ethics_course = :ethics_course WHERE name = :name", {"ethics_course": ethics_course, "name": name})
	db.commit()
	return render_template("ia/ethics/final_prep.html", name=name)

@app.route('/ia/ethics/review/<string:name>/', methods = ["GET","POST"])
def ia_ethics_review(name):
	name = name
	return render_template("ia/ethics/review.html", name=name)

@app.route('/ia/ethics/final_exam/<string:name>/', methods = ["GET","POST"])
def ia_ethics_final_exam(name):
	admin_button = check_admin()
	name = name
	return render_template("ia/ethics/final_exam.html", admin_button=admin_button, name=name)

@app.route('/ia/ethics/final_results/<string:name>/', methods = ["GET","POST"])
def ia_ethics_final_results(name):
	name = name
	date_fin = ''
	num_questions=30
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]

	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		date_fin = date_fin
		ethics_score_date = "111049-1117773-5-AL_Ethics" + "-" + final_score  + "-" + "12-05-2020" + "/" + date_fin
		db.execute("UPDATE fl_independent_adjuster_1 SET ethics_score_date = :ethics_score_date WHERE name = :name", {"ethics_score_date": ethics_score_date, "name": name})
		db.commit()
	return render_template("ia/ethics/final_results.html", name=name, date_fin=date_fin, final_score = final_score, exam_pass = exam_pass)

@app.route('/ia/ethics/course_complete/<string:name>/<int:final_score>/<path:date_fin>/', methods = ["GET","POST"])
def ia_ethics_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score
	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'
	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_independent_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = 111049
		offering_no = 1117773

	course = "Florida 5-Hour Law & Ethics Update For All-Lines Adjusters"

	return render_template("course_complete.html", user_name = user_name, first_name = first_name, last_name = last_name, address = address, course = course, license_no = license_no, license_state = license_state,  course_no = course_no, offering_no = offering_no, date_complete = date_complete,  percent = percent)

################################################################################

@app.route('/ia/homeowners/chapter_1/', methods = ["GET","POST"])
def ia_homeowners_chapter_1():
	if session.get("admin") is True:
		admin_button = True
		return render_template("ia/homeowners/chapter_1.html", admin_button=admin_button)
	name = session['name']
	homeowners_passed = db.execute("SELECT course_2_complete FROM fl_independent_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
	homeowners_passed = homeowners_passed[0][0]
	if  homeowners_passed == True:
		return redirect(url_for("ia_homeowners_final_prep", name=name))
	return render_template("ia/homeowners/chapter_1.html")
@app.route('/ia/homeowners/chapter_1_results/', methods = ["GET","POST"])
def ia_homeowners_chapter_1_results():
	answer_1 = "Declaration Page"
	answer_2 = "Indemnity Form"
	result_data = result_chapter()
	return render_template("ia/homeowners/chapter_1_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/homeowners/chapter_2/', methods = ["GET","POST"])
def ia_homeowners_chapter_2():
	admin_button = check_admin()
	return render_template("ia/homeowners/chapter_2.html", admin_button=admin_button)
@app.route('/ia/homeowners/chapter_2_results/', methods = ["GET","POST"])
def ia_homeowners_chapter_2_results():
	answer_1 = "80%"
	answer_2 = "All of the above"
	result_data = result_chapter()
	return render_template("ia/homeowners/chapter_2_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/homeowners/chapter_3/', methods = ["GET","POST"])
def ia_homeowners_chapter_3():
	admin_button = check_admin()
	return render_template("ia/homeowners/chapter_3.html", admin_button=admin_button)
@app.route('/ia/homeowners/chapter_3_results/', methods = ["GET","POST"])
def ia_homeowners_chapter_3_results():
	answer_1 = "Any of the above"
	answer_2 = "Provides coverage for people who give advice"
	result_data = result_chapter()
	return render_template("ia/homeowners/chapter_3_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/homeowners/chapter_4/', methods = ["GET","POST"])
def ia_homeowners_chapter_4():
	admin_button = check_admin()
	return render_template("ia/homeowners/chapter_4.html", admin_button=admin_button)
@app.route('/ia/homeowners/chapter_4_results/', methods = ["GET","POST"])
def ia_homeowners_chapter_4_results():
	answer_1 = "Travelers"
	answer_2 = "All of the above"
	result_data = result_chapter()
	return render_template("ia/homeowners/chapter_4_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/homeowners/chapter_5/', methods = ["GET","POST"])
def ia_homeowners_chapter_5():
	admin_button = check_admin()
	return render_template("ia/homeowners/chapter_5.html", admin_button=admin_button)
@app.route('/ia/homeowners/chapter_5_results/', methods = ["GET","POST"])
def ia_homeowners_chapter_5_results():
	answer_1 = "Protection and Indemnity Insurance"
	answer_2 = "Scheduled Property"
	result_data = result_chapter()
	return render_template("ia/homeowners/chapter_5_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/homeowners/chapter_6/', methods = ["GET","POST"])
def ia_homeowners_chapter_6():
	admin_button = check_admin()
	return render_template("ia/homeowners/chapter_6.html", admin_button=admin_button)
@app.route('/ia/homeowners/chapter_6_results/', methods = ["GET","POST"])
def ia_homeowners_chapter_6_results():
	answer_1 = "The insurance company"
	answer_2 = "50 to 70 percent"
	result_data = result_chapter()
	return render_template("ia/homeowners/chapter_6_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/homeowners/chapter_7/', methods = ["GET","POST"])
def ia_homeowners_chapter_7():
	admin_button = check_admin()
	return render_template("ia/homeowners/chapter_7.html", admin_button=admin_button)
@app.route('/ia/homeowners/chapter_7_results/', methods = ["GET","POST"])
def ia_homeowners_chapter_7_results():
	answer_1 = "Height"
	answer_2 = "25%"
	result_data = result_chapter()
	return render_template("ia/homeowners/chapter_7_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/homeowners/final_prep/<string:name>/', methods = ["GET","POST"])
def ia_homeowners_final_prep(name):
	course_2_complete = True
	name = name
	db.execute("UPDATE fl_independent_adjuster_1 SET course_2_complete = :course_2_complete WHERE name = :name", {"course_2_complete": course_2_complete, "name": name})
	db.commit()
	return render_template("ia/homeowners/final_prep.html", name=name)

@app.route('/ia/homeowners/review/<string:name>/', methods = ["GET","POST"])
def ia_homeowners_review(name):
	name = name
	return render_template("ia/homeowners/review.html", name=name)

@app.route('/ia/homeowners/final_exam/<string:name>/', methods = ["GET","POST"])
def ia_homeowners_final_exam(name):
	admin_button = check_admin()
	name = name
	return render_template("ia/homeowners/final_exam.html", admin_button=admin_button, name=name)

@app.route('/ia/homeowners/final_results/<string:name>/', methods = ["GET","POST"])
def ia_homeowners_final_results(name):
	name = name
	date_fin = ''
	num_questions = 40
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass = final_score_data[1]
	if exam_pass == True:
		date_fin = final_score_data[2]
		course_2_score_date = "111341-1119751-7-AL_Homeowners" + "-" + final_score  + "-" + "01-08-2021" + "/" + date_fin
		db.execute("UPDATE fl_independent_adjuster_1 SET course_2_score_date = :course_2_score_date WHERE name = :name", {"course_2_score_date": course_2_score_date, "name": name})
		db.commit()
	return render_template("ia/homeowners/final_results.html", name=name, final_score=final_score, date_fin=date_fin, exam_pass = exam_pass)

@app.route('/ia/homeowners/course_complete/<string:name>/<int:final_score>/<path:date_fin>/', methods = ["GET","POST"])
def ia_homeowners_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score
	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'
	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_independent_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = 111341
		offering_no = 1119751

	course = "Florida 7-Hour Property and Homeowners' Insurance Update for All-Lines Adjusters"
	return render_template("course_complete.html", user_name=user_name, first_name = first_name, last_name = last_name, address = address, course = course, license_no = license_no, license_state = license_state,  course_no = course_no, offering_no = offering_no, date_complete = date_complete,  percent = percent)

@app.route('/ia/umbrella/chapter_1/', methods = ["GET","POST"])
def ia_umbrella_chapter_1():
	if session.get("admin") is True:
		admin_button = True
		return render_template("ia/umbrella/chapter_1.html", admin_button=admin_button)
	name = session['name']
	umbrella_passed = db.execute("SELECT course_3_complete FROM fl_independent_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
	umbrella_passed = umbrella_passed[0][0]
	if  umbrella_passed == True:
		return redirect(url_for("ia_umbrella_final_prep", name=name))
	return render_template("ia/umbrella/chapter_1.html")

@app.route('/ia/umbrella/chapter_1_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_1_results():
	answer_1 = "Personal injury losses that may be limited or excluded under most homeowners’ policies"
	answer_2 = "Writing an assessment of the damage"
	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_1_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/chapter_2/', methods = ["GET","POST"])
def ia_umbrella_chapter_2():
	admin_button = check_admin()
	return render_template("ia/umbrella/chapter_2.html", admin_button=admin_button)

@app.route('/ia/umbrella/chapter_2_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_2_results():
	answer_1 = "Condition Precedent "
	answer_2 = "Maintenance of Insurance"
	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_2_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/chapter_3/', methods = ["GET","POST"])
def ia_umbrella_chapter_3():
	admin_button = check_admin()
	return render_template("ia/umbrella/chapter_3.html", admin_button=admin_button)

@app.route('/ia/umbrella/chapter_3_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_3_results():
	answer_1 = "Performance depends on the occurrence of an uncertain event "
	answer_2 = "All of the above"
	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_3_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/chapter_4/', methods = ["GET","POST"])
def ia_umbrella_chapter_4():
	admin_button = check_admin()
	return render_template("ia/umbrella/chapter_4.html", admin_button=admin_button)

@app.route('/ia/umbrella/chapter_4_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_4_results():
	answer_1 = "Licensed sales"
	answer_2 = "Windowing"
	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_4_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/chapter_5/', methods = ["GET","POST"])
def ia_umbrella_chapter_5():
	admin_button = check_admin()
	return render_template("ia/umbrella/chapter_5.html", admin_button=admin_button)

@app.route('/ia/umbrella/chapter_5_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_5_results():
	answer_1 = "Insureds"
	answer_2 = "Insurance Fraud Hall of Shame "
	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_5_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/chapter_6/', methods = ["GET","POST"])
def ia_umbrella_chapter_6():
	admin_button = check_admin()
	return render_template("ia/umbrella/chapter_6.html", admin_button=admin_button)

@app.route('/ia/umbrella/chapter_6_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_6_results():
	answer_1 = "White elephant"
	answer_2 = "Future"

	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_6_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/chapter_7/', methods = ["GET","POST"])
def ia_umbrella_chapter_7():
	admin_button = check_admin()
	return render_template("ia/umbrella/chapter_7.html", admin_button=admin_button)

@app.route('/ia/umbrella/chapter_7_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_7_results():
	answer_1 = "Single Family "
	answer_2 = "30 Days"

	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_7_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/chapter_8/', methods = ["GET","POST"])
def ia_umbrella_chapter_8():
	admin_button = check_admin()
	return render_template("ia/umbrella/chapter_8.html", admin_button=admin_button)

@app.route('/ia/umbrella/chapter_8_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_8_results():
	answer_1 = "Grandfathering"
	answer_2 = "They were in debt and needed to collect more premiums"
	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_8_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/chapter_9/', methods = ["GET","POST"])
def ia_umbrella_chapter_9():
	admin_button = check_admin()
	return render_template("ia/umbrella/chapter_9.html", admin_button=admin_button)

@app.route('/ia/umbrella/chapter_9_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_9_results():
	answer_1 = "All of the above "
	answer_2 = "School resume"
	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_9_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/chapter_10/', methods = ["GET","POST"])
def ia_umbrella_chapter_10():
	admin_button = check_admin()
	return render_template("ia/umbrella/chapter_10.html", admin_button=admin_button)

@app.route('/ia/umbrella/chapter_10_results/', methods = ["GET","POST"])
def ia_umbrella_chapter_10_results():
	answer_1 = "Congressional Act of 1803"
	answer_2 = "2,600"
	result_data = result_chapter()
	return render_template("ia/umbrella/chapter_10_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/umbrella/final_prep/<string:name>/', methods = ["GET","POST"])
def ia_umbrella_final_prep(name):
	course_3_complete = True
	name = name
	db.execute("UPDATE fl_independent_adjuster_1 SET course_3_complete = :course_3_complete WHERE name = :name", {"course_3_complete": course_3_complete, "name": name})
	db.commit()
	return render_template("ia/umbrella/final_prep.html", name=name)

@app.route('/ia/umbrella/review/<string:name>/', methods = ["GET","POST"])
def ia_umbrella_review(name):
	name = name
	return render_template("ia/umbrella/review.html", name=name)

@app.route('/ia/umbrella/final_exam/<string:name>/', methods = ["GET","POST"])
def ia_umbrella_final_exam(name):
	admin_button = check_admin()
	name = name
	return render_template("ia/umbrella/final_exam.html", admin_button=admin_button, name=name)

@app.route('/ia/umbrella/final_results/<string:name>/', methods = ["GET","POST"])
def ia_umbrella_final_results(name):
	name = name
	date_fin = ''
	num_questions = 65
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		course_3_score_date = "111509-1120510-12-AL_Flood" + "-" + final_score  + "-" + "01-22-2021" + "/" + date_fin
		db.execute("UPDATE fl_independent_adjuster_1 SET course_3_score_date = :course_3_score_date WHERE name = :name", {"course_3_score_date": course_3_score_date, "name": name})
		db.commit()
	return render_template("ia/umbrella/final_results.html", name=name, date_fin=date_fin,  final_score = final_score, exam_pass = exam_pass)

@app.route('/ia/umbrella/course_complete/<string:name>/<int:final_score>/<path:date_fin>/', methods = ["GET","POST"])
def ia_umbrella_course_complete(name,final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score
	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'
	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_independent_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = 111509
		offering_no = 1120510

	course = "Florida 12-Hour Flood, Umbrella, and Underwriting Update for All-Lines Adjusters"

	return render_template("course_complete.html", user_name = user_name, first_name = first_name, last_name = last_name, address = address, course = course, license_no = license_no, license_state = license_state,  course_no = course_no, offering_no = offering_no, date_complete = date_complete,  percent = percent)

@app.route('/ia/nfip/', methods = ["GET"])
def ia_course_4():
	session['course'] = "ia-course-4"
	chapter = ia_courses.nfip_3_intro
	return render_template("course_intro_template.html", chapter=chapter)

@app.route('/ia/nfip/chapter_1/', methods = ["GET","POST"])
def ia_course_4_chapter_1():
	chapter = ia_courses.nfip_3_chapter_1
	if session.get("admin") is True:
		admin_button = True
		return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)
	name = session['name']
	course_passed = db.execute("SELECT course_4_complete FROM fl_independent_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
	course_passed = course_passed[0][0]
	if course_passed == True:
		print ('final')
		return redirect(url_for("ia_course_4_final_prep", name=name))
	return render_template("chapter_template.html", chapter=chapter)

@app.route('/ia/nfip/chapter_1_results/', methods = ["GET","POST"])
def ia_course_4_chapter_1_results():
	chapter = ia_courses.nfip_3_chapter_1
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/nfip/chapter_2/', methods = ["GET","POST"])
def ia_course_4_chapter_2():
	chapter = ia_courses.nfip_3_chapter_2
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/ia/nfip/chapter_2_results/', methods = ["GET","POST"])
def ia_course_4_chapter_2_results():
	chapter = ia_courses.nfip_3_chapter_2
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/nfip/chapter_3/', methods = ["GET","POST"])
def ia_course_4_chapter_3():
	chapter = ia_courses.nfip_3_chapter_3
	admin_button = check_admin()
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/ia/nfip/chapter_3_results/', methods = ["GET","POST"])
def ia_course_4_chapter_3_results():
	chapter = ia_courses.nfip_3_chapter_3
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/nfip/chapter_4/', methods = ["GET","POST"])
def ia_course_4_chapter_4():
	chapter = ia_courses.nfip_3_chapter_4
	admin_button = check_admin()
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/ia/nfip/chapter_4_results/', methods = ["GET","POST"])
def ia_course_4_chapter_4_results():
	chapter = ia_courses.nfip_3_chapter_4
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/nfip/chapter_5/', methods = ["GET","POST"])
def ia_course_4_chapter_5():
	chapter = ia_courses.nfip_3_chapter_5
	admin_button = check_admin()
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/ia/nfip/chapter_5_results/', methods = ["GET","POST"])
def ia_course_4_chapter_5_results():
	chapter = ia_courses.nfip_3_chapter_5
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/ia/nfip/final_prep/<string:name>', methods = ["GET","POST"])
def ia_course_4_final_prep(name):
	name = name
	print(name)
	chapter = ia_courses.nfip_3_final_prep
	course_4_complete = True
	db.execute("UPDATE fl_independent_adjuster_1 SET course_4_complete = :course_4_complete WHERE name = :name", {"course_4_complete": course_4_complete, "name": name})
	db.commit()
	return render_template("final_prep_template.html", chapter=chapter, name=name)

@app.route('/ia/nfip/review/<string:name>', methods = ["GET","POST"])
def ia_course_4_review(name):
	name = name
	chapter = ia_courses.nfip_3_review
	return render_template("review_template.html", chapter=chapter, name=name)

@app.route('/ia/nfip/final_exam/<string:name>', methods = ["GET","POST"])
def ia_course_4_final_exam(name):
	name = name
	admin_button = check_admin()
	print(name)
	return render_template("ia/course_4/final_exam.html", admin_button=admin_button, name=name)

@app.route('/ia/nfip/final_results/<string:name>', methods = ["GET","POST"])
def ia_course_4_final_results(name):
	num_questions=20
	name = name
	date_fin = ''
	final_score_data=final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	print(final_score)

	if exam_pass==True:
		date_fin = final_score_data[2]
		course_4_score_date = "113181-1126580-3-AL_NFIP" + "-" + final_score  + "-" + "06-09-2021" + "/" + date_fin
		db.execute("UPDATE fl_independent_adjuster_1 SET course_4_score_date = :course_4_score_date WHERE name = :name", {"course_4_score_date": course_4_score_date, "name": name})
		db.commit()
	return render_template("ia/course_4/final_results.html", name=name, final_score=final_score, date_fin=date_fin, exam_pass = exam_pass)

@app.route('/ia/nfip/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def ia_course_4_course_complete(name, final_score, date_fin):
	name = name
	percent = final_score
	date_complete = date_fin

	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'

	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_independent_adjuster_1 WHERE name = :name" , {"name": name}).fetchall()
		print("data", data)
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = "113181"
		offering_no = "1126580"

	course = "Florida 3-Hour National Flood Insurance Program"
	return render_template("course_complete.html", user_name = user_name, first_name = first_name, last_name = last_name, license_no = license_no, address = address, course = course,  license_state = license_state,  course_no = course_no, offering_no = offering_no,  percent = percent, date_complete=date_complete)


###########################LIFE & HEALTH****************************************

@app.route('/life_health/ethics/chapter_1/', methods = ["GET","POST"])
def life_health_ethics_chapter_1():
	if session.get("admin") is True:
		admin_button = True
		return render_template("life_health/ethics/chapter_1.html", admin_button=admin_button)
	name = session['name']
	ethics_passed = db.execute("SELECT ethics_course FROM fl_life_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
	ethics_passed=ethics_passed[0][0]
	if  ethics_passed == True:
		return redirect(url_for("life_health_ethics_final_prep", name=name))
	return render_template("life_health/ethics/chapter_1.html")

@app.route('/life_health/ethics/chapter_1_results/', methods = ["GET","POST"])
def life_health_ethics_chapter_1_results():
	answer_1 = "Consumer Services"
	answer_2 = "Office of Inspector General"
	result_data = result_chapter()
	return render_template("life_health/ethics/chapter_1_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ethics/chapter_2/', methods = ["GET","POST"])
def life_health_ethics_chapter_2():
	admin_button = check_admin()
	return render_template("life_health/ethics/chapter_2.html", admin_button=admin_button)
@app.route('/life_health/ethics/chapter_2_results/', methods = ["GET","POST"])
def life_health_ethics_chapter_2_results():
	answer_1 = "Studying for an exam"
	answer_2 = "$10,000"
	result_data = result_chapter()
	return render_template("life_health/ethics/chapter_2_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ethics/chapter_3/', methods = ["GET","POST"])
def life_health_ethics_chapter_3():
	admin_button = check_admin()
	return render_template("life_health/ethics/chapter_3.html", admin_button=admin_button)
@app.route('/life_health/ethics/chapter_3_results/', methods = ["GET","POST"])
def life_health_ethics_chapter_3_results():
	answer_1 = "Revising eligibility requirements for multiple-employer welfare arrangements"
	answer_2 = "Home state"
	result_data = result_chapter()
	return render_template("life_health/ethics/chapter_3_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ethics/chapter_4/', methods = ["GET","POST"])
def life_health_ethics_chapter_4():
	admin_button = check_admin()
	return render_template("life_health/ethics/chapter_4.html", admin_button=admin_button)
@app.route('/life_health/ethics/chapter_4_results/', methods = ["GET","POST"])
def life_health_ethics_chapter_4_results():
	answer_1 = "Twisting"
	answer_2 = "Continuous"
	result_data = result_chapter()
	return render_template("life_health/ethics/chapter_4_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ethics/chapter_5/', methods = ["GET","POST"])
def life_health_ethics_chapter_5():
	admin_button = check_admin()
	return render_template("life_health/ethics/chapter_5.html", admin_button=admin_button)
@app.route('/life_health/ethics/chapter_5_results/', methods = ["GET","POST"])
def life_health_ethics_chapter_5_results():
	answer_1 = "Public adjuster account"
	answer_2 = "Participate in the adjustment"
	result_data = result_chapter()
	return render_template("life_health/ethics/chapter_5_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ethics/chapter_6/', methods = ["GET","POST"])
def life_health_ethics_chapter_6():
	admin_button = check_admin()
	return render_template("life_health/ethics/chapter_6.html", admin_button=admin_button)
@app.route('/life_health/ethics/chapter_6_results/', methods = ["GET","POST"])
def life_health_ethics_chapter_6_results():
	answer_1 = "Affordability index"
	answer_2 = "Mediator"
	result_data = result_chapter()
	return render_template("life_health/ethics/chapter_6_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ethics/chapter_7/', methods = ["GET","POST"])
def life_health_ethics_chapter_7():
	admin_button = check_admin()
	return render_template("life_health/ethics/chapter_7.html", admin_button=admin_button)
@app.route('/life_health/ethics/chapter_7_results/', methods = ["GET","POST"])
def life_health_ethics_chapter_7_results():
	answer_1 = "Race"
	answer_2 = "Risk Tolerance"
	result_data = result_chapter()
	return render_template("life_health/ethics/chapter_7_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ethics/final_prep/<string:name>', methods = ["GET","POST"])
def life_health_ethics_final_prep(name):
	ethics_course = True
	name = name
	db.execute("UPDATE fl_life_health_agent_1 SET ethics_course = :ethics_course WHERE name = :name", {"ethics_course": ethics_course, "name": name})
	db.commit()
	return render_template("life_health/ethics/final_prep.html", name=name)

@app.route('/life_health/ethics/review/<string:name>', methods = ["GET","POST"])
def life_health_ethics_review(name):
	name = name
	return render_template("life_health/ethics/review.html", name=name)

@app.route('/life_health/ethics/final_exam/<string:name>', methods = ["GET","POST"])
def life_health_ethics_final_exam(name):
	name = name
	admin_button = check_admin()
	return render_template("life_health/ethics/final_exam.html", admin_button=admin_button, name=name)

@app.route('/life_health/ethics/final_results/<string:name>', methods = ["GET","POST"])
def life_health_ethics_final_results(name):
	num_questions=30
	date_fin = ''
	name = name
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		ethics_score_date = "112007-1122094-5-LHV_Ethics" + "-" + final_score  + "-" + "02-21-2021" + "/" + date_fin
		db.execute("UPDATE fl_life_health_agent_1 SET ethics_score_date = :ethics_score_date WHERE name = :name", {"ethics_score_date": ethics_score_date, "name": name})
		db.commit()
	return render_template("life_health/ethics/final_results.html", name=name, date_fin=date_fin, final_score=final_score, exam_pass = exam_pass)

@app.route('/life_health/ethics/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def life_health_ethics_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score
	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'
	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_life_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		course_no = 112007
		offering_no = 1122094
		user_name = data[0][5]

	course = "Florida 5-Hour Law & Ethics Update for Life, Health, & Annuity Agents"
	return render_template("course_complete.html", user_name=user_name, first_name = first_name, last_name = last_name, address = address,
	course = course, license_no = license_no, license_state = license_state,  course_no = course_no, offering_no = offering_no, date_complete = date_complete,  percent = percent)

@app.route('/life_health/ltc/chapter_1/', methods = ["GET","POST"])
def life_health_course_2_chapter_1():

	if session.get("admin") is True:
		admin_button = True
		return render_template("life_health/course_2/chapter_1.html", admin_button=admin_button)
	name = session['name']
	course_passed = db.execute("SELECT course_2_complete FROM fl_life_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
	course_passed=course_passed[0][0]
	if  course_passed == True:
		return redirect(url_for("life_health_course_2_final_prep", name=name))
	return render_template("life_health/course_2/chapter_1.html")

@app.route('/life_health/ltc/chapter_1_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_1_results():
	answer_1 = "Quality of life"
	answer_2 = "Height"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_1_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_2/', methods = ["GET","POST"])
def life_health_course_2_chapter_2():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_2.html", admin_button=admin_button)
@app.route('/life_health/ltc/chapter_2_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_2_results():
	answer_1 = "Medicaid"
	answer_2 = "The policy must be guaranteed renewable"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_2_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_3/', methods = ["GET","POST"])
def life_health_course_2_chapter_3():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_3.html", admin_button=admin_button)
@app.route('/life_health/ltc/chapter_3_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_3_results():
	answer_1 = "All of the above"
	answer_2 = "Remain at that level"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_3_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_4/', methods = ["GET","POST"])
def life_health_course_2_chapter_4():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_4.html", admin_button=admin_button)
@app.route('/life_health/ltc/chapter_4_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_4_results():
	answer_1 = "Medicaid eligibility"
	answer_2 = "Dollar-for-Dollar"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_4_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_5/', methods = ["GET","POST"])
def life_health_course_2_chapter_5():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_5.html", admin_button=admin_button)
@app.route('/life_health/ltc/chapter_5_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_5_results():
	answer_1 = "late 1980s"
	answer_2 = "New York"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_5_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_6/', methods = ["GET","POST"])
def life_health_course_2_chapter_6():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_6.html", admin_button=admin_button)
@app.route('/life_health/ltc/chapter_6_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_6_results():
	answer_1 = "To increase exposure to the states"
	answer_2 = "Guaranteed Renewable"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_6_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_7/', methods = ["GET","POST"])
def life_health_course_2_chapter_7():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_7.html", admin_button = admin_button)
@app.route('/life_health/ltc/chapter_7_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_7_results():
	answer_1 = "Illiterate"
	answer_2 = "Health Savings Accounts"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_7_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_8/', methods = ["GET","POST"])
def life_health_course_2_chapter_8():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_8.html", admin_button=admin_button)
@app.route('/life_health/ltc/chapter_8_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_8_results():
	answer_1 = "The 'donut hole'"
	answer_2 = "30-day"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_8_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_9/', methods = ["GET","POST"])
def life_health_course_2_chapter_9():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_9.html", admin_button = admin_button)
@app.route('/life_health/ltc/chapter_9_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_9_results():
	answer_1 = "Is on welfare"
	answer_2 = "Twisting"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_9_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_10/', methods = ["GET","POST"])
def life_health_course_2_chapter_10():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_10.html", admin_button=admin_button)
@app.route('/life_health/ltc/chapter_10_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_10_results():
	answer_1 = "Adult Day Health Care"
	answer_2 = "Respite Care"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_10_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/chapter_11/', methods = ["GET","POST"])
def life_health_course_2_chapter_11():
	admin_button = check_admin()
	return render_template("life_health/course_2/chapter_11.html", admin_button=admin_button)
@app.route('/life_health/ltc/chapter_11_results/', methods = ["GET","POST"])
def life_health_course_2_chapter_11_results():
	answer_1 = "Suitability Standards"
	answer_2 = "Waiver of Premium"
	result_data = result_chapter()
	return render_template("life_health/course_2/chapter_11_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/ltc/final_prep/<string:name>', methods = ["GET","POST"])
def life_health_course_2_final_prep(name):
	course_2_complete = True
	name = name
	db.execute("UPDATE fl_life_health_agent_1 SET course_2_complete = :course_2_complete WHERE name = :name", {"course_2_complete": course_2_complete, "name": name})
	db.commit()
	return render_template("life_health/course_2/final_prep.html", name=name)

@app.route('/life_health/ltc/review/<string:name>', methods = ["GET","POST"])
def life_health_course_2_review(name):
	name = name
	return render_template("life_health/course_2/review.html", name=name)

@app.route('/life_health/ltc/final_exam/<string:name>', methods = ["GET","POST"])
def life_health_course_2_final_exam(name):
	admin_button = check_admin()
	name = name
	return render_template("life_health/course_2/final_exam.html", name=name, admin_button = admin_button)

@app.route('/life_health/ltc/final_results/<string:name>', methods = ["GET","POST"])
def life_health_course_2_final_results(name):
	num_questions=60
	name = name
	date_fin = ''
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		course_2_score_date = "112336-1123660-10-LHV_LTC" + "-" + final_score  + "-" + "03-18-2021" + "/" + date_fin
		db.execute("UPDATE fl_life_health_agent_1 SET course_2_score_date = :course_2_score_date WHERE name = :name", {"course_2_score_date": course_2_score_date, "name": name})
		db.commit()
	return render_template("life_health/course_2/final_results.html",name=name, date_fin=date_fin, final_score=final_score, exam_pass = exam_pass)

@app.route('/life_health/ltc/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def life_health_course_2_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score
	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name='admin'
	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_life_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = 1123660
		offering_no = 1123660

	course = "Florida 10-Hour Long-Term Care & Partnership Programs for Life, Health, & Annuity Agents"

	return render_template("course_complete.html", user_name=user_name, first_name = first_name, last_name = last_name, address = address, course = course, license_no = license_no, license_state = license_state,  course_no = course_no, offering_no = offering_no, date_complete = date_complete,  percent = percent)

@app.route('/life_health/medicare/chapter_1/', methods = ["GET","POST"])
def life_health_course_3_chapter_1():
	if session.get("admin") is True:
		admin_button = True
		return render_template("life_health/course_3/chapter_1.html", admin_button=admin_button)
	name = session['name']
	course_passed = db.execute("SELECT course_3_complete FROM fl_life_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
	course_passed=course_passed[0][0]
	if  course_passed == True:
		return redirect(url_for("life_health_course_3_final_prep", name=name))
	return render_template("life_health/course_3/chapter_1.html")

@app.route('/life_health/medicare/chapter_1_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_1_results():
	answer_1 = "1965"
	answer_2 = "Four"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_1_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/chapter_2/', methods = ["GET","POST"])
def life_health_course_3_chapter_2():
	admin_button = check_admin()
	return render_template("life_health/course_3/chapter_2.html", admin_button=admin_button)
@app.route('/life_health/medicare/chapter_2_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_2_results():
	answer_1 = "65"
	answer_2 = "Higher"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_2_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/chapter_3/', methods = ["GET","POST"])
def life_health_course_3_chapter_3():
	admin_button = check_admin()
	return render_template("life_health/course_3/chapter_3.html", admin_button=admin_button)
@app.route('/life_health/medicare/chapter_3_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_3_results():
	answer_1 = "20 days"
	answer_2 = "Occupational therapy"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_3_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/chapter_4/', methods = ["GET","POST"])
def life_health_course_3_chapter_4():
	admin_button = check_admin()
	return render_template("life_health/course_3/chapter_4.html", admin_button=admin_button)
@app.route('/life_health/medicare/chapter_4_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_4_results():
	answer_1 = "Medicare Part C "
	answer_2 = "Medicare Parts A and B"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_4_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/chapter_5/', methods = ["GET","POST"])
def life_health_course_3_chapter_5():
	admin_button = check_admin()
	return render_template("life_health/course_3/chapter_5.html", admin_button=admin_button)
@app.route('/life_health/medicare/chapter_5_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_5_results():
	answer_1 = "Medigap "
	answer_2 = "Fill the gaps in Original Medicare Coverage"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_5_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/chapter_6/', methods = ["GET","POST"])
def life_health_course_3_chapter_6():
	admin_button = check_admin()
	return render_template("life_health/course_3/chapter_6.html", admin_button=admin_button)
@app.route('/life_health/medicare/chapter_6_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_6_results():
	answer_1 = "The poor "
	answer_2 = "Receiving Medicare"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_6_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/chapter_7/', methods = ["GET","POST"])
def life_health_course_3_chapter_7():
	admin_button = check_admin()
	return render_template("life_health/course_3/chapter_7.html", admin_button=admin_button)
@app.route('/life_health/medicare/chapter_7_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_7_results():
	answer_1 = "Risk Management"
	answer_2 = "All of the above"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_7_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/chapter_8/', methods = ["GET","POST"])
def life_health_course_3_chapter_8():
	admin_button = check_admin()
	return render_template("life_health/course_3/chapter_8.html", admin_button=admin_button)
@app.route('/life_health/medicare/chapter_8_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_8_results():
	answer_1 = "Mutual insurance company & Stock insurance company"
	answer_2 = "Branch claims office"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_8_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/chapter_9/', methods = ["GET","POST"])
def life_health_course_3_chapter_9():
	admin_button = check_admin()
	return render_template("life_health/course_3/chapter_9.html", admin_button=admin_button)
@app.route('/life_health/medicare/chapter_9_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_9_results():
	answer_1 = "Evidence and valid facts"
	answer_2 = "Salvage"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_9_results.html",  answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/chapter_10/', methods = ["GET","POST"])
def life_health_course_3_chapter_10():
	admin_button = check_admin()
	return render_template("life_health/course_3/chapter_10.html", admin_button=admin_button)
@app.route('/life_health/medicare/chapter_10_results/', methods = ["GET","POST"])
def life_health_course_3_chapter_10_results():
	answer_1 = "Focusing on your fees"
	answer_2 = "All of the above"
	result_data = result_chapter()
	return render_template("life_health/course_3/chapter_10_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/life_health/medicare/final_prep/<string:name>', methods = ["GET","POST"])
def life_health_course_3_final_prep(name):
	name = name
	course_3_complete = True
	db.execute("UPDATE fl_life_health_agent_1 SET course_3_complete = :course_3_complete WHERE name = :name", {"course_3_complete": course_3_complete, "name": name})
	db.commit()
	return render_template("life_health/course_3/final_prep.html", name=name)

@app.route('/life_health/medicare/review/<string:name>', methods = ["GET","POST"])
def life_health_course_3_review(name):
	name = name
	return render_template("life_health/course_3/review.html", name=name)

@app.route('/life_health/medicare/final_exam/<string:name>', methods = ["GET","POST"])
def life_health_course_3_final_exam(name):
	name = name
	admin_button = check_admin()
	return render_template("life_health/course_3/final_exam.html",name=name,  admin_button=admin_button)

@app.route('/life_health/medicare/final_results/<string:name>', methods = ["GET","POST"])
def life_health_course_3_final_results(name):
	num_questions=50
	name = name
	date_fin = ''
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		course_3_score_date = "112648-1124489-9-LHV_Medicare" + "-" + final_score  + "-" + "04-17-2021" + "/" + date_fin
		db.execute("UPDATE fl_life_health_agent_1 SET course_3_score_date = :course_3_score_date WHERE name = :name", {"course_3_score_date": course_3_score_date, "name": name})
		db.commit()
	return render_template("life_health/course_3/final_results.html",name=name, date_fin=date_fin, final_score=final_score, exam_pass = exam_pass)

@app.route('/life_health/medicare/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def life_health_course_3_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score
	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'
	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_life_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = 112648
		offering_no = 1124489

	course = "Florida 9-Hour Medicare, Medicaid for Life, Health, & Annuity Agents"
	return render_template("course_complete.html", user_name=user_name, first_name = first_name, last_name = last_name, address = address, course = course, license_no = license_no, license_state = license_state,  course_no = course_no, offering_no = offering_no, date_complete = date_complete,  percent = percent)

@app.route('/lhv/insurance_claims/', methods = ["GET"])
def life_health_course_4():
	chapter = lhv_courses.insurance_claims_5_intro
	session['course'] = "life-health-course-4"
	return render_template("course_intro_template.html", chapter=chapter)

@app.route('/lhv/insurance_claims/chapter_1/', methods = ["GET","POST"])
def life_health_course_4_chapter_1():
	chapter = lhv_courses.insurance_claims_5_chapter_1
	if session.get("admin") is True:
		admin_button = True
		return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)
	name = session['name']
	course_passed = db.execute("SELECT course_4_complete FROM fl_life_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
	course_passed = course_passed[0][0]
	if course_passed == True:
		print ('final')
		return redirect(url_for("life_health_course_4_final_prep", name=name))
	return render_template("chapter_template.html", chapter=chapter)

@app.route('/lhv/insurance_claims/chapter_1_results/', methods = ["GET","POST"])
def life_health_course_4_chapter_1_results():
	chapter = lhv_courses.insurance_claims_5_chapter_1
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/lhv/insurance_claims/chapter_2/', methods = ["GET","POST"])
def life_health_course_4_chapter_2():
	chapter = lhv_courses.insurance_claims_5_chapter_2
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/lhv/insurance_claims/chapter_2_results/', methods = ["GET","POST"])
def life_health_course_4_chapter_2_results():
	chapter = lhv_courses.insurance_claims_5_chapter_2
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/lhv/insurance_claims/chapter_3/', methods = ["GET","POST"])
def life_health_course_4_chapter_3():
	chapter = lhv_courses.insurance_claims_5_chapter_3
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/lhv/insurance_claims/chapter_3_results/', methods = ["GET","POST"])
def life_health_course_4_chapter_3_results():
	chapter = lhv_courses.insurance_claims_5_chapter_3
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/lhv/insurance_claims/chapter_4/', methods = ["GET","POST"])
def life_health_course_4_chapter_4():
	chapter = lhv_courses.insurance_claims_5_chapter_4
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/lhv/insurance_claims/chapter_4_results/', methods = ["GET","POST"])
def life_health_course_4_chapter_4_results():
	chapter = lhv_courses.insurance_claims_5_chapter_4
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/lhv/insurance_claims/chapter_5/', methods = ["GET","POST"])
def life_health_course_4_chapter_5():
	chapter = lhv_courses.insurance_claims_5_chapter_5
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/lhv/insurance_claims/chapter_5_results/', methods = ["GET","POST"])
def life_health_course_4_chapter_5_results():
	chapter = lhv_courses.insurance_claims_5_chapter_5
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/lhv/insurance_claims/final_prep/<string:name>', methods = ["GET","POST"])
def life_health_course_4_final_prep(name):
	chapter = lhv_courses.insurance_claims_5_final_prep
	name = name
	course_4_complete = True
	db.execute("UPDATE fl_life_health_agent_1 SET course_4_complete = :course_4_complete WHERE name = :name", {"course_4_complete": course_4_complete, "name": name})
	db.commit()
	return render_template("final_prep_template.html", chapter=chapter, name=name)

@app.route('/lhv/insurance_claims/review/<string:name>', methods = ["GET","POST"])
def life_health_course_4_review(name):
	name = name
	chapter = lhv_courses.insurance_claims_5_review
	return render_template("review_template.html", chapter=chapter, name=name)

@app.route('/lhv/insurance_claims/final_exam/<string:name>', methods = ["GET","POST"])
def life_health_course_4_final_exam(name):
	name = name
	chapter = lhv_courses.insurance_claims_5_final_exam
	admin_button = check_admin()
	return render_template("final_exam_template.html", admin_button=admin_button, chapter=chapter, name=name)

@app.route('/lhv/insurance_claims/final_results/<string:name>', methods = ["GET","POST"])
def life_health_course_4_final_results(name):
	name = name
	date_fin = ''
	chapter = lhv_courses.insurance_claims_5_final_results
	num_questions=30
	final_score_data=final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	print ('final', final_score )
	if exam_pass==True:
		date_fin = final_score_data[2]
		course_4_score_date = "113621-1127685-5-LHV_InsClaims" + "-" + final_score  + "-" + "06-26-2021" + "/" + date_fin
		db.execute("UPDATE fl_life_health_agent_1 SET course_4_score_date = :course_4_score_date WHERE name = :name", {"course_4_score_date": course_4_score_date, "name": name})
		db.commit()

	return render_template("final_results_template.html",  name=name, date_fin=date_fin, final_score=final_score, exam_pass=exam_pass, chapter=chapter)

@app.route('/lhv/insurance_claims/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def life_health_course_4_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score

	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'

	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_life_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
		print("data", data)
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = "113621"
		offering_no = "1127685"

	course = "Florida 5-Hour Insurance Claims Update"
	return render_template("course_complete.html", user_name = user_name, first_name = first_name, last_name = last_name, license_no = license_no, address = address, course = course,  license_state = license_state,  course_no = course_no, offering_no = offering_no,  percent = percent, date_complete=date_complete)

###########################HEALTH****************************************

@app.route('/health/ethics/chapter_1/', methods = ["GET","POST"])
def health_ethics_chapter_1():
	if session.get("admin") is True:
		admin_button = True
		return render_template("health/ethics/chapter_1.html", admin_button=admin_button)
	name = session['name']
	ethics_passed = db.execute("SELECT ethics_course FROM fl_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
	ethics_passed=ethics_passed[0][0]
	if  ethics_passed == True:
		return redirect(url_for("health_ethics_final_prep", name=name))
	return render_template("health/ethics/chapter_1.html")

@app.route('/health/ethics/chapter_1_results/', methods = ["GET","POST"])
def health_ethics_chapter_1_results():
	answer_1 = "Consumer Services"
	answer_2 = "Office of Inspector General"
	result_data = result_chapter()
	return render_template("health/ethics/chapter_1_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/ethics/chapter_2/', methods = ["GET","POST"])
def health_ethics_chapter_2():
	admin_button = check_admin()
	return render_template("health/ethics/chapter_2.html", admin_button=admin_button)

@app.route('/health/ethics/chapter_2_results/', methods = ["GET","POST"])
def health_ethics_chapter_2_results():
	answer_1 = "Studying for an exam"
	answer_2 = "$10,000"
	result_data = result_chapter()
	return render_template("health/ethics/chapter_2_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/ethics/chapter_3/', methods = ["GET","POST"])
def health_ethics_chapter_3():
	admin_button = check_admin()
	return render_template("health/ethics/chapter_3.html", admin_button=admin_button)
@app.route('/health/ethics/chapter_3_results/', methods = ["GET","POST"])
def health_ethics_chapter_3_results():
	answer_1 = "Accredited state"
	answer_2 = "Home state"
	result_data = result_chapter()
	return render_template("health/ethics/chapter_3_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/ethics/chapter_4/', methods = ["GET","POST"])
def health_ethics_chapter_4():
	admin_button = check_admin()
	return render_template("health/ethics/chapter_4.html", admin_button=admin_button)
@app.route('/health/ethics/chapter_4_results/', methods = ["GET","POST"])
def health_ethics_chapter_4_results():
	answer_1 = "Twisting"
	answer_2 = "Continuous"
	result_data = result_chapter()
	return render_template("health/ethics/chapter_4_results.html",answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/ethics/chapter_5/', methods = ["GET","POST"])
def health_ethics_chapter_5():
	admin_button = check_admin()
	return render_template("health/ethics/chapter_5.html", admin_button=admin_button)
@app.route('/health/ethics/chapter_5_results/', methods = ["GET","POST"])
def health_ethics_chapter_5_results():
	answer_1 = "Public adjuster account"
	answer_2 = "Participate in the adjustment"
	result_data = result_chapter()
	return render_template("health/ethics/chapter_5_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/ethics/chapter_6/', methods = ["GET","POST"])
def health_ethics_chapter_6():
	admin_button = check_admin()
	return render_template("health/ethics/chapter_6.html", admin_button=admin_button)
@app.route('/health/ethics/chapter_6_results/', methods = ["GET","POST"])
def health_ethics_chapter_6_results():
	answer_1 = "Affordability index"
	answer_2 = "Mediator"
	result_data = result_chapter()
	return render_template("health/ethics/chapter_6_results.html", answer_1=answer_1,answer_2=answer_2, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/ethics/final_prep/<string:name>', methods = ["GET","POST"])
def health_ethics_final_prep(name):
	name = name
	ethics_course = True
	db.execute("UPDATE fl_health_agent_1 SET ethics_course = :ethics_course WHERE name = :name", {"ethics_course": ethics_course, "name": name})
	db.commit()
	return render_template("health/ethics/final_prep.html", name=name)

@app.route('/health/ethics/review/<string:name>', methods = ["GET","POST"])
def health_ethics_review(name):
	name = name
	return render_template("health/ethics/review.html", name=name)

@app.route('/health/ethics/final_exam/<string:name>', methods = ["GET","POST"])
def health_ethics_final_exam(name):
	name = name
	admin_button = check_admin()
	return render_template("health/ethics/final_exam.html", admin_button=admin_button, name=name)

@app.route('/health/ethics/final_results/<string:name>', methods = ["GET","POST"])
def health_ethics_final_results(name):
	num_questions = 30
	date_fin = ''
	name = name
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	if exam_pass==True:
		date_fin = final_score_data[2]
		ethics_score_date = "112975-1125614-5-H_Ethics" + "-" + final_score  + "-" + "05-14-2021" + "/" + date_fin
		db.execute("UPDATE fl_health_agent_1 SET ethics_score_date = :ethics_score_date WHERE name = :name", {"ethics_score_date": ethics_score_date, "name": name})
		db.commit()
	return render_template("health/ethics/final_results.html",  name=name, date_fin=date_fin, final_score=final_score, exam_pass=exam_pass)

@app.route('/health/ethics/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def health_ethics_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score
	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'
	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = 112975
		offering_no = 1125614

	course = "Florida 5-Hour Law & Ethics Update for Health Agents"
	return render_template("course_complete.html", user_name = user_name, first_name = first_name, last_name = last_name, address = address, course = course, license_no = license_no, license_state = license_state,  course_no = course_no, offering_no = offering_no, date_complete = date_complete,  percent = percent)


@app.route('/health/long_term_care/', methods = ["GET"])
def health_course_2():
	chapter = health_courses.long_term_care_10_intro
	session['course'] = "health-course-2"
	return render_template("course_intro_template.html", chapter=chapter)

@app.route('/health/long_term_care/chapter_1/', methods = ["GET","POST"])
def health_course_2_chapter_1():
	chapter = health_courses.long_term_care_10_chapter_1
	if session.get("admin") is True:
		admin_button = True
		return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)
	name = session['name']
	course_passed = db.execute("SELECT course_2_complete FROM fl_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
	course_passed = course_passed[0][0]
	if course_passed == True:
		print ('final')
		return redirect(url_for("health_course_2_final_prep", name=name))
	return render_template("chapter_template.html", chapter=chapter)

@app.route('/health/long_term_care/chapter_1_results/', methods = ["GET","POST"])
def health_course_2_chapter_1_results():
	chapter = health_courses.long_term_care_10_chapter_1
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_2/', methods = ["GET","POST"])
def health_course_2_chapter_2():
	chapter = health_courses.long_term_care_10_chapter_2
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_2_results/', methods = ["GET","POST"])
def health_course_2_chapter_2_results():
	chapter = health_courses.long_term_care_10_chapter_2
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_3/', methods = ["GET","POST"])
def health_course_2_chapter_3():
	chapter = health_courses.long_term_care_10_chapter_3
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_3_results/', methods = ["GET","POST"])
def health_course_2_chapter_3_results():
	chapter = health_courses.long_term_care_10_chapter_3
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_4/', methods = ["GET","POST"])
def health_course_2_chapter_4():
	chapter = health_courses.long_term_care_10_chapter_4
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_4_results/', methods = ["GET","POST"])
def health_course_2_chapter_4_results():
	chapter = health_courses.long_term_care_10_chapter_4
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_5/', methods = ["GET","POST"])
def health_course_2_chapter_5():
	chapter = health_courses.long_term_care_10_chapter_5
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_5_results/', methods = ["GET","POST"])
def health_course_2_chapter_5_results():
	chapter = health_courses.long_term_care_10_chapter_5
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_6/', methods = ["GET","POST"])
def health_course_2_chapter_6():
	chapter = health_courses.long_term_care_10_chapter_6
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_6_results/', methods = ["GET","POST"])
def health_course_2_chapter_6_results():
	chapter = health_courses.long_term_care_10_chapter_6
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_7/', methods = ["GET","POST"])
def health_course_2_chapter_7():
	chapter = health_courses.long_term_care_10_chapter_7
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_7_results/', methods = ["GET","POST"])
def health_course_2_chapter_7_results():
	chapter = health_courses.long_term_care_10_chapter_7
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_8/', methods = ["GET","POST"])
def health_course_2_chapter_8():
	chapter = health_courses.long_term_care_10_chapter_8
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_8_results/', methods = ["GET","POST"])
def health_course_2_chapter_8_results():
	chapter = health_courses.long_term_care_10_chapter_8
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_9/', methods = ["GET","POST"])
def health_course_2_chapter_9():
	chapter = health_courses.long_term_care_10_chapter_9
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_9_results/', methods = ["GET","POST"])
def health_course_2_chapter_9_results():
	chapter = health_courses.long_term_care_10_chapter_9
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_10/', methods = ["GET","POST"])
def health_course_2_chapter_10():
	chapter = health_courses.long_term_care_10_chapter_10
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_10_results/', methods = ["GET","POST"])
def health_course_2_chapter_10_results():
	chapter = health_courses.long_term_care_10_chapter_10
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/chapter_11/', methods = ["GET","POST"])
def health_course_2_chapter_11():
	chapter = health_courses.long_term_care_10_chapter_11
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/long_term_care/chapter_11_results/', methods = ["GET","POST"])
def health_course_2_chapter_11_results():
	chapter = health_courses.long_term_care_10_chapter_11
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/long_term_care/final_prep/<string:name>', methods = ["GET","POST"])
def health_course_2_final_prep(name):
	chapter = health_courses.long_term_care_10_final_prep
	name = name
	course_2_complete = True
	db.execute("UPDATE fl_health_agent_1 SET course_2_complete = :course_2_complete WHERE name = :name", {"course_2_complete": course_2_complete, "name": name})
	db.commit()
	return render_template("final_prep_template.html", chapter=chapter, name=name)

@app.route('/health/long_term_care/review/<string:name>', methods = ["GET","POST"])
def health_course_2_review(name):
	name = name
	chapter = health_courses.long_term_care_10_review
	return render_template("review_template.html", chapter=chapter, name=name)

@app.route('/health/long_term_care/final_exam/<string:name>', methods = ["GET","POST"])
def health_course_2_final_exam(name):
	name = name
	chapter = health_courses.long_term_care_10_final_exam
	admin_button = check_admin()
	return render_template("final_exam_template.html", admin_button=admin_button, chapter=chapter, name=name)

@app.route('/health/long_term_care/final_results/<string:name>', methods = ["GET","POST"])
def health_course_2_final_results(name):
	name = name
	date_fin = ''
	chapter = health_courses.long_term_care_10_final_results
	num_questions = 60
	final_score_data = final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass = final_score_data[1]
	print ('final', final_score )
	if exam_pass == True:
		date_fin = final_score_data[2]
		course_2_score_date = "113776-1127731-10-H_LTC" + "-" + final_score  + "-" + "07-7-2021" + "/" + date_fin
		db.execute("UPDATE fl_health_agent_1 SET course_2_score_date = :course_2_score_date WHERE name = :name", {"course_2_score_date": course_2_score_date, "name": name})
		db.commit()

	return render_template("final_results_template.html",  name=name, date_fin=date_fin, final_score=final_score, exam_pass=exam_pass, chapter=chapter)

@app.route('/health/long_term_care/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def health_course_2_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score

	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'

	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
		print("data", data)
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = "113776"
		offering_no = "1127731"

	course = "Florida 10-Hour Long Term Care & Partnership Programs"
	return render_template("course_complete.html", user_name = user_name, first_name = first_name, last_name = last_name, license_no = license_no, address = address, course = course,  license_state = license_state,  course_no = course_no, offering_no = offering_no,  percent = percent, date_complete=date_complete)

@app.route('/health/medicare/', methods = ["GET"])
def health_course_3():
	chapter = health_courses.medicare_9_intro
	session['course'] = "health-course-3"
	return render_template("course_intro_template.html", chapter=chapter)

@app.route('/health/medicare/chapter_1/', methods = ["GET","POST"])
def health_course_3_chapter_1():
	chapter = health_courses.medicare_9_chapter_1
	if session.get("admin") is True:
		admin_button = True
		return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)
	name = session['name']
	course_passed = db.execute("SELECT course_3_complete FROM fl_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
	course_passed = course_passed[0][0]
	if course_passed == True:
		print ('final')
		return redirect(url_for("health_course_3_final_prep", name=name))
	return render_template("chapter_template.html", chapter=chapter)

@app.route('/health/medicare/chapter_1_results/', methods = ["GET","POST"])
def health_course_3_chapter_1_results():
	chapter = health_courses.medicare_9_chapter_1
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/chapter_2/', methods = ["GET","POST"])
def health_course_3_chapter_2():
	chapter = health_courses.medicare_9_chapter_2
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/medicare/chapter_2_results/', methods = ["GET","POST"])
def health_course_3_chapter_2_results():
	chapter = health_courses.medicare_9_chapter_2
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/chapter_3/', methods = ["GET","POST"])
def health_course_3_chapter_3():
	chapter = health_courses.medicare_9_chapter_3
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/medicare/chapter_3_results/', methods = ["GET","POST"])
def health_course_3_chapter_3_results():
	chapter = health_courses.medicare_9_chapter_3
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/chapter_4/', methods = ["GET","POST"])
def health_course_3_chapter_4():
	chapter = health_courses.medicare_9_chapter_4
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/medicare/chapter_4_results/', methods = ["GET","POST"])
def health_course_3_chapter_4_results():
	chapter = health_courses.medicare_9_chapter_4
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/chapter_5/', methods = ["GET","POST"])
def health_course_3_chapter_5():
	chapter = health_courses.medicare_9_chapter_5
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/medicare/chapter_5_results/', methods = ["GET","POST"])
def health_course_3_chapter_5_results():
	chapter = health_courses.medicare_9_chapter_5
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/chapter_6/', methods = ["GET","POST"])
def health_course_3_chapter_6():
	chapter = health_courses.medicare_9_chapter_6
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/medicare/chapter_6_results/', methods = ["GET","POST"])
def health_course_3_chapter_6_results():
	chapter = health_courses.medicare_9_chapter_6
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/chapter_7/', methods = ["GET","POST"])
def health_course_3_chapter_7():
	chapter = health_courses.medicare_9_chapter_7
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/medicare/chapter_7_results/', methods = ["GET","POST"])
def health_course_3_chapter_7_results():
	chapter = health_courses.medicare_9_chapter_7
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/chapter_8/', methods = ["GET","POST"])
def health_course_3_chapter_8():
	chapter = health_courses.medicare_9_chapter_8
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/medicare/chapter_8_results/', methods = ["GET","POST"])
def health_course_3_chapter_8_results():
	chapter = health_courses.medicare_9_chapter_8
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/chapter_9/', methods = ["GET","POST"])
def health_course_3_chapter_9():
	chapter = health_courses.medicare_9_chapter_9
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/medicare/chapter_9_results/', methods = ["GET","POST"])
def health_course_3_chapter_9_results():
	chapter = health_courses.medicare_9_chapter_9
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/chapter_10/', methods = ["GET","POST"])
def health_course_3_chapter_10():
	chapter = health_courses.medicare_9_chapter_10
	admin_button = check_admin()
	print ("admin_button", admin_button)
	return render_template("chapter_template.html", chapter=chapter, admin_button=admin_button)

@app.route('/health/medicare/chapter_10_results/', methods = ["GET","POST"])
def health_course_3_chapter_10_results():
	chapter = health_courses.medicare_9_chapter_10
	result_data = result_chapter()
	return render_template("chapter_results_template.html", chapter=chapter, wrong_answer=result_data[0],
	result_1=result_data[1], result_2=result_data[2])

@app.route('/health/medicare/final_prep/<string:name>', methods = ["GET","POST"])
def health_course_3_final_prep(name):
	chapter = health_courses.medicare_9_final_prep
	name = name
	course_3_complete = True
	db.execute("UPDATE fl_health_agent_1 SET course_3_complete = :course_3_complete WHERE name = :name", {"course_3_complete": course_3_complete, "name": name})
	db.commit()
	return render_template("final_prep_template.html", chapter=chapter, name=name)

@app.route('/health/medicare/review/<string:name>', methods = ["GET","POST"])
def health_course_3_review(name):
	name = name
	chapter = health_courses.medicare_9_review
	return render_template("review_template.html", chapter=chapter, name=name)

@app.route('/health/medicare/final_exam/<string:name>', methods = ["GET","POST"])
def health_course_3_final_exam(name):
	name = name
	chapter = health_courses.medicare_9_final_exam
	admin_button = check_admin()
	return render_template("final_exam_template.html", admin_button=admin_button, chapter=chapter, name=name)

@app.route('/health/medicare/final_results/<string:name>', methods = ["GET","POST"])
def health_course_3_final_results(name):
	name = name
	date_fin = ''
	chapter = health_courses.medicare_9_final_results
	num_questions=50
	final_score_data=final_results(num_questions)
	final_score = final_score_data[0]
	exam_pass=final_score_data[1]
	print ('final', final_score )
	if exam_pass==True:
		date_fin = final_score_data[2]
		course_3_score_date = "113838-1127954-9-H_Medicare" + "-" + final_score  + "-" + "07-13-2021" + "/" + date_fin
		# course_4_score_date =  date_fin + "-" + final_score + "-" + "/1127954-113838-09/08/2020-5-pa_ethics"
		db.execute("UPDATE fl_health_agent_1 SET course_3_score_date = :course_3_score_date WHERE name = :name", {"course_3_score_date": course_3_score_date, "name": name})
		db.commit()

	return render_template("final_results_template.html",  name=name, date_fin=date_fin, final_score=final_score, exam_pass=exam_pass, chapter=chapter)

@app.route('/health/medicare/course_complete/<string:name>/<int:final_score>/<path:date_fin>', methods = ["GET","POST"])
def health_course_3_course_complete(name, final_score, date_fin):
	name = name
	date_complete = date_fin
	percent = final_score

	if session.get("admin") is True:
		first_name = 'admin'
		last_name = 'admin'
		license_no = 'admin'
		license_state = 'FL'
		course_no = 'admin'
		offering_no = "admin"
		address = 'admin'
		user_name = 'admin'

	else:
		data = db.execute("SELECT first, last, license_no, license_state, address, name FROM fl_health_agent_1 WHERE name = :name" , {"name": name}).fetchall()
		print("data", data)
		first_name = data[0][0]
		last_name = data[0][1]
		license_no = data[0][2]
		license_state = data[0][3]
		address = data[0][4]
		user_name = data[0][5]
		course_no = "1127954"
		offering_no = "113838"

	course = " Florida 9-Hour Medicare & Medicaid"
	return render_template("course_complete.html", user_name = user_name, first_name = first_name, last_name = last_name, license_no = license_no, address = address, course = course,  license_state = license_state,  course_no = course_no, offering_no = offering_no,  percent = percent, date_complete=date_complete)
