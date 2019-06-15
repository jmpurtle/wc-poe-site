"""Web application initial dispatch point, or "site root"."""

# HTTP status code exception for "302 Found" redirection.
from webob.exc import HTTPFound

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
		return {'name': name} # Pretending for now

	def get(self):
		"""Called to handle direct requests to the web root itself."""

		return HTTPFound(location=str(self._ctx.path.current / 'Game')) # Issue the redirect.
