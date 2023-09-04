from api.components import Companies, SysRecStates, Projects, TaskStates, Invoices, Units
from .components import input_field
from .components import select_field

fields = {
    'id_company': {
        'de': {'key': 'id_company','title':'Unternehmens ID',  'input': input_field('id_company', 'Unternehmens ID', type='number', placeholder="", min="0", max="999999999999", required=False)},
        'en':  {'key': 'id_company','title':'Company ID',  'input': input_field('id_company', 'Company ID', type='number', placeholder="", min="0", max="999999999999", required=False)},
        'dtype': 'str',
    },

    'company_name': {
        'de': {'key': 'company_name','title':'Firma',  'input': input_field('company_name', 'Firma', type='text', placeholder="", required=False)},
        'en': {'key': 'company_name','title':'Company',  'input': input_field('company_name', 'Company', type='text', placeholder="", required=False)},
        'dtype': 'str',
         },

    'company_internal_alias': {
        'de': {'key': 'company_internal_alias','title':'Alias',  'input': input_field('company_internal_alias', 'Alias', type='text', placeholder="", required=False)},
        'en': {'key': 'company_internal_alias','title':'Alias',  'input': input_field('company_internal_alias', 'Alias', type='text', placeholder="", required=False)},
        'dtype': 'str',
    },

    'company_street': {
        'de': {'key': 'company_street','title':'Strasse',  'input': input_field('company_street', 'Strasse', type='text', placeholder="", required=False)},
        'en': {'key': 'company_street','title':'Street',  'input': input_field('company_street', 'Street', type='text', placeholder="", required=False)},
        'dtype': 'str',
    },

    'company_zipcode' : {
        'de': {'key': 'company_zipcode','title':'PLZ',  'input': input_field('company_zipcode', 'PLZ', type='text', placeholder="", required=False)},
        'en': {'key': 'company_zipcode','title':'Postalcode',  'input': input_field('company_zipcode', 'Postalcode', type='text', placeholder="", required=False)},
        'dtype' : 'str',
    },

    'company_city': {
        'de': {'key': 'company_city','title':'Ort',  'input': input_field('company_city', 'Ort', type='text', placeholder="", required=False)},
        'en': {'key': 'company_city','title':'City',  'input': input_field('company_city', 'City', type='text', placeholder="", required=False)},
        'dtype': 'str',
    },

    'company_country': {
        'de': {'key': 'company_country','title':'Land',  'input': input_field('company_country', 'Land', type='text', placeholder="", required=False)},
        'en': {'key': 'company_country','title':'Country',  'input': input_field('company_country', 'Country', type='text', placeholder="", required=False)},
        'dtype': 'str',
        'widget': 'flag',
    },

    'fk_sys_rec_status': {
        'de': {'key': 'fk_sys_rec_status','title':'Land',  'input': select_field('fk_sys_rec_status', 'Status', null=True,options=SysRecStates.objects.values_list('id_sys_rec_status', 'sys_rec_status'), required=False)},
        'en': {'key': 'fk_sys_rec_status','title':'Land',  'input': select_field('fk_sys_rec_status', 'Status', null=True,options=SysRecStates.objects.values_list('id_sys_rec_status', 'sys_rec_status'), required=False)},
        'dtype': 'str',

    },
    'company_email': {
        'de': {'key': 'company_email','title': 'Email', 'input': input_field('company_email', 'Email', type='email', placeholder="test@example.com", required=False)},
        'en': {'key': 'company_email','title': 'Email', 'input': input_field('company_email', 'Email', type='email', placeholder="", required=False)},
        'dtype': 'str',

    },
    'is_customer': {
        'de': {'key': 'is_customer','title':'Kundenstatus',  'input': select_field('is_customer', 'Kudenstatus',  null=True,options=[[0, 'Nein'], [1, 'Ja']], required=False)},
        'en': {'key': 'is_customer','title':'Customer',  'input': select_field('is_customer', 'Customer',  null=True,options=[[0, 'No'], [1, 'Yes']], required=False)},
        'dtype': 'str',

    },

    'is_supplier': {
        'de': {'key': 'is_supplier','title': 'Lieferant', 'input': select_field('is_supplier', 'Lieferant', null=True, options=[[0, 'Nein'], [1, 'Ja']], required=False)},
        'en': {'key': 'is_supplier','title': 'Supplier', 'input': select_field('is_supplier', 'Supplier',  null=True,options=[[0, 'No'], [1, 'Yes']], required=False)},
        'dtype': 'str',

    },

    'is_subcontractor': {
        'de': {'key': 'is_subcontractor','title': 'Subunternehmenr', 'input': select_field('is_subcontractor', 'Subunternehmenr', null=True, options=[[0, 'Nein'], [1, 'Ja']], required=False)},
        'en': {'key': 'is_subcontractor','title': 'Subcontractor ','input': select_field('is_subcontractor', 'Subcontractor',  null=True,options=[[0, 'No'], [1, 'Yes']], required=False)},
        'dtype': 'str',

    },

    'id_project': {
        'de': {'key': 'id_project','titlid_projecte':'Projekt Nr',  'input': input_field('id_project', 'Projekt Nr', type='number', placeholder="", min="0", max="999999999999", required=False)},
        'en':  {'key': 'id_project','title':'Project ID',  'input': input_field('id_project', 'Project ID', type='number', placeholder="", min="0", max="999999999999", required=False)},
        'dtype': 'int',

    },
    'project_name': {
        'de': {'key': 'project_name','title': 'Projekt','input': input_field('project_name', 'Projekt', type='text', placeholder="", required=False)},
        'en': {'key': 'project_name','title': 'Project','input': input_field('project_name', 'Project', type='text', placeholder="", required=False)},
        'dtype': 'str',
    },

    'fk_customer': {
        'de': {'key': 'fk_customer','title': 'Kunde', 'input': select_field('fk_customer', 'Kunde', null=True, options=Companies.objects.filter(is_customer=True).values_list('id_company', 'company_name'), required=False)},
        'en': {'key': 'fk_customer','title': 'Customer ', 'input': select_field('fk_customer', 'Customer', null=True, options=Companies.objects.filter(is_customer=True).values_list('id_company', 'company_name'),required=False)},
        'dtype': 'str',

    },
    'planned_start_date': {
        'de': {'key': 'planned_start_date','title': 'Plan Start Datum', 'input': input_field('planned_start_date', 'Plan Start Datum', type='date', placeholder="", required=False)},
        'en': {'key': 'planned_start_date','title': 'Plan Start Date', 'input': input_field('planned_start_date', 'Plan Start Date', type='date', placeholder="", required=False)},
        'dtype': 'str',
    },
    'planned_end_date': {
        'de': {'key': 'planned_end_date','title': 'Plan End Datum', 'input': input_field('planned_end_date', 'Plan End Datum', type='date', placeholder="", required=False)},
        'en': {'key': 'planned_end_date','title': 'Plan End Date', 'input': input_field('planned_end_date', 'Plan End Date', type='date', placeholder="", required=False)},
        'dtype': 'str',
    },
    'effective_start_date': {
        'de': {'key': 'effective_start_date','title': 'Start Datum','input': input_field('effective_start_date', 'Start Datum', type='date', placeholder="", required=False)},
        'en': {'key': 'effective_start_date','title': 'Start Date','input': input_field('effective_start_date', 'Start Date', type='date', placeholder="", required=False)},
        'dtype': 'str',
    },
    'effective_end_date': {
        'de': {'key': 'effective_end_date','title': 'End Datum','input': input_field('effective_end_date', 'End Datum', type='date', placeholder="", required=False)},
        'en': {'key': 'effective_end_date','title': 'End Date','input': input_field('effective_end_date', 'End Date', type='date', placeholder="", required=False)},
        'dtype': 'str',
    },

    'id_task': {
        'de': {'key': 'id_task', 'title': 'Auftrag Nr.', 'input': input_field('id_task', 'Auftrag Nr', type='number', placeholder="", min="0", max="999999999999", required=False)},
        'en': {'key': 'id_task', 'title': 'Task ID', 'input': input_field('id_project', 'Project ID', type='number', placeholder="", min="0", max="999999999999", required=False)},
        'dtype': 'int',

    },

    'fk_project': {
        'de': {'key': 'fk_project', 'title': 'Projekt', 'input': select_field('fk_project', 'Projekt', null=True, options=Projects.objects.values_list('id_project', 'project_name'),required=False)},
        'en': {'key': 'fk_project', 'title': 'Project ', 'input': select_field('fk_project', 'Project', null=True, options=Projects.objects.values_list('id_project', 'project_name'),required=False)},
        'dtype': 'str',

    },

    'fk_task_state': {
        'de': {'key': 'fk_stask_state', 'title': 'Auftragsstatus', 'input': select_field('fk_task_state', 'Auftragsstatus', null=False, options=TaskStates.objects.values_list('id_task_state', 'task_state'), required=False)},
        'en': {'key': 'fk_stask_state', 'title': 'Task State ', 'input': select_field('fk_stask_state', 'Task State', null=False,options=TaskStates.objects.values_list('id_task_state', 'task_state'),required=False)},
        'dtype': 'str',

    },

    'timestamp_from': {
        'de': {'key': 'timestamp_from', 'title': 'Beginn', 'input': input_field('timestamp_from', 'Beginn', type='datetime-local', placeholder="", required=False)},
        'en': {'key': 'timestamp_from', 'title': 'Start','input': input_field('timestamp_from', 'Start', type='datetime-local', placeholder="", required=False)},
        'dtype': 'str',
    },

    'timestamp_to': {
        'de': {'key': 'timestamp_to', 'title': 'Ende','input': input_field('timestamp_to', 'Ende', type='datetime-local', placeholder="", required=False)},
        'en': {'key': 'timestamp_to', 'title': 'End','input': input_field('timestamp_to', 'End', type='datetime-local', placeholder="", required=False)},
        'dtype': 'str',
    },
    'amount': {
        'de': {'key': 'amount', 'title': 'Menge', 'input': input_field('amount', 'Menge', type='number', placeholder="", required=False)},
        'en': {'key': 'amount', 'title': 'Amount','input': input_field('amount', 'Amount', type='number', placeholder="", required=False)},
        'dtype': 'str',
    },
    'price': {
        'de': {'key': 'price', 'title': 'Stückpreis','input': input_field('price', 'Preis/Stk.', type='number', placeholder="", required=False)},
        'en': {'key': 'price', 'title': 'Unit Price','input': input_field('price', 'Unit Price', type='number', placeholder="", required=False)},
        'dtype': 'str',
    },
    'task_description': {
        'de': {'key': 'task_description', 'title': 'Beschreibung', 'input': input_field('task_description', 'Beschreibung', type='text', placeholder="", required=False)},
        'en': {'key': 'task_description', 'title': 'Description','input': input_field('task_description', 'Description', type='text', placeholder="", required=False)},
        'dtype': 'str',
    },
    'fk_invoice': {
        'de': {'key': 'fk_invoice', 'title': 'Rechnung', 'input': select_field('fk_invoice', 'Rechnung', null=True,options=Invoices.objects.values_list( 'id_invoice', 'id_invoice'),required=False)},
        'en': {'key': 'fk_invoice', 'title': 'Invoice ', 'input': select_field('fk_invoice', 'Invoice', null=True,options=Invoices.objects.values_list('id_invoice', 'id_invoice'),required=False)},
        'dtype': 'str',
    },
    'fk_unit': {
        'de': {'key': 'fk_invoice', 'title': 'Einheit', 'input': select_field('fk_unit', 'Einheit', null=True,options=Units.objects.values_list('id_unit', 'unit'),required=False)},
        'en': {'key': 'fk_invoice', 'title': 'Unit ', 'input': select_field('fk_unit', 'Unit', null=True,options=Units.objects.values_list('id_unit', 'unit'),required=False)},
        'dtype': 'str',
    },
    'internal_info': {
        'de': {'key': 'internal_info', 'title': 'Interne Information','input': input_field('internal_info', 'Interne Information', type='text', placeholder="", required=False)},
        'en': {'key': 'internal_info', 'title': 'Internal information','input': input_field('internal_info', 'Internal information', type='text', placeholder="", required=False)},
        'dtype': 'str',
    },
    'customer_reference': {
        'de': {'key': 'customer_reference', 'title': 'Referenz','input': input_field('customer_reference', 'Referenz', type='text', placeholder="", required=False)},
        'en': {'key': 'customer_reference', 'title': 'Reference','input': input_field('customer_reference', 'Reference', type='text', placeholder="",required=False)},
        'dtype': 'str',
    },
    'fk_subcontractor': {
        'de': {'key': 'fk_subcontractor', 'title': 'Subunternehmer', 'input': select_field('fk_subcontractor', 'Subunternehmer', null=True, options=Companies.objects.filter( is_subcontractor=True).values_list('id_company', 'company_name'),required=False)},
        'en': {'key': 'fk_subcontractor', 'title': 'Subcontractor ', 'input': select_field('fk_subcontractor', 'Subcontractor', null=True,options=Companies.objects.filter(is_subcontractor=True).values_list('id_company', 'company_name'),required=False)},
        'dtype': 'str',

    },


}









