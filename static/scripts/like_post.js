$('#like-form').on('submit', function(event){
    event.preventDefault();
    console.log("Submitted!")
    like_post();
});

function like_post() {
    console.log("Like post is working!") // sanity check

    var csrf_token = getCookie("csrftoken");

    $.ajax({
        url : "like_post/",
        type : "POST",
        data : { 'csrfmiddlewaretoken': csrf_token,
                 'pk' : $('#like-btn').attr('data-pk')},
        success : function(json) {
            $('#like-btn').text(json.state);
            console.log(json);
        },
        error : function(xhr, errmsg, err){
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
};