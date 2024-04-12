


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
      table.query_params = query_params
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
        create_form.submit(page_config['ajax_url'], callback);
    });
    $( "#btn_save" ).on( "click", function() {
        $('#loading_screen_wrapper').show();
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = page_config['ajax_url'] +pk + '/'
        update_form.submit(url, callback);
    });



    $('#file_upload').on('change', function() {
        $('#loading_screen_wrapper').show();

        var that = this;

        var formData = new FormData();

         // add assoc key values, this will be posts values
        formData.append("file", this.files[0], this.files[0].name);
        formData.append("upload_file", true);


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
                    $('#loading_screen_wrapper').hide();

            },
            error: function (error) {
                console.log(error)
                location.reload();
            },
            async: true,
            data: formData,
            cache: false,
            contentType: false,
            processData: false,

    });




    })


}
