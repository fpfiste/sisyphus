
jQuery.fn.setUp = function(page_config, fields) {

    // create table instance
    let lang_cookie = Cookies.get('sisyphus_language');


    $.when(
            $.ajax({url: '/api/employees/get_active_user/' ,type: 'GET'}),
            $.ajax({url: '/api/tasks/getoverview/' ,type: 'GET'}),
            $.ajax({url: '/api/sales/getoverview/' ,type: 'GET'}),
            $.ajax({url: '/api/tasks/get_ongoing_tasks/' ,type: 'GET'})
    ).done((active_user, task_overview, sales_overview, ongoing_tasks)=> {

            // greet user
            let greeting = $('#home_greeting').text()
            $('#home_greeting').text(greeting + ', '+ active_user[0]['firstname'])

            // Add task and sale summary to cards
            let open = 0 + task_overview[0]['open']
            let scheduled = 0 + task_overview[0]['scheduled']
            let executed = 0 + task_overview[0]['executed']
            let to_bill = 0 + task_overview[0]['to_bill'] + sales_overview[0]['to_bill']

            $('#home_open_value').text(open)
            $('#home_scheduled_value').text(scheduled)
            $('#home_executed_value').text(executed)
            $('#home_to_bill_value').text(to_bill)


            // list currently running tasks
            let html

            $.each(ongoing_tasks[0], (key,value)=>{
                html = '<div class="card" style="height:30%;">'
                html += '   <div class="card-body" style="display:flex; height:100%;">'
                html += '       <div style="width:50%;">'
                html += '           <h1 class="card-title">Auftrag '+ value.id_task + '</h5>'
                html += '           <div style="display:flex; flex-direction: column; flex-wrap:wrap; height:90%; padding-bottom:2px; column-gap: 150px;">'
                html += '               <div style="display:flex; align-items:center;  overflow: hidden;"><span style="font-size:12px; width: 100px;">Projekt: </span><p class="card-text" style="text-align:right; width: 100px;">'+ value.fk_project+'</p></div>'
                html += '               <div style="display:flex; align-items:center;  overflow: hidden;"><span style="font-size:12px; width: 100px;">Start: </span><p class="card-text" style="text-align:right; width: 100px;">'+ value.task_date_from+'</p></div>'
                html += '               <div style="display:flex; align-items:center;  overflow: hidden;"><span style="font-size:12px; width: 100px;">Ende: </span><p class="card-text" style="text-align:right; width: 100px;">'+ value.task_date_to+'</p></div>'
                html += '               <div style="display:flex; align-items:center;  overflow: hidden;"><span style="font-size:12px; width: 100px;">Beschreibung: </span><p class="card-text" style="text-align:right; width: 100px;">'+ value.description+'</p></div>'
                html += '               <div style="display:flex; align-items:center;  overflow: hidden;"><span style="font-size:12px; width: 100px;">Mitarbeiter 1: </span><p class="card-text" style="text-align:right; width: 100px;">'+ value.fk_employee_1+'</p></div>'
                html += '               <div style="display:flex; align-items:center;  overflow: hidden;"><span style="font-size:12px; width: 100px;">Mitarbeiter 2: </span><p class="card-text" style="text-align:right; width: 100px;">'+ value.fk_employee_2+'</p></div>'
                html += '               <div style="display:flex; align-items:center;  overflow: hidden;"><span style="font-size:12px; width: 100px;">Asset 1: </span><p class="card-text" style="text-align:right; width: 100px;">'+ value.fk_asset_1+'</p></div>'
                html += '               <div style="display:flex; align-items:center;  overflow: hidden;"><span style="font-size:12px; width: 100px;">Asset 2: </span><p class="card-text" style="text-align:right; width: 100px;">'+ value.fk_asset_2+'</p></div>'
                html += '           </div>'
                html += '       </div>'
                html += '   </div>'
                html += '</div>'

                $('#home_ongoing_tasks_card .card-body').append(html)

            })
            console.log(active_user)
            console.log(task_overview)
            console.log(sales_overview)
            console.log(ongoing_tasks)
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