# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
sitemap = 1
no_cache = 1
def get_context(context):
	category = frappe.db.get_all(doctype="Blog Category",fields=["*"])
	featured = frappe.db.get_all(doctype="Blog Post",fields=["route","title","meta_image","blog_intro","published_on","blogger","blog_category"],filters=[["published","=",1],["meta_image","!=","" ]], order_by="modified desc", page_length=6)
	posts = frappe.db.get_all(doctype="Blog Post",fields=["route","title","meta_image","blog_intro","published_on","blogger","blog_category"],filters=[["published","=",1],["meta_image","!=","" ]], order_by="modified desc", start=6,page_length=9)
	colca = frappe.db.get_all(doctype="Blog Post",fields=["route","title","meta_image","blog_intro","published_on","blogger","blog_category"],filters=[["published","=",1],["meta_image","!=","" ]], order_by="modified desc", page_length=6)
	restaurantes = frappe.db.get_all(doctype="Negocio",fields=["*"],filters=[["categoria","=","Restaurante" ]], order_by="modified desc", page_length=6)
	eleccion_del_editor = frappe.db.get_all(doctype="Blog Post",fields=["route","title","meta_image","blog_intro","published_on","blogger","blog_category"],filters=[["published","=",1],["eleccion_del_editor","=",1 ]], order_by="modified desc", page_length=9)
	
	context.category = category
	context.featured = featured
	context.colca = colca
	context.restaurantes = restaurantes
	context.eleccion_del_editor = eleccion_del_editor
	context.posts = posts