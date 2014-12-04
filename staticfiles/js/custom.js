

$(document).ready(function () {
    $("#email_signup").val('E-mail');
    
        $("#email_signup").click(function()
        {
            if ($("#email_signup").val().indexOf('E-mail') != -1)
            {
                $("#email_signup").val('');
            }
        });
    

    $("#email_signup").blur(function()
    { 
        if ($("#email_signup").val().length == 0)
        {
            $("#email_signup").val('E-mail');
        }
        else if ($("#email_signup").val().indexOf('@') == -1) {
            $("#dialog").dialog();
            $("#dialog").dialog("option", "title", "Caution");
            $("#dialog").dialog("option", "width", 500);

        }
        else {
            var email = $('#email_signup').val()
            $("#email_control").val(email);
        }
    });

    $("#date").datepicker();
    
});

