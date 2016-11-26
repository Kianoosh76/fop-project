$(document).ready(function(){
    $(".like").click(function(){
        var row = $(this).attr('row');
        $.ajax({
            url: '/like',
            method: 'POST',
            data: {
                team: $("#team-" + row).val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                member: $("#members option:selected").val()
            },
            success: function(data, status, xhttp){
                $("#votes-" + row).html(data);
            },
            error: function(result, status, xhttp){
                alert(result.responseText);
            }
        });
    });
});