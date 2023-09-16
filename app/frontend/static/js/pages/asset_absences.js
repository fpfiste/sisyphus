
$(document).ready(function(){
    let page_config
    let url = '/assets/absences'



    //*** read the config file ***//
    $.ajax({
          url: '/_config',
          async: false,
          dataType: 'json',
          success: function (response) {
            page_config = response['pages'][url]
            translations = response['translations']
          }
    });

    // create table instance
    let table = new BootstrapDataTable({
                        container:'#overview-table',
                        id: page_config['table_id'],
                        fields: page_config['fields'],
                        ajax_url: page_config['ajax_url'],
                        pk_field: page_config['pk'],
                    })


    // create form insstances
    let filter_form = new BootstrapForm({
            container: '#form_filter_container',
            id: 'filter_form',
            ajax_url: page_config['ajax_url'],
            validation:false,
            fields: page_config['fields'],


    })
    let create_form = new BootstrapForm({
            container: '#create_form_container',
            id: 'create_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            exclude: ['id_asset_absence'],
            required : ['asset_absence_from', 'asset_absence_to' , 'fk_asset', 'fk_asset_absence_code']
    })



    let update_form = new BootstrapForm({
            container: '#update_form_container',
            id: 'update_form',
            ajax_url: page_config['ajax_url'],
            validation:true,
            fields: page_config['fields'],
            disabled : ['id_asset_absence'],
            required : ['id_asset_absence', 'asset_absence_from', 'asset_absence_to' , 'fk_asset', 'fk_asset_absence_code']

    })

    // build components
    table.build();
    filter_form.build();
    create_form.build();
    update_form.build();


    // add evetn listeners
    $( "#btn_filter" ).on( "click", function() {
      let query_params = $('#filter_form').serialize();
      $.ajax({
        url: window.location.origin +page_config['ajax_url'] + '?' + query_params,
        success: function (result) {
            table.data = result;
            table.build();
            $( "#"+page_config['table_id']+" tr" ).on( "dblclick", function() {
        let record_id =  $(this).attr('data-row-pk');

        $.ajax({
            url: window.location.origin + page_config['ajax_url'] + '/' + record_id,
            success: function (result) {

                $.each(result, (key, value)=>{
                    if (value === true){
                        value = 1;
                    } else if (value === false){
                        value = 0;
                    }
                    $('#update_form #'+ key).val(value);
                });

                $('#update_modal').modal('show');
            }
            })
    } );
        }
    });

    });

    $( "#btn_form_reset" ).on( "click", function() {
        $('#filter_form').trigger("reset");
        $('#btn_filter').click();


    });

    $( "#btn_add" ).on( "click", function() {
        create_form.submit();
    });

    $( "#"+page_config['table_id']+" tr").on( "dblclick", function() {
        let record_id =  $(this).attr('data-row-pk');

        $.ajax({
            url: window.location.origin + page_config['ajax_url'] + '/' + record_id,
            success: function (result) {


                $.each(result, (key, value)=>{

                    if (value === true){
                        value = 1;
                    } else if (value === false){
                        value = 0;
                    }
                    $('#update_form #'+ key).val(value);
                });

                $('#update_modal').modal('show');
            }
            })
    } );


    $( "#btn_save" ).on( "click", function() {
        let pk = $('#update_form #' + page_config['pk']).val()
        update_form.submit(pk);
    });



});
