class SitePage:

	__dispatch__ = 'resource'

	def __init__(self, context, site, page):
		self._ctx = context # The "request context" we were constructed for.
		self._site = site # The parent (containing) Site instance.
		self._page = page # The data associated with our current site page

	def get(self):
		return self._page

	def post(self, content):
		"""Update the in-database content for the current page."""
		return {'ok': True} # For now, we pretend

	def delete(self):
		"""Delete this page from the site"""
		return {'ok': True} # For now, we only pretend.