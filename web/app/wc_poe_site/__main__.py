# Get a reference to the Application class.
from web.core import Application


# This is our WSGI application instance.
app = Application("Hi.")


# If we're run as the "main script", serve our application over HTTP.
if __name__ == "__main__":
	app.serve('wsgiref');