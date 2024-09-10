Explain how you implemented the checklist above step-by-step (not just following the tutorial).
First I created the django project by using various commands in the terminal, which did the following:
    activated and setting up the django environment
    creating the main django application
    modified the settings.py file so I'm able to host the application

Then I created a new repository in github for assignment 2
I performed routing in the project so that the application can run properly
    I pasted a code that defines URL routing for a Django application and maps a specific URL pattern to a view function.
    I configurd the code by adding the inlcude function so that it can import other URLs routes from the other apps

After that I edited the models.py file so that it will meeet the requirements of assignment 2 by adding the models 
    Name 
    Price
    Description

created a function in views.py that contains my name, class, and name of my shop that would return an html template

Then I connected the local files to my github repository by doing git commands in the terminal
    did  git remote add origin https://github.com/ZakiyDaulay/zakiyshop
    git  add .
    git push -u origin main



Performed Deployment to PWS
    edited the settings.py by adding the PWS url
    did git commands to deploy the website into the pws project

Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.
client browser --> urls.py-->views.py-->models.py-->html template-->client browser

the client sends an http request to the django app
the urls.py file routes the request to the view based on the url
the views.py file handles the request
models.py will interact with the database and returns it to the views

the html template will be passed from the view and its response will be sent back to the client


Explain the use of git in software development!
git is used by software developers to collaboarte code efficiently with a group, so that when changes are made it can be done smoothly. 

In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?
it is chosen simply because it's beginner friendly, compared to other languages.It also has built in tools for handling common tasks.

Why is the Django model called an ORM?
<<<<<<< HEAD
because it is the bridge between the database and python objects. software developers can use python classes in the django model instead of sql queries. 

=======
because it is the bridge between the database and python objects. software developers can use python classes in the django model instead of sql queries. 
>>>>>>> 3acff32dd6e0846313ba918f2b255085b551ecce
