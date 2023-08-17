---
title: API Reference
parent: Technical Docs
nav_order: 4
---



# [API reference]
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
  

- [Loginfunktion](#loginfunktion)
- [Anmeldefunktion](#anmeldefunktion)
- [Logoutfunktion](#logoutfunktion)
- [delete_note](#delete_note)
- [Notizstatusänderung](#notizstatusänderung)
- [Homeansicht](#homeansicht)
- [Darkmode](#darkmode)
  
{:toc}
</details>



---


## Loginfunktion

### `login()`

**Route:** `/login`

**Methods:** `GET` `POST` 

**Purpose:** Wenn eine nicht authentifizierte Userin auf die /login-Route gelangt, wird das Login-Formular angezeigt, damit die Userin sich anmelden kann.

**Funktionsweise:** 1.	Zu Beginn wird die Userin als current_user auf "anonym" gesetzt, da sie nicht eingeloggt ist.  
2.	Sobald das benutzerdefinierte Loginformular abgesendet wird, validiert die Funktion die eingegebenen Daten, insbesondere die Email-Adresse.  
3.	Die eingegebene Email-Adresse wird in der Datenbank gesucht. Falls die Email nicht gefunden wird, wird der Userin mitgeteilt, dass die Eingaben ungültig sind.  
4.	Wenn die Email gefunden wird, wird das eingegebene Passwort mit dem gehashten Passwort in der Datenbank mittels check_password_hash verglichen.   Bei erfolgreicher Übereinstimmung wird die Userin mithilfe von login_user eingeloggt und auf die Homepage weitergeleitet.  
5.	Falls das eingegebene Passwort nicht mit dem gespeicherten Passwort übereinstimmt, wird die Userin aufgefordert, die Eingabe zu korrigieren.

>> Die Funktion nutzt Flask-Login und den Loginmanager, um den gesamten Authentifizierungsprozess zu verwalten und die eingeloggte Userin zu setzen.

**Sample output:**

![image](https://github.com/Nekkohlas/Nekkohlas.github.io/assets/134234209/f2fd9e67-501c-4c93-8fc0-2e4c7e8f8253)


---

## Anmeldefunktion

### `sign_up()`

**Route:** `/sign-up`

**Methods:** `GET` `POST` 

**Purpose:** Die Funktion sign_up() ermöglicht UserInnen die Registrierung für die Anwendung über die Sign-up Route

**Funktionsweise:**
1.	Wenn eine Userin die /sign-up-Route aufruft, wird zuerst das zugehörige Template gerendert, die die gegenwärtige (anonymen) Userin anzeigt.  
2.	Ein individuelles Formular für die Registrierung wird dargestellt, um die notwendigen Registrierungsinformationen einzuholen.  
3.	Wenn die Userin Eingaben tätigt und das Formular absendet, werden die eingegebenen Daten mithilfe der .validate_on_submit() Methode validiert.  
4.	Anschließend wird eine neue Instanz der User-Klasse erstellt, wobei das Passwort vor der Speicherung gehasht wird.  
5.	Das Datenbankobjekt (db) fügt die erstellte Instanz der User-Klasse mithilfe von .add(new_user) zur Datenbank hinzu und speichert die Änderungen mit .commit().  
6.	Die Methode login_user() wird ausgeführt, um die Userin einzuloggen und in der aktuellen Sitzung zu registrieren.  
7.	Eine Benachrichtigung (Flash-Nachricht) wird ausgegeben, um die Userin darüber zu informieren, dass der Anmeldeprozess erfolgreich abgeschlossen wurde.  
8.	Die Userin wird anschließend auf die Home-Ansicht weitergeleitet.  


**Sample output:**

![image](https://github.com/Nekkohlas/Nekkohlas.github.io/assets/134234209/799437bd-ddd5-4064-9da2-7a8198f4692b)


---
## Logoutfunktion

### `logout()`

**Route:** `/logout`

**Methods:** keine

**Purpose:** Mit der Logoutfunktion kann sich eine angemeldete Userin abmelden.

**Funktionsweise:** Die Logoutroute hat durch den decorator @login_required die Zugriffsvoraussetzung, dass eine Userin eingeloggt ist.   Die logout Funktion loggt die gegenwärtig eingeloggte Userin mit der logout_user() Methode aus, ohne das ein User übergeben werden muss und säubert,   falls vorhanden, den remember me cookie. Wenn der logout Vorgang abgeschlossen ist, wird die Userin auf die login-URL weiterverwiesen.



---
## delete_note()

### `delete_note()`

**Route:** `/delete-note`

**Methods:** `POST` 

**Purpose:** Die delete_note() Funktion wird aufgerufen, wenn die URL /delete-note mit der POST-Methode aufgerufen wird. Sie dient dazu, eine gespeicherte Notiz zu löschen.

**Funktionsweise:**  
Die Daten, die über die POST-Anfrage gesendet werden, werden im JSON-Format übertragen und von der Funktion mithilfe von json.loads(request.data) gelesen.   Die extrahierten Daten werden in der Variablen note gespeichert.
Die Variable noteId wird verwendet, um den Wert des Schlüssels "noteId" aus dem JSON-Objekt note zu extrahieren und zu speichern.  
Anschließend wird mithilfe der Note.query.get(noteId) Methode die entsprechende Notiz in der Datenbank gesucht und in der Variable note gespeichert.  
Es erfolgt eine Überprüfung, ob die aktuelle Userin, welche die Anfrage sendet, der Besitzerin der zu löschenden Notiz ist. Wenn dies der Fall ist, wird die Notiz mithilfe von db.session.delete(note) aus der Datenbank gelöscht. Die Userin erhält eine Benachrichtigung, dass die Notiz erfolgreich gelöscht wurde.  
Die Änderungen werden in der Datenbank gespeichert, indem db.session.commit() aufgerufen wird.  
Die delete_note() Funktion gibt als Rückgabewert eine leere JSON-Antwort zurück. Da die Notiz gelöscht wurde und keine weiteren Daten zurückgegeben werden müssen,   signalisiert die leere JSON-Antwort den erfolgreichen Abschluss des Löschvorgangs.


**Sample output:**

![image](https://github.com/Nekkohlas/Nekkohlas.github.io/assets/134234209/cb315958-b808-438b-ae2b-8908027f766d)





---
## Notizstatusänderung

### `check_note()`

**Route:** `/check-note`

**Methods:** `POST` 

**Purpose:** Wird aufgerufen, wenn die Route /check-note mit der POST-Methode aufgerufen wird.

**Funktionsweise:**  
1.	In der Variable note werden die Daten aus der POST-Anfrage im JSON-Datenformat gespeichert.  
2.	Der Wert des Schlüssels "noteID" aus dem JSON-Objekt "note" wird extrahiert und in der Variable noteId abgespeichert.  
3.	Die Notiz mit der entsprechenden "noteId" wird in der Datenbank gesucht und in der Variable note gespeichert.  
4.	Es wird überprüft, ob die aktuelle Userin die Besitzerin der Notiz ist, bei der der Status geändert werden soll. Wenn dies der Fall ist, wird der Status der Notiz auf den gegenteiligen Wert gesetzt (umgekehrt).  
5.	Die Userin wird über die durchgeführte Statusänderung der Notiz benachrichtigt. Eine Benachrichtigung wird mit flash() ausgegeben, um die Userin über die Statusänderung zu informieren.
6.	Die Funktion gibt eine leere JSON-Antwort zurück, da nach der Änderung des Notizstatus keine spezifischen Daten zurückgegeben werden müssen.  


**Sample output:**

![image](https://github.com/Nekkohlas/Nekkohlas.github.io/assets/134234209/0718b6e2-ead5-45b0-8981-56270b122f4c)


---
## Homeansicht

### `home()`

**Route:** `/`

**Methods:** `GET` `POST` 

**Purpose:** Ermöglicht es dem Nutzer Notizen zu erstellen und den Fortschritt zu berechnen.

**Funktionsweise Notiz erstellen:**
Wenn die home() Funktion aufgerufen wird, überprüft sie den Anfragetyp. Wenn die Anfrage vom Typ POST ist, wird der Wert, der im Feld 'note' übermittelt wurde,   mithilfe von request.form.get abgerufen. Falls die Länge der Notiz kleiner als 1 ist, wird der Userin eine Fehlermeldung angezeigt, die besagt, dass die Notiz zu kurz ist.   Wenn die Länge ausreichend ist, wird eine neue Instanz der Note Klasse erstellt. Diese Instanz enthält die Eingabedaten ('data') sowie die ID der aktuellen Userin ('user_id'). Anschließend wird die neue Notiz in die Datenbank eingefügt und die Änderungen mit db.session.commit() gespeichert.  Die Userin erhält eine Erfolgsmeldung, die besagt, dass die Notiz erfolgreich hinzugefügt wurde.

**Funktionsweise Berechnen des Fortschritts:**
Mittels einer Schleife (for loop) wird für jede Notiz der aktuellen Userin überprüft, ob sie als erledigt ('done') markiert ist.   Falls dies der Fall ist, wird der Fortschrittcounter ('progress') erhöht. Danach wird der Wert des Fortschrittcounters durch die Anzahl der Notizen der aktuellen Userin geteilt und mit 100 multipliziert,   um den Fortschritt in Prozent zu berechnen.
Die home() Funktion gibt ein HTML-Template ('home.html') zurück, in dem die übergebenen Parameter current_user (aktuelle Userin) und progress (berechneter Fortschritt in Prozent) verwendet werden, um die Benutzeroberfläche darzustellen.


**Sample output:**

![image](https://github.com/Nekkohlas/Nekkohlas.github.io/assets/134234209/6a8378b8-6936-4e8c-b239-b1d4d70cea13)
![image](https://github.com/Nekkohlas/Nekkohlas.github.io/assets/134234209/9dcff422-11dc-4481-895f-d6daa10083c0)




---

## Darkmode

### trigger_darkmode()

**Route:** `/trigger-darkmode`

**Methods:** 'POST'

**Purpose:** Ermöglicht der Userin das Aktivieren und Deaktivieren des Darkmode

**Funktionsweise:** 
Wenn die Userin die Schaltfläche in der Navbar anklickt, wird für die gegenwärtige Userin der Darkmode auf den Gegenteiligen Status gesetzt.
Im Anschluss wird die Userin darüber informiert, dass der Darkmode aktiviert wurde. 


![image](https://github.com/Nekkohlas/Nekkohlas.github.io/assets/134234209/6530b198-1c5b-4bc0-96c6-d6d96ed3ff1a)

