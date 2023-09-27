
$(document).ready(function(){
    let page_config
    let url = '/assets/absences'



    //*** read the config file ***//
    $.ajax({
          url: '/_config',
          async: false,
          dataType: 'json',
          success: function (response) {
            page_config = response['pages'][url]
            translations = response['translations']
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





});
