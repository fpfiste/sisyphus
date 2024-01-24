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
           } else if (file_ending == 'xls') {
           image_url = '/static/img/xls.png'
           }




           let card = ''
           card += '<div class="" style="width: 7%; margin-left: 50px;">'
           card += '<a  href="'+value+'"><img class="card-img-top" src="'+image_url+'" alt="Card image cap"></a>'
           card += '<div class="card-body">'
           card += '<h5 class="card-title" style="text-align:center;">'+file_name+'</h5>'
           card += '<p class="card-text"></p>'
           card += '</div></div>'

           $('#file_container').append(card)

        })


        })




}