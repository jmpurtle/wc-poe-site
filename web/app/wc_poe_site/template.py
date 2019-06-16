# encoding: cinje

: from cinje.std.html import page

: def render context, sitepage, pageData
: using page pageData['_id']
: classes = {'SitePage'}

: if not pageData['content']
	: classes.add('placeholder')
: end

<main&{class_=classes}>
	#{pageData['content'] or "<i>No content.</i>"}
</main>
