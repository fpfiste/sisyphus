
$(document).ready(function(){
    let page_config
    let url = '/payables'
    let lang_cookie = Cookies.get('sisyphus_language');

    $('#btn_close_task' ).remove();
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
                        language: lang_cookie,
                        exclude: ['file_upload', 'positions']

                    })


    // create form insstances
    let filter_form = new BootstrapForm({
            container: '#form_filter_container',
            id: 'filter_form',
            ajax_url: page_config['ajax_url'],
            validation:false,
            fields: page_config['fields'],
            language: lang_cookie,
            exclude: ['file_upload']



    })


    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['id_payable', 'fk_invoice_status'],
            required : ['invoice_id', 'fk_terms',  'invoice_date', 'fk_company', 'fk_currency', 'net_total', 'vat', 'total'],
            language: lang_cookie

    })

    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            disabled : ['id_payable', 'fk_invoice_status', ],
            required : ['id_payable', 'invoice_id', 'fk_terms',  'invoice_date', 'fk_company', 'fk_currency', 'net_total', 'vat', 'total'],
            language: lang_cookie,
                        exclude: ['file_upload']



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



    $('#file_upload').on('change', function() {
        $('#loading_screen_wrapper').toggle();

        console.log(this)

        var that = this;

        var formData = new FormData();

         // add assoc key values, this will be posts values
        formData.append("file", this.files[0], this.files[0].name);
        formData.append("upload_file", true);

        console.log(formData)

        $.ajax({
            type: "POST",
            url: "/api/payables/extract_data/",
            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
            success: function (result) {
                   console.log(result)
                   $('#create_form').trigger("reset");
                   $.each(result, (key, value)=>{
                        if (value === true){
                            value = 1;
                        } else if (value === false){
                            value = 0;
                        }
                        if (typeof(value) === 'object') {
                            value = JSON.stringify(value);
                        }
                        $('#create_form #'+ key).val(value).trigger('change');

                    });
                    $('#loading_screen_wrapper').toggle();

            },
            error: function (error) {
                console.log(error)
                alert(error);
                location.reload();
            },
            async: true,
            data: formData,
            cache: false,
            contentType: false,
            processData: false,

    });




    })


});
