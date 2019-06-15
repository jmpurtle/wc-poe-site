# Get a reference to the Application class.
from web.core import Application

# Get references to web framework extensions.
from web.ext.annotation import AnnotationExtension
from web.ext.debug import DebugExtension
from web.ext.serialize import SerializationExtension
from web.ext.db import DBExtension

# Get a reference to our database connection adapter.
from web.db.mongo import MongoDBConnection

# Get a reference to our GameAdvert root object.
from web.app.wc_poe_site.root import Site

# This is our WSGI application instance.
app = Application(Site, extensions=[
	AnnotationExtension(),
	DebugExtension(),
	SerializationExtension(),
	DBExtension(MongoDBConnection("mongodb://localhost/test"))
	])


# If we're run as the "main script", serve our application over HTTP.
if __name__ == "__main__":
	app.serve('wsgiref');