



class BootstrapForm{

      constructor({container, id, fields, validation, ajax_url, language, exclude = [], required = [], disabled=[], method='GET'}) {
          this.container = container;
          this.ajax_url = ajax_url;
          this.id = id;
          this.required = required;
          this.fields = fields;
          this.data = null;
          this.disabled = disabled;
          this.is_valid = false;
          this.language = language
          this.method = method
      }

      set_required({fields=[]}) {
        $.each(this.fields, (key, value) => {
            let required = (fields.includes(key)) ? true : false;
            console.log('#' + this.id + ' #' + key)
            $('#' + this.id + ' #' + key).prop('required', required);


        })

      }

      text_input({id, title, max_length, pattern, disabled, required}) {
        let html = '<div class="form-group">'
        html += '<label for="'+id+'">'+title+'</label>'
        html += '<input type="text" name="'+id+'" class="form-control" id="'+id+'"' + disabled+' ' + required +'></div>'
        return html
      }

      number_input({id, title, min, max, disabled, required}) {
          let html = '<div class="form-group">'
          html += '<label for="'+id+'">'+title+'</label>'
          html += '<input type="number" name="'+id+'" class="form-control" id="'+id+'"' + min + ' ' + max + ' ' + disabled+' ' + required +'></div>'
        return html
      }

      date_input({id, title, disabled, required}) {
          let html = '<div class="form-group">'
          html += '<label for="'+id+'">'+title+'</label>'
          html += '<input type="date" name="'+id+'" class="form-control" id="'+id+'"' + disabled+' ' + required +'></div>'
        return html
      }

      time_input({id, title, disabled, required}) {
          let html = '<div class="form-group">'
          html += '<label for="'+id+'">'+title+'</label>'
          html += '<input type="time" name="'+id+'" class="form-control" id="'+id+'"' + disabled+' ' + required +'></div>'
        return html
      }

      file_upload({id, title, disabled, required}) {
          let html = '<div class="form-group">'
          html += '<label for="'+id+'">'+title+'</label>'
          html += '<input type="file" name="'+id+'" class="form-control" id="'+id+'" ' + placeholder + ' ' + disabled+' ' + required +'></div>'
        return html
      }

      email_input({id, title, disabled, required}) {
          let html = '<div class="form-group">'
          html += '<label for="'+id+'">'+title+'</label>'
          html += '<input type="email" name="'+id+'" class="form-control" id="'+id+'"' + disabled+' ' + required +'></div>'
        return html
      }

      fk_field({id, title, required, disabled, url, value_field, description_field}) {
          let html = '<div class="form-group"><label for="'+id+'">'+title+'</label><select class="form-control" id="'+id+'" name="'+id+'" '+required+' '+ disabled+'>'

          html += '<option value="">-----------</option>'

          $.ajax({
                url: url,
                async: false,
                success: function (result) {
                   $.each(result,(key,value) => {
                       html += '<option value="'+value[value_field]+'">'+value[description_field]+'</option>'
                    })
                }
            });

          return html


      }

      select({id, title, required, options, value_field, description_field, disabled}){
          let name = id;
          let html = '<div class="form-group"><label for="'+id+'">'+title+'</label><select class="form-control" id="'+id+'" name="'+id+'" '+required+' '+ disabled+'>'
          html += '<option value="">-----------</option>'
            $.each(options,(key,value) => {
                        html += '<option value="'+key+'">'+value[this.language]+'</option>'
            })
            return html
          }

      textarea({id, title, placeholder, required, disabled}) {
            let html = '<div class="form-group">'
            html += '<label for="'+id+'">'+title+'</label>'
            html += '<textarea id="'+id+'" name="'+id+'" style="width:100%; display:block;" ' + placeholder + ' '  + required+' ' + disabled +'></textarea>'
            html += '</div>'
           return html
      }

      jsonfield({id, title, placeholder, required, disabled}) {
        let html = '<div class="form-group jsonfield">'
        html +='<label for="'+id+'">'+title+'</label>'
        html +='<input type="hidden" class="form-control" id="'+id+'" name="'+id+'" placeholder="">'
        html += '<table class="table table-bordered">'
        html += '<tbody>'
        html += '<tr>'
        html += '<td><input type="text" class="form-control jsonfield_attribute" placeholder=""></td>'
        html += '<td><input type="text" class="form-control jsonfield_value" placeholder=""></td>'
        html += '<td><span class="custom_field_action_item custom_field_action_add"><i class="fa-solid fa-plus"></i></span></td>'
        html += '</tr>'
        html += '</tbody>'
        html += '</table>'
        html += '</div>'
        return html
      }

