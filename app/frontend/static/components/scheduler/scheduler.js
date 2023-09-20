

class Scheduler{

      constructor({container, id, data, scheduleDate, employee_label, asset_label, subcontractor_label, open_task_label}) {
          this.container = container;
          this.id = id;
          this.data = data
          this.employee_url = '/api/employees/?fk_sys_rec_status=1';
          this.subcontractor_url = '/api/companies?is_subcontractor=1'
          this.asset_url = '/api/assets';
          this.task_url = '/api/tasks/listday/';
          this.open_tasks_url = '/api/tasks/getOpenTasks/'
          this.get_date_url = '/api/tasks/getDate/'
          this.set_date_url = '/api/tasks/setDate/'
          this.schedule_date = Cookies.get('scheduler_date')  || new Date().toISOString().split('T')[0];
          this.employee_label= employee_label
          this.asset_label= asset_label
          this.subcontractor_label = subcontractor_label
          this.open_task_label = open_task_label
          this.show_subus = (Cookies.get('show_subus') ==='true') ? true : false;
          console.log(this.show_subus)
          this.build_grid()
      }

      get_date(){
        console.log(document.schedule_date)

      }
      ajax_call(url, type, data) {
           let result;

           return $.ajax({
               url: url,
               type: type,
               data: data,
               //async:false,
            });

        //return result;
      }


      draw_drop_down_select() {
        let drp = '<div class="dropdown">'+
                       '<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true">Dropdownd</button>' +
                            '<ul class="dropdown-menu" id=scheduler_dropdown aria-labelledby="dropdownMenu1">' +
                            '<li ><label><input type="checkbox"> Mitarbeiter</label></li>' +
                            '<li><label><input type="checkbox"> Subunternehmer</label></li>' +
                            '<li><label><input type="checkbox"> Offene Aufträge</label></li>' +
                       '</ul>' +
                  '</div>'


        return drp
      }

      draw_header() {

          let header = '<thead style="position:sticky; top:0;">'
          let input_row =  '<tr id="scheduler_input_row">' +
                                '<th colspan ="2">'+
                                    '<div class="row">' +
                                        '<div class="col">' +
                                            '<input type="date"  id="scheduler_date_input" class="scheduler-first-column" value="'+this.schedule_date+'"/>'+
                                        '</div>' +
                                        '<div class="col">' +
                                            '<button  id="scheduler_prev_date"><i class="fa-solid fa-chevron-left"></i></button>'+
                                            '<button  id="scheduler_next_date"><i class="fa-solid fa-chevron-right"></i></button>' +
                                         '</div>' +
                                    '</div>' +
                                    '<div class="row">' +
                                        '<div class="col">' +
                                            '<div class="form-check">' +
                                                '<input class="form-check-input" type="checkbox" value="" id="show_subus"'+ ((this.show_subus === true) ? 'checked' : '')+ '>' +
                                                '<label class="form-check-label" for="show_subus">' + this.subcontractor_label + '</label>' +
                                            '</div>' +
                                        '</div>' +
                                    '</div>' +
                                '</th>'+
                                '<th colspan="100"></th>'+

                           '</tr>'


          let title_row = '<tr id="scheduler_title_row">' +
                            '<th class="scheduler-first-column" id="scheduler_employee_label">'+this.employee_label+'</th>'+
                            '<th class="scheduler-second-column" id="scheduler_asset_label">'+this.asset_label+'</th>'

          let spacer_row = '<tr id="scheduler_spacer_row">'+
                                '<th class="scheduler-first-column"></th>'+
                                '<th class="scheduler-second-column"></th>'


          for (let i = 1; i < (25); i++){
              title_row += '<th class="scheduler_time_titles">'+i+':00</th>'
              spacer_row += '<th class="scheduler_time_ticks"></th>'
          }

          title_row += '</tr>'
          spacer_row +='</tr>'

          header += input_row
          header += title_row
          header += spacer_row
          header += '</thead>'

          return header
      }



