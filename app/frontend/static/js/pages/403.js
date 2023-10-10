
jQuery.fn.setUp = function(page_config, fields) {
    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');

    $('#error_message').text(page_config['message'][lang_cookie])




}