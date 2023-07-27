function toggle(some){
    $(some).toggle()
}

function toggle_link(){
    $("#create-link-button").click(function(){
        toggle(".form")
    })
}

$(document).ready(function(){
   toggle_link()
});