# Volo Requirements System

Volo Requirements System is a full stack application that meets the requirement of a user creating projects and requirements for the corresponding projects.\
This project was created to meet the criteria of the Code Institute Milestone Project 3.

![AmIResponsive Screenshot](assets/images/amiresponsive.png)

View Repository in GitHub Pages:\
https://github.com/mparker-landt/Milestone_Project_3

View Website Link:\
https://volo-requirements-system-6e36ea052d2c.herokuapp.com/

Author: Marcus Parker\
Github: [mparker-landt](https://github.com/mparker-landt)

## Table of Contents
+ [UX](#ux "UX")
  + [User Demographic](#user-demographic "User Demographic")
  + [User Stories](#user-stories "User Stories")
    + [First time User Stories](#first-time-user-stories "First time User Stories")
    + [Returning User Stories](#returning-user-stories "Returning User Stories")
  + [Design](#design "Design")
    + [Wireframes](#wireframes "Wireframes")
    + [ERD Diagram](#erd-diagram "ERD Diagram")
    + [Colour Scheme](#colour-scheme "Colour Scheme")
    + [Typography](#typography "Typography")
    + [Images](#images "Images")
+ [Features](#features "Features")
  + [Functional Features](#functional-features "Functional Features")
  + [Design Features](#design-features "Design Features")
  + [Future Features](#future-features "Future Features")
+ [Resources](#resources "Resources")
  + [Technologies](#technologies "Technologies")
  + [External Resources](#external-resources "External Resources")
+ [Testing](#testing "Testing")
  + [Performance Testing](#performance-testing "Performance Testing")
  + [HTML Validator Testing](#html-validator-testing "HTML Validator Testing")
  + [CSS Validator Testing](#css-validator-testing "CSS Validator Testing")
  + [JS Testing](#js-testing "JS Testing")
+ [Known Bugs](#known-bugs "Known Bugs")
+ [Development & Deployment](#development--deployment "Development & Deployment")
  + [Development](#development "Development")
  + [Deployment](#deployment "Deployment")
+ [Credits and Acknowledgements](#credits-and-acknowledgements "Credits and Acknowledgements")

## UX
### User Demographic
This web app is targeted towards a small business who want to add projects in development and add requirements related to the projects.

### User Stories
#### First time Visitor Goals:
- As a first-time visitor I want to be able to see Projects and Project details.
- As a first-time visitor I want to learn how to add/edit and delete Projects and Requirements.
- As a first-time visitor I want to be able to sign up for an account to use the website.

#### Returning Visitor Goals:
- As a returning user I want to login to my account with a username and password.
- As a returning user I want to be able to explore the Projects and related requirements.
- As a returning user I want to be able to add/edit and delete Projects and their related requirements.


### Design
#### Wireframes
Wireframes were created with draw.io. The design was heavily influenced by a StartBootstrap demo that provided a professional feeling website whilst allowing for flexible customisation.\
- Home Page
![Wireframe Home Page](assets/images/milestone3-home.png)
- Project Card Modal
![Wireframe Home Page](assets/images/milestone3-projectcard.png)
- Requirements Page
![Wireframe Home Page](assets/images/milestone3-reqs.png)
- Test Report Page
![Wireframe Home Page](assets/images/milestone3-tests.png)
- Sign In Page
![Wireframe Home Page](assets/images/milestone3-signin.png)
- Register Page
![Wireframe Home Page](assets/images/milestone3-register.png)

#### ERD Diagrams
ERD Diagrams were drawn roughly with hand at the beginning of the project. After the database and tables were created in psql for the project the ERD diagrams was auto generated using the program pgAdmin4. This program allows for the visualistion and editing of the SQL database.\
![ERD Diagram](assets/images/milestone3-erd.png)

#### Colour Scheme
For the colour scheme a blue and white scheme were used. This was part of the Start Bootstrap demo but suited the professional aspect of the webpage whilst keeping a nice to look visual aspect.
- <span style="color:#4E73DF">#4E73DF</span> - Used for the menu, buttons and borders for content
- <span style="color:#FFFFFF">#FFFFFF</span> - Used for the header, footer and certain font colours
- <span style="color:#F8F9FC">#F8F9FC</span> - Used for main body of the pages, as it is off white the white of content on the page were made more visually appealing and attracted attention immedietaly.

#### Typography
The font used for the webpage was [Nunito](https://fonts.google.com/specimen/Nunito), a Sans Serif typeface.


#### Images
Due to the professional setting for the application no images were used in the project. Icons for the website were aquired from Font Awesome.

## Features
### Functional Features
The application offers the features:
- Register and Log in as a User
- Create, edit and view Projects
- View a projects requirements 
- Create, edit and delete Requirements that can be linked to a Project.

### Design Features
The website was designed to be a simple yet functional multipage site that could be used in a professional work setting.\
The base template for the user interface was aquired from StartBootstrap. The demo used was [SB Admin 2](https://startbootstrap.com/theme/sb-admin-2) which was adapted upon to meet the demands for the project.\
Designed to be desktop first and to provide information in a intuitive and clean manner.
- Page\
![Page Feature](assets/images/feature-page.png)
- Header\
![Header Feature](assets/images/feature-header.png)
- Footer\
![Footer Feature](assets/images/feature-footer.png)
- Menu\
![Menu Feature](assets/images/feature-settings.png)
- Projects Page\
![Projects Page](assets/images/feature-projects.png)
![Projects New](assets/images/feature-project-addx.png)
- Project Card Modal\
![Project Card Modal Feature](assets/images/feature-projectcard.png)
![Project Card Modal Feature](assets/images/feature-project-cardx.png)
- Requirements Page\
![Requirements Page](assets/images/feature-requirements.png)
![Requirements Page](assets/images/feature-reqsx.png)
- Sign In Page\
![Sign In Page](assets/images/feature-login.png)
- Register Page\
![Register Page](assets/images/feature-register.png)
- Error Pages\
![Error 404 Page](assets/images/feature-errors.png)


### Future Features
The website was designed to have many features added in the future:
- Requirements Freeze Archive - To meet the demand of changing requirements and mitigating scope creep a freeze function could be added that could capture the Project and its requirements on a certain date. These could then not be changed but would also be available to view and compare. 
- Testing Pages - Project and Requirements could be linked to Test Reports to prove that the Requirements had been met. Data for the reports could include dates, authors and links to documents.
- Admin Levels - As well as normal users different admin levels could be created where super admins could add others and allow partial functionality for others.
- Profile Page Information - Users and admins could get a profile page that displays the ownership of Projects and Requirements changed by said user.
- Much more Project, Requirement and Test Report Information 
- At risk colour identification - If date deadline inserted notifications could be enable on the UI to flag risks and attract attentions by users.


## Resources
### Technologies
- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JS](https://en.wikipedia.org/wiki/JavaScript)
- [Jquery](https://jquery.com)
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [SQL](https://en.wikipedia.org/wiki/SQL)
- [Postgresql](https://www.postgresql.org/)
- [SQLAlchemy](https://www.psycopg.org/)
### External Resources
- [Start Bootstrap](https://startbootstrap.com/) - Used as a template to adapt the design of the UI from.
- [Datatables](https://datatables.net/) - JavaScript library used for a better functional and visually appealing table.
- [Font Awesome](https://fontawesome.com/) - Used to acquire icons for the project.
- [Draw.io](https://www.drawio.com/) - Used to create the wireframes for the project.
- [pgAdmin4](https://www.pgadmin.org/) - Used to create the ERD for the project. This tool was also used to aid in visually inspecting the SQL database for the project and the contained tables and columns
- [Miguelgrinberg Blog](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) - A blog online that provided in great detail information and a walkthrough on how to build a Flask project in VS Code. This provided a tutorial on different topics such as templates, Web Forms, User Management, Date/Time implementation and Ajax.  

## Testing
Continuous testing of the application was performed throughout its development period. The testing was performed primarily on Mobile Firefox although Google Chrome was also used.\
For the HTML and CSS testing was done with Google Chrome and Firefox Development Tools.\
For functionality testing of the JavaScript and Python/Flask backend a test group was used to provide feedback and find bugs.
Full CRUD was tested by adding, editing and deleting Project and Requirements. User access was also tested by logging out as a user and trying to do the same.
Different user profiles were created to test the register and log in and log out functionality.

### Performance Testing
The website performance was tested using Google Chrome Developer Tools Lighthouse feature.
For the webpage the Performance, Best Practices and SEO were 97, 96 and 90 respectively.
The Accessibility score was 76 which although not bad could be improved throughout the website.
![Lighthouse Performance Screenshot](assets/images/lighthouse.png)


### CSS Validator Testing
https://jigsaw.w3.org/css-validator
There were no warning or errors in the CSS code file.
![CSS Lint Screenshot](assets/images/lint-css.png)
### JS Testing
https://jshint.com
Due to the JavaScript file being extremely simple there were no errors in jshint. The warnings visable were due to jquery being used and could be ignored.
![JS Lint Screenshot](assets/images/lint-js.png)
### Python Testing
Python PEP8 standards were tested by installing the extension Pylint. This allowed for the easy visualisation of errors and warnings when working on the code.
Although not all warnings were got rid of the ones left were suggestions or Pylint not working fully as expected. 
![Python Lint Screenshot](assets/images/lint-python.png)

## Development & Deployment
### Development
This project was developed in an environment with the tools:
- VS Code - IDE to develop and view the code/
- Sourcetree - User application to connect to Github.
- Github & Git - Version and Source Control to save the code and see the history.
- Firefox Web Browser - User to view the frontend application and debug the frontend code.

To replicate the development environment:
- Open VS Code and start a new project.
- Create a virtual environment by running the command "python3 -m venv venv".
- Activate the vitual environment with the command "source venv/bin/activate".
- Install Flask "pip install flask".
- Install Flask modules that will be wanted with "pip install FLASK-NAME". This can also be done throughout the project when a module is needed.
- Make a folder called app and inside folders called templates and static.
 This is where the main program and content will be found in the project.
 - Create a python file with an appropiate name such as run.py.
 Run the command set FLASK_APP=NAME.py to create an environmental variable.
 - Test out the functionality and instructions by running "flask run" and navigating to the provided url.

The project is deployed on Github:

To acquire the code:
- Log into Github
- Navigate to the project link
- On the project page click the Code button
- Download the zip of the code
- Open the project in an environment of your choice

Forking the repository
- Log into Github
- Navigate to the project link
- On the project page click the Fork button
- Clone or download the zip of the code
- Open the project in an environment of your choice

Cloning the repository
- Log into Github
- Navigate to the project link
- On the project page click the Code button
- Copy the HTTPS or SSH link as preferred
- Clone the project using the link with the tool of your choice (Git Terminal, Github Desktop, Sourcetree etc)

### Deployment
The website was deployed live using Heroku to host the backend and frontend into a working package.

To replicate:
- Sign up to Heroku and set up a Two Step Verification method.
- Create an app in Heroku.
- Set up the config vars in Heroku settings, this includes the IP, Port and link and password to a database.
- In Deploy in Heroku link the app to a profile and repository in Github.
- In Heroku in settings in Buildpack choose the Python language.  
- In the project files run "pip freeze > requirements.txt" to create a file for Heroku to know what to install. 
- In the project files create a file called Procfile and the command "web: python NAME.py". This will link to a dyno in Heroku that will run the app.
- Push the project in git, this will be pushed to Heroku simultaenously and will build in Heroku.
- Click open app to go to the live deployed website.

## Credits and Acknowledgements
With special thanks to:
- Lauren-Nicole Popich - Mentor from the Code Institute who provided help throughout the project and was always available for support.
- Sarah Price - A colleague who suggested the idea for the project and helped produce the first Wireframes and ERD in rough draft form.
- Blog - The blog [Miguelgrinberg Blog](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) about building a Flask Webpage was greatly used for learning for the project. Especially to set up the system of Flask and its Flask Modules in VS Code. 
