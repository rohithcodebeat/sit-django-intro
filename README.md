# sit-django-intro

Django Project Creation 



Create virtualenv 
python -m virtualenv venv 

Activate virtualenv 
./venv/scripts/activate.bat 

mkdir project && cd project 

django installation 
pip install django

To create new project
django-admin startproject core .

To run the project
python manage.py runserver


# June 6th Class Notes
https://file.notion.so/f/s/5fef10c7-1e97-49f3-b5c8-6e7884fbee2d/Untitled.png?id=eb2ce2af-a79d-43e2-8924-259c09b0d0dc&table=block&spaceId=d19f43be-2d24-4d2d-9a57-f8350fdf4421&expirationTimestamp=1686121599331&signature=vVRQi2faOEPtTTgwqOVoEV_FTeVWEA6WcrnOVC7ey6o&downloadName=Untitled.png


![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5fef10c7-1e97-49f3-b5c8-6e7884fbee2d/Untitled.png)

# Relations

- One-to-One → fb → relation b/w user model and user profile model
- One-to-many (ForeignKey) → fb → user & user posts → many posts
    
    → One user have relation with more than one instance of UserPostsModel 
    
    → One Instance can be assigned to more than one other instance 
    
- many-to-many

![Screenshot 2023-06-06 at 3.27.35 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df44896b-5e4d-453b-909f-fe935f310e3a/Screenshot_2023-06-06_at_3.27.35_PM.png)

![Screenshot 2023-06-06 at 3.27.42 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a04810d-2fcc-43d3-a9d2-a074e456fc24/Screenshot_2023-06-06_at_3.27.42_PM.png)

![Screenshot 2023-06-07 at 11.38.45 AM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c083ef2b-8d37-4f7a-bf79-b2578ff9fe7d/Screenshot_2023-06-07_at_11.38.45_AM.png)