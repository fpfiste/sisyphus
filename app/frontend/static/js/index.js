$(document).ready(function(){
    //$('#loading_screen_wrapper').show();
    let page = window.location.pathname;
    let page_config;
    let fields;

    $.ajax({
          url: '/_config',
          dataType: 'json',
          async : true,
          success: function (response) {
            let lang_cookie = Cookies.get('sisyphus_language');
            page_config = response['pages'][page]
            fields = response['fields']
            $.each(response['translations'], (key, value)=> {
                $('#' + key).text(value[lang_cookie])
            })

            let page_title = response['pages'][page]['title'][lang_cookie]
            $('#page_title').text(page_title);
            document.title = page_title;

            $.fn.setUp(page_config, fields);

            $.each(page_config['remove_buttons'], (key, value)=>{
                $('#' + value).remove();

            })
            //$('#loading_screen_wrapper').hide();
          }
    });



    $('#language_selector').on('change', function() {
        console.log($(this).val())
        Cookies.set('sisyphus_language', $(this).val())
        location.reload();
        //*** read the config file ***//
        $.ajax({
              url: '/static/config.json',
              dataType: 'json',
              success: function (response) {
                console.log(response)
                $.each(response['translations'], (key, value)=> {
                let lang_cookie = Cookies.get('sisyphus_language');
                    $('#' + key).text(value[lang_cookie])
                })


              }
        });

    })

    let lang = Cookies.get('sisyphus_language');

    if (!lang) {
        lang = 'CH'
        $('#language_selector').val('ch')
        Cookies.set('sisyphus_language', 'ch')
    } else {
        $('#language_selector').val(lang)
    }

    $('.sidebar-toggle ').on('click', function(){
        $('#sidebar').toggle();
    })

    $('#update_modal, #create_modal').on('hide.bs.modal', function() {
        let form = $(this).find('form').trigger('reset')
        console.log(form)
        //.trigger("reset")
        $(form).find(':input').css('border-color', '')

    })










});