pages = {
    '/companies' : {
        'title': { 'en' : 'Companies', 'de': 'Unternehmen'},
        'pk': 'id_company',
        'template' : 'frontend/pages/overview_table.html',
        'detail_template' : 'frontend/pages/organization_profile.html',
        'url' : 'companies',
        'js_path' : 'static/js/pages/organizations.js',
        'fields': {
            'form': ['id_company','company_name', 'company_internal_alias',  'company_street', 'company_zipcode', 'company_city', 'company_country', 'fk_sys_rec_status', 'company_email', 'is_customer', 'is_supplier', 'is_subcontractor'],
            'table' : ['id_company','company_name', 'company_internal_alias',  'company_street', 'company_zipcode'],
        },

    },

    '/projects' : {
        'url': 'projects',
        'title': { 'en' : 'Projects', 'de': 'Projekte'},
        'pk': 'id_project',
        'template' : 'frontend/pages/overview_table.html',
        'detail_template': 'frontend/pages/organization_profile.html',
        'fields': {
            'form':['id_project', 'project_name', 'fk_customer', 'planned_start_date', 'planned_end_date', 'effective_start_date', 'effective_end_date'],
            'table': ['id_project', 'project_name',  'fk_customer', 'planned_start_date', 'planned_end_date', 'effective_start_date', 'effective_end_date']
        }
    },

    '/tasks': {
        'url': 'project/tasks',
        'title': {'en': 'Aufträge', 'de': 'Tasks'},
        'pk': 'id_task',
        'template': 'frontend/pages/overview_table.html',
        'detail_template': 'frontend/pages/organization_profile.html',
        'fields': {
            'form': ['id_task', 'fk_project', 'timestamp_from', 'timestamp_to', 'amount', 'price', 'task_description', 'fk_invoice', 'fk_subcontractor'],
            'table': ['id_task', 'fk_project', 'timestamp_from', 'timestamp_to', 'amount', 'price', 'task_description', 'fk_unit', 'internal_info']
        }
    },
    '/sales': {
        'url': 'project/sales',
        'title': {'en': 'Sales', 'de': 'Verkäufe'},
        'pk': 'id_sale',
        'template': 'frontend/pages/overview_table.html',
        'detail_template': 'frontend/pages/organization_profile.html',
        'fields': {
            'form': [],
            'table': []
        }
    },

    '/employees': {
        'url': 'employees',
        'title': {'en': 'Employees', 'de': 'Mitarbeiter'},
        'pk': 'id_employee',
        'template': 'frontend/pages/overview_table.html',
        'detail_template': 'frontend/pages/resource_profile.html',
        'fields': {
            'form': [],
            'table': []
        }
    },

    '/assets': {
        'url': 'assets',
        'title': {'en': 'Assets', 'de': 'Maschinen / Gegenstände'},
        'pk': 'id_asset',
        'template': 'frontend/pages/overview_table.html',
        'detail_template': 'frontend/pages/resource_profile.html',
        'fields': {
            'form': [],
            'table': []
        }
    },

    '/invoices': {
        'url': 'invoices',
        'title': {'en': 'Invoices', 'de': 'Rechnungen'},
        'pk': 'id_invoice',
        'template': 'frontend/pages/overview_table.html',
        'detail_template': 'frontend/pages/organization_profile.html',
        'fields': {
            'form': [],
            'table': []
        }
    },
}