from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import re  #regex
import datetime
import pandas as pd
from flask_session import Session
engine = create_engine("postgres://iykazvclamrzem:140bdec1e446a9119d4fb1c9e20d89fb17716e702de72b7be09f2b2e53b86d36@ec2-50-19-127-115.compute-1.amazonaws.com:5432/d134n6bd1767sd")
db = scoped_session(sessionmaker(bind=engine))
def recent_certificates():
# Provider_ID	Course_ID	Offering_ID	End_Date SSN_License_Nbr	First_Name	Last_Name	Pass_Fail	Hours	Grade	Date_Earned
# '90/6/27/2020/lh-medicare-9-1124489', 'Amy', 'Simmons', 'W188686'
	pa1 = db.execute("SELECT ethics_score_date, first, last, license_no FROM fl_public_adjuster_1").fetchall()
	# course_id = 109996
	# end_date = 09/08/2020
	pa2= db.execute("SELECT flood_score_date, first, last, license_no FROM fl_public_adjuster_1").fetchall()
	pa3 = db.execute("SELECT property_score_date, first, last,license_no FROM fl_public_adjuster_1").fetchall()
	pa4 = db.execute("SELECT course_4_score_date, first, last,license_no FROM fl_public_adjuster_1").fetchall()

	ia1 = db.execute("SELECT ethics_score_date, first, last, license_no FROM fl_independent_adjuster_1").fetchall()
	ia2 = db.execute("SELECT course_2_score_date, first, last,license_no FROM fl_independent_adjuster_1").fetchall()
	ia3 = db.execute("SELECT course_3_score_date, first, last,license_no FROM fl_independent_adjuster_1").fetchall()
	ia4 = db.execute("SELECT course_4_score_date, first, last,license_no FROM fl_independent_adjuster_1").fetchall()

	h1 = db.execute("SELECT ethics_score_date, first, last,license_no FROM fl_health_agent_1").fetchall()
	h2 = db.execute("SELECT course_2_score_date, first, last,license_no FROM fl_health_agent_1").fetchall()
	h3 = db.execute("SELECT course_3_score_date, first, last,license_no FROM fl_health_agent_1").fetchall()

	lhv1 = db.execute("SELECT ethics_score_date, first, last,license_no FROM fl_life_health_agent_1").fetchall()
	lhv2 = db.execute("SELECT course_2_score_date, first, last,license_no FROM fl_life_health_agent_1").fetchall()
	lhv3= db.execute("SELECT course_3_score_date, first, last,license_no FROM fl_life_health_agent_1").fetchall()
	lhv4= db.execute("SELECT course_4_score_date, first, last,license_no FROM fl_life_health_agent_1").fetchall()

	user_all =[]

	user_all.append(pa1), user_all.append(pa2),user_all.append(pa3),
	user_all.append(pa4),user_all.append(ia1), user_all.append(ia2),
	user_all.append(ia3),user_all.append(ia4), user_all.append(h1), user_all.append(h2),
	user_all.append(h3), user_all.append(lhv1), user_all.append(lhv2),
	user_all.append(lhv3), user_all.append(lhv4)

	course_finish_dict = {
				'FIRST NAME': [],
				'LAST': [],
		  }

	regex = '76/6/20/2020/-lh-ltc-10-1123660-109996-09/08/2020'
	# regex = '-1123660-109996-1112515-09/08/2020-w258331-Russ-Mckee-pass-9-70-7/20/2020-lhltc'
	slash = re.split("\-", regex)
	# print ("slash",slash)
	slash2 = re.split("\/", slash[0])
	# print ("slash",slash2)

	for index in user_all:
		z=0
		# print("******")
		for i in index:
			z=z+1
			if index[z-1][0] != None:
				# print(index[z-1][0])

				separate = re.split("\/", index[z-1][0])
				# print('sep',separate)

				# print('sep3',separate[0])
				month_complete = int(separate[1])
				# print('month_complete', month_complete)
				day_complete = int(separate[2])
				# print('day_complete', day_complete)
				year_complete = int(separate[3])

				now = datetime.datetime.now()
				# print("today-date", now)
				month_now = (now.month)
				day_now = (now.day)
				year_now = (now.year)
				day_diff = day_now - day_complete
				month_diff = month_now - month_complete
				year_diff = year_now - year_complete
				# if month_complete == 6:
					# if day_complete ==30:
						# print('pass_course', index[z-1])

				if month_diff == 0:

					# if (day_diff == 1 or day_diff == 2 or day_diff == 3):
					if (day_diff == 0):
						# print("***********************************************")
						print('pass_course', index[z-1])
						# separate2 = re.split("\/", index[z-1][0])
						# print(separate2)
						# separate3 = re.split("\-", separate2[0])
						# print(separate3)
						# The course id# is 109996.
						# Offering ID is 1112515

			    		# regex = '-1123660-109996-1112515-09/08/2020-w258331-Russ-Mckee-pass-9-70-7/20/2020-lhltc'
								# ProviderID_CourseID_OfferingID_End Date_SSN/License-Nbr_First-Name_Last-Name_Pass/Fail	Hours	Grade	Date Earned

						'''
						offering_id = separate3[3]
						print ("offering_id = ", offering_id)
						provider_id = 372120
						print ("provider_id = ", provider_id)
						# Course_ID
						# End_Date
						license_no = index[z-1][3]
						print ("license_no = ", license_no)
						first_name = index[z-1][1]
						print ("first_name = ", first_name)
						last_name = index[z-1][2]
						print ("last_name = ", last_name)
						pass_fail = "PASS"
						print ("pass_fail = ", pass_fail)
						hours = separate3[2]
						print("hours", hours)
						grade = separate2[0]
						print("grade = ", grade)

						date = separate2[1] + "/" + separate2[2] + "/" + separate2[3]
						print ("date_earned = ", date)
						'''


						#
						# ['90', '6', '27', '2020', 'lh-medicare-9-1124489']
						# print(separate2[4])
						# print('first',index[z-1][1])
						# print ("day differences", day_diff)

						# data = index[z-1]
						# print ("data", data)
						# data ('76/6/20/2020/lh-ltc-10-1123660', 'Ronald David', 'Salter', 'w232733')


						name_dict = {
						            'SCORE': [],
						            'FIRST': [],
									'LAST': [],
									'ID': [],
						          }
						# print('namedict', name_dict['SCORE'][3])
						# name_dict['SCORE'][3]='russ'
						# print('namedict', name_dict['SCORE'][3])
						name_dict['SCORE'].append('russ1')
						name_dict['FIRST'].append('russ2')
						name_dict['LAST'].append('russ3')
						name_dict['ID'].append('russ4')

						course_finish_dict['FIRST NAME'].append(index[z-1][1])
						course_finish_dict['LAST'].append(index[z-1][2])
						# print('namedict', name_dict['SCORE'])
						df = pd.DataFrame(course_finish_dict)

						# print ('DF',df)
						# df.to_csv('russ_file1.csv', index = False)
						course_finish = {
									'Provider_ID': [],
									'Course_ID': [],
									'Offering_ID': [],
									'End_Date': [],
									'SSN_License_Nbr': [],
									'First_Name': [],
									'Last_Name': [],
									'Pass_Fail': [],
									'Hours': [],
									'Grade': [],
									'Date_Earned': [],
							  }

