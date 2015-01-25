$(document).ready(function () {

    $('ul.nav li').click(function(){
        $('.active').removeClass('active');
        $(this).addClass('active');
    });

    var now = new Date();
    today = now.getDate()  + '/' + (now.getMonth() + 1) + '/' + now.getFullYear();
    $('#id_date').val(today);

// CAROUSSELS ANIMATION



// About Us Language Section
    $('#FR_FLAG').click(function()
    {
        $('#US').addClass('hidden');
        $('#DE').addClass('hidden');
        $('#FR').removeClass('hidden');

    });

        $('#US_FLAG').click(function()
    {
        $('#US').removeClass('hidden');
        $('#DE').addClass('hidden');
        $('#FR').addClass('hidden');

    });

        $('#DE_FLAG').click(function()
    {
        $('#US').addClass('hidden');
        $('#DE').removeClass('hidden');
        $('#FR').addClass('hidden');

    });

// About Us sub-section animation

     $('#BUREAU').hide();
     $('#ABOUT').show();

     $('#ALSACE').hide();
     $('#NYC').hide();


     $('#BUREAU_LINK').click(function()
     {
        $('.btn-about-menu-active').addClass('btn-about-menu');
        $('.btn-about-menu-active').removeClass('btn-about-menu-active');
        $(this).addClass('btn-about-menu-active');
        $('#BUREAU').slideDown();
        $('#ABOUT').hide();
        $('#ALSACE').hide();
        $('#NYC').hide();

     });

     $('#ALSACE_LINK').click(function()
     {
        $('.btn-about-menu-active').addClass('btn-about-menu');
        $('.btn-about-menu-active').removeClass('btn-about-menu-active');
        $(this).addClass('btn-about-menu-active');
        $('#BUREAU').hide();
        $('#ABOUT').hide();
        $('#ALSACE').slideDown();
        $('#NYC').hide();

     });

     $('#NYC_LINK').click(function()
     {
        $('.btn-about-menu-active').addClass('btn-about-menu');
        $('.btn-about-menu-active').removeClass('btn-about-menu-active');
        $(this).addClass('btn-about-menu-active');
        $('#BUREAU').hide();
        $('#ABOUT').hide();
        $('#ALSACE').hide();
        $('#NYC').slideDown();

     });

     $('#ABOUTUS_LINK').click(function()
     {
        $('.btn-about-menu-active').addClass('btn-about-menu');
        $('.btn-about-menu-active').removeClass('btn-about-menu-active');
        $(this).addClass('btn-about-menu-active');
        $('#BUREAU').hide();
        $('#ABOUT').slideDown();
        $('#ALSACE').hide();
        $('#NYC').hide();
     });

});



