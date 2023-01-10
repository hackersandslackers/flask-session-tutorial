# Flask-Session Tutorial

![Python](https://img.shields.io/badge/Python-v^3.9-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v^2.2.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Login](https://img.shields.io/badge/Flask--Login-v0.6.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v2.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Session](https://img.shields.io/badge/Flask--Session-v0.4.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-v2.5.1-red.svg?longCache=true&style=flat-square&logo=flask&logoColor=white&colorA=4c566a&colorB=5e81ac)
![WTForms](https://img.shields.io/badge/WTForms-v2.2.1-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![PyMySQL](https://img.shields.io/badge/PyMySQL-v1.0.2-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a)
![Redis](https://img.shields.io/badge/Redis-v4.2.2-red.svg?longCache=true&style=flat-square&logo=redis&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/flask-session-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-session-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/flask-session-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-session-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/flask-session-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-session-tutorial/network)

![Flask Session Redis Tutorial](https://github.com/hackersandslackers/flask-session-tutorial/blob/master/.github/flask-session2@2x.jpg?raw=true)

**Tutorial**: https://hackersandslackers.com/managing-user-session-variables-with-flask-sessions-and-redis/

## Getting Started

Get set up locally in two steps:

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application; should be `wsgi.py`.
* `FLASK_DEBUG`: Toggle debug mode on (`True`) or off (`False`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database.
* `SESSION_REDIS`: Connection URI of a Redis instance.
* `LESS_BIN` *(optional for static assets)*: Path to your local LESS installation via `which lessc`.
* `ASSETS_DEBUG` *(optional)*: Debug asset creation and bundling in `development`.
* `LESS_RUN_IN_DEBUG` *(optional)*: Debug LESS while in `development`.
* `COMPRESSOR_DEBUG` *(optional)*: Debug asset compression while in `development`.

*Remember never to commit secrets saved in .env files to Github.*

### Installation

Get up and running with `make deploy`:

```shell
git clone https://github.com/hackersandslackers/flask-session-tutorial.git
cd flask-session-tutorial
make deploy
```

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.