function toggle(some){
    $(some).toggle()
}

function create_service(){
    $("#create-service").click(function(){
        toggle("#service-form")
    })
}


$(document).ready(function(){
    create_service()
});