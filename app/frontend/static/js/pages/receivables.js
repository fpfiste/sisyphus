
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
            language: lang_cookie,
            method: 'PUT'

    })

    update_form.build();


    let send_form_fields = {};

    $.each(page_config['send_form_fields'], (key,value)=>{
       send_form_fields[value] = fields[value];
    })

    let send_form = new BootstrapForm({
            container: '#send_form_container',
            id: 'send_form',
            ajax_url: page_config['ajax_url'],
            validation:false,
            fields: send_form_fields,
            language: lang_cookie,
            method:'POST'
    })

    send_form.build();
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


    $('#btn_print').on('click', function() {
        //$('#loading_screen_wrapper').show();
        let pk = $('#update_form #id_invoice').val();

        let url = page_config['ajax_url'] + pk + '/pdf'

        $.ajax({
           url: url,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
           console.log(response)
                $('body').append('<a id="invoice_download_link" href="'+response['file_url']+'" download></a>')
                $('#invoice_download_link')[0].click()
                $('#invoice_download_link').remove();
                //var doc = window.open(response['file_url'], '_blank');
                //doc.focus();
                //$('#loading_screen_wrapper').hide();
           },
           error: function(error){
           console.log(error)
            alert(error)
            location.reload();

           }
        });
    })

    $('#btn_delete').on('click', function() {
        //$('#loading_screen_wrapper').show();
        update_form.required = ['id_task']
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/receivables/' + pk + '/'

        let task_state = $('#fk_invoice_state').val()

        if (task_state >= 2) {
            alert('Invoice cannot be canceld since it was already booked')
            location.reload();
        }

        $.ajax({
           url: url,
           type: 'DELETE',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                console.log(response)
                $('body').append('<a id="invoice_download_link" href="'+response['file_url']+'" download></a>')
                $('#invoice_download_link')[0].click()
                $('#invoice_download_link').remove();
                  $('#create_modal, #update_modal').modal('hide');
                  $('#create_form, #update_form').trigger("reset")
                  table.build();
                  $('#loading_screen_wrapper').hide();

           },
           error: function(error){
            console.log(error)
            alert(error)
            location.reload();
           }
        });
    })

    let callback = function(response) {
          console.log('callback executed')
          $('#update_modal').modal('hide');
          update_form.reset()
          table.build();
          $('#loading_screen_wrapper').hide();
    }


    $('#btn_close_task').on('click', function() {
        $('#loading_screen_wrapper').show();
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/receivables/' + pk + '/close/'
        update_form.submit(url, callback);
    })


    $('#update_modal').on('show.bs.modal', function() {
        let task_status = $('#update_form #fk_invoice_state').val()
        console.log(task_status)
        if (
            (task_status == "4") ||
            (task_status == "3")
        ){
            $('#btn_delete').prop('disabled', true)
            $('#btn_close_task').prop('disabled', true)
            $('#btn_save').prop('disabled', true)
            $('#btn_open_send').prop('disabled', true)
        } else {
            $('#btn_delete').prop('disabled', false)
            $('#btn_close_task').prop('disabled', false)
            $('#btn_save').prop('disabled', true)
            $('#btn_open_send').prop('disabled', false)
        }

    })

    $('#send_modal').on('show.bs.modal', function() {
        send_form.reset();

        let project_id = $('#update_form #fk_project').val();

        $.ajax({
           url: '/api/projects/?id_project=' + project_id,
           type: 'GET',
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           success: function(response) {
                console.log(response)

                $('#send_form #email_to').val(response['data'][0]['fk_customer']['company_invoice_email'])
           },
           error: function(error){
            console.log(error)
           }
        });

        $('#send_form #email_subject').val('Rechnung: ' + $('#update_form #id_invoice').val())


        let mail_template = `Geschätzter Kunde

Gerne senden wir Ihnen die Rechnung `+$('#update_form #id_invoice').val()+` im Anhang zu.

Dies ist eine automatische Nachricht. Bitte antworten Sie nicht auf diese E-Mail.

Bei Fragen entnehmen Sie die Kontaktangaben bitte direkt der Rechnung.

Vielen Dank!
`
        $('#send_form #email_text').val(mail_template)
        console.log(lang_cookie)

    })
    $('#btn_send').on('click', function() {
        let pk = $('#update_form #' + page_config['pk']).val()
        let url = '/api/receivables/' + pk + '/send/'
        send_form.submit(url, callback);
        location.reload()

    })

}
