---
title: Design Decisions
parent: Technical Docs
nav_order: 5
---

[Jane Dane]
{: .label }

# [Design decisions]
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
  
- [Design Decisions](#design-decisions)
  - [01: Wie verwalte ich die Datenbank?](#01-wie-verwalte-ich-die-datenbank)
    - [Meta](#meta)
    - [Problem statement](#problem-statement)
    - [Decision](#decision)    
  - [02: Wie kann ich zeitnah UserInnen verwalten?](#02-wie-kann-ich-zeitnah-userinnen-verwalten)
    - [Meta](#meta-1)
    - [Problem statement](#problem-statement-1)
    - [Decision](#decision-1)
  - [03: Kommunizieren mit UserInnen](#03-kommunizieren-mit-userinnen)
    - [Meta](#meta-2)
    - [Problem statement](#problem-statement-2)
    - [Decision](#decision-2)
  - [04: Fortschrittanzeige](#04-fortschrittanzeige)
    - [Meta](#meta-3)
    - [Problem statement](#problem-statement-3)
    - [Decision](#decision-3)
  - [05: Sicherheitsüberlegungen](#05-sicherheitsüberlegungen)
    - [Meta](#meta-4)
    - [Problem statement](#problem-statement-4)
    - [Decision](#decision-4)

{:toc}
</details>

---
>> da es keine weiteren Gruppenmitglieder gibt, wurden alle Entscheidungen von mir alleine getroffen

## 01: Wie verwalte ich die Datenbank?

### Meta

Status
: Work in progress - **Decided** - Obsolete


### Problem statement

Sollen Datenbankeinträge mit plain-SQL / CRUD vorgenommen werden oder eine Alternative wie SQLAlchemy verwendet werden?

### Decision

Ich habe mich aus folgenden Gründen für SQLAlchemy entschieden:  

**Fehler vermeiden**  

Nach meiner Recherche habe ich mich für SQLAlchemy entschieden, da es die Interaktion mit der Datenbank erleichtert. Somit werden auch etwaige Tippfehler, die sich einschleichen könnten verhindert.   

**Objektorientierung** 

SQLAlchemy erlaubt weiter die Datenbankverbindung mit Python code herzustellen, SQL queries mit objektorientierter Programmierung und den workflow zu vereinfachen.    
SQLAlchemy hat Datenbankmodelklassen. Mithilfe von weiteren Imports wie UserMixin kann die Instanz der Datenbankmodellklasse dann   Eigenschaften wie den Authentifizierungsstatus erben, was das Anzeigen der Ansichten vereinfacht. 

Insgesamt gehe ich davon aus, dass durch das Nutzen von SQLAlchemy das Business-Ziel, die App nutzbar zu machen, effizienter erreicht werden kann,   als durch das verwenden von CRUD SQL Praxis.

---
## 02: Wie kann ich zeitnah UserInnen verwalten?

### Meta

Status
: Work in progress - **Decided** - Obsolete


#### problem statement

Ich muss einen Weg finden, UserInnen in einer Flaskanwendung einloggen, ausloggen und erinnern zu können, um an der eigentlichen App zu arbeiten.

### Decision

**Flask_login:**  

Nach meiner Recherche bin ich schnell auf Flask Login und den Login_manager gestoßen.
Aufgrund seiner Beliebtheit in der Community und den damit mannigfaltig vorhandenen Ressourcen, wie man die Erweiterung für Userinnenauthentifizierung nutzt, fiel mir die Entscheidungen relativ einfach. 

**UserMixin:**

Ausschlaggebend für meine Entscheidung war jedoch UserMixin, welches durch flask_login importiert werden kann. Hiermit können User Eigenschaften wie ihren Authentifizierungsstatus implementiert bekommen, was das Darstellen der Ansichten wesentlich vereinfachen sollte. 
https://flask-login.readthedocs.io/en/latest/

---

## 03: Kommunizieren mit UserInnen

### Meta

Status
: Work in progress- **Decided** - Obsolete


### Problem statement

Ich muss einen weg finden, mit den UserInnen zu kommunizieren, ob Aktionen erfolgreich waren

### Decision
Hier habe der Einfachheit halber Flasks Flash-messages verwendet, da das Framework diese Erweiterung anbietet und für den Zweck der Anwendung ausreicht.

---

## 04: Fortschrittanzeige

### Meta

Status
: Work in progress - **Decided** - Obsolete


### Problem statement

Ich muss einen Weg finden, die Fortschrittanzeige darzustellen

### Decision

Hier habe ich ursprünglich überlegt, den Fortschritt mithilfe von Diagrammen o.Ä. darzustellen, was aber nicht ganz mit meiner Vision zusammenpasste.
Da die Idee der Fortschrifttsanzeige ursprünglich von Videospielen inspiriert war, bin ich schnell auf die Progressbar von Bootstrap gestoßen.

Da die Progressbar als Bootstrap Komponente der Idee sehr nahekam und für mich als innerhalb der zeitlichen Vorgaben implementierbar erschien, fiel die Entschiedung auf die Progressbar.


---
## 05: Sicherheitsüberlegungen

### Meta

Status
: Work in progress - **Decided** - Obsolete


### Problem statement

Da das speichern von Passwörtern in plaintext aus Sicherheitsgründen nicht diskutabel ist, muss ich einen Weg finden, die Passwörter sicher zu speicehrn.

### Decision

Um die Passwörter nicht in Klartext zu speichern, habe ich entschieden das Passwort der UserInnen zu hashen. Bei meiner Recherche bin ich auf werkzeug.security und generate_password_hash und check_password_hash gestoßen.  
Ausschlaggebend für die Entscheidung diese zu verwenden waren meine begrenzten Kenntnisse in diesen Dingen sowie die vielfältigen Ressourcen, wo die Vorgehensweise dargelegt wird.

---
