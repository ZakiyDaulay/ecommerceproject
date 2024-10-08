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
 What is the difference between HttpResponseRedirect() and redirect()?
redirect() is a more flexible as it can take a URL,view name or object. HttpResponseRedirect() can only take a URL.

 Explain how the MoodEntry model is linked with User!
the MoodEntry model and User model is linked by using a foreign key. it gives the ability for each entry created to be associated with the logged-in user. 
 What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.

 Authentication refers to the process of verifying the identity of the user and Authorization is the process of determining what a user can do after they're authenticated. Django uses `django.contrib.auth` for authentication by creting a session for the user and setting a session ID as a cookie in the browser. Django has a permission system to handle authorization, which assigns a user to have specififc permissions to perform actions. Django has other decorators such as @login_required and @permission_required for security.

 How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.

 Django uses cookies and sessions to remember logged-in users. Other uses of cookies aside from managing sessions are user preferences, authentication tokens, remember me functions, tracking, etc. By default, not all cookes are safe. While cookies are generally safe, it is not perfect as they fall into the wrong hands attacks can access browsing session and steal sensitive data.

 Explain how did you implement the checklist step-by-step
 1. Created a register function that will automatically generate a registration form that will create a user account
 2. Create the `register.html` file for the layout of the webpage of the register function
 3. Add a URL path for the register function in urls.py
 4. Created a login function that will authenticate the user to login
 5. Create the `login.html` file for the layout of the webpage of the login function
 6. Add a URL path for the login function in `urls.py`
 7. Created a logout function that will have a log out button so the user can log out of their account in `views.py`
 8. In `main.html`, add a button labelled "Logout" for the logout functin
 9. Add a URL path for the logout function in `urls.py`
 10. Add and import a login_required code on top of the show_main function in `views.py`, which will require the user to log in to their account to access the application.
 11. Add imports `HttpResponseRedirect`, `reverse`, and `datetime` at the very top.
 12. Add a `last_login` in the `login_user` function to track when the user last logged in.
 13. Modified the `show_main` function to have a `last_login` variable.
 15. Link the Products and User model with a foreignkey, making each product entry associated with the logged in user.
 16. run the model migration with `python manage.py makemigrations` in terminal
 17. select a value for the user field 
 18. finish the migration by running `python manage.py migrate`
 19. imported os and changed the `DEBUG` variable in `settings.py`

## ASSIGNMENT 5 README

if there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!

CSS will use "specificity", which is a system that can determine which style rule has priority. the prioritiy is as follows:inline styles, ID selectors, classes, element selectors, and universal selector



 Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!
it's become an important concept because it gives web applications the ability to adapt to different device platforms (phones,laptops,tv,etc.). The most popular applications that have responsive design, one of them being Youtube. Because of the growing popularity of youtube, developers have to adapt youtube to different devices such as TVs and phones, and they use responsive design to make it possible. An example of applicatinos that don't use responsive design are usually older websites that haven't been updated. A good example would be the SIAKNG website by UI. when you open the website on your phone, the layout doesn't adapt properly, as the full layout doesn't cover the entire screen.


Explain the differences between margin, border, and padding, and how to implement these three things!
Padding is the space between the border and the content of the element. it is implemented by specifying the padding of the sides. Border is the line that separates padding from the margine by surrounding the element. implementation is done by defining the border of the sides. Margin is the space outside the border. it's the space between the elements and the surrounding elements. it is impemented by defining the sides.

 Explain the concepts of flex box and grid layout along with their uses!
 flex box and grid layouts are css layout models, used to assist developers to create responsive layouts. flexbox is one-dimensional layout model that allows the developer to align and distribute items within a container. grid layouts allow for a more complex approach, as it divides the page into rows and columns.

 Explain how you implemented the checklist above step-by-step (not just following the tutorial)
 1. added tailwind into my application.
 2. created the edit_product function in `views.py`.
 3. created the html file for the edit_product function.
 4. added a url path for the function in `urls.py`
 5. created a delete_product function in `views.py`.
 6. created the html file for the delete_product function.
 7. added a url path for the function in `urls.py`.
 8. modified the html files for both so that there's a button for editing and deleting
 9. created a navigation bar to the application by creating `navbar.html`.
 10. added the burger button for the phone, so when it expands it will show the logout button.
 11. linked the navbar to main,create product entry, and edit mood html files by using tags. 
 12. added whitenoise middleware to automatically manage static files.
 13. created `global.css` to define the general look for the features.
 14. modified the html files of edit and delete product to look nice
 15. edited the other features of the website to look nice such as the way the products look after being added, and the login page.
 16. created `card_info.html` to display name, class, and npm. 

## ASSIGNMENT 6 README

 Explain the benefits of using JavaScript in developing web applications!

 There are many benefits of using Javascript in web development. using Javascript can be faster to use as it runs directly in the user's browser. this means that various forms of interaction in the program will happen instantly as it doesn't require any server communication. AJAX is also very useful and beneficial as it enables asynchronous data fetching, which can request ddata from a server without reloading the page. 


 Explain why we need to use await when we call fetch()! What would happen if we don't use await?


calling fetch() is an asynchornous function that essentially returns a 'promise', which represents a forthcoming result. Sometimes, calling a fetch() can be unsuccessful, as fetch() can run and still be in progress of requesting, while the code is running in the background which can cause problems. using await will pause the execution of the code until the promise is returned by fetch(), ensuring that we get the correct response. 


 Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?



like the title of the decorator, it's used to exempt a view from the csrf protection. Django has CSRF protection on all of its POST requests (including AJAX POST requests) by default for security purpose. if the CSRF protections are applied on the AJAX requests, the tokens might not be correctly handled which can lead to errors. 

 On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?


If the user input sanitization is done in the front-end, it can lead to serious security issues.  if it were in the front-end, the code can be easily modified by the users, most commonly done by inspecting the website. they could change the code and logic of the sanitization, which can lead to malicious data sent to your server.


Explain how you implemented the checklist above step-by-step
1. modified the `login_user` function so that an error message will display of the username or password is invalid.
2. created a new function in `views.py` called  add `add_product_entry_by_ajax` that has a CSRF_EXEMPT decorator so that it won't check the CSRF_token in the post request. 
3. routed the new function in `urls.py`.
4. modified `views.py` and `main.html` so that the product entry objects are fetched from the /json endpoint. 
5. added a new div element that will become the container for the product entries.. 
6. created a new function called `refreshProductEntries` in `main.html` that will refresh the products data asynchronously
7. implemented the modal in `main.html` 
8. added a javascript function called `addProductEntry` that can add data bsed on the input in an AJAX
9. added `strip_tags` in `forms.py` and `views.py`, a function that will remove all HTML that are in the data sent by the user. This is done as a security measure against XSS.
10. used DOMPurify to clean up data on the frontend side, by implementing it in the `refreshProductEntris` function, and in the `main.html` file.