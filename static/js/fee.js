$( document ).ready(function() {
 
    //console.log('Hello World');

    $.urlParam = function(name){
    var results = new RegExp('[\?&amp;]' + name + '=([^&amp;#]*)').exec(window.location.href);
    return results[1] || 0;
    }

    var type = $.urlParam('type');


    if (type == '1') {
        $('select>option:eq(0)').prop('selected', true);
        // $('#amount').val('Member');
        $('#friend').hide();

    }
    else {
        $('select>option:eq(1)').prop('selected', true);
        //$('#amount').val('Friend');
        $('#member').hide();
    }

    var action= $.urlParam('action');

    if (action == 'renew'){
        $('#application').hide();
    }
    else {
        $('#renewal').hide();
    }


 
});