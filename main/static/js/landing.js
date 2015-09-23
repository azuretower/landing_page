$('#logged-in-badge').click(function(e){
    e.preventDefault();
    if($('#logged-in-badge').hasClass('closed')) {
        $('#logged-in-badge').removeClass('closed')
        $('#logged-in-badge').addClass('open')

        $('#new-post-badge').removeClass('pullup1')
        $('#logout-badge').removeClass('pullup2')
        $('#new-post-badge').addClass('dropdown1')
        $('#logout-badge').addClass('dropdown2')

    } else if($('#logged-in-badge').hasClass('open')) {
        $('#logged-in-badge').removeClass('open')
        $('#logged-in-badge').addClass('closed')

        $('#new-post-badge').removeClass('dropdown1')
        $('#logout-badge').removeClass('dropdown2')
        $('#new-post-badge').addClass('pullup1')
        $('#logout-badge').addClass('pullup2')
    };

})

$('#social-badge').click(function(e){
    e.preventDefault();
    if($('#social-badge').hasClass('closed')) {
        $('#social-badge').removeClass('closed')
        $('#social-badge').addClass('open')

        $('#social-badge').removeClass('social-in')
        $('#social-badge').addClass('social-out')
    } else if($('#social-badge').hasClass('open')) {
        $('#social-badge').removeClass('open')
        $('#social-badge').addClass('closed')

        $('#social-badge').removeClass('social-out')
        $('#social-badge').addClass('social-in')
    }
})
