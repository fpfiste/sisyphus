jQuery.fn.setUp = function(page_config, fields) {
    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');

    $.when(
      $.ajax({url: '/_list_media' ,type: 'GET'})
    ).done((files)=> {
        console.log(files)

        $.each(files['data'], (key, value)=>{

           let file_ending = value.split('.').at(-1)
           let file_name = value.split('/').at(-1)

           let image_url = '/static/img/txt.png'
           if (file_ending == 'csv') {
            image_url = '/static/img/csv.png'
           } else if  (file_ending == 'pdf') {
            image_url = '/static/img/pdf.png'
           } else if ((file_ending == 'xls') | (file_ending == 'xlsx')) {
           image_url = '/static/img/xls.png'
           }

           let card = ''
           card += '<div class="file-wrapper card" style="width: 10%; height: 200px; margin: 5px;" data-file-path="'+value+'">'

           card += '<div class="card-body">'
           card += '<img class="card-img-top" src="'+image_url+'" style="display:block; margin:auto; width: 75%; max-width: 100px;>'
           card += '<p class="card-text"></p>'
           card += '<h5 class="card-title" style="text-align:center;">'+file_name+'</h5>'

           card += '</div></div>'

           $('#file_container').append(card)


        })

        $('.file-wrapper').on('click', (e)=>{
            console.log(e.currentTarget)
            let file = $(e.currentTarget).attr('data-file-path')
            $('.file-wrapper').css('border', '')
            $(e.currentTarget).css('border', '1px solid red')

            $('#btn_download').parent().attr('href', file)


        })


        })




}