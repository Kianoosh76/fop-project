$(document).ready(function(){

    set_votes_color();
    function get_member(){
        return $("#members option:selected").val();
    }

    function get_team(row){
        return $("#team-" + row);
    }

    function get_vote(member, team){
        return $("#vote-" + member + "-" + team);
    }

    function set_vote_color(row){
        var member = get_member();
        var team = get_team(row).val();
        var vote = get_vote(member, team);
        var color = 'red';
        if (!vote.length || vote.val () != 'True')
            color = 'black'
        $("#votes-" + row).css('color', color);
        $("#" + row).css('color', color);
    }

    function set_votes_color(){
        for (var i=1; ; i++){
            if (get_team(i).length){
                set_vote_color(i);
            }
            else
                break;
        }
    }

    $(".like").click(function(){
        var row = $(this).attr('id');
        var member = get_member();
        var team = get_team(row).val();
        $.ajax({
            url: '/like',
            method: 'POST',
            data: {
                team: team,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                member: member
            },
            success: function(data, status, xhttp){
                $("#votes-" + row).html(data);
                var vote = get_vote(member, team);
                if (vote.length){
                    if (vote.val() == 'True')
                        vote.attr('value', 'False');
                    else
                        vote.attr('value', 'True');
                }
                else{
                    $("#votes").append($('<input>').attr('type', 'hidden').attr('id', 'vote-'+member+'-'+team).attr('value', 'True'));
                }

                set_vote_color(row);
            },
            error: function(result, status, xhttp){
                alert(result.responseText);
            }
        });
    });

    $("#members").change(function(){
        set_votes_color();
    });
});