def recent_certificates_csv():
	print("CSV.......................")
# Provider_ID	Course_ID	Offering_ID	End_Date SSN_License_Nbr	First_Name	Last_Name	Pass_Fail	Hours	Grade	Date_Earned
# '90/6/27/2020/lh-medicare-9-1124489', 'Amy', 'Simmons', 'W188686'
	pa1 = db.execute("SELECT ethics_score_date, first, last, license_no FROM fl_public_adjuster_1").fetchall()
	# course_id = 109996
	# end_date = 09/08/2020
	pa2= db.execute("SELECT flood_score_date, first, last, license_no FROM fl_public_adjuster_1").fetchall()
	pa3 = db.execute("SELECT property_score_date, first, last,license_no FROM fl_public_adjuster_1").fetchall()
	pa4 = db.execute("SELECT course_4_score_date, first, last,license_no FROM fl_public_adjuster_1").fetchall()

	ia1 = db.execute("SELECT ethics_score_date, first, last, license_no FROM fl_independent_adjuster_1").fetchall()
	ia2 = db.execute("SELECT course_2_score_date, first, last,license_no FROM fl_independent_adjuster_1").fetchall()
	ia3 = db.execute("SELECT course_3_score_date, first, last,license_no FROM fl_independent_adjuster_1").fetchall()
	ia4 = db.execute("SELECT course_4_score_date, first, last,license_no FROM fl_independent_adjuster_1").fetchall()

	h1 = db.execute("SELECT ethics_score_date, first, last,license_no FROM fl_health_agent_1").fetchall()
	h2 = db.execute("SELECT course_2_score_date, first, last,license_no FROM fl_health_agent_1").fetchall()
	h3 = db.execute("SELECT course_3_score_date, first, last,license_no FROM fl_health_agent_1").fetchall()

	lhv1 = db.execute("SELECT ethics_score_date, first, last,license_no FROM fl_life_health_agent_1").fetchall()
	lhv2 = db.execute("SELECT course_2_score_date, first, last,license_no FROM fl_life_health_agent_1").fetchall()
	lhv3= db.execute("SELECT course_3_score_date, first, last,license_no FROM fl_life_health_agent_1").fetchall()
	lhv4= db.execute("SELECT course_4_score_date, first, last,license_no FROM fl_life_health_agent_1").fetchall()

	user_all =[]

	user_all.append(pa1), user_all.append(pa2),user_all.append(pa3),
	user_all.append(pa4),user_all.append(ia1), user_all.append(ia2),
	user_all.append(ia3),user_all.append(ia4), user_all.append(h1), user_all.append(h2),
	user_all.append(h3), user_all.append(lhv1), user_all.append(lhv2),
	user_all.append(lhv3), user_all.append(lhv4)

	course_finish_dict = {
				'FIRST NAME': [],
				'LAST': [],
		  }

	regex = '76/6/20/2020/-lh-ltc-10-1123660-109996-09/08/2020'
	# regex = '-1123660-109996-1112515-09/08/2020-w258331-Russ-Mckee-pass-9-70-7/20/2020-lhltc'
	slash = re.split("\-", regex)
	# print ("slash",slash)
	slash2 = re.split("\/", slash[0])
	# print ("slash",slash2)

	for index in user_all:
		z=0
		# print("******")
		for i in index:
			z=z+1
			if index[z-1][0] != None:
				# print(index[z-1][0])

				separate = re.split("\/", index[z-1][0])
				# print('sep',separate)

				# print('sep3',separate[0])
				month_complete = int(separate[1])
				# print('month_complete', month_complete)
				day_complete = int(separate[2])
				# print('day_complete', day_complete)
				year_complete = int(separate[3])

				now = datetime.datetime.now()
				# print("today-date", now)
				month_now = (now.month)
				day_now = (now.day)
				year_now = (now.year)
				day_diff = day_now - day_complete
				month_diff = month_now - month_complete
				year_diff = year_now - year_complete
				# if month_complete == 6:
					# if day_complete ==30:
						# print('pass_course', index[z-1])

				if month_diff == 0:

					# if (day_diff == 1 or day_diff == 2):
					if (day_diff == 0):
						# print("***********************************************")
						print('pass_course', index[z-1])
						separate2 = re.split("\/", index[z-1][0])
						print('regex /', separate2)

						date = separate2[1] + "/" + separate2[2] + "/" + separate2[3]
						print('date', date)
						# separate2 = index[z-1][0]
						# print(separate2)
						# separate3 = re.split("\-", separate2[0])
						# print(separate3)
						# The course id# is 109996.
						# Offering ID is 1112515

			    		# regex = '-1123660-109996-1112515-09/08/2020-w258331-Russ-Mckee-pass-9-70-7/20/2020-lhltc'
								# ProviderID_CourseID_OfferingID_End Date_SSN/License-Nbr_First-Name_Last-Name_Pass/Fail	Hours	Grade	Date Earned

						'''
						offering_id = separate3[3]
						print ("offering_id = ", offering_id)
						provider_id = 372120
						print ("provider_id = ", provider_id)
						# Course_ID
						# End_Date
						license_no = index[z-1][3]
						print ("license_no = ", license_no)
						first_name = index[z-1][1]
						print ("first_name = ", first_name)
						last_name = index[z-1][2]
						print ("last_name = ", last_name)
						pass_fail = "PASS"
						print ("pass_fail = ", pass_fail)
						hours = separate3[2]
						print("hours", hours)
						grade = separate2[0]
						print("grade = ", grade)

						date = separate2[1] + "/" + separate2[2] + "/" + separate2[3]
						print ("date_earned = ", date)
						'''


						#
						# ['90', '6', '27', '2020', 'lh-medicare-9-1124489']
						# print(separate2[4])
						# print('first',index[z-1][1])
						# print ("day differences", day_diff)

						# data = index[z-1]
						# print ("data", data)
						# data ('76/6/20/2020/lh-ltc-10-1123660', 'Ronald David', 'Salter', 'w232733')


						name_dict = {
						            'SCORE': [],
						            'FIRST': [],
									'LAST': [],
									'ID': [],
						          }
						# print('namedict', name_dict['SCORE'][3])
						# name_dict['SCORE'][3]='russ'
						# print('namedict', name_dict['SCORE'][3])
						name_dict['SCORE'].append('russ1')
						name_dict['FIRST'].append('russ2')
						name_dict['LAST'].append('russ3')
						name_dict['ID'].append('russ4')

						course_finish_dict['FIRST NAME'].append(index[z-1][1])
						course_finish_dict['LAST'].append(index[z-1][2])
						# print('namedict', name_dict['SCORE'])
						df = pd.DataFrame(course_finish_dict)

						# print ('DF',df)
						# df.to_csv('russ_file1.csv', index = False)
						course_finish = {
									'Provider_ID': [],
									'Course_ID': [],
									'Offering_ID': [],
									'End_Date': [],
									'SSN_License_Nbr': [],
									'First_Name': [],
									'Last_Name': [],
									'Pass_Fail': [],
									'Hours': [],
									'Grade': [],
									'Date_Earned': [],
							  }



# Define a class
class Student:
	def __init__(self, name, license, course, final_score, date_fin, admin):
		self.name = name
		self.license = license
		self.course = course
		self.final_score = final_score
		self.date_fin = date_fin
		self.admin = admin

	def tell_me_about_the_octopus(self):
		print("This octopus is " + self.color + ".")
		print(self.name + " is the octopus's name.")
