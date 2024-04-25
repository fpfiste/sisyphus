
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

    let table = new BootstrapDataTable({
                        container:'#billing_table_container',
                        id: 'billing_table',
                        //fields: sales_table_fields,
                        //ajax_url: '/api/sales/',
                        //query_params: 'fk_sales_status=1&fk_clearing_type=2',
                        //pk_field: 'id_sale',
                        language: lang_cookie,
                    })
    //sales_table.build();

    // TASK TABLE INSTANCE
    let task_table_fields = {};

    $.each(page_config['task_table_fields'], (key,value)=>{
       task_table_fields[value] = fields[value];
    })

    let task_table = new BootstrapDataTable({
                        container:'#billing_table',
                        id: "task_billing_table",
                        fields: task_table_fields,
                        ajax_url: '/api/tasks/',
                        query_params: 'fk_task_state=4&fk_clearing_type=2',
                        ajax_url: page_config['ajax_url'],
                        pk_field: 'id_task',
                        language: lang_cookie,
                    })

    waitForEl('#select_transaction_type', function() {
        $('#select_transaction_type').on('change', function() {
            let type = $(this).val()

            $('#billing_table_container').empty()

            let project = 'fk_project=' + $('#fk_project').val();
            let vat = '&fk_vat=' + $('#fk_vat').val();
            let currency = '&fk_currency='+ $('#fk_currency').val();
            let revenue_type = '&fk_revenue_type='+ $('#fk_revenue_type').val();


            if ($(this).val() == '0'){
                        table.fields = task_table_fields
                        table.ajax_url = '/api/tasks/'
                        table.query_params =project+ vat+currency+ revenue_type + '&fk_task_state=4&fk_clearing_type=2'
                        table.filter_params ='fk_task_state=4&fk_clearing_type=2'
                        table.pk_field = 'id_task'
                        table.transaction_type = type
                        table.build()

            } else if ($(this).val() == '1'){
                        table.fields = sales_table_fields
                        table.ajax_url = '/api/sales/'
                        table.query_params = project+ vat+currency+ revenue_type + '&fk_sales_status=1&fk_clearing_type=2'
                        table.filter_params = 'fk_sales_status=1&fk_clearing_type=2'
                        table.pk_field ='id_sale'
                        table.transaction_type = type
                        table.build()

            }



            console.log('Transaction Type: ' + table.transaction_type)

        });
     });


    let change = function() {
        let positions = []
        $('#billing_table tbody td:first-child input:checked').each(function(){
            let selected = $(this)[0].checked
            if (selected){
                positions.push($(this).parent().parent().attr('data-row-pk'))
            }

        })


          let query_params = $('#create_form').serialize();

          console.log('Params: ' + query_params)
          let project = 'fk_project=' + $('#fk_project').val();
          let vat = '&fk_vat=' + $('#fk_vat').val();
          let currency = '&fk_currency='+ $('#fk_currency').val();
          let revenue_type = '&fk_revenue_type='+ $('#fk_revenue_type').val();

          table.query_params = project+ vat+currency+ revenue_type + '&' + table.filter_params
          console.log(table.query_params)
          table.build(function(){
            $('#billing_table tbody tr').each(function(){
            current_pk = $(this).attr('data-row-pk')
            if (positions.includes(current_pk)) {
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

     waitForEl('#fk_revenue_type', function() {
        $('#fk_revenue_type').on('change', change);
     });


    $( "#btn_reset" ).on( "click", function() {
        $('#create_form').trigger("reset");
        //$('#btn_filter').click();
        $('#select_transaction_type').val("")
        $('#billing_table_container').empty()

    });


    $('#btn_add').on('click', function() {
        $('#loading_screen_wrapper').show();
        create_form.validate()

        let valid = true
        if (create_form.is_valid == false) {
            $('#loading_screen_wrapper').hide();
            valid = false
        }

        let form_data = create_form.serialize();

        let positions = []
        $('#billing_table tbody td:first-child input:checked').each(function(){
            let selected = $(this)[0].checked
            if (selected){
                positions.push($(this).parent().parent().attr('data-row-pk'))
            }

        })



        console.log(positions)

        if (positions.length == 0){
            $('#loading_screen_wrapper').hide();
            $('input:checkbox').css('outline', '1px solid red')
            valid = false
        } else {
            $('input:checkbox').css('outline', '1px solid green')
        }

        console.log('Valid ' + valid)
        if (valid == false) {
            console.log('return')
            return
        }

        console.log('not return')
        let data = {
            'fk_project': $('#fk_project').val(),
            'fk_vat': $('#fk_vat').val(),
            'fk_currency': $('#fk_currency').val(),
            'invoice_text' : $('#invoice_text').val(),
            'fk_invoice_terms': $('#fk_invoice_terms').val(),
            'discount' : $('#discount').val(),
            'positions' : positions,
            'position_type' : table.transaction_type,
        }



        $.ajax({
           url: '/api/receivables/',
           type: 'POST',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           data:data,

           success: function(response) {
                console.log(response)
                $('#loading_screen_wrapper').hide();
                $('#nextStepModal').modal('show');
                create_form.reset();
                $('#select_transaction_type').val("")
                $('#billing_table_container').empty();
           },
           error: function(error){
            console.log(error)
            alert(error['responseJSON']['message'])
            location.reload();
           }
        });


    })

}

