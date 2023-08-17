# Quellen:
# Der komplette code in diesem file ist übernommen aus: https://www.youtube.com/watch?v=dam0GPOAvVI&t=710s&ab_channel=TechWithTim
# und dem dazugehörigen Code-Repository https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/__init__.py
# Erklärungen / Kommentare nach meinem Verständnis aus https://www.youtube.com/watch?v=dam0GPOAvVI&t=710s&ab_channel=TechWithTim und  
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#check-the-sqlalchemy-documentation, https://flask-login.readthedocs.io/en/latest/ 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()       #erstellt Instanz SQLAlchemy-Klasse, = Bibl. um Arbeit mit Python Datenbanken zu erleichtern
DB_NAME ="database.db"  #erstellt Var. die den Namen der Datenbank enthält/angibt

# Quelle: https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/__init__.py bzw. https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#check-the-sqlalchemy-documentation "configure the extension"
def create_app():               #Funktion um bei Aufruf die Anwendung zu erstellen
    app = Flask(__name__)       #Standardweg um Flask Framework Instanz in __init__.py file zu erstellen
    app.config['SECRET_KEY'] ='do not share this since its the secret key for a reason' #Secret Key signiert Sitzungsdaten, Server prüft, nicht vom Client manipulierbar
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'#Uniform resource Identifier mit dem die App arbeitet für DB. DB_Name wird eingefügt, Sqlite Datenbank 
    db.init_app(app)#SQLAlch Instanz "db" Initialisierung und Bindung an "app" - App kann mit DB interagieren, Data abrufen und speichern...
    

    #der Code erstellt eine Flask-App und konfiguriert sie um mit SQLITE datenbank zu arbeiten. Die wird in database.db gespeichert. SQL Alch.Instanz "db" wird mit app verbunden
    #so können Datenbankoperationen durchgeführt werden, Secret key = sicherheit der app 
    
#Quelle: https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/__init__.py 
    from .views import views    #importiert code aus views.py, enthält Funkt. u. Routen f. Webanwendung
    from .auth import auth      #importiert code aus auth.py, "" 

#Quelle: https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/website/__init__.py    
    app.register_blueprint(views, url_prefix='/')   #Registriert views als Blueprint in Flaskapp. URL-Präfix =alle Routes in Blueprint beginnen mit '/'
    app.register_blueprint(auth, url_prefix='/')    #Registriert auth als Blueprint

    

    from .models import User, Note #importiert Klassen "User" und "Note" aus "models"
    
    create_database(app)    #Funktion siehe unten - erstellt Database

    login_manager =LoginManager()   #initialisiert login_manager Instanz der Klasse LoginManager (login_manager enthält code, der app und Flask-Login verbindet, bspw. load user via ID oder wo User landet, wenn er einloggen muss usw.)
    login_manager.login_view ='auth.login'  #login_view Eigenschaft der Loginmanager Klasse zuweisen. Gibt Route an, auf die Benutzer weitergeleitet wird, wenn nicht authentifiziert aber auf geschützte Seite zugreifen möchte
    login_manager.init_app(app)     #LoginManager Instanz initialisiert und an Flask App "app" gebunden. SO kann LManager mit app interagieren und Benutzerauthentifizierung bereitstellen - secret key pflicht

    @login_manager.user_loader #setzt user_loader callback, verwen. um Userobjekt in Session neuzuladen 
    def load_user(id):  #Funktion load user wird definiert. Nimmt Parameter mit dem Namen "id" entgegen der die eindeutige Identifikation eines Benutzters repräsentiert
        return User.query.get(int(id))  #ruft User.query.get(int(id)) auf und ruft Nutzer mit angegebener id aus der Datanbank ab
                                        #query sql, get =hol mir query und setz die userID ein

    return app #gibt Flask-App "app" von FUnktion create_database zurück, nachdem der Datanbankerstellungsprozess abgeschlossen ist 

def create_database(app):   #funktion create_database, erwartet Argument mit Namen app, das eine Flask-App repräsentiert
    if not path.exists('website/' + DB_NAME): #überprüft ob Datei "DB_Name" im Verzeichnis website exisitiert, path exists() prüft, ob Datei im Verzeichnis existiert, wenn nicht existiert, wird der Code danach ausgeführt
        with app.app_context(): #erstellt einen Kontext für die App. Relevant für SQLAlchemy, damit DB Operationen innerhalb des Kontext ausgeführt werden - Ordnung für DB ressourcen und connections...
            db.create_all() #ruft create_all() Methode, requires context, kreiert Tabellen, Datenbankstrukturen in DB, basierend auf in Anw. definierten Modellen und Klassen
            
        print('Created Database!')

        