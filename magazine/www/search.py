# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
sitemap = 1
no_cache = 1

def get_context(context):
	
	message_context = frappe._dict()

	category = frappe.db.get_all(doctype="Blog Category",fields=["*"])
	featured = frappe.db.get_all(doctype="Blog Post",fields=["route","title","meta_image","blog_intro","published_on","blogger","blog_category"],filters=[["published","=",1],["meta_image","!=","" ]], order_by="modified desc", page_length=6)
	posts = frappe.db.get_all(doctype="Blog Post",fields=["route","title","meta_image","blog_intro","published_on","blogger","blog_category"],
	filters=[["published","=",1],["meta_image","!=","" ]],
	or_filters=[

	["title","like","%"+frappe.local.form_dict.query+"%" ],["blog_intro","like","%"+frappe.local.form_dict.query+"%" ]
	]
	, order_by="modified desc")

	

	context.pregunta = frappe.local.form_dict.query
	context.category = category
	context.featured = featured
	context.posts = posts