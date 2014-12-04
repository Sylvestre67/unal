$(document).ready(function () {

    $("#about_us").click(function()
    {
        $(".about_sub").toggleClass("inactive");
        $(".about_caret").toggleClass("rot180");
    });

    $("#gastro").click(function()
    {
        $(".gastro_sub").toggleClass("inactive");
        $(".gastro_caret").toggleClass("rot180");
    });
});