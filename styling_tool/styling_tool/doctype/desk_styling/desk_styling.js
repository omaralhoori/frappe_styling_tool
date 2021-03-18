// Copyright (c) 2021, Omar Alhori and contributors
// For license information, please see license.txt

frappe.ui.form.on('Desk Styling', {
	onload: function(frm) {
		frappe.call({
			method: 'styling_tool.styling_tool.doctype.desk_styling.desk_styling.get_modules_data',
			callback: function(r) {
				console.log(r.message)
				var options = [];
				(r.message || []).forEach(function(row){   // start a loop over all options in the response, or in a empty list; 
				options.push({'value': row.module_name, 'label': row.label}) // makes a option entry 'value' and 'label'
				});
				console.log(frm.fields_dict.desk_module.df.options)
				frm.fields_dict.desk_module.df.options = options;
			}
		})
	}
});
