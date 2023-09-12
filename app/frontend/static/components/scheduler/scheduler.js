

class Scheduler{

      constructor({container, id, data, scheduleDate}) {
          this.container = container;
          this.id = id;
          this.data = data
          this.employee_url = '/api/employees/';
          this.employee_data = this.ajax_call(this.employee_url, 'GET');
          this.asset_url = '/api/assets';
          this.asset_data = this.ajax_call(this.asset_url, 'GET');
          this.task_url = '/api/tasks/listday/';
          this.task_data = this.ajax_call(this.task_url, 'GET');
          this.get_date_url = '/api/tasks/getDate/'
          this.set_date_url = '/api/tasks/setDate/'
          this.schedule_date = this.ajax_call(this.get_date_url, 'GET')['date'];
          this.scheduleDateStart = new Date(this.schedule_date + ' 00:00:00');
          this.scheduleDateEnd = new Date(this.schedule_date + ' 23:59:00');

          this.build_grid()
      }


      ajax_call(url, type, data) {
           let result;

           $.ajax({
               url: url,
               type: type,
               data: data,
               async: false,
               success: function(response) {
                 result =  response;
               }
            });

        return result;
      }


      build_grid() {
          $(this.container).empty();

            //* draw the grid of the new table object
            let table_grid = '<div id="scheduler_container" style="overflow:scroll;"><table id="schedule_table" class="table"><thead style="position:sticky; top:0;"></thead><tbody></tbody><tfoot></tfoot></table></div>';
            $(this.container).append(table_grid);

            let header =  '<tr><th><input type="date" id="scheduler_date_input" class="scheduler-first-column" value="'+this.schedule_date+'" /></th><th class="scheduler-second-column" ><button><i class="fa-solid fa-chevron-left"></i></button><button><i class="fa-solid fa-chevron-right"></i></button></th><div class="overflow_part>"'
            for (let i = 0; i < (25); i++){
                header += '<th colspan="4">'+i+':00</th>'
            }
            header += '</div></tr>'
            header +='<tr><th class="scheduler-first-column">Mitarbeiter</th><th class="scheduler-second-column" >Geräte</th>'

            for (let i = 1; i < (97); i++){
                header += '<th></th>'
            }
            header += '</tr>'
            $('#scheduler_container thead').append(header);
            //$('#schedule_table').append('<tr></tr>');

            $.each(this.employee_data, (key,value) => {
                let row = '<tr id="employee_'+value.id_employee+'"><td class="scheduler-first-column">'+value.employee_internal_alias+'</td><td id="resource_lane_'+value.id_employee+'"><ul style="list-style:None; padding: 0px; margin-bottom: 0px;"></ul></td><td id="task_lane_'+value.id_employee+'" class="task_lane" colspan="100" ><ul style="list-style:None; padding: 0px; margin-bottom: 0px;"></ul></td></tr>'
                $('#schedule_table').append(row);
            })

            let footer = '<tr id="open_task_row"><td colspan="2">Open Tasks</td><td colspan="100"></td></tr>'
            $('#schedule_table tfoot').append(footer);
      }


      get_asset(asset_id) {
         let asset = this.asset_data.filter(a => a.id_asset == asset_id);

         return asset[0]
      }

      add_row(employee_id, task_id, task_title, event_box_width, left, asset_1, asset_2) {
        let task_span = '<li><span class="scheduled_task_span badge badge-primary" style = "box-sizing: border-box; margin-left:' + left + 'px; width:' + event_box_width + 'px">'+ task_title +'</span></li>'
        let task_lane = $('#task_lane_'+employee_id + ' ul').append(task_span);

        asset_1 = this.get_asset(asset_1);
        asset_2 = this.get_asset(asset_2);

        let asset_html = '<li>';
        if ( asset_1 ) {
            asset_html += '<span class="asset_span badge badge-primary">'+ asset_1.asset_internal_alias +'</span>'
        }

        if ( asset_2 ) {
            asset_html += '<span class="asset_span badge badge-primary">'+ asset_2.asset_internal_alias +'</span>'
        }

        asset_html += '</li>'

        $('#resource_lane_'+employee_id + ' ul').append(asset_html)


      }

      populate() {
        $.each(this.task_data, (key,value) => {
            let startDate = new Date(value.task_date_from +' '+value.task_time_from);
            let endDate = new Date(value.task_date_to +' '+ value.task_time_to);
            if (this.scheduleDateStart > startDate) {
                startDate = this.scheduleDateStart
            }

            if (this.scheduleDateEnd < endDate) {
                endDate = this.scheduleDateEnd;
            }

            let width_of_time_table = $('#task_lane_'+value.fk_employee_1).width()
            let event_duration = (endDate - startDate) / 1000 / 60 / 60
            let event_box_width = width_of_time_table / 24 * event_duration


            let left_offset_h = (startDate - this.scheduleDateStart) / 1000 / 60 / 60;

            let left_offset_px = width_of_time_table / 24 * left_offset_h;
            console.log(left_offset_px)

            this.add_row(value.fk_employee_1, value.id_task, value.fk_project + '-' + value.task_description, event_box_width, left_offset_px, value.fk_asset_1, value.fk_asset_2)
        })




      }

      create_event_handlers() {
            $('#scheduler_date_input').on("change", ()=> {
                let date = $('#scheduler_date_input').val();
                date = this.ajax_call(this.set_date_url, 'POST', {'date': date})
                this.task_data =  this.ajax_call(this.task_url, 'GET');
                this.schedule_date = date['date']
                this.build()
            })





      }


      build(){
         this.build_grid();
         this.populate();
         this.create_event_handlers();

      }

}