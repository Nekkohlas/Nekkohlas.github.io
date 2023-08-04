from . import db                            #importiert Modul db aus dem aktuellen Verzeichnis, das ermöglicht wiederrum Nutzung von Funkt. und Meth. von SQLAlchemy um mit Datenbank zu arbeiten  
from flask_login import UserMixin           #importiert UserMixin aus Modul "flask_login" - UM Klasse gibt implementation von is_authenticated(), is_active(),is_anonym(),get_id() Methoden
from sqlalchemy.sql import func             #func aus sqlalchelmy.sql, bietet verschiedenen Funktionen für SQL Abfragen

#User und Notiz Tabellen
class Note(db.Model):                                                       #Klasse "Note" erbt von db.Model -SQLalchemy Model Klasse
    id = db.Column(db.Integer, primary_key=True)                            #id ist eine Spalte vom Typ Integer, dient als Primarykey, i.e. jede Notiz einen eindeitigen Indentifikator
    data = db.Column(db.String(10000))                                      # Spalte "data" (für Notizen) vom Typ "String" mit einer max Länge von 10k Zeichen 
    date = db.Column(db.DateTime(timezone=True), default= func.now())       #Spalte "DateTime" typ (für Tag und Uhrzeit), default=func.now() setzt standardmäßig aktuelles Datum und aktuelle Uhrzeit - SQLAlchemy 
    done = db.Column(db.Boolean())                                          #booleanSpalte um den status der Notiz zu speichern (done flag)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))               #Spalte "user_id" in Datenbanktabelle, typ int, speichert f.key, der auf Benutzter verweist, dem die Notiz gehört
    #must pass existing valid users id (one to many relationship )
    #Primärschlüssel der Tabelle auf die wir verweisen ist in Spalte 11 
 
class User(db.Model, UserMixin):                    #inherit from db.Model(Klasse) (sqlalchemy Object), also inherit from UserMixin(Klasse) die zusätzliche FUnktionen und Eigenschafen enthält
                                                    #Alle Spalten die in der Datenbank gespeichert werden sollen in Nutzer-Objekt(en)
    id = db.Column(db.Integer, primary_key = True)  #jeder Benutzerdatensatz hat eine eindeutige ID vom Typ integer 
    email = db.Column(db.String(150), unique=True)  #email ist vom Typ String in der Datenbank, max. Länge von xxx Zeichen, unique=true bedeutet jede Email innerhalb Tabelle muss eindeutig sein
    password =db.Column(db.String(150))             #pw ist ebenfalls von Typ String in der Datenbank, max Länge xxx
    first_name = db.Column(db.String(150))          #wie oben 
    notes = db.relationship('Note')                 #setzt die Datenbankbeziehung zwischen "Note" Klasse und User-Klasse 