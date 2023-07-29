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

function toggle(some){
    $(some).toggle()
}

/**** Home ****/

function login(){
    $("#login").click(function(){
        $(".admin-login").css("display", "block")
    });
};
function close_login(){
    $("#close").click(function(){
        $(".admin-login").css("display", "none")
    })
}

/***** Kennel *****/

function toggle_dog_man(){
    $("#dog-man-button").click(function(){
        toggle("#dog-man")
    })
}

function toggle_dog_woman(){
    $("#dog-women-button").click(function(){
        toggle("#dog-women")
    })
}
function toggle_dog_pup(){
    $("#dog-pup-button").click(function(){
        toggle("#dog-pup")
    })
}

function create_dog(){
    $("#create-dog-button").click(function(){
        toggle("#create-dog")
    })
}
function dog_img(){
    $(".dog-img").click(function(){
        $(".dog-img").removeClass("dog-img-active")
        $(this).addClass("dog-img-active")
    })
}

/***** Service *****/

function create_service(){
    $("#create-service").click(function(){
        toggle("#service-form")
    });
};

const css_array_on = [".gallery-service-name", ".gallery-buttons", ".service-name-active"]
const css_array_off = [".admin-button-delete", ".gallery-headline", ".create-gallery"]

function display_on(some){
    for (let i=0; i < some.length; i++){
        $(some[i]).css("display", "block")
    }
}

function display_off(some){
    for (let i=0; i < some.length; i++){
        $(some[i]).css("display", "none")
    }
}

function gallery(){
    $(".gallery-img").click(function(){
        $(this).addClass("slide-active").removeClass("gallery-img");
        $(".gallery").addClass("gallery-active").removeClass("gallery");
        $(".gallery-img").addClass("slide").removeClass("gallery-img");
        $(".gallery-img-text").addClass("text-active").removeClass("gallery-img-text");
        display_on(css_array_on);
        display_off(css_array_off);
    });
};

function close_gallery(){
    $(".close").click(function(){
        $(".slide-active").removeClass("slide-active").addClass("gallery-img")
        $(".gallery-active").addClass("gallery").removeClass("gallery-active")
        $(".slide").addClass("gallery-img").removeClass("slide")
        $(".text-active").addClass("gallery-img-text").removeClass("text-active")
        display_on(css_array_off);
        display_off(css_array_on);
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

/***** Links *****/

function toggle_link(){
    $("#create-link-button").click(function(){
        toggle(".form")
    })
}

$(document).ready(function(){
    hamburger();
    login();
    close_login();
    toggle_dog_man()
    toggle_dog_woman()
    toggle_dog_pup()
    dog_img()
    create_dog()
    create_service();
    gallery();
    close_gallery();
    next_slide();
    prev_slide();
    toggle_link()
});