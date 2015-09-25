var page = 0
var page_size = 3
// loadPreviews(page, page_size);

function loadPreviews(page, page_size) {

    $.ajax({
        url: window.PREVIEWS,
        data: {
            page: page,
            page_size: page_size
        },
        success: function(result) {

            if (result.length === 0) {
                $('#post-previews').append("<p>That's All I've Got For Now...</p>")
                $('#older-posts').hide();
            } else {
                $('#post-previews').append(result);
            }
        }
    })
}

$('#older-posts').click(function(e){
    e.preventDefault();
    page++
    loadPreviews(page);
})
