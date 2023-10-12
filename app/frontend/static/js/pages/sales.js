

jQuery.fn.setUp = function(page_config, fields) {
    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');


    // Table setup with field form config file
    let table_fields = {};

    $.each(page_config['table_fields'], (key,value)=>{
       table_fields[value] = fields[value];
    })

    let table = new BootstrapDataTable({
                        container:'#overview-table',
                        id: page_config['table_id'],
                        fields: table_fields,
                        ajax_url: page_config['ajax_url'],
                        pk_field: page_config['pk'],
                        language: lang_cookie,
                    })
    table.build();

    // filter form instance

    let filter_form_fields = {};

    $.each(page_config['filter_form_fields'], (key,value)=>{
       filter_form_fields[value] = fields[value];
    })

    let filter_form = new BootstrapForm({
            container: '#form_filter_container',
            id: 'filter_form',
            ajax_url: page_config['ajax_url'],
            validation:false,
            fields: filter_form_fields,
            language: lang_cookie,
            method:'GET'
    })

    filter_form.build();

    // create form instance

    let create_form_fields = {};

    $.each(page_config['create_form_fields'], (key,value)=>{
       create_form_fields[value] = fields[value];
    })

    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: create_form_fields,
            required : page_config['create_form_fields_required'],
            language: lang_cookie,
            method:'POST'
    })

    create_form.build();

    // update form instance
    let update_form_fields = {};

    $.each(page_config['update_form_fields'], (key,value)=>{
       update_form_fields[value] = fields[value];
    })

    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: update_form_fields,
            disabled : page_config['update_form_fields_disabled'],
            required : page_config['update_form_fields_required'],
            language: lang_cookie,
            method: 'PUT'

    })

    update_form.build();


    // add evetn listeners
    $( "#btn_filter" ).on( "click", function() {
      let query_params = $('#filter_form').serialize();
      table.query_params = '?' + query_params
      table.build();
    });

    $( "#btn_reset" ).on( "click", function() {
        $('#filter_form').trigger("reset");
        $('#btn_filter').click();
    });

    $( "#btn_add" ).on( "click", function() {
        let url = page_config['ajax_url']
        create_form.submit(url, 'POST')
    });



    $( "#btn_save" ).on( "click", function() {
        update_form.set_required({fields: page_config['update_form_fields_required']})
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] +pk + '/'
        update_form.submit(url, 'PUT');
    });

    $( "#sales_template" ).on( "change", function() {
        $('#loading_screen_wrapper').show();

        let template_id = $(this).val();

        $('#create_form').trigger("reset");

        let url = '/api/templates/'+ template_id + '/'
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
              console.log(response)
              $('#task_template').val(template_id);
              $.each(response, (key, value)=>{
                $('#create_modal #'+ key).val(value)

              })

              $('#loading_screen_wrapper').hide();
           },
           error: function(error){
            console.log(error)
           }
        });
    });

    $('#btn_delete').on('click', function() {
        update_form.required = ['id_task']
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/sales/' + pk + '/'

        let task_state = $('#fk_task_state').val()

        if (task_state >= 4) {
            alert('Task cannot be deleted because it was already closed or billed')
            location.reload();
        }

        update_form.submit(url, 'DELETE');
    })

    $('#btn_print').on('click', function() {
        $('#loading_screen_wrapper').toggle();

        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/sales/' + pk + '/pdf/'
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                console.log(response)
                window.open(response['file_url'], '_blank').focus();
                    $('#loading_screen_wrapper').toggle();

           },
           error: function(error){
           console.log(error)
           alert(error)
           location.reload()

           }
        });
    })



    $('#update_modal').on('show.bs.modal', function() {
            $('#loading_screen_wrapper').toggle();

        let task_status = $('#update_form #fk_sales_status').val()
        console.log(task_status)
        if (
            (task_status == "3") ||
            (task_status == "2") ||
            (task_status == "-1")
        ){

                $('#update_form').find(':input').prop('disabled', true)
                $('#btn_delete').prop('disabled', true)
                $('#btn_close_task').prop('disabled', true)
                $('#btn_save').prop('disabled', true)

        } else {
            $('#update_form').find(':input').prop('disabled', false)
            $('#update_form #id_sale').prop('disabled', true);
            $('#update_form #fk_sales_status').prop('disabled', true);
            $('#btn_delete').prop('disabled', false)
            $('#btn_close_task').prop('disabled', false)
            $('#btn_save').prop('disabled', false)
        }
            $('#loading_screen_wrapper').toggle();

    })
};




