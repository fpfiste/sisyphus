
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


    $('#btn_print').on('click', function() {
        $('#loading_screen_wrapper').show();
        let pk = $('#update_form #id_invoice').val();

        let url = page_config['ajax_url'] + pk + '/pdf'

        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
           console.log(response)
                var doc = window.open(response['file_url'], '_blank');
                doc.focus();
                $('#loading_screen_wrapper').hide();
           },
           error: function(error){
           console.log(error)
            alert(error)
            location.reload();

           }
        });
    })

    $('#btn_delete').on('click', function() {
        $('#loading_screen_wrapper').show();
        update_form.required = ['id_task']
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/receivables/' + pk + '/'

        let task_state = $('#fk_invoice_state').val()

        if (task_state >= 2) {
            alert('Invoice cannot be canceld since it was already booked')
            location.reload();
        }

        $.ajax({
           url: url,
           type: 'DELETE',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                console.log(response)
                window.open(response['file_url'], '_blank').focus();
                  $('#create_modal, #update_modal').modal('hide');
                  $('#create_form, #update_form').trigger("reset")
                  table.build();
                  $('#loading_screen_wrapper').hide();

           },
           error: function(error){
            console.log(error)
            alert(error)
            location.reload();
           }
        });
    })

}



/*

$(document).ready(function(){
    let page_config
    let url = '/receivables'
    let lang_cookie = Cookies.get('sisyphus_language');

    $('#btn_close_task, #btn_save, #btn_create' ).remove();
    $.ajax({
          url: '/_config',
          async: false,
          dataType: 'json',
          success: function (response) {
            page_config = response['pages'][url]
            translations = response['translations']
          }
    });



    // create table instance
    let table = new BootstrapDataTable({
                        container:'#overview-table',
                        id: page_config['table_id'],
                        fields: page_config['fields'],
                        ajax_url: page_config['ajax_url'],
                        pk_field: page_config['pk'],
                        language: lang_cookie

                    })


    // create form insstances
    let filter_form = new BootstrapForm({
            container: '#form_filter_container',
            id: 'filter_form',
            ajax_url: page_config['ajax_url'],
            validation:false,
            fields: page_config['fields'],
            language: lang_cookie



    })



    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            disabled : ['id_invoice', 'fk_invoice_state', 'fk_invoice_terms',  'invoice_date', 'invoice_text'],
            required : ['id_invoice', 'fk_invoice_state', 'fk_invoice_terms',  'invoice_date'],
            language: lang_cookie


    })

   // build components
    table.build();
    filter_form.build();
    update_form.build();



});
*/