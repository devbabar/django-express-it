### Disclaimer: This is a dummy application and only intended to demonstrate coding and programming. 

# django-express-it
Express-it is a very simple but robust and scalable application. It allows the registered users to share images.

# Objective & features:
* Express-it homepage where users can view posted images, content, register, login and logout options.
* Users can only view the limited details of each image (title and author name). To view details of the post, create post, they must need to register and login.
* Register new user, login and logout sessions. The Django authentication system is being used handles both authentication and authorization.
* @Login_required decoraters is being used to only allow logged in users to view profile and create post.
* Django messaging framework to display custom messages. Each message will disappeared after 5 seconds using javascript.
* During registraion of new user, check if username exists in real-time through Ajax without reloading the page.
* Custom navbar to stay visible on scrolldown and back to the top button to get back to the top of the page.
* Responsive design for any screensize.
* Django form validation for registration and login.
* Django debug toolbar to optimize performance during development.

# Javascript & JQuery animations and Ajax calls.
* HTML 'marquee' tag is being used to scroll banner and other section headings.
* Flashing heading boxes.
* Slide in effects on scrolldown from left to right.
* Post section fade in slowly when scrolldown the page.
* Day and Night photography sections display related contents on clicking each section without reload page. Hover and scrolldown each section and on mouseleave, it will go back to it's origin.
* Fixed footer at the bottom of the page.

# Tools:
* Django==1.10
* django-debug-toolbar==1.9.1
* MySQL-python==1.2.5
* Pillow==4.3.0
* selenium==3.10.0
* Javascript
* jquery
* Bootstrap.
* HTML & CSS

# Steps to run:
### Step 1:
Create a folder.

$ mkdir express_it

Create a virtual enviroment.

$pip install virtualenv

$ cd express_it

$ virtualenv env

$ source env/bin/activate

### Step 2:
Install requirements.txt

$pip install -r requirements.txt

