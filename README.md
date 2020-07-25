# Soteria

Soteria is a Full stack django web application.

### 🚀 Running the app:

- Navigate the folder which contains requirements.txt in terminal
- Execute the following code inside the terminal
```
pip install -r requirements.txt
python manage.py runserver
```
- Go to the mentioned link in the terminal after executing these commands.

### 💻 Note for Developers

The web app is rigorously documented and follow all the conventions of django. Moreover, to add to the reliability of the project, it is thoroughly tested using CI/CD with Travis-CI. The file structure is as follows:<br>

    .
    ├── main_app/                  # Django app that contains main info for web app
    │   ├── static/css/               
    │   ├── templates/main_app/       
    │   ├── admin.py                 
    │   ├── models.py                 # Contains models for the database
    │   ├── tests.py                  # Unit tests for the project
    │   ├── urls.py                   # Contains url routes
    │   └── views.py                  # All the python functions to execute server side processing
    ├── media/                     
    ├── soteria/                   # Default app provided by django
    ├── manage.py                  
    ├── .gitignore                 
    ├── LICENSE
    ├── README.md
    └── requirements.txt

### 🤝 Contributors

This is a project under Sigma Hacks 2020.
Aditya Goyal, Turja Chowdhury, Roan Numa, Ankitha 