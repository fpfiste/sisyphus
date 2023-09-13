$(document).ready(function(){
    let page = window.location.pathname;

    $.ajax({
          url: '/static/config.json',
          dataType: 'json',
          success: function (response) {
            let lang_cookie = Cookies.get('sisyphus_language');
            $.each(response['translations'], (key, value)=> {
                $('#' + key).text(value[lang_cookie])
            })
            console.log(lang_cookie)
            let page_title = response['pages'][page]['title'][lang_cookie]
            console.log(page_title)
            $('#page_title').text(page_title);
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
    console.log()
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










});