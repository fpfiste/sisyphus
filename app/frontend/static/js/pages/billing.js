
jQuery.fn.setUp = function(page_config, fields) {
    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');


    // CREATE FORM INSTANCE
    let create_form_fields = {};

    $.each(page_config['create_form_fields'], (key,value)=>{
       create_form_fields[value] = fields[value];
    })

    let create_form = new BootstrapForm({
            container: '#form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: create_form_fields,
            required : page_config['create_form_fields_required'],
            language: lang_cookie,
            method:'POST'
    })

    create_form.build();

    // SALES TABLE INSTANCE
    let sales_table_fields = {};

    $.each(page_config['sales_table_fields'], (key,value)=>{
       sales_table_fields[value] = fields[value];
    })

    let sales_table = new BootstrapDataTable({
                        container:'#sales_billing',
                        id: 'sales_billing_table',
                        fields: sales_table_fields,
                        ajax_url: '/api/sales/',
                        query_params: 'fk_sales_status=1&fk_clearing_type=2',
                        pk_field: 'id_sale',
                        language: lang_cookie,
                    })
    sales_table.build();

    // TASK TABLE INSTANCE
    let task_table_fields = {};

    $.each(page_config['task_table_fields'], (key,value)=>{
       task_table_fields[value] = fields[value];
    })

    let task_table = new BootstrapDataTable({
                        container:'#task_billing',
                        id: "task_billing_table",
                        fields: task_table_fields,
                        ajax_url: '/api/tasks/',
                        query_params: 'fk_task_state=4&fk_clearing_type=2',
                        ajax_url: page_config['ajax_url'],
                        pk_field: 'id_task',
                        language: lang_cookie,
                    })
    task_table.build();

    let change = function() {
        let sales = []
        $('#sales_billing_table tbody td:first-child input:checked').each(function(){
            let selected = $(this)[0].checked
            if (selected){
                sales.push($(this).parent().parent().attr('data-row-pk'))
            }

        })

        let tasks = []
        $('#task_billing_table tbody td:first-child input:checked').each(function(){
            let selected = $(this)[0].checked
            if (selected){
                tasks.push($(this).parent().parent().attr('data-row-pk'))
            }

        })

          let query_params = $('#create_form').serialize();
          console.log(query_params)
          let project = '&fk_project=' + $('#fk_project').val();
          let vat = '&fk_vat=' + $('#fk_vat').val();
          let currency = '&fk_currency='+ $('#fk_currency').val();

          sales_table.query_params = project+ vat+currency+ '&fk_sales_status=1&fk_clearing_type=2'
          task_table.query_params = project+ vat+currency+'&fk_task_state=4&fk_clearing_type=2'
          sales_table.build(function(){
            $('#sales_billing_table tbody tr').each(function(){
            current_pk = $(this).attr('data-row-pk')
            if (sales.includes(current_pk)) {
                console.log($(this).find('input'))
                $(this).find('input:checkbox').prop('checked', true)
            }

          })
          });
          task_table.build(function(){
            $('#task_billing_table tbody tr').each(function(){
            current_pk = $(this).attr('data-row-pk')
            if (tasks.includes(current_pk)) {
                console.log($(this).find('input'))
                $(this).find('input:checkbox').prop('checked', true)
            }

          })
          });


    }

    waitForEl('#fk_project', function() {
        $('#fk_project').on('change', change);
     });

    waitForEl('#fk_vat', function() {
        $('#fk_vat').on('change', change);
     });

    waitForEl('#fk_currency', function() {
        $('#fk_currency').on('change', change);
     });


    $( "#btn_reset" ).on( "click", function() {
        $('#filter_form').trigger("reset");
        $('#btn_filter').click();
        sales_table.query_params = '?fk_sales_status=2&fk_clearing_type=2'
        sales_table.build()
        task_table.query_params = '?fk_task_state=4&fk_clearing_type=2'
        task_table.build()
    });


    $('#btn_add').on('click', function() {
        $('#loading_screen_wrapper').show();
        create_form.validate()

        if (create_form.is_valid == false) {
            $('#loading_screen_wrapper').hide();
            $('input:checkbox').css('outline', '1px solid red')
            return
        }

        let form_data = create_form.serialize();

        let sales = []
        $('#sales_billing_table tbody td:first-child input:checked').each(function(){
            let selected = $(this)[0].checked
            if (selected){
                sales.push($(this).parent().parent().attr('data-row-pk'))
            }

        })

        let tasks = []
        $('#task_billing_table tbody td:first-child input:checked').each(function(){
            let selected = $(this)[0].checked
            if (selected){
                tasks.push($(this).parent().parent().attr('data-row-pk'))
            }

        })

        console.log(tasks)

        if ((tasks.length == 0) && (sales.length == 0)){
            $('#loading_screen_wrapper').hide();
            $('input:checkbox').css('outline', '1px solid red')
            return
        }

        let data = {
            'fk_project': $('#fk_project').val(),
            'fk_vat': $('#fk_vat').val(),
            'fk_currency': $('#fk_currency').val(),
            'invoice_text' : $('#invoice_text').val(),
            'fk_invoice_terms': $('#fk_invoice_terms').val(),
            'discount' : $('#discount').val(),
            'sales' : sales,
            'tasks' : tasks,
        }



        $.ajax({
           url: '/api/receivables/',
           type: 'POST',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           data:data,

           success: function(response) {
                console.log(response)
                $('#loading_screen_wrapper').toggle();
                var doc = window.open(response['file_url'], '_blank');
                location.reload();
                doc.focus();
                $('#loading_screen_wrapper').hide();

           },
           error: function(error){
            console.log(error)
            alert(error['responseJSON']['message'])
            location.reload();
           }
        });

    })

}

