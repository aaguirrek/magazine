# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
sitemap = 1
no_cache = 1
def get_context(context):
	category = frappe.db.get_all(doctype="Blog Category",fields=["*"])
	post = frappe.db.get_all(doctype="Blog Post",fields=["*"],filters=[["published","=",1],["meta_image","!=","" ]])
	context.category = category
	context.post = post