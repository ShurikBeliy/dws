# Apologize
This project isn't ready yet. We will finish this project in a few months.

# Django Web Store (DWS)
Django Web Store is a very simple and clean but powerful project for your business.
Use this project to create web store for your own business.
In the DWS you can create categories for items and different filters for items.
We used Django3, Sass and TypeScript4 in our project and prepare styles and scripts that you can change easily for your future projects.
We decided not to use bootstrap and keep our project clean. Instead of bootstrap we are create simple styles using BEM approach.

# Install
Before installing this project you should install:
- Install Python: 3.9+
- Install Pip 20.2+
- Install postgresql 13.2+ (highly recommended)

To install DWS you need to do following steps:
- Create virtual environment for python (highly recommended)
- Install requirements from requirements.txt
- Add logs/ directory to base directory
- Add .env file into app directory and add settings e.g.:

SECRET_KEY=yoursecretkey

DATABASE_NAME=databsename

DATABASE_USER=databaseuser

DATABASE_PASS=databasepass

DATABASE_HOST=localhost

ALLOWED_HOST=yourhost

- Make migrations
- Start django server

Happy usage!

# Desctiption
core - here you can find main functions and classes that might be necessary everywhere in the project. We put there middleware and main views.

templates - we have a template in the root directory. That templates that we can use everywhere in the project. We also have templates in the apps, e.g. in the catalog app.

catalog - main app that contains views and templates for our catalog 

catalog/services - we put there main functions that work with logic. We decided that it's better to separate them because we can use them again in different parts of the project (DRY). Our models and views clean. We also can test them easily.

static/sass - we put there our SASS styles. They will be automatically converted to CSS