      build(){
        $(this.container).empty();


        let form = '<form id="'+this.id+'" class="needs-validation" style="overflow:auto; height:100%;"></form>';
        $(this.container).append(form);

        let skip = this.exclude;
        let req = this.required;
        let disabled_fields = this.disabled;


        // looo all field configs and build fields
        $.each(this.fields,(key,value) => {

            let input_type = value.input_type;
            let title = value.title[this.language];

            let required = (req.includes(key)) ? 'required' : '';
            let disabled = (disabled_fields.includes(key)) ? 'disabled' : '';

            let field;

            console.log(input_type)
            switch (input_type) {
                case 'text_input':
                    field = this.text_input({id: key, title: title, required:required, disabled:disabled});
                    break;

                case 'number_input':
                    field = this.number_input({id: key, title: title, min: value.min, max: value.max, required:required, disabled:disabled});
                    break;
                case 'date_input':
                    field = this.date_input({id: key, title: title, required:required, disabled:disabled});
                    break;
                case 'time_input':
                    field = this.time_input({id: key, title: title, required:required, disabled:disabled});
                    break;
                case 'file_upload':
                    field = this.file_upload({id: key, title: title, required:required, disabled:disabled});
                    break;
                case 'email_input':
                    field = this.email_input({id: key, title: title, required:required, disabled:disabled})
                    break;
                case 'fk_field':
                    let url = (value.api_filter == 'undefined') ? value.api_endpoint : value.api_endpoint + '?' + value.api_filter
                    field = this.fk_field({id: key, title: title, url: url, required:required, disabled:disabled, value_field: value.pk_field, description_field: value.display_field})
                    break;
                case 'select':
                    field = this.select({id: key, title: title, options: value.options, value_field:value.pk_field, description_field: value.display_field, required:required, disabled:disabled})
                    break;
                case 'textarea':
                    field = this.textarea({id: key, title:title, required:required, disabled:disabled})
                    break;
                case 'jsonfield':
                    field = this.jsonfield({id:key, title:title, required:required, disabled:disabled})
                    break;

            }

            $('#' + this.id).append(field)

        });

        this.add_event_handlers();
      }

      validate(){
        let form = $('#' + this.id)
        let form_fields = $(form).find(':input')
        let valid = true
        $.each(form_fields, (key,value)=>{
            console.log(value)
            if ($(value).prop('validity').valid == false){
                valid = false
                $(value).css('border-color', 'red')
            } else {
                $(value).css('border-color', 'green')
            }
        })

        this.is_valid = valid;

        }


      populate_json_field() {
            let jsonfields =  $('#' + this.id + ' .jsonfield')
            let custom_fields = {}

            $.each(jsonfields, (key, value)=>{
                let hidden_input = $(value).find('input:hidden')
                let rows = $(value).find('tbody tr')

                $.each(rows, (index, row) => {

                    let attriubte_input = $(row).find('.jsonfield_attribute')[0]
                    let value_input = $(row).find('.jsonfield_value')[0]

                    let json_key = $(attriubte_input).val()
                    let json_value = $(value_input).val()
                    if (json_key != '' && json_value!=''){
                        custom_fields[json_key] = json_value
                    }

                })


                $(hidden_input).val(JSON.stringify(custom_fields))


            })
      }




      serialize() {
        let form = $('#' + this.id)
        let form_fields = $(form).find(':input')

        $.each(form_fields, (key,value)=>{
            $(value).prop('disabled', false);
        })

        this.populate_json_field()

        let array = $(form).serialize();

        $.each(this.fields, (key,value)=>{
            if (this.disabled.includes(key)){
                $('#' + this.id + ' #' + key).prop('disabled', true);
            }
        })

        return array;
      }


      submit(url){
        let form = $('#' + this.id)
        let form_fields = $(form).find(':input')

        this.validate();

        if (this.is_valid == false){
            return
        }

        let array = this.serialize();


        $('#loading_screen_wrapper').toggle();
        $.ajax({
           url: url,
           type: this.method,
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           data:array,
           success: function(response) {
              $('#loading_screen_wrapper').toggle();
              location.reload();
           },
           error: function(error){
            console.log(error)
           console.log('here')

            //location.reload();
           }
        });
      }

