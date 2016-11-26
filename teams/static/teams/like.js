$(document).ready(function(){
    $(".like").click(function(){
        var row = $(this).attr('row');
        $.ajax({
            url: '/like',
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'team': $("#"),
                'member': $("#members:selected").val()
            },
            success: function(data, status, xhttp){
            },
            error: function(data, status, xhttp){
                alert(data.responseText);
            }
        });
    });
});