from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Theme Customization"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Desk Icons",
					"description": _("Desk Modules Icons"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Desk Module",
					"description": _("Desk Modules"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Theme Settings",
					"onboard": 1,
				}
			]
		}
	]