/*
$(document).ready(function(){
    let page_config
    let url = '/sales'
    let lang_cookie = Cookies.get('sisyphus_language');



    $.ajax({
          url: '/_config',
          async: false,
          dataType: 'json',
          success: function (response) {
            page_config = response['pages'][url]
            translations = response['translations']
          }
    });

    $('#btn_close_task').remove();


    // create table instance
    let table = new BootstrapDataTable({
                        container:'#overview-table',
                        id: page_config['table_id'],
                        fields: page_config['fields'],
                        ajax_url: page_config['ajax_url'],
                        pk_field: page_config['pk'],
                        exclude: ['fk_invoice', 'sale_custom_fields', 'sales_template'],
                        language: lang_cookie
                    })


    // create form insstances
    let filter_form = new BootstrapForm({
            container: '#form_filter_container',
            id: 'filter_form',
            ajax_url: page_config['ajax_url'],
            validation:false,
            fields: page_config['fields'],
            exclude: ['sale_description', 'fk_invoice', 'sale_custom_fields', 'sales_template'],
            language: lang_cookie


    })
    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['id_sale', 'fk_invoice', 'fk_sales_status'],
            required : ['sale_date', 'amount', 'unit_price', 'description', 'sale_time', 'fk_currency', 'fk_project', 'fk_unit', 'fk_vat', 'fk_clearing_type'],
            language: lang_cookie

    })
    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['fk_invoice', 'sales_template'],
            disabled : ['id_sale', 'fk_invoice', 'fk_sales_status'],
            required : ['id_sale', 'sale_date', 'amount', 'unit_price', 'description', 'sale_time', 'fk_currency', 'fk_project', 'fk_unit', 'fk_vat', 'fk_clearing_type'],
            language: lang_cookie

    })

   // build components
    table.build();
    filter_form.build();
    create_form.build();
    update_form.build();


    // add evetn listeners
    $( "#btn_filter" ).on( "click", function() {
      let query_params = $('#filter_form').serialize();
      table.query_params = '?' + query_params
      table.build();
    });

    $( "#btn_reset" ).on( "click", function() {
        $('#filter_form').trigger("reset");
        $('#btn_filter').click();
    });

    $( "#btn_add" ).on( "click", function() {
        let url = page_config['ajax_url']
        create_form.submit(url, 'POST')
    });



    $( "#btn_save" ).on( "click", function() {
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] +pk + '/'
        update_form.submit(url, 'PUT');
    });


    $('#update_modal').on('show.bs.modal', function() {
            $('#loading_screen_wrapper').toggle();

        let task_status = $('#update_form #fk_sales_status').val()
        console.log(task_status)
        if (
            (task_status == "3") ||
            (task_status == "2") ||
            (task_status == "-1")
        ){

                $('#update_form').find(':input').prop('disabled', true)
                $('#btn_delete').prop('disabled', true)
                $('#btn_close_task').prop('disabled', true)
                $('#btn_save').prop('disabled', true)

        } else {
            $('#update_form').find(':input').prop('disabled', false)
            $('#update_form #id_sale').prop('disabled', true);
            $('#update_form #fk_sales_status').prop('disabled', true);
            $('#btn_delete').prop('disabled', false)
            $('#btn_close_task').prop('disabled', false)
            $('#btn_save').prop('disabled', false)
        }
            $('#loading_screen_wrapper').toggle();

    })

    $('#btn_print').on('click', function() {
            $('#loading_screen_wrapper').toggle();

        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/sales/' + pk + '/pdf/'
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                console.log(response)
                window.open(response['file_url'], '_blank').focus();
                    $('#loading_screen_wrapper').toggle();

           },
           error: function(error){
           alert(error)
           location.reload()
            console.log(error)
           }
        });
    })

    $('#btn_delete').on('click', function() {

        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/sales/' + pk + '/'

        let state = $('#fk_sales_state').val()

        if (state >= 2) {
            alert('Sale cannot be deleted because it was already billed')
            location.reload();
        }

        update_form.submit(url, 'DELETE');
    })

    $( "#sales_template" ).on( "change", function() {
            $('#loading_screen_wrapper').toggle();

        let template_id = $(this).val();

        $('#create_form').trigger("reset");

        let url = '/api/templates/'+ template_id + '/'

        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
              console.log(response)
              $('#sales_template').val(template_id);
              $.each(response, (key, value)=>{
                $('#create_modal #'+ key).val(value)

              })
                  $('#loading_screen_wrapper').toggle();

           },
           error: function(error){
            console.log(error)
            alert(error);
            location.reload();
           }
        });
    });

});
*/