---
title: App Behavior
parent: Technical Docs
nav_order: 2
---


# [App behavior]
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
  
- [Registrierung](#registrierung)  
- [Anmeldung nach Registrierung](#anmeldung-nach-registrierung)  
- [Home-Ansicht](#home-ansicht)  
- [User flow Diagramm](#user-flow-diagramm)
  
{:toc}

## Registrierung:
Beim ersten Besuch von NiceNotes landen neue Userinnen auf der Login-Seite.  
Um sich anzumelden, müssen sie ein UserInnenprofil erstellen.  
In der Navbar gibt es einen Button, der zur Registrierungsansicht führt.  Solange die Userinnen noch nicht registriert ist, wird er in der Navbar als "Gast" begrüßt.  
Eingaben in den Registrierungsfeldern müssen den vorgegebenen Formatierungen entsprechen. Andernfalls wird die Userin aufgefordert, die Eingaben entsprechend anzupassen.  
Wenn alle Eingaben den Anforderungen entsprechen, wird geprüft, ob die eingegebenen Passwörter übereinstimmen.   Andernfalls erhält die Userin eine entsprechende Benachrichtigung.  
Nach erfolgreicher Validierung der Eingaben wird die Userin registriert.   Das Profil wird in der Datenbank mit einer eindeutigen ID erstellt, und Userin erhält eine Bestätigung über den erfolgreichen Vorgang.  
Schließlich wird die nun registrierte Userin zur Home-Ansicht weitergeleitet.

## Anmeldung nach Registrierung:
Bei zukünftigen Besuchen können registrierte Userinnen sich direkt von der Login-Seite aus anmelden, sofern sie die korrekten Anmeldedaten eingeben.

## Home-Ansicht:
Nach dem Anmelden erreichen Userinnen die Home-Ansicht.  
Hier können sie ihre gespeicherten Notizen anzeigen lassen.  
Es besteht die Möglichkeit, neue Notizen in das dafür vorgesehene Eingabefeld einzugeben und in der Datenbank zu speichern.  
Userinnen können außerdem ihre Notizen als "erledigt" markieren und den Status von Aufgaben ändern.   Dies erfolgt durch eine spezielle Schaltfläche.  
Wenn Userinnen Notizen eingeben und diese als "erledigt" markieren, wird der Fortschritt mithilfe einer Fortschrittsanzeige visualisiert.   Diese Anzeige wird durch die Verwendung einer Bootstrap Progressbar implementiert.  
Der Nutzer kann zwischen einer hellen und dunklen Benutzeroberfläche entscheiden, indem er das entsprechende Bedienelement in der Navbar verwendet.  
Die Notizen werden nach ihrem Status in seperaten Listen angezeigt, eine Liste hält die unerledigten, die andere die erledigten Notizen.

## User flow Diagramm 
![User-flow](../assets/images/User-Flow.png)


</details>
