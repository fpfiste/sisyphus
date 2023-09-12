
$(document).ready(function(){
    let page_config
    let url = '/tasks'
    let employees;
    let assets;

    //*** read the config file ***//
    $.ajax({
          url: '/static/config.json',
          async: false,
          dataType: 'json',
          success: function (response) {
            page_config = response['pages'][url]
          }
    });



    // create table instance
    let table = new BootstrapDataTable({
                        container:'#overview-table',
                        id: page_config['table_id'],
                        fields: page_config['fields'],
                        ajax_url: page_config['ajax_url'],
                        pk_field: page_config['pk'],
                        exclude: ['task_template','fk_employee_1', 'fk_employee_2', 'fk_asset_1', 'fk_asset_2', 'fk_subcontractor', 'fk_invoice', 'fk_project', 'fk_task_state', 'fk_unit'],
                    })


    let scheduler = new Scheduler({
            container:'#schedule_container',
            id:'scheduler',
            data : table.data
          })

    // create form insstances
    let filter_form = new BootstrapForm({
            container: '#form_filter_container',
            id: 'filter_form',
            ajax_url: page_config['ajax_url'],
            validation:false,
            fields: page_config['fields'],
            exclude: ['task_template', 'task_description', 'fk_invoice', 'internal_info', 'employees', 'assets', 'amount', 'unit_price', 'fk_unit']


    })
    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['id_task', 'fk_invoi console.log(this.fields)ce'],
            required : ['fk_project', 'fk_task_status' , 'task_description']

    })
    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['fk_invoice', 'task_template'],
            disabled : ['id_task', 'fk_invoice'],
            required : ['id_task', 'fk_project', 'fk_task_status' , 'task_description']

    })

    // build components
    table.build();
    scheduler.build();
    filter_form.build();
    create_form.build();
    update_form.build();

    $('#table_container').css('height', '30vh')
    // add evetn listeners
        // add evetn listeners
    $( "#btn_filter" ).on( "click", function() {
      let query_params = $('#filter_form').serialize();
      table.query_params = '?' + query_params,

      table.build()


    });
    $( "#btn_form_reset" ).on( "click", function() {
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
        console.log(url)
         update_form.submit(url, 'PUT');
    });

    $( "#btn_delete" ).on( "click", function() {
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] + '/' +pk + '/'
        console.log(url)
         update_form.submit(url, 'DELETE');
    });

});
