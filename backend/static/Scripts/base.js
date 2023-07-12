function hamburger(){
    $("#hamburger").click(function(){
        $(".nav").addClass("nav-active").removeClass("nav")
        $(".navbar").addClass("navbar-active")
    })
};


$(document).ready(function(){
    hamburger();
});