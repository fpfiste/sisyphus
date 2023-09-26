
$(document).ready(function(){
    let page_config
    let url = '/tasks'
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
                        exclude: ['task_template','fk_employee_1', 'fk_employee_2', 'fk_asset_1', 'fk_asset_2', 'fk_subcontractor', 'fk_invoice', 'fk_project', 'fk_task_state', 'fk_unit', 'fk_currency', 'fk_vat', 'task_custom_fields'],
                        language: lang_cookie
                    })



    // create form insstances
    let filter_form = new BootstrapForm({
            container: '#form_filter_container',
            id: 'filter_form',
            ajax_url: page_config['ajax_url'],
            validation:false,
            fields: page_config['fields'],
            exclude: ['task_template', 'task_description', 'fk_invoice', 'internal_info', 'employees', 'assets', 'amount', 'unit_price', 'fk_unit', 'task_custom_fields'],
            language: lang_cookie

    })
    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['id_task', 'fk_invoice'],
            required : ['fk_project',  'task_description'],
            disabled : ['fk_task_state'],
            language: lang_cookie

    })
    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['fk_invoice', 'task_template'],
            disabled : ['id_task', 'fk_invoice', 'fk_task_state' ,],
            required : ['id_task', 'fk_project',  'task_description'],
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

    $( "#task_template" ).on( "change", function() {
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
           },
           error: function(error){
            console.log(error)
           }
        });
    });

    $('#btn_close_task').on('click', function() {
        update_form.required = ['id_task', 'fk_project', 'task_date_from', 'task_date_to', 'task_time_from', 'task_time_to', 'amount', 'unit_price', 'task_description', 'fk_unit', 'fk_currency', 'fk_vat']
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/tasks/' + pk + '/close/'
        update_form.submit(url, 'PUT');
    })

    $('#btn_delete').on('click', function() {
        update_form.required = ['id_task']
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/tasks/' + pk + '/'

        let task_state = $('#fk_task_state').val()

        if (task_state >= 4) {
            alert('Task cannot be deleted because it was already closed or billed')
            location.reload();
        }

        update_form.submit(url, 'DELETE');
    })

    $('#btn_print').on('click', function() {
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/tasks/' + pk + '/pdf/'
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                console.log(response)
                window.open(response['file_url'], '_blank').focus();

           },
           error: function(error){
            console.log(error)
           }
        });
    })




    $('#update_modal').on('show.bs.modal', function() {
        let task_status = $('#update_form #fk_task_state').val()
        console.log(task_status)
        if (
            (task_status == "4") ||
            (task_status == "5") ||
            (task_status == "6")
        ){
                $('#update_form').find(':input').prop('disabled', true)
                $('#btn_delete').prop('disabled', true)
                $('#btn_close_task').prop('disabled', true)
                $('#btn_save').prop('disabled', true)

        } else {
            $('#update_form').find(':input').prop('disabled', false)
            $('#update_form #id_task').prop('disabled', true);
            $('#update_form #fk_task_state').prop('disabled', true);
            $('#btn_delete').prop('disabled', false)
            $('#btn_close_task').prop('disabled', false)
            $('#btn_save').prop('disabled', false)
        }

    })

});
