function toggle(some){
    $(some).toggle()
}

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

$(document).ready(function(){
    toggle_dog_man()
    toggle_dog_woman()
    toggle_dog_pup()
    create_dog()
});