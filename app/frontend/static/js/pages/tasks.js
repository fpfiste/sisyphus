
$(document).ready(function(){
    let page_config
    let url = '/tasks'



    //*** read the config file ***//
    $.ajax({
          url: '/static/config.json',
          async: false,
          dataType: 'json',
          success: function (response) {
            page_config = response['pages'][url]
          }
    });

    let scheduler = new Scheduler({container:'#schedule_container', id:'scheduler'})

    // create table instance
    let table = new BootstrapDataTable({
                        container:'#overview-table',
                        id: page_config['table_id'],
                        fields: page_config['fields'],
                        ajax_url: page_config['ajax_url'],
                        pk_field: page_config['pk'],
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
            exclude: ['id_task', 'fk_invoice'],
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
    filter_form.build();
    create_form.build();
    update_form.build();

    $('#table_container').css('height', '30vh')
    // add evetn listeners
    $( "#btn_filter" ).on( "click", function() {
      let query_params = $('#filter_form').serialize();
      $.ajax({
        url: window.location.origin +page_config['ajax_url'] + '?' + query_params,
        success: function (result) {
            table.data = result;
            table.build();
            $( "#"+page_config['table_id']+" tr" ).on( "dblclick", function() {
        let record_id =  $(this).attr('data-row-pk');

        $.ajax({
            url: window.location.origin + page_config['ajax_url'] + '/' + record_id,
            success: function (result) {

                $.each(result, (key, value)=>{
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
        }
    });

    });

    $( "#btn_form_reset" ).on( "click", function() {
        $('#filter_form').trigger("reset");
        $('#btn_filter').click();


    });

    $( "#btn_add" ).on( "click", function() {
        let form = $('#' + create_form.id);
        let form_fields = $(form).find(':input')

        create_form.validate();

        if (create_form.is_valid == false){
            alert('Alle Felder ausfüllen!')
            return
        }

        let array = $(form).serialize();
        let url = page_config['ajax_url'] + '/';

        let employees = $(form).find('#fk_employee').val()
        let assets = $(form).find('#fk_asset').val()
        let task_data;

        $.ajax({
               url: url,
               type: 'POST',
               data:array,
               async:false,
               success: function(response) {
                  task_data = response;
                  console.log(task_data);
               },
               error: function(error){
                console.log(error)
               }
            });

        url = '/api/employee-allocation/'

        $.each(employees, (key,value)=>{
            let payload = {'fk_task':task_data['id_task'], 'fk_employee': value}
            $.ajax({
                   url: url,
                   type: 'POST',
                   data:payload,
                   async:false,
                   success: function(response) {
                      console.log(response);
                   },
                   error: function(error){
                    console.log(error)
                   }
            });
        })


        url = '/api/asset-allocation/'
        $.each(assets, (key,value)=>{
            let payload = {'fk_task':task_data['id_task'], 'fk_asset': value}
            $.ajax({
                   url: url,
                   type: 'POST',
                   data:payload,
                   async:false,
                   success: function(response) {
                      console.log(response);
                   },
                   error: function(error){
                    console.log(error)
                   }
            });
        })

    });




    $( "#"+page_config['table_id']+" tr").on( "dblclick", function() {
        let record_id =  $(this).attr('data-row-pk');

        $.ajax({
            url: window.location.origin + page_config['ajax_url'] + '/' + record_id,
            success: function (result) {

                console.log(result)
                $.each(result, (key, value)=>{

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
        let pk = $('#update_form #' + page_config['pk']).val()
        update_form.submit(pk);
        });


});
