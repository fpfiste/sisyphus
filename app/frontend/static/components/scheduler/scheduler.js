

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
              title_row += '<th class="scheduler_time_titles" style="width:96px;">'+i+':00</th>'
              spacer_row += '<th class="scheduler_time_ticks" style="width:96px;"></th>'
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
                                '<ul class="task-lane-ul" data-employee='+value.id_employee+' style="list-style:None; padding: 0px; margin-bottom: 0px; height:100%;"></ul>'+
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



      add_row(row_id, task_id, task_title, startDate, endDate, asset_1, asset_2, employee, field, task_data) {

        let width_of_time_table = $('#task_lane_'+row_id).width()
        let event_duration = (endDate - startDate) / 1000 / 60 / 60
        let event_box_width = width_of_time_table / 24 * event_duration

        if (event_box_width == '') {
            event_box_width = '100px'
        }

        let left_offset_h = (startDate - this.scheduleDateStart) / 1000 / 60 / 60;
        let lane_height = $('#task_lane_'+row_id).height()
        let left_offset_px = width_of_time_table / 24 * left_offset_h;

        let right_offset = width_of_time_table - event_box_width - left_offset_px


        let lane = '<li id="task-lane-li-'+task_id+'" data-employee-row='+employee+' data-employee-update-field="'+field+'" class="scheduler-lane" draggable="true">'
        let task_lane = $('#task_lane_'+row_id + ' ul').append(lane);

        let task_object = '<div class="task scheduled_task badge badge-primary" style = "position:relative; box-sizing: border-box; margin-left:' + left_offset_px + 'px;  margin-right:' + right_offset + 'px;" data-row-pk="'+task_id+'" data-task-data='+encodeURIComponent(JSON.stringify(task_data))+'><div class="spacer-left" style="position:absolute; left: 0; top: 0; bottom: 0; width: 5px;cursor: e-resize;"></div>'+ task_title +'<div class="spacer-right" style="position:absolute; right: 0; top: 0; bottom: 0; width: 5px;cursor: e-resize;"></div></div></li>'
        $('#task_lane_'+row_id + ' ul #task-lane-li-'+task_id).append(task_object);

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



                this.add_row('e'+value.fk_employee_1, value.id_task, value.id_task + '-' + value.description, startDate, endDate, value.fk_asset_1, value.fk_asset_2, value.fk_employee_1, 'fk_employee_1', value)
                this.add_row('e'+value.fk_employee_2, value.id_task, value.id_task + '-' + value.description, startDate, endDate, value.fk_asset_1, value.fk_asset_2, value.fk_employee_2, 'fk_employee_2', value)

            })

          $.each(this.open_tasks, (key,value) => {
                 let task_span = '<span class="task open_task badge badge-primary" style = "box-sizing: border-box; margin-left: 1vw; width: 200px" data-row-pk="'+value.id_task+'">'+ value.id_task +'-' + value.description +'</span>'
                 $('#task_lane_o').append(task_span)

          })




      }

      round_time_to_quarter(time) {
            time.setMilliseconds(Math.round(time.getMilliseconds() / 1000) * 1000);
            time.setSeconds(Math.round(time.getSeconds() / 60) * 60);
            time.setMinutes(Math.round(time.getMinutes() / 15) * 15);
            return time;
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


            $('.scheduler-lane').on('dragstart', (event)=> {
                //event.preventDefault();
                console.log($(event.target))



                event.originalEvent.dataTransfer.setData('row_id', event.target.id);
                event.originalEvent.dataTransfer.setData('old-employee', event.target.getAttribute('data-employee-row'));

            });

            /*
            $('.task-lane-ul').on('dragenter', (event)=>{


                //$(event.currentTarget).css('border', '1px solid green')

            })

            */
            $('.task-lane-ul').on('dragover',(event)=> {
                //event.preventDefault();
                //$(event.currentTarget).css('border', '1px solid green')
                event.preventDefault();

                if (event.currentTarget.className == 'task-lane-ul') {
                     $(event.currentTarget).css('border', '5px solid green')
                }

            })


            $('.task-lane-ul').on('dragleave', (event) => {
                 event.preventDefault();
                 $(event.currentTarget).css('border', '')

            })


            $('.task-lane-ul').on('drop', (event)=> {
                event.preventDefault();
                event.stopPropagation();

                let row_id = event.originalEvent.dataTransfer.getData("row_id");
                //let employee_old =event.originalEvent.dataTransfer.getData("old-data");

                let new_employee = $(event.currentTarget).attr('data-employee')
                let old_employee = event.originalEvent.dataTransfer.getData("old-employee");

                //console.log(employee_old)

                let lane = $('#'+row_id)

                let taskdata = $('#'+row_id).find('.task').attr('data-task-data')

                taskdata = JSON.parse(decodeURIComponent(taskdata))

                if (event.currentTarget.className == 'task-lane-ul') {

                    $(event.currentTarget).css('border', '')




                    if ((new_employee == taskdata.fk_employee_1) | (new_employee == taskdata.fk_employee_2)) {
                        return

                    }

                    if (taskdata.fk_employee_1 == old_employee) {
                        taskdata['fk_employee_1'] = new_employee
                    } else {
                        taskdata['fk_employee_2'] = new_employee
                    }


                    let proxy_this = this

                    $.ajax({
                    url: window.location.origin +'/api/tasks/' + taskdata.id_task + '/',
                    method: 'PUT',
                    headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                    data: taskdata,
                    success: function (result) {
                        $(lane).attr('data-employee-row', new_employee)
                        $(lane).find('.task').attr('data-task-data', encodeURIComponent(JSON.stringify(result)))
                        $(event.currentTarget).append(lane);

                        var items = $(event.currentTarget).find('li').get();


                        items.sort(function(a,b){
                          var keyA = $(a).find('.task').attr('data-task-data');

                          keyA = JSON.parse(decodeURIComponent(keyA))
                          keyA = keyA.task_date_from + ' ' + keyA.task_time_from
                          var keyB = $(b).find('.task').attr('data-task-data');
                          keyB = JSON.parse(decodeURIComponent(keyB))
                          keyB = keyB.task_date_from + ' ' + keyB.task_time_from

                          console.log(keyA)
                          console.log(keyB)
                          if (keyA < keyB) return -1;
                          if (keyA > keyB) return 1;
                          return 0;
                        });
                        var ul = $(event.currentTarget);
                        $.each(items, function(i, li){
                          ul.append(li); /* This removes li from the old spot and moves it */
                        });;
                    }
                    })
                    console.log(taskdata)


                }




            });


            $('.spacer-left').on('mousedown', (e)=>{
              e.preventDefault()
              let element = $(event.target).parent()

              let data = $(element).attr('data-task-data')
              data = JSON.parse(decodeURIComponent(data))


              console.log(data.task_date_from)
              console.log(this.schedule_date)
              if (data.task_date_from == this.schedule_date) {
                          let offset_l = $(element).css('margin-left')
                          offset_l =   Number(offset_l.substring(0, offset_l.length - 2));

                          let task_start_date = $(element)

                          let offset_r = $(element).css('margin-right')
                          offset_r =   Number(offset_r.substring(0, offset_r.length - 2));

                          let lane_width = $(element).parent().parent().width()
                          let min_width = $(element).parent().parent().width() / 24 / 4 //15 minutes


                          let initX = e.originalEvent.clientX



                          $(document).on('mousemove', (e)=> {

                            let current_position = e.originalEvent.clientX
                            let distance = initX - current_position

                            let new_offset = offset_l - distance
                            let new_width = lane_width - offset_r - new_offset
                            let parent_width =  $(element).parent().parent().width()

                            if ((new_width > min_width) & (new_offset > 0) ) {
                                new_offset  = Math.round(new_offset/min_width)*min_width


                                $("div")
                                    .find('[data-row-pk='+$(element).attr('data-row-pk')+']')
                                    .css('margin-left', new_offset +'px')
                            }



                            //element.style.width = e.pageX - element.getBoundingClientRect().left + 'px'
                          })
                          $(document).on('mouseup', (e)=> {
                            console.log('up')
                            let task_width = $(element).css('width')
                            task_width =   Number(task_width.substring(0, task_width.length - 2));

                            let task_offset_L = $(element).css('margin-left')
                            task_offset_L =   Number(task_offset_L.substring(0, task_offset_L.length - 2));

                            let total_width = $(element).parent().parent().width()

                            let offset_seconds = task_offset_L / total_width * 86000
                            let duration_seconds = task_width / total_width * 86000

                            let start_ts = this.round_time_to_quarter(new Date(0,0,0,0,0,offset_seconds))
                            let end_ts = this.round_time_to_quarter(new Date(0,0,0,0,0,offset_seconds + duration_seconds))

                            let data = $(element).attr('data-task-data')
                            data = JSON.parse(decodeURIComponent(data))

                            if (data.task_date_from == this.schedule_date) {
                                data['task_time_from'] = start_ts.toTimeString().split(' ')[0];
                            }

                            if (data.task_date_to == this.schedule_date) {
                                data['task_time_to'] = end_ts.toTimeString().split(' ')[0];
                            }

                            console.log(data)

                            $.ajax({
                                url: window.location.origin +'/api/tasks/' + data.id_task + '/',
                                method: 'PUT',
                                headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                                data: data,
                                success: function (result) {

                                    $(element).attr('data-task-data', encodeURIComponent(JSON.stringify(result)))


                                    var items = $(element).parent().parent().find('li').get();


                                    items.sort(function(a,b){
                                      var keyA = $(a).find('.task').attr('data-task-data');

                                      keyA = JSON.parse(decodeURIComponent(keyA))
                                      keyA = keyA.task_date_from + ' ' + keyA.task_time_from
                                      var keyB = $(b).find('.task').attr('data-task-data');
                                      keyB = JSON.parse(decodeURIComponent(keyB))
                                      keyB = keyB.task_date_from + ' ' + keyB.task_time_from

                                      console.log(keyA)
                                      console.log(keyB)
                                      if (keyA < keyB) return -1;
                                      if (keyA > keyB) return 1;
                                      return 0;
                                    });
                                    var ul = $(element).parent().parent();
                                    $.each(items, function(i, li){
                                      ul.append(li); /* This removes li from the old spot and moves it */
                                    });;
                                }
                                })
                            console.log(start_ts)
                            console.log(end_ts)
                            $(document).off('mousemove');

                          })



              }

            })


            $('.spacer-right').on('mousedown', (e)=>{
              e.preventDefault()
              let element = $(event.target).parent()

              let data = $(element).attr('data-task-data')
              data = JSON.parse(decodeURIComponent(data))

              if (data.task_date_to == this.schedule_date) {

                      let offset_l = $(element).css('margin-left')
                      offset_l =   Number(offset_l.substring(0, offset_l.length - 2));

                      let offset_r = $(element).css('margin-right')
                      offset_r =   Number(offset_r.substring(0, offset_r.length - 2));

                      let lane_width = $(element).parent().parent().width()
                      let min_width = $(element).parent().parent().width() / 24 / 4 //15 minutes



                      let initX = e.originalEvent.clientX


                      $(document).on('mousemove', (e)=> {

                        let current_position = e.originalEvent.clientX
                        let distance = current_position - initX


                        //let new_offset = offset_l - distance
                        let new_offset = offset_r - distance
                        let new_width = lane_width - offset_l - new_offset

                        new_offset  = Math.round(new_offset/min_width)*min_width
                        console.log(new_width)
                        if ((new_width > min_width) & (new_offset > 0)  ) {

                            let task_lane_id = $(element).parent().attr('data-employee')

                            $("div")
                            .find('[data-row-pk='+$(element).attr('data-row-pk')+']')
                            .css('margin-right', new_offset +'px')
                            //$(element).css('margin-right', new_offset +'px')


                        }



                        //element.style.width = e.pageX - element.getBoundingClientRect().left + 'px'
                      })
                      $(document).on('mouseup', (e)=> {
                        console.log('up')
                        let task_width = $(element).css('width')
                        task_width =   Number(task_width.substring(0, task_width.length - 2));

                        let task_offset_L = $(element).css('margin-left')
                        task_offset_L =   Number(task_offset_L.substring(0, task_offset_L.length - 2));

                        let total_width = $(element).parent().parent().width()

                        let offset_seconds = task_offset_L / total_width * 86000
                        let duration_seconds = task_width / total_width * 86000

                        let start_ts = this.round_time_to_quarter(new Date(0,0,0,0,0,offset_seconds))
                        let end_ts = this.round_time_to_quarter(new Date(0,0,0,0,0,offset_seconds + duration_seconds))

                        let data = $(element).attr('data-task-data')
                        data = JSON.parse(decodeURIComponent(data))

                        if (data.task_date_from == this.schedule_date) {
                            data['task_time_from'] = start_ts.toTimeString().split(' ')[0];
                        }

                        if (data.task_date_to == this.schedule_date) {
                            data['task_time_to'] = end_ts.toTimeString().split(' ')[0];
                        }


                        console.log(data)

                        $.ajax({
                            url: window.location.origin +'/api/tasks/' + data.id_task + '/',
                            method: 'PUT',
                            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                            data: data,
                            success: function (result) {



                                $("div")
                                    .find('[data-row-pk='+$(element).attr('data-row-pk')+']')
                                    .attr('data-task-data', encodeURIComponent(JSON.stringify(result)))

                                var items = $(element).parent().parent().find('li').get();


                                items.sort(function(a,b){
                                  var keyA = $(a).find('.task').attr('data-task-data');

                                  keyA = JSON.parse(decodeURIComponent(keyA))
                                  keyA = keyA.task_date_from + ' ' + keyA.task_time_from
                                  var keyB = $(b).find('.task').attr('data-task-data');
                                  keyB = JSON.parse(decodeURIComponent(keyB))
                                  keyB = keyB.task_date_from + ' ' + keyB.task_time_from

                                  console.log(keyA)
                                  console.log(keyB)
                                  if (keyA < keyB) return -1;
                                  if (keyA > keyB) return 1;
                                  return 0;
                                });
                                var ul = $(element).parent().parent();
                                $.each(items, function(i, li){
                                  ul.append(li); /* This removes li from the old spot and moves it */
                                });;
                            }
                            })

                        $(document).off('mousemove');

                      })



              }


            })




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