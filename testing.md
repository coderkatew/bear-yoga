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
