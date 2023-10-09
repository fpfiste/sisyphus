

jQuery.fn.setUp = function(page_config, fields) {

    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');


    // PROFILE FORM
    let profile_form_fields = {};

    $.each(page_config['profile_fields'], (key,value)=>{
       profile_form_fields[value] = fields[value];
    })

    let profile_form = new BootstrapForm({
            container: '#profile_form_container',
            id: 'profile_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: profile_form_fields,
            language: lang_cookie,
            required: page_config['profile_fields_required'],
            disabled: page_config['profile_fields_disabled'],
            method:'POST'
    })

    profile_form.build();

    $.ajax({
          url: '/api/employees/get_employee_by_username/',
          async: true,
          dataType: 'json',
          success: function (response) {

              $.each(response, (key, value)=>{
                 $('#profile_form #'+ key).val(value)
              })
          }
    });






    // PROFILE FORM

    let company_form_fields = {};

    $.each(page_config['company_fields'], (key,value)=>{
       company_form_fields[value] = fields[value];
    })

    let company_form = new BootstrapForm({
            container: '#company_form_container',
            id: 'company_form',
            ajax_url: '/api/config/setCompany/',
            validation:true,
            fields: company_form_fields,
            language: lang_cookie,
            required: page_config['company_fields_required'],
            disabled: page_config['company_fields_disabled'],
            method:'POST'
    })

    company_form.build();

    $.ajax({
      url: '/api/companies/0/',
      async: true,
      dataType: 'json',
      success: function (response) {

          $.each(response, (key, value)=>{
             $('#company_form #'+ key).val(value)
          })
      }
    });


    // DOCUMENT CONFIG

    let doc_form_fields = {};

    $.each(page_config['doc_config_fields'], (key,value)=>{
       doc_form_fields[value] = fields[value];
    })

    let doc_form = new BootstrapForm({
            container: '#doc_config_form_container',
            id: 'doc_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: doc_form_fields,
            language: lang_cookie,
            required: page_config['doc_config_fields_required'],
            method:'POST'
    })

    doc_form.build();

    $.ajax({
      url: '/api/config/',
      async: true,
      dataType: 'json',
      success: function (response) {
          console.log(response)

          let logo_content_type = ''
          let logo_bytes = ''
          $.each(response, (key, value)=>{
            console.log('#doc_form #'+ value['config_key'])
             if (value['config_key'] == 'doc_logo') {
                logo_content_type = value['value_string']
                logo_bytes = value['value_bytes']
                $('#doc_form #image_binary').val(logo_content_type+','+logo_bytes)
             } else {
                $('#doc_form #'+ value['config_key']).val(value['value_string'])
             }
          })

        let image_binary = $('#doc_form #image_binary').val()
        let width = $('#doc_logo_width').val()
        let height = $('#doc_logo_height').val()
        let x_off = $('#doc_logo_x_offset').val()
        let y_off = $('#doc_logo_y_offset').val()

        var clone = $('#document_header_preview').clone();
        clone.css("visibility","hidden");
        $('#profile .card-body').append(clone);

        canvas_height = clone.height();
        clone.remove();

        console.log(canvas_height)
        let canvas_width = (canvas_height * 2)
        $('#document_header_preview').css('width', (canvas_height * 2) + 'px')

        console.log(canvas_width)

        let canvas_cm = canvas_width / 21

        let img_width = (width * canvas_cm)
        let img_height = (height * canvas_cm)

        let x_offset = (x_off * canvas_cm)
        let y_offset = (y_off * canvas_cm)

        logo = '<img id="doc_logo_img" src="'+image_binary+'" style="position:absolute; width:'+img_width+'px; height:'+img_height+'px; margin-left:'+x_offset+'px; margin-top: '+y_offset+'px">'
        $('#document_header_preview').append(logo);

        let address_sender = '<div id="address_sender" style="position:absolute; margin-left:'+(2 * canvas_cm)+'px; margin-top:'+(6 * canvas_cm)+'px"><p>XXXXXXXXXXXXXXXXXXXX</p><p>XXXXXXXXXXXXXXXXXXXX</p><p>XXXXXXXXXXXXXXXXXXXX</p></div>'
        let receiver_address = '<div id="address_sender" style="position:absolute; margin-left:'+(13 * canvas_cm)+'px; margin-top:'+(6 * canvas_cm)+'px"><p>XXXXXXXXXXXXXXXXXXXX</p><p>XXXXXXXXXXXXXXXXXXXX</p><p>XXXXXXXXXXXXXXXXXXXX</p></div>'
        $('#document_header_preview').append(address_sender);
        $('#document_header_preview').append(receiver_address);

      }
    });

    $('#file_upload').on('change', (key, value)=> {
        console.log('change')
        let file = $('#file_upload')[0].files[0]
        if (file){
          let reader = new FileReader();
          reader.onload = function(event){
            $('#doc_form #image_binary').val(event.target.result).trigger('change')
            console.log(event.target.result)
          }
          console.log(reader.readAsDataURL(file));
        }
    })


    $('#image_binary, #doc_logo_width, #doc_logo_height, #doc_logo_x_offset, #doc_logo_y_offset').on('change', (key, value)=> {
        $('#document_header_preview').empty();

        let image_binary = $('#doc_form #image_binary').val()
        let width = $('#doc_logo_width').val()
        let height = $('#doc_logo_height').val()
        let x_off = $('#doc_logo_x_offset').val()
        let y_off = $('#doc_logo_y_offset').val()

        let canvas_height =  $('#document_header_preview').height();
        let canvas_width = (canvas_height * 2)
        let canvas_cm = canvas_width / 21

        let img_width = (width * canvas_cm)
        let img_height = (height * canvas_cm)

        let x_offset = (x_off * canvas_cm)
        let y_offset = (y_off * canvas_cm)

        logo = '<img id="doc_logo_img" src="'+image_binary+'" style="position:absolute; width:'+img_width+'px; height:'+img_height+'px; margin-left:'+x_offset+'px; margin-top: '+y_offset+'px">'
        $('#document_header_preview').append(logo);

        let address_sender = '<div id="address_sender" style="position:absolute; margin-left:'+(2 * canvas_cm)+'px; margin-top:'+(6 * canvas_cm)+'px"><p>XXXXXXXXXXXXXXXXXXXX</p><p>XXXXXXXXXXXXXXXXXXXX</p><p>XXXXXXXXXXXXXXXXXXXX</p></div>'
        let receiver_address = '<div id="address_sender" style="position:absolute; margin-left:'+(13 * canvas_cm)+'px; margin-top:'+(6 * canvas_cm)+'px"><p>XXXXXXXXXXXXXXXXXXXX</p><p>XXXXXXXXXXXXXXXXXXXX</p><p>XXXXXXXXXXXXXXXXXXXX</p></div>'
        $('#document_header_preview').append(address_sender);
        $('#document_header_preview').append(receiver_address);

    })

    $('#btn_save_doc').on('click', (key,value)=> {

        var formData = new FormData();

        formData.append("file",  $('#image_binary').val());
        formData.append("doc_logo_width", $('#doc_logo_width').val());
        formData.append("doc_logo_height", $('#doc_logo_height').val());
        formData.append("doc_logo_x_offset", $('#doc_logo_x_offset').val());
        formData.append("doc_logo_y_offset", $('#doc_logo_y_offset').val());

        $.ajax({
            type: "POST",
            url: "/api/config/setDocumentConf/",
            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
            success: function (result) {
                   console.log(result)
                   location.reload()


            },
            error: function (error) {
                console.log(error)
                alert(error);
                //location.reload();
            },
            async: true,
            data: formData,
            cache: false,
            contentType: false,
            processData: false,

        });

    })

    $('#btn_save_rec').on('click', (key,value)=> {

        let endpoint = $('#ms_form_rec_endpoint').val()
        let api_key = $('#ms_form_rec_key').val()

        if (endpoint == null || api_key == null) {
            alert('all fields required')
        }

        let data = {
            'endpoint': endpoint,
            'key': api_key
        }

         $.ajax({
            type: "POST",
            url: "/api/config/setRecoginizerConfig/",
            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
            success: function (result) {
                   console.log(result)
                  location.reload()

            },
            error: function (error) {
                console.log(error)
                alert(error);
                location.reload();
            },
            data: data,


    });


});

    $('#btn_save_profile').on('click', (key,value)=>{
        let pk = $('#profile_form #id_employee').val()
        let url = '/api/employees/' +pk + '/'
        profile_form.submit(url, 'PUT');
    })

    $('#btn_save_company').on('click', (key,value)=>{
        let url = '/api/config/setCompany/'
        company_form.submit(url, 'POST')

    })
}
/*
$(document).ready(function(){
    let page_config
    let url = '/settings'
    let lang_cookie = Cookies.get('sisyphus_language');
    $('#loading_screen_wrapper').toggle();
    $.ajax({
          url: '/_config',
          async: false,
          dataType: 'json',
          success: function (response) {
            page_config = response['pages'][url]
            translations = response['translations']
            $('#loading_screen_wrapper').toggle();
          }
    });



    $('#logo_input, #logo_input, #logo_width, #logo_height, #logo_x_offset, #logo_y_offset').on('change', (key, value)=> {
        $('#document_header_preview').empty();
        let file = $('#logo_input')[0].files[0]
        let width = $('#logo_width').val()
        let height = $('#logo_height').val()
        let x_off = $('#logo_x_offset').val()
        let y_off = $('#logo_y_offset').val()

        let canvas_width = $('#document_header_preview').width()
        let canvas_cm = canvas_width / 21
        let img_width = (width * canvas_cm)
        let img_height = (height * canvas_cm)

        let x_offset = (x_off * canvas_cm)
        let y_offset = (y_off * canvas_cm)

        console.log(canvas_width / 21)
        if (file){
          let reader = new FileReader();
          reader.onload = function(event){
            console.log(event.target.result);
            $('#document_header_preview').append('<input type="image" src="'+event.target.result+'" alt="Submit" style="position:absolute; width:'+img_width+'px; height:'+img_height+'px; margin-left:'+x_offset+'px; margin-top: '+y_offset+'px">')
            let address_sender = '<div id="address_sender" style="position:absolute; margin-left:'+(2 * canvas_cm)+'px; margin-top:'+(6 * canvas_cm)+'px"><p>Absender GMBH</p><p>Musterstrasse 1</p><p>CH-1111 Musterstadt</p></div>'
            let receiver_address = '<div id="address_sender" style="position:absolute; margin-left:'+(13 * canvas_cm)+'px; margin-top:'+(6 * canvas_cm)+'px"><p>Absender GMBH</p><p>Musterstrasse 1</p><p>CH-1111 Musterstadt</p></div>'
            $('#document_header_preview').append(address_sender);
            $('#document_header_preview').append(receiver_address);
          }
          reader.readAsDataURL(file);
        }
    })

    $('#btn_save_doc').on('click', (key,value)=> {

        console.log($('#logo_input')[0]['files'][0])
        var formData = new FormData();

        formData.append("file", $('#logo_input')[0]['files'][0], $('#logo_input')[0]['files'].name);
        formData.append("upload_file", true);
        formData.append("logo_width", $('#logo_width').val());
        formData.append("logo_height", $('#logo_height').val());
        formData.append("logo_x_offset", $('#logo_x_offset').val());
        formData.append("logo_y_offset", $('#logo_y_offset').val());

        console.log(formData)




        console.log(formData)

        $.ajax({
            type: "POST",
            url: "/api/config/setDocumentConf/",
            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
            success: function (result) {
                   console.log(result)
                   location.reload()


            },
            error: function (error) {
                console.log(error)
                alert(error);
                //location.reload();
            },
            async: true,
            data: formData,
            cache: false,
            contentType: false,
            processData: false,

    });


    })

    $('#btn_save_rec').on('click', (key,value)=> {

        let endpoint = $('#ms_form_rec_endpoint').val()
        let api_key = $('#ms_form_rec_key').val()

        if (endpoint == null || api_key == null) {
            alert('all fields required')
        }

        let data = {
            'endpoint': endpoint,
            'key': api_key
        }

         $.ajax({
            type: "POST",
            url: "/api/config/setRecoginizerConfig/",
            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
            success: function (result) {
                   console.log(result)


            },
            error: function (error) {
                console.log(error)
                alert(error);
                //location.reload();
            },
            data: data,


    });



    })

});
*/