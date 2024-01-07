# Proiect_IS_Sudoku
Proiect la Inginerie Software, care prespune implementarea unui joc de sudoku sub forma unei aplicatii web server-client;

# Descriere generala
  Proiectul reprezinta o aplicatie web care permite rularea unui joc de sudoku cu 1 din cele 3 dificultati: easy, medium si hard. Utilizatorul poate introduce orice cifra de la 1 la 9 in casutele libere si primeste in timp un real un mesaj care confirma corectitudinea cifrei alese ("Correct so far") sau un mesaj care il anunta pozitia cifrei gresite ("Incorrect number on row x, column y"). De asemenea, casuta gresita se va colora cu rosu. Aplicatia web permite si autentificarea jucatorilor, astfel incat sa poata accesa pagina personala, care contine datele utilizatorului si statistici de joc, cum ar fi numarul de jocuri castigate si numarul de jocuri incepute. 
  Aplicatia tine de cont si de timp, astfel incat deasupra jocului apare un timer si un buton de pauza, care opreste temporar posibilitatea modificarii casutelor, iar pe pagina personala a utilizatorului se memoreaza si statistici de timp (timp total petrecut in joc si cel mai bun timp de rezolvare a unui nivel de sudoku).

# Tehnologii & framework-uri
Partea de frontend: React.js (JavaScript) -> rol de client
Partea de backend: Django (Python) -> rol de server
Partea de persistenta: MySQL (SQL)

# Comunicare intre framework-uri
Se face prin intermediul request-urilor HTTP, cu un client numit Axios, pentru primirea/trimiterea/verificarea cererilor de la server la client si invers care respecta un format JSON.

# Initializare & rulare proiect
Pasi pentru initializarea si rularea proiectului, avand descarcate fisierele sursa:
1. Deschiderea unui command prompt in folder-ul ”IS-final”
2. Rularea comenzii ”pip install pipenv”
3. Rularea comenzii ”pipenv install djangorestframework”
4. Rularea comenzii ”pipenv install django-cors-headers”
5. Deschiderea folderului ”IS final” ca proiect in PyCharm
6. Rularea in terminal a comenzilor:
• ”python manage.py makemigrations”
• ”python manage.py migrate”
• ”python manage.py runserver”
7. Deschiderea folderului ”frontend” ca proiect in WebStorm
8. Rularea in terminal a comenzii ”npm start”
9. * In caz de eroare, nu este instalat clientul Axios, si trebuie rulata comanda
”npm install axios”
10. In browser se va deschide automat pagina aplicatiei web
