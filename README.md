# Soteria

[![Build Status](https://travis-ci.org/AdityaGoyal1999/SigmaHacks.svg?branch=master)](https://travis-ci.org/AdityaGoyal1999/SigmaHacks)

### 🦠 Information

The inspiration for this project comes from our shared desire to support the health care workers. Our primary objective through this platform is to provide an Airbnb alternative for the front line workers. Being in a high risk category, finding a place to temporarily stay to keep their families and community safe should not be another hassle for them. Secondly, this platform creates incentives for the landlords to have consistent renters. The healthcare workers are getting employed and paid, so they will definitely pay the rent. This creates a healthy supply and demand to be used in the practical atmosphere of this global pandemic.
In short, COVID-19 has created a marketplace for secluded housing. 

That is why we bring you 'Soteria'. Just like the name, Soteria, which signified the goddess of safety in the Greek mythology, we bring safety to medical workers. Not only does our web app protect medical workers but also to a substantial portion of the housing market from completely collapsing.


There were several different tools that were used to build this project. Our platform is a full stack web application that is through the use of Python framework Django. For the database, we used SQLite. Moreover, in regards to the style of the project, we used Materialize CSS to speed up the process. 

### 🚀 Running the app:

- Navigate the folder which contains requirements.txt in terminal
- Execute the following code inside the terminal
```
pip install -r requirements.txt
python manage.py runserver
```
- Go to the mentioned link in the terminal after executing these commands.

### 💻 Note for Developers

The web app is rigorously documented and follow all the conventions of django. Moreover, to add to the reliability of the project, it is thoroughly tested using Continuous Integration/CD with Travis-CI. The file structure is as follows:<br>

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

### 🗣 Contributors

This is a project under Sigma Hacks 2020.
Aditya Goyal, Turja Chowdhury, Roan Numa, Ankitha 