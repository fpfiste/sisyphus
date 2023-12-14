
jQuery.fn.setUp = function(page_config, fields) {
    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');
    console.log('here')

    let employee_label = (lang_cookie == 'en') ? 'Employees' : 'Mitarbeiter'
    let resource_label = (lang_cookie == 'en') ? 'Resources' : 'Hilfsmittel'
    let open_task_label = (lang_cookie == 'en') ? 'Open Tasks' : 'Offene Aufträge'
    let employee_type_label = (lang_cookie == 'en') ? 'Emplyoee Types' : 'Mitarbeiter Typen'

    // create scheduler

    let scheduler = new Scheduler({
        container:'#schedule_container',
        id:'scheduler',
        employee_label: employee_label,
        asset_label:resource_label,
        open_task_label:open_task_label,
        employee_type_label:employee_type_label
      })

    scheduler.build()

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


    waitForEl('#task_template', function() {
        $( "#task_template" ).on( "change", function() {
            $('#loading_screen_wrapper').show();

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
                $('#'+ key).val(value)

              })
                  $('#loading_screen_wrapper').hide();

           },
           error: function(error){
            console.log(error)
            alert(error);
            location.reload();
           }
        });
    });
    });



    $( "#btn_reset" ).on( "click", function() {
        $('#filter_form').trigger("reset");
        $('#btn_filter').click();


    });


    let callback = function(response) {

          $('#create_modal, #update_modal').modal('hide');
          create_form.reset()
          update_form.reset()
          scheduler.build();
          $('#loading_screen_wrapper').hide();
    }

    $( "#btn_add" ).on( "click", function() {
        $('#loading_screen_wrapper').show();
        let url = page_config['ajax_url']
        create_form.submit(url, callback)
    });

    $( "#btn_save" ).on( "click", function() {
        $('#loading_screen_wrapper').show();
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] +pk + '/'
         update_form.submit(url, callback);
    });

    $( "#btn_delete" ).on( "click", function() {
        $('#loading_screen_wrapper').show();
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] + '/' +pk + '/'
        console.log(url)
        update_form.submit(url, callback);
    });

    $('#btn_print').on('click', function() {
        $('#loading_screen_wrapper').show();

        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/tasks/' + pk + '/pdf/'
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {

                window.open(response['file_url'], '_blank').focus();
                $('#loading_screen_wrapper').hide();
           },
           error: function(error){
            console.log(error)
            alert(error)
            location.reload();
           }
        });
    })


    $('#btn_print_schedule').on('click', function() {
        $('#loading_screen_wrapper').show();
        let url = '/api/tasks/printSchedule/?date=' + scheduler.schedule_date
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                window.open(response['file_url'], '_blank').focus();
                $('#loading_screen_wrapper').hide();
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
                $('#update_form').find('input').prop('disabled', true)
                $('#btn_delete').prop('disabled', true)
                $('#btn_close_task').prop('disabled', true)
                $('#btn_save').prop('disabled', true)

        } else {
            $('#update_form').find('input').prop('disabled', false)
            $('#update_form #id_task').prop('disabled', true);
            $('#update_form #fk_task_state').prop('disabled', true);
            $('#btn_delete').prop('disabled', false)
            $('#btn_close_task').prop('disabled', false)
            $('#btn_save').prop('disabled', false)
        }

    })


}

