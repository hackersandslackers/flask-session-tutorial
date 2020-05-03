# Flask-Session Tutorial

![Python](https://img.shields.io/badge/Python-v^3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v^1.1.1-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Login](https://img.shields.io/badge/Flask--Login-v0.5.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v2.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Session](https://img.shields.io/badge/Flask--Session-v0.3.1-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-v2.3.2-red.svg?longCache=true&style=flat-square&logo=flask&logoColor=white&colorA=4c566a&colorB=5e81ac)
![WTForms](https://img.shields.io/badge/WTForms-v2.2.1-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![PyMySQL](https://img.shields.io/badge/PyMySQL-v0.9.3-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a)
![Redis](https://img.shields.io/badge/Redis-v3.2.1-red.svg?longCache=true&style=flat-square&logo=redis&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/flask-session-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-session-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/flask-session-tutorial.svg?style=flat-square8&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-session-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/flask-session-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-session-tutorial/network)

![Flask Session Redis Tutorial](https://github.com/hackersandslackers/flask-session-tutorial/blob/master/application/static/dist/img/flask-session2@2x.jpg)

Source code for the accompanying tutorial found here: https://hackersandslackers.com/managing-user-session-variables-with-flask-sessions-and-redis/


## Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/hackersandslackers/flask-session-tutorial.git
$ cd flask-session-tutorial
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ flask run
```

**Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)**:

```shell
$ git clone https://github.com/hackersandslackers/flask-session-tutorial.git
$ cd flask-session-tutorial
$ pipenv shell
$ pipenv update
$ flask run
```

## Configuration

Configuration is handled by creating a **.env** file. This should contain the following variables (replace the values with your own):

```.env
SECRET_KEY="YOURSECRETKEY"
FLASK_ENV="production"
SESSION_REDIS="redis://:[PASSWORD]@[HOST]:[PORT]"
SQLALCHEMY_DATABASE_URI="mysql+pymysql://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE_NAME]"
SQLALCHEMY_TRACK_MODIFICATIONS=False
```
-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
