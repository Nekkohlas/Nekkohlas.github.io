# Quellen:
# Ein Großteil des Code in diesem file ist übernommen aus: https://www.youtube.com/watch?v=dam0GPOAvVI&t=710s&ab_channel=TechWithTim
# und dem dazugehörigen Code-Repository https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/auth.py

# Erklärungen / Kommentare nach meinem Verständnis aus:  https://www.youtube.com/watch?v=dam0GPOAvVI&t=710s&ab_channel=TechWithTim und  
# https://werkzeug.palletsprojects.com/en/2.3.x/utils/#werkzeug.security.generate_password_hash, https://werkzeug.palletsprojects.com/en/2.3.x/utils/#werkzeug.security.check_password_hash,
# https://flask-login.readthedocs.io/en/latest/, https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/



from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

from .forms import login_form, register_form # eigens erstellte forms aus forms.py


auth = Blueprint('auth', __name__) #erstellt auth Blueprint, Blueprints zwecks Aufteilung/Orga einer App

#Quelle: Code übernommen aus https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/auth.py und umgebaut, sodass eigenes login_form mit validatoren verwendet wird
@auth.route('/login', methods= ['GET', 'POST']) #Funkt. ausgeführt wernn Nutzer /login Seite Anwendung aufruft 
def login():            #definiert loginfunktion, wenn Benutzer /login aufruft
    form = login_form() #form = custom form
    prev_login = ''     #speichern, wenn user vorher email eingegeben hat damit diese stehen bleibt 
    if form.validate_on_submit():   #überprüft Felder der Form, welche im Post gesendet werden, mit den in forms.py festgelegten Validatoren
        user = User.query.filter_by(email=form.email.data).first()  #sucht nach in Form angegebener Email
        if user:    # user gefunden
            if check_password_hash(user.password, form.password.data): #überprüft sicher, ob Eingabe mit PW übereinstimmt, check_password_hash                 
                flash('Logged in successfully!', category = 'success') #flash success
                login_user(user, remember=True)                        #Benutzer login 
                return redirect(url_for('views.home'))                 #weiterleiten auf views.home
            else:
                prev_login = form.email.data                           
                flash('Incorrect password, try again.', category = 'error') #flash falsche Passwort Eingabe
        else:
            flash('Email does not exist, make sure you type it in correctly!', category='error') # flash Email gibt es nicht
         
    return render_template("login.html", user=current_user, prev_login=prev_login, form=form) 

#Quelle: Code übernommen aus https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/auth.py
@auth.route('/logout')                      #Route mit pfad "/logout" für auth Blueprint
@login_required                             #Voraussetzung auf diese Route zuzugreifen ist, dass der Benutzer eingeloggt ist
def logout():                               #logout Funktion
    logout_user()                           #loggt Benutzer aus, "löscht" den remember me cookie falls vorhanden
    return redirect(url_for('auth.login'))  #leitet Benutzer an auth.login Seite weiter


#Quelle: Code übernommen aus https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/auth.py und umgebaut, sodass eigenes register_form mit Validatoren verwendet wird
@auth.route('/sign-up', methods= ['GET', 'POST'])
def sign_up():
    form = register_form()
    
    if form.validate_on_submit():                       #überprüft Felder der Form, welche im Post gesendet werden, mit den in forms.py festgelegten Validatoren
        new_user = User(email=form.email.data, first_name=form.first_name.data, password=generate_password_hash(form.password.data, method='sha256'))
                                                        #user ist Datenbankmodell, überträgt formfelder direkt in die Datenbank mit Ausnahme Passwordfeldes, welches vorher gehashed wird.
        db.session.add(new_user)                        #neuer User soll in die Datenbank geschrieben werden
        db.session.commit()                             #Änderungen werden in die Datenbank geschrieben
        login_user(new_user, remember=True)             #log in the user #aktuelle Session wird auf User registriert
        flash('Account created!', category = 'success') #flash nachricht 
        
        return redirect (url_for('views.home'))         #url_for schaut welche Route für home seite verwendet wird und redirected zum Wiedergabewert 
        

    return render_template("sign_up.html", user=current_user, form=form)    #rendert template für signup, vorausgesetzt wir haben noch keine form daten 
                                                                            #wenn keine formdaten, bieten wir dem nutzer die möglichkeit die formdaten einzugeben 