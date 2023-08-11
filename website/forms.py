from wtforms import *
from flask_wtf import FlaskForm
from wtforms.validators import *
import email_validator
from flask_login import current_user
from .models import User

class register_form(FlaskForm):     #class register_form that inherits from FlaskForm-class //class is for registration
    email = StringField(            #email is a StringField - email input is handled as StringField 
        validators=[                #validators=[ is a List of validators that are applied to the emailfield - validators handle input criteria
            InputRequired(),        #InputRequired validates that input was provided for this field 
            Length(10, 32),          #Length(min ,max) validates the length of a string
            Email(),                #Email() validates an valid email address, requires email_validator to be installed 
        ]
    )
    first_name = StringField(      #first_name is a Stringfield, such is its handling 
        validators=[                # validators that are applied on first_name
            InputRequired(),        #validates that input was provided
            Length(2, 32),          #validates min and max length of provided input
        ]
    )
    password = PasswordField(       #password is a passwordfield (practically the first password)
        validators=[                #validators applied 
            InputRequired(),        #validates whether input was provided   #sets flag 
            Length(9, 64),          #validates min max length of input
        ]
    )
    cp_password = PasswordField(    #password two so to speak   
        validators=[                #validators applied to cp_password
            InputRequired(),        #validates whether input was given
            Length(9,64),           #validates min max length of input 
            EqualTo("password", message="Password must match")  #Equalto is not run in case the password field is left empty, first param is the name of the other field to comparre to, 
            #message is the raised error message in case of validation error.
        ]
    )
    
    def validate_email(self, email):                            #method within class w 2 parameters; (self, - refers to the instance of the class and .., email) represents the email input validated
        if User.query.filter_by(email=email.data).first():      #checks for if user is already in database, User model is query object /queried , 
                                                                #.filter_by(email=email.data) filters the query to retrieve whether the email column mathes the value provided in the email param of the method
                                                                #email.data retrieves the data entered in the email field of the form, .first() retrieves the first matching record of the filtered query results
            raise ValidationError("Email already registered!")  #if the samel email exists, a ValidationError(is a class of Flask_wtf) excepteion is raised
                                                                #the message tells the user the email has already been used 

class login_form(FlaskForm):    #class for login_form inherits from Flask Form class
    email = StringField(        #field email is a Stringfield (i.e. text input)
        validators=[            #validators used follow
            InputRequired(),    #validates if input was put 
            Length(10, 32),     #validates min max length within paranthesis
            Email(),            #validates whether a valid email was used 
        ]
    )
    password = PasswordField(   #password is a PasswordField 
        validators=[            #validators applied
            InputRequired(),    #validates input was given 
            Length(9, 64),      #validates min max length within parenthesis 
        ]
    )