    add_event_handlers() {
           $("#" + this.id + " input[type='hidden']").on('change', (event)=> {
            let target = event.target

            let table = $(target).siblings('table')
            $(table).find('tbody').empty();

            let json = JSON.parse($(event.target).val());
            let html = ''

            if (Object.keys(json).length > 0){

                 $.each(json, (key, value)=> {
                      html += '<tr>'
                        html += '<td><input type="text" class="form-control jsonfield_attribute" value="'+key+'"></td>'
                        html += '<td><input type="text" class="form-control jsonfield_value" value="'+value+'"></td>'
                        html += '<td><span class="custom_field_action_item custom_field_action_remove"><i class="fa-regular fa-trash-can"></i></span></td>'
                        html += '</tr>'
                })
                    html += '<tr>'
                    html += '<td><input type="text" class="form-control jsonfield_attribute" value=""></td>'
                    html += '<td><input type="text" class="form-control jsonfield_value" value=""></td>'
                    html += '<td><span class="custom_field_action_item custom_field_action_add"><i class="fa-regular fa-plus"></i></span></td>'
                    html += '</tr>'
                    $(table).find('tbody').append(html)

            } else {
                        html += '<tr>'
                        html += '<td><input type="text" class="form-control jsonfield_attribute" value=""></td>'
                        html += '<td><input type="text" class="form-control jsonfield_value" value=""></td>'
                        html += '<td><span class="custom_field_action_item custom_field_action_add"><i class="fa-regular fa-plus"></i></span></td>'
                        html += '</tr>'
                    $(table).find('tbody').append(html)
            }

           $("#" + this.id + " .fa-trash-can").on('click', function() {
                $(this).parent().parent().parent().remove();
           })

           $("#" + this.id + " .fa-plus").on('click', (event)=> {
                let html = '<tr>'
                        html += '<td><input type="text" class="form-control jsonfield_attribute" value=""></td>'
                        html += '<td><input type="text" class="form-control jsonfield_value" value=""></td>'
                        html += '<td><span class="custom_field_action_item custom_field_action_remove"><i class="fa-regular fa-trash-can"></i></span></td>'
                        html += '</tr>'
                    $(event.target).parent().parent().parent().parent().prepend(html)

                $("#" + this.id + " .fa-trash-can").on('click', (event)=> {

                    $(event.target).parent().parent().parent().remove();
                })
           })


        })
           $("#create_form input[type='hidden']").on('change', (event)=> {

            let target = event.target

            let table = $(target).siblings('table')
            $(table).find('tbody').empty();

            let json = JSON.parse($(event.target).val());
            let html = ''



            if (Object.keys(json).length > 0){

                 $.each(json, (key, value)=> {
                      html += '<tr>'
                        html += '<td><input type="text" class="form-control jsonfield_attribute" value="'+key+'"></td>'
                        html += '<td><input type="text" class="form-control jsonfield_value" value="'+value+'"></td>'
                        html += '<td><span class="custom_field_action_item custom_field_action_remove"><i class="fa-regular fa-trash-can"></i></span></td>'
                        html += '</tr>'
                })
                    html += '<tr>'
                    html += '<td><input type="text" class="form-control jsonfield_attribute" value=""></td>'
                    html += '<td><input type="text" class="form-control jsonfield_value" value=""></td>'
                    html += '<td><span class="custom_field_action_item custom_field_action_add"><i class="fa-regular fa-plus"></i></span></td>'
                    html += '</tr>'
                    $(table).find('tbody').append(html)

            } else {
                        html += '<tr>'
                        html += '<td><input type="text" class="form-control jsonfield_attribute" value=""></td>'
                        html += '<td><input type="text" class="form-control jsonfield_value" value=""></td>'
                        html += '<td><span class="custom_field_action_item custom_field_action_add"><i class="fa-regular fa-plus"></i></span></td>'
                        html += '</tr>'
                    $(table).find('tbody').append(html)


            }

           $("#" + this.id + " .fa-trash-can").on('click', function() {
                $(this).parent().parent().parent().remove();
           })
           $("#" + this.id + " .fa-plus").on('click', (event)=> {

                let html = '<tr>'
                        html += '<td><input type="text" class="form-control jsonfield_attribute" value=""></td>'
                        html += '<td><input type="text" class="form-control jsonfield_value" value=""></td>'
                        html += '<td><span class="custom_field_action_item custom_field_action_remove"><i class="fa-regular fa-trash-can"></i></span></td>'
                        html += '</tr>'
                    $(event.target).parent().parent().parent().parent().prepend(html)

                $("#" + this.id + " .fa-trash-can").on('click', (event)=> {

                    $(event.target).parent().parent().parent().remove();
           })
           })


        })
           $("#" + this.id + " .fa-trash-can").on('click', function() {
                $(this).parent().parent().parent().remove();
           })
           $("#" + this.id + " .fa-plus").on('click', (event)=> {

                let html = '<tr>'
                        html += '<td><input type="text" class="form-control jsonfield_attribute" value=""></td>'
                        html += '<td><input type="text" class="form-control jsonfield_value" value=""></td>'
                        html += '<td><span class="custom_field_action_item custom_field_action_remove"><i class="fa-regular fa-trash-can"></i></span></td>'
                        html += '</tr>'
                    $(event.target).parent().parent().parent().parent().prepend(html)

                $("#" + this.id + " .fa-trash-can").on('click', (event)=> {

                    $(event.target).parent().parent().parent().remove();
           })
           })

      }

}

