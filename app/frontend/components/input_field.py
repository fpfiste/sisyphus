


def input_field(id, title, type='number', placeholder="", min=None, max=None, required=False):

    if min:
        min = f'min="{min}"'
    else:
        min = ''

    if max:
        max = f'max="{max}"'
    else:
        max = ''

    if required:
        required = f'required'
    else:
        required = ''

    html = f'''
        <div class="form-group">
            <label for="{id}">{title}</label>
            <input type="{type}" name="{id}" class="form-control" id="{id}" placeholder="{placeholder}" {min} {max} {required}>
        </div>'''
    
    
    return html
