ChatApp
=====================


Installing dependencies
-----------------------


Python dependencies
~~~~~~~~~~~~~~~~~~~

First create a new virtualenv for this project and then install all
the dependencies inside it as follows ::

    $ mkvirtualenv chatapp
    $ pip install -r requirements.txt


Environment variables
---------------------

Add the ``DATABASE_URL`` variable to the environment ::

    $ export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME

Replace the values USER, PASSWORD, HOST, PORT and NAME with your database
configuration.

Setup and populate the database
-------------------------------

Setting up database
~~~~~~~~~~~~~~~~~~~~~~~~

Create All the tables. ::

    $ python manage.py syncdb

Run the migrations. ::

    $ python manage.py migrate


Start the webapp
----------------

There are two servers we need to run.The first one is
a django server for dealing with normal requests.
For that run the following command ::

    $ python manage.py runserver

Alternative add the parameter '0.0.0.0:8000' to runserver to allow the
app to be accessed from any host.

This will start a development web server on port ``8000``.

Next is to start the websocket server. This can be done as ::

    $ python manage.py omnibusd



Now visit the URL http://127.0.0.1:8000 in a browser.

