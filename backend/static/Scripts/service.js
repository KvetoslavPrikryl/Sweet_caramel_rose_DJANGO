function toggle(some){
    $(some).toggle();
};

function create_service(){
    $("#create-service").click(function(){
        toggle("#service-form")
    });
};

function gallery(){
    $(".gallery-img").click(function(){
        $(this).addClass("slide-active").removeClass("gallery-img")
        $(".gallery").addClass("gallery-active").removeClass("gallery")
        $(".gallery-img").addClass("slide").removeClass("gallery-img")
        $(".gallery-img-text").addClass("text-active").removeClass("gallery-img-text")
        $(".gallery-service-name").css("display", "none")
        $(".gallery-buttons").css("display", "block")
        $(".admin-button-delete").css("display", "none")
        $(".service-name-active").css("display", "block")
    });
};

function close_gallery(){
    $(".close").click(function(){
        $(".slide-active").removeClass("slide-active").addClass("gallery-img")
        $(".gallery-active").addClass("gallery").removeClass("gallery-active")
        $(".slide").addClass("gallery-img").removeClass("slide")
        $(".text-active").addClass("gallery-img-text").removeClass("text-active")
        $(".gallery-buttons").css("display", "none")
        $(".gallery-service-name").css("display", "block")
        $(".admin-button-delete").css("display", "block")
        $(".service-name-active").css("display", "none")
    })
}

function next_slide(){
    $("#right").click(function(){
        var slide_active = $(".slide-active")
        var next_slide = slide_active.next()

        if(next_slide.length){
            slide_active.addClass("slide").removeClass("slide-active")
            next_slide.addClass("slide-active").removeClass("slide")
        }
    })
}
function prev_slide(){
    $("#left").click(function(){
        var slide_active = $(".slide-active")
        var prev_slide = slide_active.prev()

        if(prev_slide.length){
            slide_active.addClass("slide").removeClass("slide-active")
            prev_slide.addClass("slide-active").removeClass("slide")
        }
    })
}



$(document).ready(function(){
    create_service();
    gallery();
    close_gallery();
    next_slide();
    prev_slide();
});