
base = {



}

pages = {
    'comapanies' : {
        'url': 'company',
        'title': { 'en' : 'Companies', 'de': 'Unternehmen'},
        'pk': 'id_company',
        'fields': {
            'id_company' : {
                'de': 'Unternehmens ID', 'en' : 'Company ID', 'dtype': 'str', 'input': '<input type="number" class="form-control" id="id_company_field">'
            },
            'company_name' :
                {'de' : 'Firma', 'en' : 'Company Name', 'dtype' : 'str', 'input': '<input type="text" class="form-control" id="company_name">'
                 },
            'company_internal_alias' : {
                'de' : 'Alias','en' : 'Alias','dtype': 'str', 'input': '<input type="text" class="form-control" id="company_internal_alias">'
            },
            'company_street' : {'de': 'Strasse','en': 'Street','dtype': 'str', 'input': '<input type="text" class="form-control" id="company_street">'},
            'company_zipcode' : {'de': 'PLZ','en' : 'Postalcode','dtype' : 'str', 'input': '<input type="text" class="form-control" id="company_zipcode">'},
            'company_city': {'de' : 'Ort','en' : 'city','dtype' : 'str','input': '<input type="text" class="form-control" id="company_city">'},
            'company_country' : {'de': 'Land', 'en': 'Country', 'dtype' : 'str', 'widget' : 'flag', 'input': '<input type="text" class="form-control" id="company_country">'},
            'fk_sys_rec_status' : {'de' : 'Status', 'en': 'State', 'dtype' : 'str', 'input': '<input type="text" class="form-control" id="fk_sys_rec_status">'},
        }
    },

    'projects' : {
        'url': 'projects',
        'title': { 'en' : 'Projects', 'de': 'Projekte'},
        'pk': 'id_project',
        'fields': {
            'id_project' : {'de': 'Projekt ID', 'en' : 'Project ID', 'dtype': 'int','input': '<input type="number" class="form-control" id="id_project">'},
            'project_name' : {'de' : 'Projekt Name', 'en' : 'Project Name', 'dtype' : 'str', 'input': '<input type="text" class="form-control" id="project_name">'},
            'planned_start_date' : {'de' : 'Geplantes Start Datum','en' : 'Planned Start Date','dtype': 'date', 'input': '<input type="date" class="form-control" id="planned_start_date">'},
            'planned_end_date' : {'de': 'Geplantes End Datum','en': 'Planned End Date','dtype': 'date', 'input': '<input type="date" class="form-control" id="planned_end_date">'},
            'effectiv_start_date' : {'de': 'Effektives Start Datum','en' : 'Effective Start date','dtype' : 'date', 'input': '<input type="date" class="form-control" id="effectiv_start_date">'},
            'effective_end_date': {'de' : 'Effektives End Datum','en' : 'Effective End Date','dtype' : 'date', 'input': '<input type="date" class="form-control" id="effective_end_date">'},
            'fk_customer' : {'de': 'Kunde', 'en': 'Customer', 'dtype' : 'int'},
        }
    },


}