



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
      textarea({id, title, placeholder, required, disabled}) {
        if (placeholder === undefined){
            placeholder = ''
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
      let field = ''
        let csrf_token = Cookies.get('csrftoken');

        $(this.container).empty();


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
            } else if (value.input_type =='textarea') {
                field = this.textarea({  id:key,
                                         title: value.title[this.language],
                                         required: value.required,
                                         disabled:value.disabled,
                                         })

            } else if (value.input_type == 'jsonfield') {
                    field = this.jsonfield({  id:key,
                                 title: value.title[this.language],
                                 required: value.required,
                                 disabled:value.disabled,
                                 })


            }else {
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

        this.add_event_handlers();
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

      submit(url, method){
        $('#loading_screen_wrapper').toggle();


        let form = $('#' + this.id)
        let form_fields = $(form).find(':input')

        this.validate();

        if (this.is_valid == false){
            alert('Alle Felder ausfüllen!')
            location.reload();
            return
        }

        let array = this.serialize();


        $.ajax({
           url: url,
           type: method,
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
}

