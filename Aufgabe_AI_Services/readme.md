# KI-Microservices mit Docker

Du sollst eine Web-Applikation bauen, die handschriftliche Notizen digitalisiert, korrigiert und übersetzt. Anstatt alles in ein Programm zu schreiben, bauen wir eine **Microservice-Architektur**. Jeder Dienst läuft in seinem eigenen Docker-Container.

## 2. Das Ziel-Szenario
Dein Service besteht aus folgenden Containern:
1. **Frontend**: Eine Webseite (HTML/JS) für den Upload.
2. **Das Auge (OCR)**: Erkennt Text in Bildern.
3. **LLM Container**: Ein Ollama Image welches alle Modelle die Ihr verwendet "hosted", ihr könnt bei den Request mitschicken welches Modell verwendet werden soll.

---

## 3. Deine Aufgaben

### Schritt 1: Modell-Recherche auf Hugging Face 
Gehe auf [huggingface.co/models](https://huggingface.co/models) und suche nach passenden Modellen für deine Container. Achte darauf, dass sie klein genug für deinen Laptop sind (SLMs - Small Language Models). 

* **Für die Handschrift (OCR):** Hier baut ihr ein Image mit dieser Anleitung: https://dev.to/moni121189/from-image-to-text-in-seconds-tesseract-ocr-in-a-docker-container-1ohi

Das Dockerfile habe ich euch bereits hingestellt, es funktioniert aber nur für Englisch. 
Erweitert es doch noch für andere Sprachen.

* **Für Korrektur & Übersetzung:** Sucht hier nach kleinen spezifischen Modellen die genau das können was ihr wollt (Typos korrigieren und Texte übersetzen)

### Schritt 2: Die Container-Vernetzung flicken 
Ich habe dir die Software vorbereitet, aber die "Kabel" zwischen den Containern fehlen noch. 

1.  Öffne die Datei `app.py`.
2.  Überlege welche Anpassungen du machen musst, damit die Software innerhalb eines Docker Netzwerkes funktioniert (das Default Bridge Netzwerk von docker compose)

### Schritt 3: Docker-Compose konfigurieren
Erstelle ein `docker-compose.yml`, sodass jeder Dienst sein eigenes Image bekommt. Nutze für die KI-Modelle das **Ollama-Image**, da es den Betrieb von Hugging-Face-Modellen sehr einfach macht.

### Schritt 4: Vergleicht verschiedene Modelle
Sucht auf Huggingface verschiedene Modelle, tauscht diese aus und beobachtet die Resultate (Performance in Sachen Zeit aber auch Qualität).

Dokumentiere deine Ergebnisse

### Schritt 5: Macht OCR auch mit einem LLM
Baut den Schritt von OCR um, so dass ihr auch den Ollama Container mit einem Image Modell aufruft.


---
