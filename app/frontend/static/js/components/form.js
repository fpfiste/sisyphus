



class BootstrapForm{

      constructor({container, id, fields, validation, ajax_url}) {
          this.container = container;
          this.ajax_url = ajax_url;
          this.id = id;
          this.fields = fields;
          this.data = null;
      }


      input_field({id, title, type, placeholder, min, max, required}) {
        if (placeholder === undefined){
            placeholder = ''
        }

        if (min === undefined){
            min = ''
        } else {
            min = 'min="'+ min +'"'
        }

        if (max === undefined){
            max = ''
        } else {
            max = 'max="'+ max +'"'
        }

        if (required === undefined){
            required = ''
        } else {
            required = 'required="'+ required +'"'
        }


        let html = '<div class="form-group">'
        html += '<label for="'+id+'">'+title+'</label>'
        html += '<input type="'+type+'" name="'+id+'" class="form-control" id="'+id+'" ' + placeholder + ' ' + min + ' ' + max + ' ' + required+'></div>'

        return html
      }

      select_field({id, title, required, ajax_url, options, value_field, description_field}){

          if (required) {
            required = 'required'
          } else {
            required = ''
          }
          let html = '<div class="form-group"><label for="'+id+'">'+title+'</label><select class="form-control" id="'+id+'" name="'+id+'" '+required+'>'

          html += '<option value="">-----------</option>'

          if (options){

            $.each(options,(key,value) => {
                html += '<option value="'+key+'">'+value+'</option>'


            })


          } else if (ajax_url) {

              $.ajax({
                    url: ajax_url,
                    async: false,
                    success: function (result) {

                       $.each(result,(key,value) => {

                           html += '<option value="'+value[value_field]+'">'+value[description_field]+'</option>'
                           return html
                        })
                    }
                });

          }
        return html
      }

      build(){
        let form = '<form id="'+this.id+'" class="needs-validation"></div>';
        $(this.container).append(form);
        let field = ''
        $.each(this.fields,(key,value) => {

            if (value.type == 'select'){
                field = this.select_field({id:key, title: value.title, ajax_url:value.ajax_url, options: value.options, value_field: value.value_field, description_field: value.description_field, required:value.required})
            } else{
               field = this.input_field({id:key, title: value.title, type: value.type, min: value.min, max: value.max, required: value.required})

            }
            $('#' + this.id).append(field)

        });



      }

      submit(pk){


        let form = $('#' + this.id)
        let form_fields = $(form).find(':input')

        let valid = true
        $.each(form_fields, (key,value)=>{
            if ((value.required == true) && (value.value == '')){
                valid = false
            }
        })

        if (valid == false){
            alert('Alle Felder ausfüllen!')
            return
        }

        let array = $(form).serializeArray(); // Encodes the set of form elements as an array of names and values.
        let json = {};
        $.each(array, function () {
            json[this.name] = this.value || "";
        });
        console.log(json);

        if (pk){
            let url = this.ajax_url + pk + '/';
            $.ajax({
               url: url,
               type: 'PUT',
               data:json,
               success: function(response) {
                 location.reload();
               }
            });
        } else {
            $.ajax({
               url: this.ajax_url,
               type: 'POST',
               data:json,
               success: function(response) {
                 location.reload();
               }
            });


        }



      }
}

