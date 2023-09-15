# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
sitemap = 1
#no_cache = 1

def get_context(context):
	category = frappe.db.get_all(doctype="Blog Category",fields=["*"])
	featured = frappe.db.get_all(doctype="Blog Post",fields=["route","title","meta_image","blog_intro","published_on","blogger","blog_category"],filters=[["published","=",1],["meta_image","!=","" ]], limit=6)
	restaurantes = frappe.db.get_all(doctype="Negocio",fields=["*"],filters=[["categoria","=","Restaurante" ]], order_by="modified desc", page_length=6)
	context.category = category
	context.featured = featured
	context.restaurantes = restaurantes