      draw_body() {
        let body = '</tbody>'


        $.each(this.employee_data, (key,value) => {
            let row = '<tr id="e'+value.id_employee+'">' +
                            '<td class="scheduler-first-column">'+value.employee_internal_alias+'</td> '+
                            '<td id="resource_lane_e'+value.id_employee+'">'+
                                '<ul style="list-style:None; padding: 0px; margin-bottom: 0px;"></ul>'+
                            '</td>'+
                            '<td id="task_lane_e'+value.id_employee+'" class="task_lane" colspan="100" >' +
                                '<ul style="list-style:None; padding: 0px; margin-bottom: 0px;"></ul>'+
                            '</td>'+
                        '</tr>'
            body += row;
        })


        if (this.show_subus) {
            body += '<tr id="scheduler_sub_contractor_header"><th colspan="2" id="scheduler_subcontractor_label">'+this.subcontractor_label+'</th><th colspan="100"></th></tr>'
          $.each(this.subcontractor_data, (key,value) => {
            let row = '<tr id="s'+value.id_company+'">' +
                            '<td class="scheduler-first-column">'+value.company_internal_alias+'</td> '+
                            '<td id="resource_lane_s'+value.id_company+'">'+
                                '<ul style="list-style:None; padding: 0px; margin-bottom: 0px;"></ul>'+
                            '</td>'+
                            '<td id="task_lane_s'+value.id_company+'" class="task_lane" colspan="100" >' +
                                '<ul style="list-style:None; padding: 0px; margin-bottom: 0px;"></ul>'+
                            '</td>'+
                        '</tr>'
            body += row;
        })

        }




        body += '</tbody>'
        return body
      }

      draw_footer() {
        let footer = '<tfoot>'

        footer += '<tr id="open_task_row">' +
                        '<th colspan="2" id="scheduler_open_task_label">'+this.open_task_label+'</th>'+
                        '<td id="task_lane_o" colspan="100"></td>' +
                    '</tr>'

        footer += '</tfoot>'
        return footer
      }


      build_grid() {
          $(this.container).empty();

            let header = this.draw_header();
            let body = this.draw_body();
            let footer = this.draw_footer();
            //* draw the grid of the new table object
            let table_grid = '<div id="scheduler_container" style="overflow:scroll; min-height:100%; height:100%;"><table id="schedule_table" class="table" style="height:100%">'+header+body+footer+'</table></div>';
            $(this.container).append(table_grid);
      }


      get_asset(asset_id) {
         let asset = this.asset_data.filter(a => a.id_asset == asset_id);
         return asset[0]
      }



      add_row(row_id, task_id, task_title, startDate, endDate, asset_1, asset_2) {

        let width_of_time_table = $('#task_lane_'+row_id).width()
        let event_duration = (endDate - startDate) / 1000 / 60 / 60
        let event_box_width = width_of_time_table / 24 * event_duration

        if (event_box_width == '') {
            event_box_width = '100px'
        }

        let left_offset_h = (startDate - this.scheduleDateStart) / 1000 / 60 / 60;
        let lane_height = $('#task_lane_'+row_id).height()
        console.log(lane_height)
        let left_offset_px = width_of_time_table / 24 * left_offset_h;
        let task_span = '<li><span class="task scheduled_task badge badge-primary" style = "box-sizing: border-box; margin-left:' + left_offset_px + 'px; width:' + event_box_width + 'px;" data-row-pk="'+task_id+'">'+ task_title +'</span></li>'
        let task_lane = $('#task_lane_'+row_id + ' ul').append(task_span);

        asset_1 = this.get_asset(asset_1);
        asset_2 = this.get_asset(asset_2);

        let asset_html = '<li>';
        if ( asset_1 ) {
            asset_html += '<span class="asset badge badge-primary">'+ asset_1.asset_internal_alias +'</span>'
        }

        if ( asset_2 ) {
            asset_html += '<span class="asset badge badge-primary">'+ asset_2.asset_internal_alias +'</span>'
        }

        asset_html += '</li>'

        $('#resource_lane_'+row_id + ' ul').append(asset_html)


      }


