# -*- coding: utf-8 -*-
# Copyright (c) 2021, Omar Alhori and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.config import desktop as frappe_desktop
from erpnext.config import desktop as erpnext_desktop
class DeskStyling(Document):
	pass

@frappe.whitelist()
def get_modules_data():
	modules = frappe_desktop.get_data()
	modules.extend(erpnext_desktop.get_data())
	return modules