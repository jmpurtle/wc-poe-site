# encoding: cinje

: from cinje.std.html import page

:def render context, sitepage, page
: using page page['_id']
: classes = {'SitePage'}

: if not page['content']
	: classes.add('placeholder')
: end

<main&{class_=classes}>
	#{page['content'] or "<i>No content.</i>"}
</main>
