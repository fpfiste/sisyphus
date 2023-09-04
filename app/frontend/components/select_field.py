



def select_field(id, title, null=True, options=[], required=False):
    html = f'''
        <div class="form-group">
            <label for="{id}">{title}</label>
            <select class="form-control" id="{id}" name="{id}">'''

    if null:
        html += '<option value="">-----------</option>'

    for option in options:
        html += f'<option value={option[0]}>{option[1]}</option>'

    html += '</select></div>'

    return html