

class Scheduler{

      constructor({container, id, data, scheduleDate, employee_label, asset_label, open_task_label, employee_type_label}) {
          this.container = container;
          this.id = id;
          this.data = data
          this.employee_url = '/api/employees/?fk_sys_rec_status=1&SORT=employee_internal_alias';
          this.employee_type_url = '/api/employees/types/'
          this.asset_url = '/api/assets';
          this.task_url = '/api/tasks/listday/';
          this.open_tasks_url = '/api/tasks/getOpenTasks/'
          this.get_date_url = '/api/tasks/getDate/'
          this.set_date_url = '/api/tasks/setDate/'
          this.schedule_date = Cookies.get('scheduler_date')  || new Date().toISOString().split('T')[0];
          this.excluded_employee_types = (Cookies.get('excluded_employee_types')  || '').split(',');
          this.employee_label= employee_label
          this.employee_type_label = employee_type_label
          this.asset_label= asset_label
          this.open_task_label = open_task_label
          this.build_grid()
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


      checkbox(id, value, label) {
        let checked = ''
        if (this.excluded_employee_types.includes(value.toString())){
            checked = ''
        } else {
            checked = 'checked'
        }
        let checkbox = '<div class="form-check">'
        checkbox += '<input class="form-check-input employee_type_checkbox" type="checkbox" value="'+value+'" id="'+id+'" '+checked +'>'
        checkbox += '<label class="form-check-label" for="'+id+'">'+label+'</label>'
        checkbox += '</div>'

        return  checkbox
      }

      drop_down() {
        let drop_down = '<div id="employee_type_filter" class="dropdown show">'
        drop_down += '<a class="btn btn-light dropdown-toggle" role="button" id="employee_type_dropdown_button" aria-expanded="false">'+this.employee_type_label+'</a>'
        drop_down += '<div id="employee_type_filter_dropdown" class="dropdown-menu">'
        $.each(this.employee_types, (key, value)=>{
            drop_down += this.checkbox(value['id_employee_type'], value['id_employee_type'], value['employee_type_description'])
        })
        drop_down += '<hr>'

        drop_down += '<button type="button" class="btn btn-danger btn-sm" id="schedule_employee_type_fitler_btn">Filter</button>'
        drop_down += '</div></div>'





        return drop_down

      }

      draw_input_section() {
               let input = '<div class="row" style="min-height:10%; height:10%;">' +
                                        this.drop_down() +
                                     '<div id="date_input_section">'+
                                            '<input type="date"  id="scheduler_date_input" class="scheduler-first-column" value="'+this.schedule_date+'"/>'+
                                            '<button  id="scheduler_prev_date"><i class="fa-solid fa-chevron-left"></i></button>'+
                                            '<button  id="scheduler_next_date"><i class="fa-solid fa-chevron-right"></i></button>' +
                                    '</div></div>'
            return input;
      }

      draw_header() {

          let header = '<thead style="position:sticky; top:0;">'



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


          header += title_row
          header += spacer_row
          header += '</thead>'

          return header
      }



      draw_body() {
        let body = '</tbody>'


        $.each(this.employee_data, (key,value) => {
            if (!this.excluded_employee_types.includes(value['fk_employee_type']['id_employee_type'].toString())){
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
            }

        })







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
            let input_section = this.draw_input_section()
            let header = this.draw_header();
            let body = this.draw_body();
            let footer = this.draw_footer();
            //* draw the grid of the new table object
            let table_grid = input_section+'<div id="scheduler_container" style="overflow:scroll; min-height:90%; height:90%;"><table id="schedule_table" class="table" style="height:100%">'+header+body+footer+'</table></div>';
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



                this.add_row('e'+value.fk_employee_1, value.id_task, value.id_task + '-' + value.description, startDate, endDate, value.fk_asset_1, value.fk_asset_2)
                this.add_row('e'+value.fk_employee_2, value.id_task, value.id_task + '-' + value.description, startDate, endDate, value.fk_asset_1, value.fk_asset_2)
                this.add_row('s'+value.fk_subcontractor, value.id_task, value.id_task + '-' + value.description, startDate, endDate, value.fk_asset_1, value.fk_asset_2)
            })

          $.each(this.open_tasks, (key,value) => {
                 let task_span = '<span class="task open_task badge badge-primary" style = "box-sizing: border-box; margin-left: 1vw; width: 200px" data-row-pk="'+value.id_task+'">'+ value.id_task +'-' + value.description +'</span>'
                 $('#task_lane_o').append(task_span)

          })




      }

      create_event_handlers() {
            $('#scheduler_date_input').on("change", ()=> {
                let date = $('#scheduler_date_input').val();
                Cookies.set('scheduler_date', date);
                this.schedule_date = date;


                this.build()
            })

            $('.scheduled_task, .open_task').on( "dblclick", function() {
                let record_id =  $(this).attr('data-row-pk');

                $.ajax({
                    url: window.location.origin +'/api/tasks/' + record_id,
                    success: function (result) {

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



            $('#scheduler_prev_date').on('click', ()=> {
                let d = new Date(this.schedule_date)
                d.setDate(d.getDate() - 1)
                let date = d.toISOString().split('T')[0];
                this.schedule_date = date;
                Cookies.set('scheduler_date', date);
                this.build();
            })

            $('#scheduler_next_date').on('click', ()=> {
                let d = new Date(this.schedule_date)
                d.setDate(d.getDate() + 1)
                let date = d.toISOString().split('T')[0];
                this.schedule_date = date;
                Cookies.set('scheduler_date', date);
                this.build();
            })

            $('#employee_type_dropdown_button').on('click', ()=> {
                $('#employee_type_filter_dropdown').toggle();
            })

            $('#schedule_employee_type_fitler_btn').on('click', ()=>{
                let exclude = []

                let unchecked = $('.employee_type_checkbox:checkbox:not(:checked)')
                $.each(unchecked, (index, value)=>{
                    exclude.push(value.value)
                })

                Cookies.set('excluded_employee_types', exclude);
                this.excluded_employee_types = exclude
                console.log(this.excluded_employee_types)
                this.build();


            })

            $('employee_type_filter_dropdown').on('focusout', function () {
                 $('#employee_type_filter_dropdown').hide();
            });


      }


      build(){
        $.when(
            this.ajax_call(this.employee_url, 'GET'),
            this.ajax_call(this.employee_type_url, 'GET'),
            this.ajax_call(this.asset_url, 'GET'),
            this.ajax_call(this.task_url + '?date='+ this.schedule_date, 'GET'),
            this.ajax_call(this.open_tasks_url, 'GET')


        ).done((empl, empl_type, asset, tasks, open_tasks)=> {
            this.employee_data = empl[0]['data']
            console.log(this.employee_data)
            this.employee_types = empl_type[0]['data']
            this.asset_data = asset[0]['data']
            this.task_data = tasks[0]
            this.open_tasks = open_tasks[0]
            this.build_grid();
            this.populate();
            this.create_event_handlers();
        }


        )


      }

}