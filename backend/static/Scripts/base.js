function hamburger(){
    $("#hamburger").click(function(){
        if ($(this).childern("nav")){
            $(".nav").addClass("active").removeClass("nav")
        }
        else if ($(this).childern("active")){
            $(".active").addClass("nav").removeClass("active")
        }
        
    })
};


$(document).ready(function(){
    hamburger();
});