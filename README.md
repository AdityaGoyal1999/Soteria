# Soteria

Full stack application.

### 🚀Running the app:

- Navigate the folder which contains requirements.txt in terminal
- Execute the following code inside the terminal
```
pip install -r requirements.txt
python manage.py runserver
```
- Go to the mentioned link in the terminal after executing these commands.

### Note for Developers

The web app is rigorously documented and follow all the conventions of django. Moreover, to add to the reliability of the project, it is thoroughly tested using CI/CD with Travis-CI. The file structure is as follows:<br>

    .
    ├── main_app/                  # Django app that contains main info for web app
    │   ├── static/css/               # Contains the CSS files
    │   ├── templates/main_app/       # Contains HTML templates for the project
    │   ├── admin.py                  # Regulates the admin page for django
    │   ├── models.py                 # Contains models for the database
    │   ├── tests.py                  # Unit tests for the project
    │   ├── urls.py                   # Contains url routes
    │   └── views.py                  # All the python functions to execute server side processing
    ├── media/                     # Contains the media for the project
    ├── soteria/                   # Default app provided by django
    ├── manage.py                  
    ├── .gitignore                 
    ├── LICENSE
    ├── README.md
    └── requirements.txt

### Contributors

Aditya Goyal, Turja Chowdhury, Roan Numa, Ankitha 