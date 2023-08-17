# Inhalt des Repository

Dieses Repository enthält den Code für die Notizapp NiceNotes und die Präsentationsunterlagen.


## Steps to execute the example code

**Step 1:** Klonen Sie das Repository https://github.com/Nekkohlas/Nekkohlas.github.io.git (dieses repository)


```shell
clone https://github.com/Nekkohlas/Nekkohlas.github.io.git
```

**Step 2:** Führen sie das Kommando `run python -m venv .venv` aus:

```shell
python -m venv .venv
```

**Step 3:** Führen Sie das Activate Script aus: .venv\Scripts\Activate.[bat,ps1,sh - Abhängig von Ihrem System] `.venv\Scripts\Activate.__`:

```shell
.venv\Scripts\Activate.bat
```

```shell
.venv\Scripts\Activate.ps1
```

```shell
.venv\Scripts\Activate.sh
```

**Step 4:** Führen Sie das Kommando aus python -m pip install -r requirements.txt

```shell
python -m pip install -r requirements.txt
```

**Step 5:** Starten Sie den Webserver via:  flask run
```shell
flask run
```


```shell

Created Database!
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 
```

**Step 6:** Besuchen Sie: [http://127.0.0.1:5000/](http://127.0.0.1:5000/) um NiceNotes zu benutzen
