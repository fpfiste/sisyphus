



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
          this.fk_data = {}
      }

    ajax_call(url, type, data, variable) {
           let result = this.fk_data

           return $.ajax({
               url: url,
               type: type,

               //async:false,
            });

        //return result;
      }

      build() {
        let fk_fields = Object.entries(this.fields).filter(v => v[1].input_type === "fk_field");

        let promises = []
        let keys = []
        $.each(fk_fields, (key, value)=>{
            let endpoint = value[1].api_endpoint
            let filter = (value[1].api_filter == null) ?  '' : value[1].api_filter
                 let url = endpoint + '?' + filter
                promises.push(this.ajax_call(url, 'GET', value[0]))
                keys.push(value[0])
        })

        let instance = this
        $.when.apply($, promises).done(function(){

            let results ={};

            let params = Array.from(arguments)
            if (params.length > 0) {
                if (params[0]['page_size'] != null) {
                    params = [arguments, ]
                }

                $.each(params, (i,row) => {
                    results[keys[i]] = row[0]['data']
                });


            }
            instance.populate(results)




        })
      }

      set_required({fields=[]}) {
        $.each(this.fields, (key, value) => {
            let required = (fields.includes(key)) ? true : false;
            $('#' + this.id + ' #' + key).prop('required', required);


        })

      }

      text_input({id, title, max_length, pattern, disabled, required}) {
        let html = '<div class="form-group">'
        html += '<label for="'+id+'">'+title+'</label>'
        html += '<input type="text" name="'+id+'" class="form-control" id="'+id+'"' + disabled+' ' + required +' maxlength="'+max_length+'"></div>'
        return html
      }

      number_input({id, title, min, max, disabled, required, step}) {
          let html = '<div class="form-group">'
          html += '<label for="'+id+'">'+title+'</label>'
          html += '<input type="number" name="'+id+'" class="form-control" step="'+step+'" id="'+id+'"' + min + ' ' + max + ' ' + disabled+' ' + required +'></div>'
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
          html += '<input type="file" name="'+id+'" class="form-control" id="'+id+'" ' + disabled+' ' + required +'></div>'
        return html
      }

      email_input({id, title, disabled, required}) {
          let html = '<div class="form-group">'
          html += '<label for="'+id+'">'+title+'</label>'
          html += '<input type="email" name="'+id+'" class="form-control" id="'+id+'"' + disabled+' ' + required +'></div>'
        return html
      }

      fk_field({id, title, required, disabled, data, value_field, description_field}) {
          let html = '<div class="form-group"><label for="'+id+'">'+title+'</label><select class="form-control" id="'+id+'" name="'+id+'" '+required+' '+ disabled+'>'

          html += '<option value="">-----------</option>'

            $.each(data,(key,value) => {
                html += '<option value="'+value[value_field]+'">'+value[description_field]+'</option>'

            })
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

      textarea({id, title, placeholder, required, disabled, max_length}) {
            let html = '<div class="form-group">'
            html += '<label for="'+id+'">'+title+'</label>'
            html += '<textarea id="'+id+'" name="'+id+'" style="width:100%; display:block;" ' + placeholder + ' '  + required+' ' + disabled +'  maxlength="'+max_length+'"></textarea>'
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

      hidden_input({id, title, required, disabled}) {
        let html = '<div class="form-group">'
        html +='<input type="hidden" class="form-control" id="'+id+'" name="'+id+'" placeholder="">'
        return html
      }

      populate(fk_data){
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

            switch (input_type) {
                case 'text_input':
                    field = this.text_input({id: key, title: title, required:required, disabled:disabled, max_length:value.max_length});
                    break;

                case 'number_input':
                    field = this.number_input({id: key, title: title, min: value.min, max: value.max, required:required, disabled:disabled, step:value.step});
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
                    field = this.fk_field({id: key, title: title, data: fk_data[key], required:required, disabled:disabled, value_field: value.pk_field, description_field: value.display_field})
                    break;
                case 'select':
                    field = this.select({id: key, title: title, options: value.options, value_field:value.pk_field, description_field: value.display_field, required:required, disabled:disabled})
                    break;
                case 'textarea':
                    field = this.textarea({id: key, title:title, required:required, disabled:disabled, max_length:value.max_length})
                    break;
                case 'jsonfield':
                    field = this.jsonfield({id:key, title:title, required:required, disabled:disabled})
                    break;
                case 'hidden' :
                    field = this.hidden_input({id:key, title:title, required:required, disabled:disabled})

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
            if ($(value).prop('validity').valid == false){
                valid = false
                $(value).css('border-color', 'red')
            } else {
                $(value).css('border-color', 'green')
            }
        })

        this.is_valid = valid;

        }


       reset(){
        let form = $('#' + this.id).trigger("reset")
        $(form).find(':input').css('border-color', '')
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


      submit(url, callback){
        let form = $('#' + this.id)
        let form_fields = $(form).find(':input')

        this.validate();

        if (this.is_valid == false){
             $('#loading_screen_wrapper').hide();
            return
        }

        let array = this.serialize();


        $.ajax({
           url: url,
           type: this.method,
           headers: {'X-CSRFToken': Cookies.get('csrftoken')},
           data:array,
           success: callback,
           error: function(error){
            console.log(error);
            alert(error)
            location.reload();
           }
        });
      }

    add_event_handlers() {
           $("#" + this.id + " #custom_fields").on('change', (event)=> {
            let target = event.target

            let table = $(target).siblings('table')
            $(table).find('tbody').empty();
            console.log($(event.target).val())
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

