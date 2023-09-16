
$(document).ready(function(){
    let page_config
    let url = '/sales'
    let lang_cookie = Cookies.get('sisyphus_language');



    //*** read the config file ***//
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
                        exclude: ['fk_invoice'],
                        language: lang_cookie
                    })


    // create form insstances
    let filter_form = new BootstrapForm({
            container: '#form_filter_container',
            id: 'filter_form',
            ajax_url: page_config['ajax_url'],
            validation:false,
            fields: page_config['fields'],
            exclude: ['sale_description', 'fk_invoice'],
            language: lang_cookie


    })
    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['id_sale', 'fk_invoice', 'fk_sales_status'],
            required : ['sale_date', 'fk_project', 'sale_amount', 'sale_unit_price', 'sale_description', 'fk_unit'],
            language: lang_cookie

    })
    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['fk_invoice'],
            disabled : ['id_sale', 'fk_invoice', 'fk_sales_status'],
            required : ['id_sale', 'sale_date', 'fk_project', 'sale_amount', 'sale_unit_price', 'sale_reference', 'fk_unit'],
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

    $('#btn_close_task').on('click', function() {
        update_form.required = ['id_sale', 'fk_project', 'sale_date', 'sale_time','sale_amount', 'sale_unit_price', 'fk_unit', 'fk_vat', 'fk_currency', 'sale_description']
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/sales/' + pk + '/close/'
        update_form.submit(url, 'PUT');
    })

    $('#update_modal').on('show.bs.modal', function() {
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

    })


});
