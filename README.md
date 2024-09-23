PWS APPLICATION:http://zakiy-makarim-ecommerceprojectassignment2.pbp.cs.ui.ac.id/


## ASSIGNNMENT 2 README
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
did git remote add origin https://github.com/ZakiyDaulay/zakiyshop
git add .
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
because it is the bridge between the database and python objects. software developers can use python classes in the django model instead of sql queries.

## ASSIGNMENT 3 README

Step-by-Step Explanation:


Explain why we need data delivery in implementing a platform.

1.created a new html file called 'base' in the templates folder that will be the base template for the web page

2.added an id model and modified the other models in the models file

3.did model migrations to make sure that all the changes made are migrated

4.edited forms.py  so to make sure that the new models created will be used as the form. it will be able to save new data added as a product entry

5.created a new function in views.py that makes the ability to create a new entry with the input by the user 

6.created a new html file create_product_entry.html to make the actions that setups the webpage to allow the user to add a product entry by submitting a form to the server

7.modified main.html so that the data can be displayed in the webpage and the add product entry button will redirect the user to the form page

8.imported HttpResponse and serilizers to views.py for xml files. created a function "show_xml"  that will contiain serialised data result as an xml. created a function "show_xml_by_id" that does the same function as show_xml but can return a particular product. 

9. added a URl path for the xml functions which wil be able to return a response of the xml data.

10.Created function "show_json" and "show_json_by_id" which has the same purpose as the xml functions but json uses less complex data structures which makes it faster to transmit.

11. added a url path for the json functions which will be able to return a repsonse of the json data

screen shots of Postman
JSON: https://imgur.com/a/kCmsiGV
JSON with ID: https://imgur.com/a/8yEVsFn
XML : https://imgur.com/a/DsbfUBP
XML with ID : https://imgur.com/a/BmdP1f6


In your opinion, which is better, XML or JSON? 
 Based on viewing the data in postman  , I prefer JSON since its easier to read the data and it's less verbose

 
Why is JSON more popular than XML?
As mentioned before, the main reason JSON is considered to be more popular because of how easy it is to read for humans and its lightweight compared to XML.



Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.

is_valid() important to check if the data submitted by the user is valid based on the fields. We need it because it ensures that valid data will be processed and to minimize errors that can be caused by the user.  


Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?

the csrf_token is needed when creating a form because it protects the webpage from CSRF attacks. it protects the page by creating a randomly generated token from every session and user.

CSRF attacks can happen if we don't user the csrf token. the attacker could have access to the data of the user and steal it for malicious intent. 

the attackers could take advantage of the lack of protection by manipulating the users into submitting request that could give them sensitive data


## ASSIGNMENT 4 README

Answer the following questions in README.md in the root folder. (Modify your README.md that you have already created; add a subtitle for each assignment).

 What is the difference between HttpResponseRedirect() and redirect()?

 Explain how the MoodEntry model is linked with User!

 What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.

 How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.

 Explain how did you implement the checklist step-by-step (apart from following the tutorial).