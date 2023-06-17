# Search_Api_Django
By implementing a search API in Django,Users with a powerful and flexible search functionality that allows them to find the information they need efficiently using with Mongodb.


## Installing
Step by step commands on how to run this project on your computer.

1)- Install Virtualenv
```
pip install virtualenv
```
2)- Create Virtualenv
```
virtualenv venv
```
3)- Activate virtual env
```
source env/bin/activate
```
4)- Install requirements
```
pip install -r requirements.txt
```
Note: Above lines are required for first time installation.

### Use Mongodb as a backend database for django project

5.1)- Install djongo:
```
pip install djongo
```
5.2)- Into settings.py file of your project, add:
```
DATABASES = {
     'default': {
         'ENGINE': 'djongo',
         'NAME': 'your-db-name',
     }
 }
 ```

6)- Execute below commands
```
python manage.py makemigrations
python manage.py migrate
```
Note: Above commands should be executed if there is any db level changes

7)- Create superuser for admin access and follow instruction, if not created one
```
python manage.py createsuperuser
```
## Running the server
```
python manage.py runserver
```
And the project is ready for use on your computer!.

## ScreenShot of the project
# api Page:
<img width="1440" alt="Screenshot 2023-06-14 at 8 01 29 PM" src="https://github.com/Ajyrajput-2811/Search_Api_Django/assets/119350384/e9445f6e-e63d-4b0f-9759-67f1e3472f06">

# Postman:
<img width="1440" alt="Screenshot 2023-06-14 at 8 01 52 PM" src="https://github.com/Ajyrajput-2811/Search_Api_Django/assets/119350384/50c73580-6032-4232-85ad-debc018a4651">
<img width="1440" alt="Screenshot 2023-06-14 at 8 02 14 PM" src="https://github.com/Ajyrajput-2811/Search_Api_Django/assets/119350384/df548f60-92c2-4cad-bd36-f610e0ac9a3d">

# MongoDB:
<img width="1440" alt="Screenshot 2023-06-17 at 2 20 53 PM" src="https://github.com/Ajyrajput-2811/Search_Api_Django/assets/119350384/e40d6a15-10d2-460b-86bb-54d5fd070483">

# Django Admin:
<img width="1440" alt="Screenshot 2023-06-17 at 2 30 59 PM" src="https://github.com/Ajyrajput-2811/Search_Api_Django/assets/119350384/ac16c93a-6622-43e2-a99e-56961bd2ae59">


