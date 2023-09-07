



class BootstrapForm{

      constructor({container, id, fields, validation, ajax_url, exclude = [], required = [], disabled=[]}) {
          this.container = container;
          this.ajax_url = ajax_url;
          this.id = id;
          this.exclude = exclude;
          this.required = required;
          this.fields = fields;
          this.data = null;
          this.disabled = disabled;
      }




      input_field({id, title, type, placeholder, min, max, required, disabled}) {
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

        if (disabled) {
            disabled = 'disabled'
        } else {
            disabled = ''
        }

        let html = '<div class="form-group">'
        html += '<label for="'+id+'">'+title+'</label>'
        html += '<input type="'+type+'" name="'+id+'" class="form-control" id="'+id+'" ' + placeholder + ' ' + min + ' ' + max + ' ' + required+' ' + disabled +'></div>'

        return html
      }

      select({id, title, required, ajax_url, options,value_field, description_field, disabled}){

          if (required) {
            required = 'required'
          } else {
            required = ''
          }

                  if (disabled) {
            disabled = 'disabled'
        } else {
            disabled = ''
        }
          let html = '<div class="form-group"><label for="'+id+'">'+title+'</label><select class="form-control" id="'+id+'" name="'+id+'" '+required+' '+ disabled + '>'

          html += '<option value="">-----------</option>'

          if (ajax_url){
                  let url = window.location.origin + ajax_url

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

          } else if (options) {

                $.each(options,(key,value) => {
                            html += '<option value="'+key+'">'+value.de+'</option>'
                            return html
                })


          }




        return html
      }


      build(){
        let form = '<form id="'+this.id+'" class="needs-validation"></div>';
        $(this.container).append(form);
        let field = ''

        let skip = this.exclude;
        let req = this.required;
        let disabled = this.disabled;

        if (!skip) {
            skip = [];
        }

        if (!req) {
            req = [];
        }

        if (!disabled) {
            disabled = [];
        }

        $.each(this.fields,(key,value) => {
            if (skip.includes(key)){
                return;
            }

            if (req.includes(key)) {
                value.required = true;
            }

            if (disabled.includes(key)){
                value.disabled = true;

            }
            if (value.input_type == 'select'){

                field = this.select({
                                            id:key,
                                            title: value.title.de,
                                            ajax_url:value.api_endpoint,
                                            options: value.options,
                                            value_field: value.pk_field,
                                            description_field: value.display_field,
                                            required:value.required,
                                            disabled:value.disabled,
                                         })
            } else {
               field = this.input_field({
                                         id:key,
                                         title: value.title.de,
                                         type: value.input_type,
                                         min: value.min,
                                         max: value.max,
                                         required: value.required,
                                         disabled:value.disabled,
                                         })

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

        $.each(form_fields, (key,value)=>{
            $(value).prop('disabled', false);
        })

        let array = $(form).serializeArray(); // Encodes the set of form elements as an array of names and values.
        let json = {};
        $.each(array, function () {
            json[this.name] = this.value || "";
        });
        console.log(json)
        $.each(this.fields, (key,value)=>{
            if (this.disabled.includes(key)){
                $('#' + this.id + ' #' + key).prop('disabled', true);
            }
        })



        if (pk){
            let url = this.ajax_url + '/' + pk + '/';
            $.ajax({
               url: url,
               type: 'PUT',
               data:json,
               success: function(response) {

                  location.reload();
               },
               error: function(error){
                console.log(error)
               }
            });
        } else {
            $.ajax({
               url: this.ajax_url + '/',
               type: 'POST',
               data:json,
               success: function(response) {

                 location.reload();
               },
               error: function(error) {
                console.log(error)
               }
            });


        }



      }
}

