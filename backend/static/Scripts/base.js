function hamburger(){
    $("#hamburger").click(function(){
        if ($(this).children(".nav")){
            $(".nav").addClass("active").removeClass("nav")
        }
        else if ($(this).children(".active")){
            $(".active").addClass("nav").removeClass("active")
        }
        
    })
};


$(document).ready(function(){
    hamburger();
});