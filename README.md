# Bear Yoga

<img src="static/images/bear-yoga-cover.png" style="margin: 0;">

<br>

[Visit Bear Yoga](https://bear-yoga.herokuapp.com/ "Bear Yoga")


# Project Outline
<br>

## Login Credentials and Stripe Payment Details
**Login Details**<br>
Website visitors may browse and purchase products on the site without registering while egistered users have the option to save products to buy at a later date, save delivery and payment information, and view information about upcoming retreats. 
To register for the site, users will need to provide a verified email address but this has been set to 'optional' for the purposes of this project.<br>
Super user login details have been provided to Code Institute on project submission. 
**Test Card Details**<br>
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
<br>

**Contact App**<br>
Name | KEY (Database) | Field Type | Validation<br>
------------ | ------------- | ------------- | -------------
Name | name | CharField | max_length=254 
Email | email | EmailField | max_length=254, null=True, blank=False 
Message | message | TextField |
<br>

**Product App**<br>
<br>

***Categories***
Name | KEY (Database) | Field Type | Validation<br>
------------ | ------------- | ------------- | -------------
Name | name | CharField | max_length=254
Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True 
<br>

***Products***
Name | KEY (Database) | Field Type | Validation<br>
------------ | ------------- | ------------- | -------------
Category | category | ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL 
SKU | sku | CharField | max_length=254, null=True, blank=True 
Name | name | CharField | max_length=254
Description | description | TextField | 
Price | price  | DecimalField | max_digits=6, decimal_places=2
Rating | rating | IntegerFiel | null=True, blank=True
Image URL | image_url | URLField | max_length=1024, null=True, blank=True 
Image | image | ImageField | null=True, blank=True
<br>

**Profile App**<br>
Name | KEY (Database) | Field Type | Validation<br>
------------ | ------------- | ------------- | -------------
User | user | OneToOneField | User, on_delete=models.CASCADE 
Phone Number | default_phone_number | CharField | max_length=20, null=True, blank=True
Street Address 1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
Street Address 2| default_street_address2 | CharField | max_length=80, null=True, blank=True
Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True
County or Region | default_county | CharField | max_length=80, null=True, blank=True
Country | default_country | CountryField  | blank_label='Country', null=True, blank=True
Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
<br>

**Retreats App**<br>
Name | KEY (Database) | Field Type | Validation<br>
------------ | ------------- | ------------- | -------------
Name| name | CharField | max_length=200
Date | date | CharField | max_length=200 
Duration | duration| CharField | max_length=200 
Description| description | TextField | null=False, blank=False, default=''
Price | price | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 
Location| location| CharField | max_length=200
Image URL | image_url | URLField | max_length=1024, null=True, blank=True 
Image | image | ImageField | null=True, blank=True
<br>

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