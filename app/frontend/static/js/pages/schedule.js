
$(document).ready(function(){
    let page_config
    let translations
    let url = '/tasks'
    let lang_cookie = Cookies.get('sisyphus_language');

    //*** read the config file ***//
    $.ajax({
          url: '/static/config.json',
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
            open_task_label:translations['scheduler_open_task_label'][lang_cookie]
          })


    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['id_task', 'fk_invoice', 'fk_task_state'],
            required : ['fk_project', 'task_description'],


    })
    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['fk_invoice', 'task_template', 'fk_invoice'],
            disabled : ['id_task', 'fk_task_state'],
            required : ['id_task', 'fk_project', 'task_description']

    })


    scheduler.build();
    create_form.build();
    update_form.build();



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
        let url = page_config['ajax_url'] + '/' +pk + '/'
         update_form.submit(url, 'PUT');
    });

    $( "#btn_delete" ).on( "click", function() {
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] + '/' +pk + '/'
        console.log(url)
         update_form.submit(url, 'DELETE');
    });

});
