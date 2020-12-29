# Bear Yoga

<img src="static/images/bear-yoga-cover.png" style="margin: 0;">

<br>

[Visit Bear Yoga](https://bear-yoga.herokuapp.com/ "Bear Yoga")


# Project Outline
<br>

## Login Credentials and Stripe Payment Details
Website visitors may browse and purchase products on the site without registering while egistered users have the option to save products to buy at a later date, save delivery and payment information, and view information about upcoming retreats. 
To register for the site, users will need to provide a verified email address but this has been set to 'optional' for the purposes of this project.

Super user login details have been provided to Code Institute on project submission. 

The following test card details can be used to submit test Stripe payments on the site:

**Card Number -** 4242 4242 4242 4242<br>
**CVC -** Any 3 digit number<br>
**Expiration Date -** Any date in the future<br>
**Phone Number, Address and Email Address -** These can all be fictional<br><br>

## UX
<br>

## Documentation
<br>

## Features
<br>

## Information Architecture

### Database
I used sqlite3 as a database for development and moved to Heroku's PostgreSQL for deployment.<br><br>

### Data Models

**Checkout App**<br>
Name | KEY (Database) | Field Type | Validation<br>
------------ | ------------- | ------------- | -------------
Order Number | order_number | CharField | max_length=32, null=False, editable=False
User | user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
Full Name | full_name | CharField | max_length=50, null=False, blank=False
Email Address | email | EmailField | max_length=254, null=False, blank=False
Phone Number | phone_number | CharField | max_length=20, null=False, blank=False
Country | country | CountryField  | blank_label='Country *', null=False, blank=False
Postcode | postcode | CharField | max_length=20, null=True, blank=True
Town or City | town_or_city | CharField | max_length=40, null=False, blank=False
Street Address 1 | street_address1 | CharField | max_length=80, null=False, blank=False
Street Address 2| street_address2 | CharField | max_length=80, null=False, blank=False
County or Region | county | CharField | max_length=80, null=False, blank=False
Date | date | DateTimeField| auto_now_add=True
Delivery Fee | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
Subtotal | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Shopping Bag| original_bag | TextField | null=False, blank=False, default=''
Stripe PID | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

## Technologies Used
<br>
The following technologies were used to build this project:

**HTML, CSS, JavaScript and Python** - Programming languages used.

**Gitpod IDE** - IDE to build this project.

**Django** - Python framework for rapid development and design.

**Bootstrap** - For website structure elements.

**Stripe** - Payment platform to validate and accept payments.

**Google Fonts** - To style project fonts.

**Font Awesome** - To present navigation icons.

**Django Crispy Forms** - To style django forms.

**AWS S3** - To store static and media files.

**PIP** - To install required tools.

**GitHub** - To store project repository.

**Heroku** - Project deployment.

**Postgres** - Project database.

**Balsamiq** - To create project wireframes.

## Testing
<br>

## Deployment
<br>

## Credits and Acknowledgements
<br>