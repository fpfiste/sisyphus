
jQuery.fn.setUp = function(page_config, fields) {

    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');


    $.when(
            $.ajax({url: '/api/employees/get_active_user/' ,type: 'GET'}),
            $.ajax({url: '/api/tasks/getoverview/' ,type: 'GET'}),
            $.ajax({url: '/api/sales/getoverview/' ,type: 'GET'}),
            $.ajax({url: '/api/receivables/getoverview/' ,type: 'GET'})
    ).done((active_user, task_overview, sales_overview, receivables_overview)=> {

            // greet user
            let greeting = $('#home_greeting').text()
            $('#home_greeting').text(greeting + ', '+ active_user[0]['firstname'])

            console.log(task_overview)
            // Add task and sale summary to cards
            let open = 0 + task_overview[0]['open']
            let scheduled = 0 + task_overview[0]['scheduled']
            let executed = 0 + task_overview[0]['executed']
            let to_bill = 0 + task_overview[0]['to_bill']

            $('#home_open_value').text(open)
            $('#home_scheduled_value').text(scheduled)
            $('#home_executed_value').text(executed)
            $('#home_to_bill_value').text(to_bill)


            console.log(sales_overview)
            // add sales overview
            to_bill = 0  + sales_overview[0]['to_bill']
            $('#sales_to_bill').text(to_bill)
            // list currently running tasks


            // Add receivables summary to cards
            let created = 0 + receivables_overview[0]['created']
            let exported = 0 + receivables_overview[0]['exported']


            $('#home_receivables_open_value').text(created)
            $('#home_receivables_exported_value').text(exported)

        }


    )

}

/*



    $.ajax({
          url: '/api/tasks/getoverview/',
          async: false,
          dataType: 'json',
          success: function (response) {

            $('#loading_screen_wrapper').toggle();

          }
    });

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

    $.ajax({
          url: '/api/tasks/get_ongoing_tasks/',
          async: false,
          dataType: 'json',
          success: function (response) {
            console.log(response)
          }
    });


}

*/