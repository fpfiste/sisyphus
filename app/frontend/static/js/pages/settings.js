
$(document).ready(function(){
    let page_config
    let url = '/settings'
    let lang_cookie = Cookies.get('sisyphus_language');
    $('#loading_screen_wrapper').toggle();
    //*** read the config file ***//
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
