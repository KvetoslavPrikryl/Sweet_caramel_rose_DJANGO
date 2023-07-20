function hamburger(){
    $("#hamburger").click(function(){
        if ($(this).children("nav")){
            $(".nav").addClass("nav-active").removeClass("nav")
            $(".navbar").addClass("navbar-active").removeClass("navbar")
        }
        else if ($(this).children("active")){
            $(".nav-active").addClass("nav").removeClass("nav-active")
            $(".navbar-active").addClass("navbar").removeClass("navbar-active")
        }
        
    })
};


$(document).ready(function(){
    hamburger();
});