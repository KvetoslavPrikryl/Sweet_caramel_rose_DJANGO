function hamburger(){
    $("#hamburger").click(function(){
        $(".nav").addClass("active").removeClass("nav")
    })
};


$(document).ready(function(){
    hamburger();
});