# Project Testing


1. Automated Testing

2. Manual Testing

3. User Stories

4. Bugs

<br>

[Go to Bear Yoga site](https://bear-yoga.herokuapp.com/)

[Go to README.md](https://github.com/coderkatew/bear-yoga/blob/master/README.md)
<br>
<br>

## Automated Testing
### Django Unit Tests
I created a number of Django unit tests following the guidelines on [Django Projects](https://docs.djangoproject.com/en/3.1/topics/testing/overview/).<br>
The test files can be viewed here:
* [Checkout App](https://github.com/coderkatew/bear-yoga/blob/master/checkout/tests.py)
* [Contact App](https://github.com/coderkatew/bear-yoga/blob/master/contact/tests.py)
* [Retreats App](https://github.com/coderkatew/bear-yoga/blob/master/retreats/tests.py)
* [Saved App](https://github.com/coderkatew/bear-yoga/blob/master/saved/tests.py)

You can use the command `python3 manage.py test` to run these unit tests in the terminal.

I completed these tests towards the end of the project rather than taking a Test Driven Development approach throughout the project so I would like to carry out more extensive and complex automated testing when I revisit this project in the future.

### Flake8 Tests
I used the `python3 -m flake8` command in the terminal to ensure the code adheres to the PEP 8 style guidelines and updated formatting across the project to address errors that came up. 


### Validation Programs
* The project HTML files were tested using W3C Markup Validator.
* The project CSS files were tested using Jigsaw CSS Validator. 
* The project Javascript functions were tested using JSHint. 


## Manual Testing
This project has been tested manually on desktop, iPad and mobile in Chrome, Safari and Firefox. 
<br>I used Chrome Developer Tools to carry out some of the mobile testing. 
<br>All images are under 5MB to ensure they load quickly.

## User Stories
<br>

**As a registered user, I want to:**
<br>

* **View a list of products so that I can select items I want to purchase**.
By navigating to https://bear-yoga.herokuapp.com/products/ I can scroll through products and click on an item to view details and add it to the shopping bag. Note: only the product image is clickable - the entire tile could be made clickable for a future release.
* **View individual product details so that I can easily see the price, description and product rating.**
I can click on the image for any product to open the product detail view where the price, description and product rating are listed. Note: the price and product rating are also displayed below the image in the all products view, before clicking on the image to select the product.
* **Easily view the total cost of the items in my shopping bag so that I can keep track of my spending.**
I can view the bag total in the main navbar and it increases from $0.00 as products are added to the bag. When a product is added, a toast is displayed which indicates the item that has just been added, as well as the current total and threshold for free delivery.
* **Easily register for an account so that I can save my details and view my purchase history.**
I can register for an account by navigating to 'Register' in the 'Account' dropdown and filling in my details in the form that is displayed. It currently logs in without email verification. Note: Email verification has been set to 'optional' temporarily for testing purposes. Once logged in, the Profile section with my details and purchase history (currently empty) is accessible from the 'Account' dropdown. 
* **Sort the list of products so that I can quickly identify the cheapest or most expensive items.**
I can achieve this by selecting 'By Price' in the 'All Products' menu in the category navbar.
* **Sort the list of products so that I can quickly identify products with the highest ratings.**
I can do this by selecting 'By Rating' in the 'All Products' menu in the category navbar.
* **Search for an item using a keyword so I can find relevant products.**
When I enter the keyword 'mat' into the search bar at the top of the page, only mats are displayed in the results.
* **Sort by category so that I can view all items in a specific category.**
I can do this by selecting 'Category' in the 'All Products' menu in the category navbar. I can also select a sub-category in the category navbar.
* **Adjust the quantity of items I am ordering so that I can add more than one of each item to my shopping bag at a time, or adjust the quantity if I change my mind.**
I can increase and decrease the number of items on the shopping bag page before adding a product to the shopping bag, or when reviewing the items in the bag before checking out.
* **See some form of feedback on screen when I take an action so that I can be sure I have completed the action I intended to.**
Throughout the site, toasts are displayed when I add, save or edit quantities of items to confirm the item. When I purposely left a field empty in the Contact form an alert was displayed before I could submit the form. On the checkout form, when I enter a phone number in the email field, an alert is also displayed until I enter an email format.
* **Easily contact the shop owner so that I can ask for more information about products and retreats, or notify them of issues with my order.**
I can do this using the Contact form. For a future release, an instant messaging feature would provide a better (i.e. faster) experience for the user.
<br>

**As a registered user, I want to:**
<br>

* **Easily sign in and sign out so that I can access my account information quickly.**
I can do this by selecting the relevant option on the 'Account' menu.
* **Easily recover my password so that I can access my account if I have forgotten my password.**
I can do this by navigating to the 'Sign In' page and selecting 'Forgot password?'.
* **View my personal profile so that I can view and update or delete my details.**
Once logged in, I can access my profile from the 'Account' menu and view or edit my details there. 
* **View my order history so that I can see what products I have ordered in the past if I want to order again.**
I can also view my order history on the 'Profile' page. Once I had completed a purchase, the order was displayed in the Order History section and I could view the order confirmation by clicking on the order number in the list.
* **Save products to my profile so that I can easily find them if I decide to purchase them at a later time.**
I can do this by selecting a product and the clicking 'Save to Bag'. The item is added to 'Saved Items' which I can access via the 'Account' dropdown. Note: This option isn't visible when I am signed out.
* **View a list of upcoming yoga retreats so that I can decide if I will attend a retreat.**
I can do this by clicking on Retreats in the category navbar and then clicking on an individual retreat for more details. This page isn't visible when I am signed out.
* **Save my payment information so that I can checkout quickly the next time I place an order.**
I can do this by ticking the save box on the checkout form when making a purchase.
<br>

**As a site owner or shop administrator, I want to:**
* **Have special permissions so that I can add, view, edit and delete (CRUD) products and retreats on the site.**
When I sign in with superuser account details, I have access to an 'Admin' dropdown menu which has options to add retreats and products. I can add both entry types by completing the forms. The new entries are displayed in the main pages and edit and delete options are displayed on all product and retreat entries. Both edit and delete options are functioning correctly.
* **Easily access an admin menu so that I can quickly add products and retreats to the site.**
This menu is displayed on the main navbar when I sign in with superuser account details and I can select 'Add Product' or 'Add Retreat'.

## Interesting Bugs