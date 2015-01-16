$( document ).ready(function() {
 
    console.log('Hello World');

    $.urlParam = function(name){
    var results = new RegExp('[\?&amp;]' + name + '=([^&amp;#]*)').exec(window.location.href);
    return results[1] || 0;
    }

    var type = $.urlParam('type');


    if (type == '1') {
        $('#amount').val('40');
        $('#friend').hide();

    }
    else {
        $('#amount').val('20');
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