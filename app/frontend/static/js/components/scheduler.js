

class Scheduler{

      constructor({container, id, dim1_url, dim2_url}) {
          this.container = container;
          this.id = id;
          this.dim1 = {"title":{"en": "Employee", "de":"Mitarbeiter"},"dim_api":'/api/employees', "dim_pk_field": "id_employee", "dim_display_field":"employee_internal_alias"};
          this.dim2 =  {"title":{"en": "Asset", "de":"Geräte"}, "dim_api":'/api/assets', "dim_pk_field": "id_asset", "dim_display_field":"asset_internal_alias"};
          this.dim1_data = null;
          this.dim2_data = null;
          this.build_grid()
      }

      get_data(url){
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

      build_grid() {
          $(this.container).empty();

          this.dim1_data = this.get_data(this.dim1.dim_api);
          this.dim2_data = this.get_data(this.dim2.dim_api);

          console.log(this.dim1_data)
            //* draw the grid of the new table object
            let table_grid = '<div id='+this.id+'><table class="table table-bordered"><thead></thead><tbody></tbody></table></div>';
            $(this.container).append(table_grid);

            $('#' + this.id + ' thead').append()

            let header = '<tr><th>'+this.dim1.title.de+'</th><th>'+this.dim2.title.de+'</th>';

            for (let i = 1; i < (25); i++){
                header += '<th>'+i+'</th>'

            }
            header += '</tr>'
            $('#' + this.id + ' thead').append(header);

            let dim_mok_data = ['Fabian', 'Ramon']

            $.each(this.dim1_data, (key, value) => {
                $('#' + this.id + ' tbody').append('<tr data-pk='++'><td>' + value + '</td><td></td><td colspan="25"></td></tr>')


            })


      }

}