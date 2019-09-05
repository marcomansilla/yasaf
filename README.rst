Yet Another Shortener with Flask
================================

Motivation
----------

Just the need to learn, test, and explore.

What it does?
-------------

Just shortens links in 6 characters as most shorteners, nothing too fancy.

How does it work?
-----------------

 - Just clone the repo
 - pip3 install -r requirements.txt
 - python3 app.py
 - open the browser on http://localhost:5000

The app stores the links in a sqlite3 database managed by pyDAL, and with Flask would be the only deppendencies to make it work.
Should it do more?
------------------

Not sure, URL shortening and manging some statistics on earch link should be enough.

**It does not accepts an URL twice, checks if it is already stored and returns existing link**
