

class BootstrapDataTable{

      constructor({container, id, fields, pk_field, ajax_url, query_params = '', language}) {
          this.container = container;
          this.id = id;
          this.fields = fields;
          this.pk_field = pk_field;
          this.ajax_url = ajax_url;
          this.query_params = query_params
          this.language = language;
          this.build_grid()
          this.max_pages;
          this.page_size = 10;
          this.page = 1
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
        let value = (element == null) ? '' : element

         let html =  '<td>'+value+'</td>'
         return html;
      };


      checkbox_field(checked, disabled) {
        if (checked) {
             return  '<td><input type="checkbox" checked '+disabled+'/></td>'
        } else {
             return  '<td><input type="checkbox" '+disabled+'/></td>'
        }


      }


      fk_field(data, display_field) {
        let value = (data == null) ? '' : data[display_field]
        return '<td>'+value+'</td>';
      }


      draw_header() {

        let header = '<thead style="position:sticky; top:0; background:white;">'

        $.each(this.fields,(key,value) => {
                header += '<th>'+value.title[this.language]+'</th>'

        });
        return header


      }

      draw_pagination(){
        let html = '<div class="form-group row" >'
         html  += '<div class="col" style="display:flex; justify-content:flex-end;"><select id="id_page_size" class="form-select" style="min-width: 100px;width:10%;"><option selected value="10">10</option><option value="20">20</option><option value="50">50</option><option value="100">100</option></select>'
         html += '<nav aria-label="Page navigation example">'
         html += '<ul class="pagination" style="margin-bottom:0px;">'
         html +=  '<li class="page-item" id="prev-page" data-page-nr='+ (Number(this.page) - 1) +'><a class="page-link" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'


         html += '<li class="page-item page-number" data-page-nr='+this.page+'><a class="page-link"> '+this.page+'</a></li>'

         if (this.page + 1 <= this.max_pages){
            html += '<li class="page-item page-number" data-page-nr='+(this.page+1)+'><a class="page-link"> '+(this.page + 1)+'</a></li>'
         }

         if ((this.page+2) <= this.max_pages){
            html += '<li class="page-item page-number" data-page-nr='+(this.page+2)+'><a class="page-link"> '+(this.page + 2)+'</a></li>'
         }


         html += '<li class="page-item" id="next-page" data-page-nr='+ (Number(this.page) + 1) +'><a class="page-link"  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
         html += '</ul>'
         html += '</nav>'
         html +='</div>'


         return html
      }



      build_grid() {
            $(this.container).empty();
            let header = this.draw_header()
            //* draw the grid of the new table object

            //let page_size_select = '<select class="form-select"><option selected value="10">10</option><option value="20">20</option><option value="50">50</option><option value="100">100</option></select>'
            let pagination = this.draw_pagination()
            let table_grid = '<div id=table_pagination style=height:100%;>'+pagination+'</div><div id="table_container" style="overflow:scroll; white-space:nowrap; height:90%;"><table class="table table-striped table-hover table-bordered table-lg" id="'+this.id+'">'+header+'<tbody></tbody></table></div>';
            $(this.container).append(table_grid);

      }


      populate() {
        //* remove older renderings of the object
        //* load the data to populate the table

        $('#id_page_size').val(this.page_size)

        //* loop all the rows in this.data object and add it to the table
        $.each(this.data,(key,element) => {



            //* create the row wrapper for the current record
            let row = '<tr data-row-pk="'+element[this.pk_field]+'"data-row-url="'+this.ajax_url  +element[this.pk_field] +'/">';

            //* loop all elements of the current record
            $.each(this.fields,(field,config) => {

                //* get corresponding field based on the field name from the data object
                //* continue if the fieldname is url
              switch(config.display_type) {
                  case 'action_checkbox':

                    row += this.checkbox_field(element[field], '')
                    break;
                  case 'text':
                    row += this.text_field(element[field])
                    break;
                  case 'checkbox':
                    row += this.checkbox_field(element[field], 'disabled')
                    break
                  case 'fk_field':

                    row += this.fk_field(element[field], config.display_field)
                    break;
                }


            });


            row += '</td>';
            $('#'+this.id + ' tbody').append(row);
        });

      }

      build(){
            let url = this.ajax_url + '?LIMIT=' + this.page_size + '&PAGE=' + this.page+ '&'  + this.query_params
        $.when(

            this.ajax_call(url, 'GET')
        ).done((data)=> {
            this.data = data['data'];
            this.max_pages = data['num_pages']
            this.page = data['page']
            this.build_grid();
            this.populate();
            this.draw_event_handlers();
            }
        ).catch((error)=> {
            console.log(error)
        })



        }




      draw_event_handlers() {

            $("#"+this.id +" tr").on( "dblclick", function() {


                let url = $(this).attr('data-row-url');
                $.ajax({
                url: url,

                success: function (result) {
                   $('#update_form').trigger("reset");
                   $.each(result, (key, value)=>{
                        if (value === true){
                            value = 1;
                        } else if (value === false){
                            value = 0;
                        }
                        if (value != null & typeof(value) === 'object') {
                            value = JSON.stringify(value);
                        } else if (value == null) {
                            value = JSON.stringify({});
                        }
                        $('#update_form #'+ key).val(value).trigger('change');

                    });

                    $('#update_modal').modal('show');
                }
                })
            });

            $('#id_page_size').on('change', (event)=> {
                this.page_size = $('#id_page_size').val();

                this.build();
                $('#id_page_size').val(this.page_size);

            })

            $('#next-page').on('click', (event)=> {
                if (this.page >= this.max_pages){
                    this.page = this.max_pages
                } else {
                this.page += 1
                }
                this.build();


            })

            $('#prev-page').on('click', (event)=> {
                if (this.page <= 1){
                    this.page = 1
                } else {
                this.page -= 1
                }
                this.build();


            })

            $('.page-number').on('click', (event)=> {
                let page = $(event.currentTarget).attr('data-page-nr')
                this.page = Number(page)
                this.build();


            })

      }



}








