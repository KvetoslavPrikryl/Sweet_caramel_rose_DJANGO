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

$(document).ready(function(){
    login();
    close_login();
});