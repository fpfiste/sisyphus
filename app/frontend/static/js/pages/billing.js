
$(document).ready(function(){
    let page_config
    let url = '/billing'
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
    let sales_table = new BootstrapDataTable({
                        container:'#sales_billing',
                        id: 'sales_billing_table',
                        fields: page_config['fields'],
                        ajax_url: '/api/sales/',
                        query_params: '?fk_sales_status=1',
                        pk_field: 'id_sale',
                        language: lang_cookie,
                        exclude: ['fk_project', 'invoice_text', 'id_task', 'amount', 'unit_price']

                    })
     // build components


    let task_table = new BootstrapDataTable({
                    container:'#task_billing',
                    id: 'task_billing_table',
                    fields: page_config['fields'],
                    ajax_url: '/api/tasks/',
                    query_params: '?fk_task_state=4',
                    pk_field: 'id_task',
                    language: lang_cookie,
                    exclude: ['fk_project', 'invoice_text', 'id_sale', 'sale_amount', 'sale_unit_price']
                })



    let create_form = new BootstrapForm({
            container: '#form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['select_position','id_task' , 'id_sale', 'amount', 'sale_amount', 'unit_price', 'sale_unit_price'],
            required : ['fk_project', 'fk_currency', 'vat' , 'due_days'],
            language: lang_cookie

    })





    task_table.build(),
    sales_table.build()




    create_form.build();




    $( "#btn_reset" ).on( "click", function() {
        $('#create_form').trigger("reset");
        $('#btn_filter').click();
    });

    $( "#btn_add" ).on( "click", function() {
        let url = page_config['ajax_url']
        create_form.submit(url, 'POST')
    });

    $('#fk_project, #fk_vat, #fk_currency').on('change', function() {
      let query_params = $('#create_form').serialize();
      console.log(query_params)
      sales_table.query_params = '?' + query_params + '&fk_sales_status=1'
      task_table.query_params = '?' + query_params +'&fk_task_state=4'
      sales_table.build();
      task_table.build();


    });

    $( "#btn_reset" ).on( "click", function() {
        $('#filter_form').trigger("reset");
        $('#btn_filter').click();
        sales_table.query_params = '?fk_sales_status=2'
        sales_table.build()
        task_table.query_params = '?fk_task_state=4'
        task_table.build()
    });


    $('#btn_add').on('click', function() {
        create_form.validate()

        if (create_form.is_valid == false) {
            alert('Form is not valid')
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

        if ((tasks.length == 0) && (sales.length == 0)){
            return
        }
        console.log('here')
        let data = {
            'fk_project': $('#fk_project').val(),
            'fk_vat': $('#fk_vat').val(),
            'fk_currency': $('#fk_currency').val(),
            'invoice_text' : $('#invoice_text').val(),
            'fk_invoice_terms': $('#fk_invoice_terms').val(),
            'sales' : sales,
            'tasks' : tasks,
        }
        $.ajax({
           url: '/api/invoices/',
           type: 'POST',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           data:data,

           success: function(response) {

                var doc = window.open(response['file_url'], '_blank');
                location.reload();
                doc.focus();

           },
           error: function(error){
            console.log(error)
           }
        });

    })


});