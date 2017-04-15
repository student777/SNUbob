$(function(){
    $("div.item").first().addClass('active');
})

// toaster
$(function(){
    $("#comment_form").submit(function() {
        var url = $(this).attr("action");
        var content = $(this).find("input[name=content]").val();
        var star = $(this).find("select[name=star]").val();
        if(content ==""){
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
                content: content,
                star: star,
            }
        }).fail(function() {
            $.toaster({
                    title: 'fail',
                    priority: 'danger',
                    message: '다시 시도해 주세요'
            });
        }).done(function(html) {
            $("#comment_list").append(html);
            $("#tofade").hide();
            $.toaster({
                    title: 'success',
                    priority: 'success',
                    message: '새 댓글이 등록되었습니다'
            });
            $("input[name=content]")[0].value="";
        });
        return false;
    });
});

// image upload
$(function() {
    $("input[type='file']").change( function() {
        $file = $(this).val();
        if ($file == null || $.isEmptyObject($file)) return;
        var formData = new FormData(document.getElementById('image_form'));
        $.ajax({
            url : "/" + bob_id + "/add_image/",
            data : formData,
            processData : false,
            contentType : false,
            type : "POST",
            success : function(response) {
                location.href = '';
            },
            error : function(xhr, status, error) {
                console.error(status + " : " + error);
            }
        })
    })
})