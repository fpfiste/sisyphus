
jQuery.fn.setUp = function(page_config, fields) {
    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');

    let employee_label = (lang_cookie = 'en') ? 'Employees' : 'Mitarbeiter'
    let resource_label = (lang_cookie = 'en') ? 'Resources' : 'Hilfsmittel'
    let open_task_label = (lang_cookie = 'en') ? 'Open Tasks' : 'Offene Aufträge'
    let employee_type_label = (lang_cookie = 'en') ? 'Emplyoee Types' : 'Mitarbeiter Typen'

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

    $( "#task_template" ).on( "change", function() {
            $('#loading_screen_wrapper').toggle();

        let template_id = $(this).val();

        $('#create_form').trigger("reset");

        let url = '/api/templates/'+ template_id + '/'

        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {

              $('#task_template').val(template_id);
              $.each(response, (key, value)=>{
                $('#'+ key).val(value)

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

    $( "#btn_delete" ).on( "click", function() {
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] + '/' +pk + '/'
        console.log(url)
         update_form.submit(url, 'DELETE');
    });

    $('#btn_print').on('click', function() {
        $('#loading_screen_wrapper').toggle();

        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/tasks/' + pk + '/pdf/'
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                    $('#loading_screen_wrapper').toggle();

                window.open(response['file_url'], '_blank').focus();
           },
           error: function(error){
            console.log(error)
            alert(error)
            location.reload();
           }
        });
    })


    $('#btn_print_schedule').on('click', function() {
        let url = '/api/tasks/printSchedule/?date=' + scheduler.schedule_date
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                window.open(response['file_url'], '_blank').focus();
           },
           error: function(error){
            console.log(error)
           }
        });
    })


}

/*
$(document).ready(function(){
    let page_config
    let translations
    let url = '/tasks'
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



    let scheduler = new Scheduler({
            container:'#schedule_container',
            id:'scheduler',
            employee_label: translations['scheduler_employee_label'][lang_cookie],
            asset_label:translations['scheduler_asset_label'][lang_cookie],
            subcontractor_label:translations['scheduler_subcontractor_label'][lang_cookie],
            open_task_label:translations['scheduler_open_task_label'][lang_cookie],
            employee_type_label: translations['scheduler_employee_type_label'][lang_cookie]
          })


    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['id_task', 'fk_invoice', 'fk_task_state'],
            required : ['fk_project', 'description'],
            language: lang_cookie


    })
    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['fk_invoice', 'task_template', 'fk_invoice'],
            disabled : ['id_task', 'fk_task_state'],
            required : ['id_task', 'fk_project', 'description'],
            language: lang_cookie
    })


    scheduler.build();
    create_form.build();
    update_form.build();

    $( "#task_template" ).on( "change", function() {
            $('#loading_screen_wrapper').toggle();

        let template_id = $(this).val();

        $('#create_form').trigger("reset");

        let url = '/api/templates/'+ template_id + '/'

        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {

              $('#task_template').val(template_id);
              $.each(response, (key, value)=>{
                $('#'+ key).val(value)

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

    $( "#btn_delete" ).on( "click", function() {
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] + '/' +pk + '/'
        console.log(url)
         update_form.submit(url, 'DELETE');
    });

    $('#btn_print').on('click', function() {
        $('#loading_screen_wrapper').toggle();

        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/tasks/' + pk + '/pdf/'
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                    $('#loading_screen_wrapper').toggle();

                window.open(response['file_url'], '_blank').focus();
           },
           error: function(error){
            console.log(error)
            alert(error)
            location.reload();
           }
        });
    })


    $('#btn_print_schedule').on('click', function() {
        let url = '/api/tasks/printSchedule/?date=' + scheduler.schedule_date
        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                window.open(response['file_url'], '_blank').focus();
           },
           error: function(error){
            console.log(error)
           }
        });
    })



});
*/