
$(document).ready(function(){

    let url = window.location.origin + '/api/companies'
    let table = new BootstrapDataTable({
                        container:'#overview-table',
                        id:'table',
                        fields: {
                            'id_company': {title: 'Nr'},
                            'company_name': {title: 'Firma'},
                            'company_internal_alias': {title: 'Alias'},
                            'company_street' : {title: 'Strasse'},
                            'company_zipcode': {title: 'PLZ' },
                            'company_city' : {title: 'Stadt'},
                            'company_country': {title: 'Land'},
                            'fk_sys_rec_status': {path: 'fk_sys_rec_status.sys_rec_status', title: 'Status'},
                            'company_email': {title: 'Email'},
                            'is_customer': {title: 'Ist Kunde'},
                            'is_supplier': {title: 'Ist Lieferant'},
                            'is_subcontractor': {title: 'Ist Subunternehmer'}
                        },
                        pk_field: 'id_company',
                    })
    let filter_form = new BootstrapForm({
            container: '#form_filter_container',
            id: 'filter_form',
            validation:false,
            fields: {
                'id_company': {title: 'Nr', type: 'number', min:0, max:99999999},
                'company_name': {title: 'Firma', type:'text'},
                'company_internal_alias': {title: 'Alias' ,type:'text'},
                'company_street' : {title: 'Strasse' ,type:'text'},
                'company_zipcode': {title: 'PLZ' ,type:'text'},
                'company_city' : {title: 'Stadt',type:'text'},
                'company_country': {title: 'Land' ,type:'text'},
                'fk_sys_rec_status': {title: 'Status' ,type:'select', ajax_url:window.location.origin + '/api/sysrecstate', value_field:'id_sys_rec_status', description_field:'sys_rec_status'},
                'company_email': {title: 'Email' ,type:'email'},
                'is_customer': {title: 'Ist Kunde' ,type:'checkbox', options : [(0, 'Nein'), (1, 'Ja')]},
                'is_supplier': {title: 'Ist Lieferant' ,type:'checkbox', options : [(0, 'Nein'), (1, 'Ja')]},
                'is_subcontractor': {title: 'Ist Subunternehmer' ,type:'checkbox', options : [(0, 'Nein'), (1, 'Ja')]}
            }

    })
    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: url+'/',
            validation:true,
            fields: {
                'company_name': {title: 'Firma', type:'text', required:true},
                'company_internal_alias': {title: 'Alias' ,type:'text', required:true},
                'company_street' : {title: 'Strasse' ,type:'text', required:true},
                'company_zipcode': {title: 'PLZ' ,type:'text', required:true},
                'company_city' : {title: 'Stadt',type:'text', required:true},
                'company_country': {title: 'Land' ,type:'text', required:true},
                'fk_sys_rec_status': {title: 'Status' ,type:'select', ajax_url:window.location.origin + '/api/sysrecstate', value_field:'id_sys_rec_status', description_field:'sys_rec_status',  required:true},
                'company_email': {title: 'Email' ,type:'email', required:true},
                'is_customer': {title: 'Ist Kunde' ,type:'select', options : [(0, 'Nein'), (1, 'Ja')], required:true},
                'is_supplier': {title: 'Ist Lieferant' ,type:'select', options : [(0, 'Nein'), (1, 'Ja')], required:true},
                'is_subcontractor': {title: 'Ist Subunternehmer' ,type:'select', options : [(0, 'Nein'), (1, 'Ja')], required:true}
            }

    })
    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: url+'/',
            validation:true,
            fields: {
                'id_company': {title: 'Nr', type: 'number', min:0, max:99999999, required:true},
                'company_name': {title: 'Firma', type:'text', required:true},
                'company_internal_alias': {title: 'Alias' ,type:'text', required:true},
                'company_street' : {title: 'Strasse' ,type:'text', required:true},
                'company_zipcode': {title: 'PLZ' ,type:'text', required:true},
                'company_city' : {title: 'Stadt',type:'text', required:true},
                'company_country': {title: 'Land' ,type:'text', required:true},
                'fk_sys_rec_status': {title: 'Status' ,type:'select', ajax_url:window.location.origin + '/api/sysrecstate', value_field:'id_sys_rec_status', description_field:'sys_rec_status',  required:true},
                'company_email': {title: 'Email' ,type:'email', required:true},
                'is_customer': {title: 'Ist Kunde' ,type:'select', options : [(0, 'Nein'), (1, 'Ja')], required:true},
                'is_supplier': {title: 'Ist Lieferant' ,type:'select', options : [(0, 'Nein'), (1, 'Ja')], required:true},
                'is_subcontractor': {title: 'Ist Subunternehmer' ,type:'select', options : [(0, 'Nein'), (1, 'Ja')], required:true}
            }

    })
    $.ajax({
        url: url,
        success: function (result) {
            table.data = result
            table.build()
        }
    });

    filter_form.build();
    create_form.build();
    update_form.build();

    $( "#btn_filter" ).on( "click", function() {
      let query_params = $('#filter_form').serialize();
      console.log(url + '?' + query_params)
      $.ajax({
        url: url + '?' + query_params,
        success: function (result) {
            console.log(result);
            table.data = result;
            table.build();
        }
    });

    });

    $( "#btn_form_reset" ).on( "click", function() {
        $('#filter_form').trigger("reset");

    });

    $( "#btn_add" ).on( "click", function() {
        create_form.submit();
    });

    $( "#table tr" ).on( "dblclick", function() {
        let record_id =  $(this).attr('data-row-pk');

        $.ajax({
            url: url + '/' + record_id,
            success: function (result) {
                console.log(result);

                $.each(result, (key, value)=>{
                    console.log(key)
                    if (value === true){
                        value = 1;
                    } else if (value === false){
                        value = 0;
                    }
                    $('#update_form #'+ key).val(value);
                });

                $('#update_modal').modal('show');
            }
            })
    } );


    $( "#btn_save" ).on( "click", function() {
        let pk = $('#update_form #id_company').val()
        update_form.submit(pk);
    });



});
