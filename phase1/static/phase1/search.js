$(document).ready(function () {

    $("#search").keyup(function (event) {
        if (event.keyCode == 13) {
            $("#search_button").click();
        }
    });
    $("#categorized").change(function(){
        $("#search_button").click();
    })
    $(document).on('click','.category',function(){
        var val=$(this).attr('val');
        $("#search").val(val);
        $("#search_button").click();
    });
    $("#search_button").click(function(){
        var text=$("#search").val();
        var isCat = $("#categorized").prop('checked');
        console.log(isCat);
        $.ajax({
            url:'/news',
            method:'GET',
            data:{
                category: text,
                isCat: isCat,
            },
            success: function(data, status, xhttp) {
                console.log(data);
                var news=data;
               // console.log(news.length);
                newsDiv = $('#accordion');
                newsDiv.empty();
                if (news.length == 0){
                    var appendingData = '<div class="alert alert-danger">' +
                                        '<strong> There are not any news with this category </strong> ' +
                                        '</div>'
                    newsDiv.append(appendingData)
                }
                for(var i=0;i<news.length;i++)
                {
                    var categoriesList='';
                    for(var j=0;j<news[i].categories.length;j++)
                    {
                        categoriesList+='<button type="button" class="btn btn-warning category" style="margin-bottom: 10px" id="category-'+i+'-'+j+'" val="'+news[i].categories[j].category+'">'+news[i].categories[j].category+'</button>&nbsp';
                    }
                    var appendingData =
                        '<div class="panel panel-default " style="margin: 20px;">' +
                            '<div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse'+i+'" >'+
                                '<h4 class="panel-title">'+
                                    '<a>'+news[i].title+'</a>' +
                                    '<span style="float:right">'+news[i].date+'</span>'+
                                '</h4>'+
                            '</div>'+
                            '<div id="collapse'+i+'" class="panel-collapse collapse">'+
                                '<div class="panel-body">'+news[i].description+'</div>'+
                                '<div style="margin:5px;">'+categoriesList+'</div>'+
                            '</div>'+
                        '</div>';
                    newsDiv.append(appendingData);
                }
            },
            error: function(result, status, xhttp){
                $('#accordion').empty();
            }
        });

    })
});