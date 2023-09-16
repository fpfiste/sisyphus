



class BootstrapForm{

      constructor({container, id, fields, validation, ajax_url, language, exclude = [], required = [], disabled=[]}) {
          this.container = container;
          this.ajax_url = ajax_url;
          this.id = id;
          this.exclude = exclude;
          this.required = required;
          this.fields = fields;
          this.data = null;
          this.disabled = disabled;
          this.is_valid = false;
          this.language = language
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
      select({id, title, required, ajax_url, api_endpoint_filter, options,value_field, description_field, disabled, multiple}){
           let name = id;
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

        if (multiple) {
            multiple = 'multiple'
            name = id + '[]'
        } else {
            multiple = ''
        }
          let html = '<div class="form-group"><label for="'+id+'">'+title+'</label><select class="form-control" id="'+id+'" name="'+id+'" '+required+' '+ disabled + ' ' + multiple + '>'

          html += '<option value="">-----------</option>'

          if (ajax_url){
                  let url = ajax_url + '?' + api_endpoint_filter

                  $.ajax({
                        url: url,
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
                            html += '<option value="'+key+'">'+value[this.language]+'</option>'
                            return html
                })


          }




        return html
      }



      build(){
      let field = ''
        let csrf_token = Cookies.get('csrftoken');
        let form = '<form id="'+this.id+'" class="needs-validation" style="overflow:auto; height:100%;"></form>';
        $(this.container).append(form);

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

            } else {
                value.disabled = false;
            }
            if (value.input_type == 'select'){

                field = this.select({
                                            id:key,
                                            title: value.title[this.language],
                                            ajax_url:value.api_endpoint,
                                            options: value.options,
                                            value_field: value.pk_field,
                                            description_field: value.display_field,
                                            required:value.required,
                                            disabled:value.disabled,
                                            multiple: value.multiple,
                                            api_endpoint_filter: value.api_filter
                                         })
            } else {
               field = this.input_field({
                                         id:key,
                                         title: value.title[this.language],
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

      validate(){
        let form = $('#' + this.id)
        let form_fields = $(form).find(':input')

        let valid = true
        $.each(form_fields, (key,value)=>{
            if ((value.required == true) && (value.value == '')){
                valid = false
            }
        })

        this.is_valid = valid;

      }


      serialize() {
        let form = $('#' + this.id)
        let form_fields = $(form).find(':input')
        $.each(form_fields, (key,value)=>{
            $(value).prop('disabled', false);
        })

        let array = $(form).serialize();


        $.each(this.fields, (key,value)=>{
            if (this.disabled.includes(key)){
                $('#' + this.id + ' #' + key).prop('disabled', true);
            }
        })


        return array;
      }

      submit(url, method){


        let form = $('#' + this.id)
        let form_fields = $(form).find(':input')

        this.validate();

        if (this.is_valid == false){
            alert('Alle Felder ausfüllen!')
            return
        }

        let array = this.serialize();


        $.ajax({
           url: url,
           type: method,
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           data:array,
           success: function(response) {

              location.reload();
           },
           error: function(error){
            console.log(error)
           }
        });
      }
}

