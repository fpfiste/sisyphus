
jQuery.fn.setUp = function(page_config, fields) {

    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');

    // GET THE ACTIVE USER
    $.ajax({
          url: '/api/employees/get_active_user/',
          async: true,
          dataType: 'json',
          success: function (response) {
            let greeting = $('#home_greeting').text()
            console.log(greeting)
            $('#home_greeting').text(greeting + ', '+ response['firstname'])
            console.log($('#home_greeting').text())


          }
    });


    //*** read the open tasks ***//
    $.ajax({
          url: '/api/tasks/getoverview/',
          async: false,
          dataType: 'json',
          success: function (response) {
            console.log(response)
            let open = $('#home_open_value').text()
            let scheduled = $('#home_scheduled_value').text()
            let executed = $('#home_executed_value').text()
            let to_bill = $('#home_to_bill_value').text()

            $('#home_open_value').text( Number(open) + Number(response['open']))
            $('#home_scheduled_value').text( Number(scheduled) + Number(response['scheduled']))
            $('#home_executed_value').text( Number(executed) + Number(response['executed']))
            $('#home_to_bill_value').text( Number(to_bill) + Number(response['to_bill']))
            $('#loading_screen_wrapper').toggle();

          }
    });

    //*** read the sales to bill ***//
    $.ajax({
          url: '/api/sales/getoverview/',
          async: false,
          dataType: 'json',
          success: function (response) {
            console.log(response)

            let to_bill = $('#home_to_bill_value').text()


            $('#home_to_bill_value').text( Number(to_bill) + Number(response['to_bill']))
          }
    });




}

