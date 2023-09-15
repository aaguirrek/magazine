# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
sitemap = 1
no_cache = 1

def get_context(context):
	name = frappe.form_dict.name
	category = frappe.db.get_all(doctype="Blog Category",fields=["*"])
	post = frappe.db.get_all(doctype="Blog Post",fields=["*"],filters=[["name","=",name ]])
	blogger = frappe.db.get_all(doctype="Blogger",fields=["*"],filters=[["name","=",post[0].blogger ]])
	featured = frappe.db.get_all(doctype="Blog Post",fields=["route","title","meta_image","blog_intro","published_on","blogger","blog_category"],filters=[["published","=",1],["meta_image","!=","" ]], limit=6)
	restaurantes = frappe.db.get_all(doctype="Negocio",fields=["*"],filters=[["categoria","=","Restaurante" ]], order_by="modified desc", page_length=6)
	context.category = category
	context.post = post[0]
	context.blogger = blogger[0]
	context.featured = featured
	context.restaurantes = restaurantes