      populate() {

          this.scheduleDateStart = new Date(this.schedule_date + ' 00:00:00');
          this.scheduleDateEnd = new Date(this.schedule_date + ' 23:59:00');
            $.each(this.task_data, (key,value) => {
                let startDate = new Date(value.task_date_from +' '+value.task_time_from);
                let endDate = new Date(value.task_date_to +' '+ value.task_time_to);
                if (this.scheduleDateStart > startDate) {
                    startDate = this.scheduleDateStart
                }

                if (this.scheduleDateEnd < endDate) {
                    endDate = this.scheduleDateEnd;
                }



                this.add_row('e'+value.fk_employee_1, value.id_task, value.fk_project + '-' + value.task_description, startDate, endDate, value.fk_asset_1, value.fk_asset_2)
                this.add_row('e'+value.fk_employee_2, value.id_task, value.fk_project + '-' + value.task_description, startDate, endDate, value.fk_asset_1, value.fk_asset_2)
                this.add_row('s'+value.fk_subcontractor, value.id_task, value.fk_project + '-' + value.task_description, startDate, endDate, value.fk_asset_1, value.fk_asset_2)
            })

          $.each(this.open_tasks, (key,value) => {
                 let task_span = '<span class="task open_task badge badge-primary" style = "box-sizing: border-box; margin-left: 1vw; width: 200px" data-row-pk="'+value.id_task+'">'+ value.id_task +'-' + value.task_description +'</span>'
                 $('#task_lane_o').append(task_span)

          })




      }

      create_event_handlers() {
            $('#scheduler_date_input').on("change", ()=> {
                let date = $('#scheduler_date_input').val();
                console.log(date)
                Cookies.set('scheduler_date', date);
                this.schedule_date = date;


                this.build()
            })

            $('.scheduled_task, .open_task').on( "dblclick", function() {
                let record_id =  $(this).attr('data-row-pk');

                $.ajax({
                    url: window.location.origin +'/api/tasks/' + record_id,
                    success: function (result) {

                        console.log(result)
                        $.each(result, (key, value)=>{

                            if (value === true){
                                value = 1;
                            } else if (value === false){
                                value = 0;
                            }
                            $('#update_form #'+ key).val(value);
                        });

                        $('#update_modal').modal('show');
                    }
                    })
    } );

            $('#show_subus').on('change', ()=> {
                console.log(this.show_subus)
                this.show_subus = !this.show_subus;
                Cookies.set('show_subus', this.show_subus);
                this.build();
            })

            $('#scheduler_prev_date').on('click', ()=> {
                let d = new Date(this.schedule_date)
                console.log(d.toISOString())
                d.setDate(d.getDate() - 1)
                let date = d.toISOString().split('T')[0];
                this.schedule_date = date;
                Cookies.set('scheduler_date', date);
                this.build();
            })

            $('#scheduler_next_date').on('click', ()=> {
                let d = new Date(this.schedule_date)
                console.log(d.toISOString())
                d.setDate(d.getDate() + 1)
                let date = d.toISOString().split('T')[0];
                this.schedule_date = date;
                Cookies.set('scheduler_date', date);
                this.build();
            })

      }


      build(){
        $.when(
            this.ajax_call(this.employee_url, 'GET'),
            this.ajax_call(this.subcontractor_url, 'GET'),
            this.ajax_call(this.asset_url, 'GET'),
            this.ajax_call(this.task_url + '?date='+ this.schedule_date, 'GET'),
            this.ajax_call(this.open_tasks_url, 'GET')


        ).done((empl, subcon, asset, tasks, open_tasks)=> {
            this.employee_data = empl[0]
            this.subcontractor_data = subcon[0]
            this.asset_data = asset[0]
            this.task_data = tasks[0]
            this.open_tasks = open_tasks[0]
            this.build_grid();
            this.populate();
            this.create_event_handlers();
        }


        )


      }

}