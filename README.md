# python_scrap_ndtv
Scrapping NDTV world news and store them in mongodb and use private api to retrieve them.
#Setup MongoDB

#Install Mongodb
Download MongoDB from given link according to your os architecture:-
https://www.mongodb.com/download-center

#Setup MongoDB:-
https://docs.mongodb.com/manual/installation/

#Run Mongodb Server in command Prompt:-
"C:\Program Files\MongoDB\Server\3.4\bin\mongod.exe"

#Setup Project:-
#Installation:
1. virtualenv folder-name
2. cd folder-name
#Install Django
1. Insatll django using command:-
pip install django==1.9

#Create Project
1. Create Project using command:-
python .\Scripts\django-admin.py createproject project-name
2. cd project-name

#Download Project
1. Clone the project using command:-
git clone https://github.com/shivam04/python_scrap_ndtv.git

#Requirements
1. Right there, you will find the requirements.txt file that has all the great debugging tools. To install them, simply type:
pip install -r requirements.txt

#Migrate Database:-
1. Migrate User Table and Profile Table 
User Table conatains username , email , password
Profile Table contain token for a particual user
python manage.py migrate

#Run Server
1. Finally Run Server using command:-
python manage.py runserver
