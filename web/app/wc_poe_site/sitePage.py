from .template import render

class SitePage:

	__dispatch__ = 'resource'

	def __init__(self, context, site, page):
		self._ctx = context # The "request context" we were constructed for.
		self._site = site # The parent (containing) Site instance.
		self._page = page # The data associated with our current site page

	def get(self):
		"""Retrieve the page data or render an HTML page."""

		candidates = ['text/html'] + list(self._ctx.serialize)
		match = self._ctx.request.accept.best_match(candidates, default_match='text/html')

		if match == 'text/html':
			return render(self._ctx, self, self._page)

		return self._page

	def post(self, content):
		"""Update the in-database content for the current page.
		This will create the page if one by this name doesn't already exist.
		"""

		result = self._ctx.db.sitepages.update_one(
			{'_id': self._page['_id']}, # A query identifying the document to update.
			{ # The following are the MongoDB update operations to apply to the document.
				'$set': { # Update the page content.
					'content': content,
				},
				'$currentDate': { # Also update the last-modified time.
					'modified': True,
				}
			}
		)

		if not result.matched_count: # Nothing was updated... so let's create instead.
			return self._site.post(self._page['_id'], content) # Internally POST

		return {
			'ok': True,
			'acknowledged': result.acknowledged,
			'name': self._page['_id']
		}

	def delete(self):
		"""Delete this page from the site"""

		result = self._ctx.db.sitepages.delete_one({'_id': self._page['_id']})

		if not result.deleted_count: # Nothing was deleted, page likely did not exist.
			return {
				'ok': False,
				'reason': 'missing',
				'message': 'Cannot delete something that does not exist.',
				'name': self._page['_id'],
			}

		return {
			'ok': True,
			'acknowledged': result.acknowledged,
			'name': self._page['_id'],
		}
