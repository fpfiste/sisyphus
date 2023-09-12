

class BootstrapDataTable{

      constructor({container, id, fields, pk_field, ajax_url, exclude}) {
          this.container = container;
          this.id = 'detail_table';
          this.fields = fields;
          this.pk_field = pk_field;
          this.ajax_url = ajax_url;
          this.query_params = ''
          this.exclude = exclude;
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





      text_field(element) {
         element =  '<td>'+element+'</td>'
         return element;
      };

      checkbox_field(checked) {

        if (checked) {
             return  '<td><input type="checkbox" checked disabled/></td>'
        } else {
             return  '<td><input type="checkbox" disabled/></td>'
        }


      }

      fk_field(url_endpoint, display_field, pk) {
            let data;
            let url = window.location.origin + url_endpoint + '/' + pk

            $.ajax({
               url: url,
               type: 'GET',
               async: false,
               success: function(response) {

                 data =  response;
               }
            });


            return '<td>'+data[display_field]+'</td>';



      }


      draw_header() {

        let header = '<thead>'

        $.each(this.fields,(key,value) => {
            if (this.exclude.includes(key)) {
                return
            } else {
                header += '<th>'+value.title.de+'</th>'
            }
        });
        console.log(header)
        return header


      }

      build_grid() {
            $(this.container).empty();
            let header = this.draw_header()
            console.log(header)
            //* draw the grid of the new table object
            let table_grid = '<div id="table_container" style="overflow:auto; white-space:nowrap; height:100%;"><table class="table table-striped table-hover table-bordered table-lg" id="detail_table">'+header+'<tbody></tbody></table></div>';
            $(this.container).append(table_grid);

      }


      populate() {
        //* remove older renderings of the object
        //* load the data to populate the table



        //* loop all the rows in this.data object and add it to the table
        $.each(this.data,(key,element) => {


            //* create the row wrapper for the current record
            let row = '<tr data-row-pk="'+element[this.pk_field]+'"data-row-url="'+this.ajax_url + '/' +element[this.pk_field] +'">';

            //* loop all elements of the current record
            $.each(this.fields,(field,config) => {

                if (this.exclude.includes(field)) {
                    return;
                }


                //* get corresponding field based on the field name from the data object
                //* continue if the fieldname is url

               if (element[field] == null) {
                row += '<td></td>'
               } else if(config.display_type == 'text') {
                    row += this.text_field(element[field])
                } else if (config.display_type == 'checkbox') {
                    row += this.checkbox_field(element[field])
                } else if (config.display_type == 'fk_field') {
                    row += this.fk_field(config.api_endpoint, config.display_field, element[field])

                }
            });
            row += '</td>';
            $('#'+this.id + ' tbody').append(row);
        });

      }

      build(){
        $.when(
            this.ajax_call(this.ajax_url + this.query_params, 'GET')
        ).done((data)=> {
            this.data = data;

            this.build_grid();
            this.populate();
            this.draw_event_handlers();
        })

      }


      draw_event_handlers() {

            $("#detail_table tr").on( "dblclick", function() {


                let url = $(this).attr('data-row-url');
                $.ajax({
                url: url,

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
            });



      }



}








