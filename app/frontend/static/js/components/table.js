

class BootstrapDataTable{

      constructor({container, id, fields, pk_field, ajax_url}) {
          this.container = container;
          this.id = id;
          this.fields = fields;
          this.data = this.ajax_get(ajax_url);;
          this.pk_field = pk_field;
          this.ajax_url = ajax_url;
          this.build_grid()
      }

      ajax_get(url){
      /**
         * make an ajax get request to the url specified
         * @param  string url:      ajax call endpoint
         * @return object response: result from ajax call
      */
        let result;
           $.ajax({
               url: url,
               type: 'GET',
               async: false,
               success: function(response) {

                 result =  response;
               }
            });
        return result;
      }





      text_field(element) {
      /**
         * draw a simple text table cell
         * @param  string url:      ajax call endpoint
         * @return object response: result from ajax call
      */


        return '<td>'+element+'</td>';
      };

      checkbox_field(checked) {

        if (checked) {
             return '<td><input type="checkbox" checked disabled/></td>'
        } else {
             return '<td><input type="checkbox" disabled/></td>'
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

      build_grid() {
          $(this.container).empty();


            //* draw the grid of the new table object
            let table_grid = '<div style="overflow:auto; white-space:nowrap;"><table class="table table-striped table-hover" id='+this.id+'><thead></thead><tbody></tbody></table></div>';
            $(this.container).append(table_grid);

            //* add header field to the grid from this.fields object
            $.each(this.fields,(key,value) => {
                $('#'+this.id + ' thead').append('<th>'+value.title.de+'</th>');
            });

      }


      build() {
        //* remove older renderings of the object
        //* load the data to populate the table

        $('#'+this.id + ' tbody').empty()

        //* loop all the rows in this.data object and add it to the table
        $.each(this.data,(key,element) => {


            //* create the row wrapper for the current record
            let row = '<tr data-row-pk="'+element[this.pk_field]+'">';

            //* loop all elements of the current record
            $.each(this.fields,(field,config) => {

                //* get corresponding field based on the field name from the data object
                //* continue if the fieldname is url



                if(config.display_type == 'text') {
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


}








