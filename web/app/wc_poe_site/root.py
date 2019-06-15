"""Web application initial dispatch point, or "site root"."""
from datetime import datetime # Python's standard date + time object.

# HTTP status code exception for "302 Found" redirection.
from webob.exc import HTTPFound

# MongoDB exceptions that may be raised when manipulating data.
from pymongo.errors import DuplicateKeyError

# Get a reference to our SitePage resource class.
from .sitePage import SitePage

class Site:
	"""Main site."""

	__dispatch__ = 'resource' # The site is a collection of pages, so use resource dispatch
	__resource__ = SitePage # Declare the type of resource we contain
	
	def __init__(self, context, collection=None, record=None):
		"""Executed when the root of the site (or children) are accessed, on each request."""
		self._ctx = context # Store the "request context" for later use.

	def __getitem__(self, name):
		data = self._ctx.db.sitepages.find_one({'_id': name})

		if not data: # If no record was found, populate some default data.
			data = {
				'_id': name,
				'content': None,
				'modified': None,
			}

		return data

	def get(self):
		"""Called to handle direct requests to the web root itself."""

		return HTTPFound(location=str(self._ctx.path.current / 'Game')) # Issue the redirect.

	def post(self, name, content):
		try:
			result = self._ctx.db.sitepages.insert_one({
				'_id': name,
				'content': content,
				'modified': datetime.utcnow(),
			})

		except DuplicateKeyError:
			return {
				'ok': False,
				'reason': 'duplicate',
				'message': "A page with that name already exists.",
				'name': name,
			}

		# All is well, so we inform the client.
		return {
			'ok': True,
			'acknowledged': result.acknowledged,
			'name': result.inserted_id
		}
		