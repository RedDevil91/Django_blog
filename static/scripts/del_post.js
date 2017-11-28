$('#del-form').on('submit', function(event){
    event.preventDefault();
    console.log("DELETED!")
    del_post();
});

function del_post() {
    console.log("Del post is working!") // sanity check

    var csrf_token = getCookie("csrftoken");

    $.ajax({
        url : "del_post/",
        type : "POST",
        data : { 'csrfmiddlewaretoken': csrf_token,
                 'pk' : $('#del-btn').attr('data-pk')},
        success : function(json) {
            console.log(json);
            window.location.href = "http://127.0.0.1:8000/blog/";
        },
        error : function(xhr, errmsg, err){
            console.log("ERROR!");
        }
    });
};