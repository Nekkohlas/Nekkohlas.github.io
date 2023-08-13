from flask import Blueprint, render_template, request, flash, jsonify

#nikolas-test@gmail.com
#test12345
from flask_login import login_required, current_user
from .models import Note #importiert Note aus dem Modul .models, punkt sagt relativ zum aktuellen Verzeichnis das Model suchen
from . import db #importiert Datenbankinstanz "db" aus dem aktuellen Modul, der punkt vor "db" bdeutet, dass "db" relativ zum aktuellen Verzeichnis gesucht werden soll
import json #ermöglicht arbeiten mit JSON-Daten 
#Blueprint für Erstellung Blueprints, "render_template" für das Rendern von HTML-Vorlagen, "request" für Zugriff auf Anfragedaten, "flash" für ANzeigen von Meldungen an Benutzer und
#jsonify für Konvertieren von Daten in das JSON-Format 

views = Blueprint('views', __name__)  #erstellt BLueprint, mit Namen views, um Flask-Funktionen zuz organisieren. 'views' gibt den Namen des BLueprints __name__ gibt das aktuelle Modul an 

@views.route('/', methods = ['GET', 'POST']) #Funktion soll aufgerufen werden, wenn Startseite der Anwendung aufgerufen wird. methods get post gibt an, dass sowohl get als auch Post anfragen verarbeitet werden können
@login_required #login required stellt sicher, dass nur angemeldete Benutzer auf diese Seite zugreifen können
def home(): #Funktion wird ausgeführt, wenn die Startseite (home) aufgerufen wird
    if request.method =='POST': #prüft, ob die Anfrage eine Post Anfrage ist, also ob ein Formular auf der Seite abgesendet wurde
        note = request.form.get('note') #holt den Wert des Formularfelds mit dem Namen "note" aus der POST-Anfrage, nimmt an, dass ein Eingabefeld mit Namen "note" vorhanden ist (home z 17)

        if len(note)<1:
            flash('Note is too short!', category = 'error') #eingabe darf nicht kleiner sein als 1, sonst flash errpr  "too short"
        else:   #wenn länge i.O. wird codeblock ausgeführt
            new_note = Note(data=note, user_id=current_user.id) #erstellt neues Objekt der Klasse Note mit den werten data (eingabe Notiz) und "user_id" (id des akt. Benutzers)
            db.session.add(new_note)    #Diese Zeile fügt neue Notiz zur Datenbank hinzu
            db.session.commit() # diese Zeile speichert die Änderungen in der Datenbank 
            flash('Note addded!', category = 'success')# flash nachricht teilt mit, dass Note hinzugefügt wurde
            
    done_one = Note.query.filter_by(done=True, user_id=current_user.id).all()
    debug = f"Progress: {len(done_one)}/{len(current_user.notes)}"
    # Calculate progress in %
    progress = 0
    for note in current_user.notes:
        if note.done:
            progress += 1
    if (len(current_user.notes) > 0):
        progress = round(((progress / len(current_user.notes))) * 100)
    
    return render_template("home.html", user = current_user, progress = progress, debug=debug) # Rendert das Html template "home.html" und gibt Rückgabewert. Aktuelles BenutzerObjekt "current_user" wird an Template übergeben

@views.route('/delete-note', methods=['POST'])#decorator views route zusammen mit /delete note als URL Muster, um anzugeben, dass diese Funktion aufgerufen werden soll 
#wenn die URL "/delete-note" aufgerufen wird. Die Option methods "POST" gibt an, dass die Funktion nur POST-Anfragen akzeptiert 
def delete_note():#Funktion "delete_note" die ausgeführt wird, wenn URL '/delete-Note" aufgerufen wird
    note= json.loads(request.data)#liest Daten aus POST Anfrage als JSON und speichert sie in der Variable "note" JSON ist Datenformat zum Speichern und Austauschen von Daten 
    noteId = note['noteId']#extrahiert den Wert des Schlüssels "noteID" aus dem JSON-Objekt "note" und speichert in in der variable noteid
    note= Note.query.get(noteId)#sucht in der Datenbank nach einer Notiz mit entsprechender "noteid" und speichert sie in der Var "note", hier wird angenommen, dass es Datenbanktabelle "Note" gibt, die die Notizen enthält
    if note:#überprüft ob die Notiz mit der gegebenen noteid in der Datenbank gefunden wurde
        if note.user_id == current_user.id:#überprüft ob aktueller Nutzer der Besitzer der notiz ist, die gelöscht werden soll
            db.session.delete(note)#löscht die gefundene Notiz aus der Datenbank
            flash("Notiz wurde gelöscht")
            db.session.commit()#speichert die Änderungen in der Datenbank
    return jsonify({})#gibt eine leere JSON antwort zurück, das heißt, es wird nach dem Löschen der Notiz keine spezifische Daten zurückgegeben

@views.route('/check-note', methods=['POST'])
def check_note():#Funktion "check_note" die ausgeführt wird, wenn URL '/check-note" aufgerufen wird
    note = json.loads(request.data) #liest Daten aus POST Anfrage als JSON und speichert sie in der Variable "note" JSON ist Datenformat zum Speichern und Austauschen von Daten 
    noteId = note['noteId']#extrahiert den Wert des Schlüssels "noteID" aus dem JSON-Objekt "note" und speichert in in der variable noteid
    note = Note.query.get(noteId)#sucht in der Datenbank nach einer Notiz mit entsprechender "noteid" und speichert sie in der Var "note", hier wird angenommen, dass es Datenbanktabelle "Note" gibt, die die Notizen enthält
    if note:#wenn resultat
        if note.user_id == current_user.id:
            note.done = not note.done #gegenteil
            db.session.commit()#speichert Änderung in der Datenbank
            flash(f"Notiz wurde als {'' if note.done else 'nicht '}erledigt makiert.")
    return jsonify({})#gibt eine leere JSON antwort zurück, das heißt, es wird nach dem Löschen der Notiz keine spezifische Daten zurückgegeben