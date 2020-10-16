## Data Centric Development Milestone Project (MS3) for Code Institute
<hr>
This project is a practical illustration of the material learned in modules 8 (Python Fundamentals), 9 (Practical Python) and 10 (Data Centric Development) of the Code Institute Ful Stack Developer course.

## Index
* [Project purpose](#purpose-and-functionality)
* [Functionality](#functionality)
* [Demo](#demo)
* [UX](#ux)
    * [User Stories](#user-stories)
    * [Design](#design)
        * [1. Font](#1-font)
        * [2. Color Scheme](#2-color-scheme)
        * [3. Logo](#3-logo)
        * [4. Skeleton](#4-skeleton)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to Implement](#features-to-implement)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
    * [Manual testing of all elements on all pages](#manual-testing-of-all-elements-on-all-pages)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Acknowledgements](#acknowledgements)

***

## Watcha Selling

The idea for this website emerged when I one day, my sister and I were returning home from the gym driving her car, and passed by a garage sale, almost too quickly. I called it out and asked her if she wanted stop by (knowing how much she loved garage sales). She said that she had no idea about the sale and that if I had not told her she would have missed it. That's when the idea came to mind to reolve this issue: a Yard Sale locator and finder.

### Project purpose
The website purpose is to connect buyers and sellers of yard sale items and to serve as a repository of and publishing tool for yard sales.
The website's goal is to easily search, find and manage (add, edit or delete) of one or several yard sales. The website must be easy to use while as it is highly interactive. It must also display relevant information about what the site is and does. Simplicity is key on this website. 


### Functionality


### Demo
A live demo can be found [HERE](https://watcha-selling.herokuapp.com/)

GitHub repository link can be found [HERE](https://github.com/EliBec/my--first-data-centric-development-milestone-project)

### UX

### User Story
The website consists of a few pages. The Home page displays the published yard sales for the present date eliminating the need to search for them. Also in the Home page, the search criteria is displayed right below the banner image so there is little need to scroll down or to navigate to other pages in order to find the yard sales. 
The header (which contains the links to the pages), is convenienty fixed and available to the user as he/she scrolls down or up.


**User Type (Scope)**
There are two types of users this website is scoped for: Buyer and Sellers
- Anybody interested on finding a yard sale and anybody who wishes to broadcast/publish his/her yard sale. 
- Live anywhere in the world but geared more towards residents of the United States of America
- All levels of disposible income
- English speaking

**As a user:**
- If I am a buyer, I expect to easily search and find the yard sales, using the different search filters available. Also, I expect to easily find information about what the website is and how to contact them. 
- If I am a seller, I expect to easily add/publish, update and delete a yard sale. This process must be done intuitively and the proper pages must be easy to find and readily avialable. Also, I expect to easily find information about what the website is and how to contact them.

**Developer:**
* As a Developer, I want to expand my knowledge with Python and Flask by creating an extensive management database application.
* As a Developer, I want to create a fully-responsive mobile-friendly multi-language faceted project to showcase what I have learned whilst on this course.
* As a Developer, I want a project which can evolve as I grow as a developer.
* As a Developer, I want to be able to use the app for myself in my Olympic Weightlifting sessions.

### Strategy
The website's strategy is centered in two words: simplicty and usefulness.  The goal is to easily and concisely show the users how to locate and manage a yard sale. The user should see and understand at first glance the purpose of the site and feel compelled to use the website's functionality. The website includes a map of the yard sale location which supplies a nice and simple illustration. The yard sale's information must be complete and sufficient for the buyer to make the decision to attend the yard sale event. 


### Structure used to help them users achieve these things:
- The website is mostly linear, with easy-to-read fonts and intuitive options to follow. 
- The website contains a separate page for each section, as opposed to a single long page. This will help he user do the task easily by placin the focus on the page's single task. 
- The header navigation bar is clipped to the top and remains that way as the user scrolls down or up, thus providing convenient way to access the pages. 
- Footer provides quick links, which act as a shortcut to, for example, planning their visit and events. Footer also includes social media icons


### Design
The website is fully responsive. To achieve this, I used [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/download/) as well as [Materialize 0.100.2](http://archives.materializecss.com/0.100.2/)

### Font
The font-family is 'Concert One', with cursive style; used for the top header (menu), headlines and subtitles. This font was imported from [Google Fonts](https://fonts.google.com/specimen/Concert+One?query=concert+). The font style is conveys a casual motive, as yard sales tend to be. It is a friendly, easy-to-read font. The default font is Helvetica

### Logo
Very simple image, which conveys the messsage: a sale. 
The logo is actually an icon from [Materialize](http://archives.materializecss.com/0.100.2/icons.html). Now, for purpose of this project I decided to use it as a logo, but in real-case, I would adjust the image to make it unique. 


### Color Scheme
All colors were chosen using the [Adobe Color Wheel](https://color.adobe.com/create/color-wheel). I only chose two main colors, the teal to bring brightness and the purple to bring a little more darkness. A white background to give a clean look. 

Nav color:
- ![#6200ea](https://placehold.it/15/6200ea/000000?text=+) #6200ea.

Some font color:
- ![#0000E1](https://placehold.it/15/0000E1/000000?text=+) `Blue`

Other colors:
  ![#008000](https://placehold.it/15/008000/000000?text=+) `Green`

Font color: ![#fafafa](https://placehold.it/15/fafafa/000000?text=+) `#fafafa`


### Skeleton

Each wireframe file displays desktop, tablet and mobile phone view. 

[Landing Page wireframe](https://github.com/EliBec/my--first-data-centric-development-milestone-project/blob/master/static/wireframes/Home%20Page.png)

[Add your Yard Sale wireframe](https://github.com/EliBec/my--first-data-centric-development-milestone-project/blob/master/static/wireframes/Add%20your%20Yard%20Sale.png)

[Update your Yard Sale wireframe](https://github.com/EliBec/my--first-data-centric-development-milestone-project/blob/master/static/wireframes/Update%20your%20Yard%20Sale.png)

[Update_Delete your Yard Sale main page wireframe](https://github.com/EliBec/my--first-data-centric-development-milestone-project/blob/master/static/wireframes/Update_Delete%20your%20Yard%20Sale%20main%20page.png)

[About Us wireframe](https://github.com/EliBec/my--first-data-centric-development-milestone-project/blob/master/static/wireframes/About%20Us.png)

[Contact Us wireframe](https://github.com/EliBec/my--first-data-centric-development-milestone-project/blob/master/static/wireframes/Contact%20Us.png)

## Features
<hr>

Each page features a responsive navigation bar with conventional placing of logo (top left). Each page has a footer with copyright information, social media icons (currently, there is no real link social media pages for there is no existing social media accounts) and quick links to other pages within the website.
Every page displays a picture banner (same banner image for all pages).

#### Home page
Simple information in a few words on the banner: Yard Sales Locator and List Yours. Search criteria filters are available so user can start searching right away.  The user can choose one or more search filter. Search results will correspond to the search criterai input from the user. 
Also, yard sales for the current date are conveniently displayed on the bottom area so user does not have to search it. 

### Add Your Yard Sale
Page displays a form with the required information regardig the seller and the yard sale. There is a Save and a Clear button. The Save button will insert a new record on the database collection and the Clear button will clear all the fields on the form. 

### Update/Delete Your Yard Sale main page
This page offers the user a search filter so that the yard sale can be displayed to then be either updated or deleted. 
the search section includes a Search and a Clear button. 
Once the search results displays the fetched yard sales, the user can choose to click either the Update button or the Delete button. The Update button will take the user to the Update your Yard Sales page and the Delete button will perform the removal of the yard sale from the current page, not without first asking the user for confirmation.

### Update Your Yard Sale
Page displays a form displaying all the current data for the selected yard sale. All the fields are enabled so that the user can change it as desired. There is a Save and a Clear button. The Save button will update the current record on the database collection and the Clear button will clear all the fields on the form. 

#### About us 
Brief information of the business origins and how they came up with the idea. Also there is an image i the broadcasting of Yard Sales.

#### Contact us
This page offers a simple contact form (fully functional with Email JS API) for questions and concerns. The user will receive a "Thank you" message once the form is submitted. 

### Existing Features:
- Header logo and header website title: displayed on each page and positioned on the top lef-hand side. When clicked on, it will take the user to the home page.
- Header Navigation Bar: is present on each page. It is fixed to the top of the screen and available to the user as the screen is scrolled down or up. The nav's purpose is to conveniently navigate to the different pages. 
- Footer's Copyright Info: is present on every page. This is informational and with the purpose of protecting the author's rights.
- Footer's Social Icons: is present on every page. It offers the user an easy way to access social media pages. 
About Page: it allows the user to obtain information about what the business is all about and what it offers in a concise way, with no need of too much scrolling.
Contact Form: it allows the user to reach out to the business with questions or comments. Also, it allows the user to find information on how to get to the site address and see an illustrative map


## Features to implement:
Some of the features listed below could have been implemented, but time constraints did not make it possible for the moment
- Add en End Time to the Yard Sale Information
- Geolocation so that yard sales are dispalyed based on the user's location and not based on the date
- Add CAPTCHA to contact form - Allows business to protect the contact form from spam
- Share button for each Yard Sale
- Log in and Register for user accounts


## Technologies Used

Frontend was built using: HTML5, CSS3, and [Materialize 0.100.2](http://archives.materializecss.com/0.100.2/)and [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/download/) frameworks

[Google Fonts](https://fonts.google.com/): for website fonts

[Font-Awesome-5](https://fontawesome.com/) and [FontAwesome's](https://www.bootstrapcdn.com/fontawesome/) Bootstrap CDN: for icons

[Gitpod](https://www.gitpod.io/): for IDE used on this project (MS2)

[Python](https://www.python.org/): backend programming language

[Flask](https://flask.palletsprojects.com/en/1.1.x/): web microframework written in Python

[Jinja](https://jinja.palletsprojects.com/en/2.11.x/): template engine for the Python programming language used for templates with Python for the website
 
 [jQuery](https://jquery.com/): used for the accordion functionality on Events page

[Google API](https://cloud.google.com/maps-platform/): for Google Map in Contact us page 

[EmailJS API](https://www.emailjs.com/): for email functionality in Events page and Contact us page

[Heroku](https://www.heroku.com/): A cloud platform as a service enabling deployment for this CRUD application.


#### Tools Used:

[MongoDB Atlas](https://www.mongodb.com/) -  document-based, distributed database built for modern application developers and for the cloud era. Used for database hosting. 

[Adobe Color Wheel](https://color.adobe.com/create/color-wheel)
for color picking. 

Google Chrome Dev Tools - for testing of the application's responsiveness, on-th-fly testing css editing tool and for console monitoring for Javascript and JQuery 

[Balsamiq](https://balsamiq.com/) for the creation of wireframes

[Favicon Generator](https://favicon.io/) for the creation of a fav icon. It is not exactly the same as the logo (due to time contraints) but close enough to convey the brand.

[Free Formatter](https://www.freeformatter.com/html-validator.html) for HTML code checking

[CSS Validation Service](https://jigsaw.w3.org/css-validator/) for CSS code checking

[JSHint](https://jshint.com/) for Javascript code checking

[PEP 8 Online](http://pep8online.com) for Python code checking


## Testing

Test has been performed throughtout the different stages of the website build. Responsiveness of the website has been tested using both physical devices (including smart cellphones, tablets and desktop) as well as browser tools such as Google Chrome Dev Tool.
The website has been tested on a variety of internet browsers, such as: Google Chrome, Internet Explorer, Micresift Edge, Firefox and Opera to ensure compability. 

The following tools were used to ensure code quality:

For HTML: [Free Formatter](https://www.freeformatter.com/html-validator.html)

For CSS: [CSS Validation Service](https://jigsaw.w3.org/css-validator/)

For Javascript: [JSLint](https://jshint.com/) version 2.11.1

For Python: [PEP 8 Online](http://pep8online.com) for Python code checking


#### User Experience testing: 

The user will mainly come to this website to find information on the yard sales available, information about them and to publish and manage (add, update or delete) her/his own yard sale. 

The user would also want to reach us via email with questions, comments or requests. 

As a user I want to be able to be able to eaily search yard sales or add/update/delete my own. Also, I want to easily learn about what the website it about. I want to be able to navigate the site and not go through a lot of "clicks" to get the information I am looking for or perform the task.
 - The website satisfies this need by:
    1. Supplying a navigation bar containing descriptive titles links to the different pages. The nav bar is anchored to the top area of the screen and is available as the user scrolls down, saving the user's need to scroll back to the top of the page in order to use it. 
    2. The logo, located on the top left-hand side allows a direct access to the home page
    3. Quick links on the footer offer other helpful links to some of the pages
    4. Search criteria filters are visible and well located below the banner, so the user does not have to scroll too much. 
    5. The yard sale information is concise and includes a map to give the user a better idea of where it is

  As a curious user, I would like to know more about the organization, and how the idea emerged. 
   - The website satisfies this need by supplying the About us page, which shows how the idea of how the business came about.

 As a user, I would like to be able to reach out to the business for any questions, comments or requests I may have. I would like to be able to have the choice to communicate by phone, email or via a contact form.
  - the website satisfies this need by supplying the different ways to reach the business suah as the easy to access Contact us page, which includes a contact form to fill-out, telephone number and an email address. 


### Manual testing of all elements on all pages

#### Home Page:
 1. Testing of page responsiveness
    Change the screen size from desktop to tablet. Change the screen from desktop to mobile. Make sure images scale properly, the conventional nav manu switches to burger nav button
 2. Testing of the logo
    Click the logo to make sure you are directed to the Home page 
 3. Testing of nav bar links
    Click on each nav link to ensure you are taken to the pertaining page. Hovering over each link should result on the link's title text to change the background color. Once you are directed to the page
 4. Testing of screen scrolling and nav bar
    Scroll down to the page. The nav bar should be move with the scrolling remaining "fixed" to the top of the screen
 5. Testing of buttons: 
    For all buttons: all buttons must change opacity when user hovers over them
     * In Home page: when entering the information on the search filter, the Search and Clear buttons must go from dull gray to Blue and Yellow respectively. The Search button shall trigger the find and fetch the collection records based on the criteria search and display the search results below the search filters on the current page. The Clear button shall clear all the search filters as well as making the Clear and Save buttons dull gray again.  
     * In Add Yard Sale page: upon clicking on any field form the Add Yard Sale and Clear All buttons must go from dull gray to Blue and Yellow respectively. The Add Yard Sale button functionality consists of inserting a new record in the collection with the information entered by the user. The Clear button shall clear all the form's fields. 
     * In Update/Delete Yard Sale main page: when entering the information on the search filter, the Search and Clear buttons must go from dull gray to Blue and Yellow respectively. The Search button shall trigger the find and fetch the collection records based on the criteria search and display the search results below the search filters on the current page. The Clear button shall clear all the search filters as well as making the Clear and Save buttons dull gray again.
     * In Update Yard Sale page: The Save Changes button functionality consists of updating the current collection record with the information entered by the user. The Clear button shall clear all the form's fields. On this page, there is also a + and a - minus button. The + button should add a new line and the - button should remove a line on the Item List section
     * In Contact us page: the submit button must submit the form, and email should be received by the recipient and a Thank You message should appear back to the Contact us page 

 6. Testing of the forms 
    * Add Yard Sale Form: most the fields on the form are required. Test by leaving a few fields empty and proceed to search. This should result in the form NOT being submitted and the return of the message letting the user know that fields must be filled as they are required. 
    Test filling out all the fields and then submitting the form. The result should be the addition of your yard sale, a message informing the user of such ("Your Yard Sale has been added") and the display of the yard sale on the getyardsales.html page when if the yard sale meets the search criteria

    * Update Yard Sale Form:  most the fields on the form are required. Test by leaving a few fields empty and proceed to search. This should result in the form NOT being submitted and the return of the message letting the user know that fields must be filled as they are required. 
    Test filling out all the fields and then submitting the form. The result should be the update of your yard sale, a message informing the user of such ("Your Yard Sale has been updated") and the display of the yard sale on the getyardsales.html page when if the yard sale meets the search criteria.

 7. Testing of the search filters:
    * In Add Yard Sale page and Update/Delete Yard Sale main page have the same functionality: enter information on the search filters and proceed to search or clear. The seach filters are cleared by the default when the page is accessed.
    Leaving the search filters blank and proceeding to search will result in the display of all existing yard sales. 

 7. Testing of footer section
    * Social Media Icons: hover over each icon to ensure the font color turns a bit darker.  Note: social media pages have not being created, so don't expect results here except being directed to the same page you are currently on.
    
#### Contact page
Fillout the form except the required First Name field and click the submit buttom. You should expect an error message alerting you about the missing required field. Form submission should not be successful. Do this step with every required field. 
Once all the information is completed, click the Submit button; an email should be received by the company's email service

#### Note:
Social media pages have not been created yet, but icons there are available on the front end.
Purchase ticket functionality has not been implemented yet, so Purchase Ticket buttons will not take the user to a purchasing page 


## Deployment

### Remote Deployment

 Heroku was used to deploy this project, using the master branch on GitHub, following these steps:

1. Generate a requirements.txt file so Heroku can install the required dependencies to run the app. This is created like so:
sudo pip3 freeze --local > requirements.txt

2. Create a Procfile to tell Heroku what type of application is being deployed, and how to run it.This is done like so:
echo web: python run.py > Procfile

3. Sign up for a free Heroku account, create the project's app, and click the Deploy tab, at which point you can Connect GitHub as the Deployment Method, and select Enable Automatic Deployment.

4. In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables as follows:

* IP : 0.0.0.0
* PORT : 5000
* MONGO_URI : <link to your Mongo DB>
* MONGO_DBNAME : <Mongo DB name>

5. Once the above was done, the app was deployed via this link: "https://watcha-selling.herokuapp.com/". 

6. the repository of this project can be found on via this link:
https://github.com/EliBec/my--first-data-centric-development-milestone-project


### Clone Repo

To clone the repository:

1. Select the Repository from the Github Dashboard.

2. Click on the "Clone or download" dropdown button which is located beside the Gitpod button to the right.

3. Click on the "clipboard icon" to the right to copy the web URL.

4. Open your preferred Integrated Development Environment (IDE) and navigate to the terminal window.

5. Change the directory to where you want to clone the repository too.

6. Paste the Git URL copied from above and click "Ok". .

## Credits

<hr>

### Content

- The idea for this project came to mind when I faced the need for this tool in real life (see story in the [Watcha Selling](watcha-selling) section at the beginning of this document)

- The use of the CRUD functionality was learned from the CI course. 

-  How to set up enviroment variables and store mongo db username and passwords in env.py file and put into .gitignore was assisted by guidelines provided by a CI support tutor

- Google Maps dynamic functionality code was learned from Google API and from from another student's [project](https://github.com/maliahavlicek/what2do2day) 

- The + and - button functionality code snipet was partially learned and taken from another student's [project](https://github.com/LibbyH52/Cookbook-App) 


### Code

Some research was done using sites and learning material other than CI.

These are:

* [Stack Overflow](https://stackoverflow.com/)
* [W3Schools](https://www.w3schools.com/)
* [Career Karma](https://careerkarma.com/blog/python-add-to-dictionary/#:~:text=To%20add%20an%20item%20to%20a%20Python%20dictionary%2C,value%20you%20want%20to%20store%20in%20your%20dictionary)
* [pymongo Documentation](https://pymongo.readthedocs.io/en/stable/api/pymongo/index.html)
* [Jinja Documentation](https://jinja.palletsprojects.com/en/2.11.x/)
* [W3Resources](https://www.w3resource.com/mongodb/nosql.php)

### Media

- The image for both the banner the About us page were purchased from [iStockphoto](https://www.istockphoto.com/).

### Acknowledgements

- I would like give a huge thank you to the Slack community, the tutor support team (you guys rock!) and for all the guidance from my mentor Moosa Hassan

Disclaimer: This project's website is created as a educational project (Milestone project 3) for the Code Institute's Full Stack Developer course.

