from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Icons"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Desk Icons",
					"description": _("Desk Modules Icons"),
					"onboard": 1,
				}
			]
		}
	]
