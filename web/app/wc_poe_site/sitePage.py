class SitePage:

	__dispatch__ = 'resource'

	def __init__(self, context, site, page):
		self._ctx = context # The "request context" we were constructed for.
		self._site = site # The parent (containing) Site instance.
		self._page = page # The data associated with our current site page

	def get(self):
		return "I'm a site page named " + self._page['name'];
		