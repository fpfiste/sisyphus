

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

    let callback = function(response) {
          $('#create_modal, #update_modal').modal('hide');
          create_form.reset()
          update_form.reset()
          table.build();
          $('#loading_screen_wrapper').hide();
    }

    $( "#btn_add" ).on( "click", function() {
        $('#loading_screen_wrapper').show();
        let url = page_config['ajax_url']
        create_form.submit(url, callback)
    });



    $( "#btn_save" ).on( "click", function() {
        $('#loading_screen_wrapper').show();
        update_form.set_required({fields: page_config['update_form_fields_required']})
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] +pk + '/'
        update_form.submit(url, callback);
    });

    console.log($('#sales_template').length)



    waitForEl('#sales_template', function() {
      $( "#sales_template" ).on( "change", function() {
        $('#loading_screen_wrapper').show();
        console.log('here')
        let template_id = $(this).val();

        $('#create_form').trigger("reset");

        if (template_id == '') {
            $('#loading_screen_wrapper').hide();
            return
        }


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
    });




    $('#btn_delete').on('click', function() {
        $('#loading_screen_wrapper').show();
        update_form.required = ['id_sale']
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/sales/' + pk + '/'

        let task_state = $('#fk_sales_status').val()
        update_form.method = 'DELETE'
        if (task_state >= 2) {
            alert('Sale cannot be deleted because it was already closed or billed')
            location.reload();
        }

        update_form.submit(url, callback);
        update_form.method = 'PUT'
    })

    $('#btn_print').on('click', function() {
        $('#loading_screen_wrapper').show();

        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/sales/' + pk + '/pdf/'
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                console.log(response)
                window.open(response['file_url'], '_blank').focus();
                $('#loading_screen_wrapper').hide();

           },
           error: function(error){
           console.log(error)
           alert(error)
           location.reload()

           }
        });
    })



    $('#update_modal').on('show.bs.modal', function() {
        $('#loading_screen_wrapper').show();

        let sale_status = $('#update_form #fk_sales_status').val()

        if (
            (sale_status == "3") ||
            (sale_status == "2") ||
            (sale_status == "-1")
        ){

                $('#update_form').find('input, select, textarea').prop('disabled', true)
                $('#btn_delete').prop('disabled', true)
                $('#btn_close_task').prop('disabled', true)
                $('#btn_save').prop('disabled', true)

        } else {
            $('#update_form').find('input, select, textarea').prop('disabled', false)
            $('#update_form #id_sale').prop('disabled', true);
            $('#update_form #fk_sales_status').prop('disabled', true);
            $('#btn_delete').prop('disabled', false)
            $('#btn_close_task').prop('disabled', false)
            $('#btn_save').prop('disabled', false)
        }
            $('#loading_screen_wrapper').hide();

    })
};


