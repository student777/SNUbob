$(function(){
    $("#comment_form").find("input[name=star]").remove()
    $("#star_rate").rating();
    var len = {{ bob.comment_set.count}};
    for(var i=0;i<len;i++){
        var k = parseInt($(".stars")[i].innerHTML);
        var str = '<span class="glyphicon glyphicon-star-empty" aria-hidden="true"></span>'
        $(".stars")[i].innerHTML=str.repeat(k);
    }
    $("div.item").first().addClass('active')
    })
$(function(){
    var tex = $("textarea:first");
    tex.className = "form-control";
    tex.attr("rows", "3");
    tex.css("width", "100%");
    $("form div").contents().filter(function(){ return this.nodeType != 1; }).remove();
});
$(function(){
    $("#comment_form").submit(function() {
        var url = $(this).attr("action");
        var content_value = $(this).find("textarea[name=content]").val();
        var star = $("#star_rate")[0].value;
        if(content_value ==""){
            $.toaster({
                    title: 'fail',
                    priority: 'danger',
                    message: '내용을 입력해 주세요'
                });
            return false;
        }
        $.ajax({
            url: url,
            method: "POST",
            data: {
                content: content_value,
                star: star,
            }
        }).fail(function() {
            $.toaster({
                    title: 'fail',
                    priority: 'danger',
                    message: '다시 시도해 주세요'
            });
        }).done(function(html) {
            $("#comment_list").prepend(html);
            $("#tofade").hide();
            $.toaster({
                    title: 'success',
                    priority: 'success',
                    message: '새 댓글이 등록되었습니다'
            });
            $("textarea")[0].value="";
        });
        return false;
    });
    $(document).on('click', '#delete_comment', function(){
        if ( confirm("Are you sure?") ) {
            var url = $(this).attr("href");
            var comment_id = $(this).data("comment-id");
            $.ajax({
                url: url,
                method: "POST"
            }).fail(function() {
                $.toaster({
                    title: 'fail',
                    priority: 'danger',
                    message: '다시 시도해 주세요'
                });
            }).done(function() {
                $("#" + comment_id).remove();
                $.toaster({
                    title: 'success',
                    priority: 'success',
                    message: '댓글을 삭제하였습니다'
                });
            });
        }
        return false;
    });
});