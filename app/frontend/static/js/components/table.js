
function flattenObject(ob) {
    var toReturn = {};

    for (var i in ob) {
        if (!ob.hasOwnProperty(i)) continue;

        if ((typeof ob[i]) == 'object' && ob[i] !== null) {
            var flatObject = flattenObject(ob[i]);
            for (var x in flatObject) {
                if (!flatObject.hasOwnProperty(x)) continue;

                toReturn[i + '.' + x] = flatObject[x];
            }
        } else {
            toReturn[i] = ob[i];
        }
    }
    return toReturn;
}




class BootstrapDataTable{

      constructor({container, id, fields, pk_field}) {
          this.container = container;
          this.id = id;
          this.fields = fields;
          this.data = null;
          this.pk_field = pk_field;
      }


      build() {

        $(this.container).empty();

        let table_grid = '<div style="overflow:auto";><table class="table table-striped table-hover" id='+this.id+'><thead></thead><tbody></tbody></table></div>';

        $(this.container).append(table_grid);

        $.each(this.fields,(key,value) => {
            $('#'+this.id + ' thead').append('<th>'+value.title+'</th>');
        });


        $.each(this.data,(key,element) => {

            let data = flattenObject(element)
            console.log(data)

            let row = '<tr data-row-pk="'+element[this.pk_field]+'">';


            $.each(element,(idx,attribute) => {

                let field = this.fields[idx];
                console.log(field)
                let path = field.path
                if (path === undefined) {
                    path = idx
                }

                console.log(path)
                if (attribute === true){
                    row += '<td><input type="checkbox"checked disabled/></td>';
                } else if (attribute === false) {
                    row += '<td><input type="checkbox" disabled/></td>';

                } else {
                    row += '<td>'+data[path]+'</td>';
                }


            });

            row += '</td>';
            $('#'+this.id + ' tbody').append(row);
        });

      }


}








