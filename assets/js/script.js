$(document).ready(function() {
    var sign_button = $("#hack-button");

    $(sign_button).click(function(e){
        e.preventDefault();
        $('#myModal').modal('show');
    });
});