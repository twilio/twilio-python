==============================
Deploying to Google App Engine
==============================

Adding the `twilio-python` library to a Google App Engine project is a little
tricky. Let's walk you through one way to do it.


Laying Out Your Project
-----------------------

The key is to lay out your project in a way that makes sense. 

#.  Create a project folder called ``twilio-demo``. You can name the
    folder anything you like, but for the rest of this tutorial, we'll assume
    it's named ``twilio-demo``. At the command line, add a `virtualenv
    <http://www.virtualenv.org/en/latest/>`_ inside of that folder, by running:

    .. code-block:: bash

        mkdir twilio-demo       # Creates a new twilio-demo folder
        cd twilio-demo          # Move into that folder
        virtualenv .            # Create a new virtual environment

    You should now have a directory structure that looks like this:

    .. code-block:: bash

        twilio-demo
        ├── bin
        ├── include
        └── lib

    We'll get to the Google App Engine part in a few steps.

#.  Now let's install the ``twilio-python`` library in our Virtualenv. If your
    current working directory is ``twilio-demo``, we want to source the
    ``activate`` file in the ``bin`` folder, then install the library with
    ``pip``.

    .. code-block:: bash

        source bin/activate     # Activate our virtual environment
        pip install twilio      # Install the twilio-python library

#.  Now let's add a new folder called ``src``. This is the folder that contains
    your ``app.yaml`` and your other Google App Engine files. You can add this 
    at the command line. If your current directory is ``twilio-demo``:

    .. code-block:: bash

        mkdir src

#.  Create a basic ``app.yaml`` file in your ``src`` directory, per the
    instructions Google App Engine provides. Your folder structure should now
    look something like this:

    .. code-block:: bash

        twilio-demo
        ├── bin
        │   ├── activate
        │   └── ... about 20 files
        ├── include
        │   └── python2.7 -> /path/to/system/python-2.7
        ├── lib
        │   └── python2.7       # This folder contains a bunch of files
        └── src
            ├── app.yaml
            └── helloworld.py

#. Link the twilio-python library into your ``src`` directory. We are going
   to use a symbolic link. Google will pick this up and import the library into
   the correct place. In the terminal, run these three commands from the ``src``
   directory inside ``twilio-demo``:

    .. code-block:: bash

        ln -s ../lib/python2.7/site-packages/twilio .
        ln -s ../lib/python2.7/site-packages/httplib2 .
        ln -s ../lib/python2.7/site-packages/six.py .

    This should create a symbolic link inside the src directory to the
    ``twilio-python`` module. You can test the link as follows. Inside the
    ``twilio-demo/src`` folder, create a file called ``helloworld.py`` and put
    this inside it:

    .. code-block:: python

        import webapp2
        import twilio

        class MainPage(webapp2.RequestHandler):
          def get(self):
              self.response.headers['Content-Type'] = 'text/plain'
              self.response.write("The twilio version is " + twilio.__version__)

        app = webapp2.WSGIApplication([('/', MainPage)],
                                      debug=True)

#.  Finally, configure your app in Google App Engine and deploy it. Here are
    the settings you want in Google App Engine - Note the folder path ends with
    ``twilio-demo/src``.

    .. image:: https://www.evernote.com/shard/s265/sh/1b9407b0-c89b-464d-b352-dbf8fc7a7f41/f536b8e79747f43220fc12e0e0026ee2/res/5b2f83af-8a7f-451f-afba-db092c55aa44/skitch.png

    Once App Engine is running locally, in your browser, you should be able to
    navigate to ``http://localhost`` + the provided Port and view the twilio
    library version number, as well as deploy your app to Google. Once you have
    this set up, adding more complicated actions using the ``twilio`` library
    should be a snap.

    Hope that helps! If you have questions, we're always listening at
    `help@twilio.com <mailto:help@twilio.com>`_.
