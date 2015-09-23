$('#logged-in-badge').click(function(e){
    e.preventDefault();
    if($('#logged-in-badge').hasClass('closed')) {
        $('#logged-in-badge').removeClass('closed')
        $('#logged-in-badge').addClass('open')

        $('#logged-in-badge').addClass('grow')

        $('#new-post-badge').removeClass('pullup1')
        $('#logout-badge').removeClass('pullup2')
        $('#new-post-badge').addClass('dropdown1')
        $('#logout-badge').addClass('dropdown2')

    } else if($('#logged-in-badge').hasClass('open')) {
        $('#logged-in-badge').removeClass('open')
        $('#logged-in-badge').addClass('closed')

        $('#logged-in-badge').removeClass('grow')

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

        $('#github-link').addClass('rotate1')
        $('#facebook-link').addClass('rotate2')
        $('#email-link').addClass('rotate3')
        $('#twitter-link').addClass('rotate4')
        $('#linkedin-link').addClass('rotate5')
    } else if($('#social-badge').hasClass('open')) {
        $('#social-badge').removeClass('open')
        $('#social-badge').addClass('closed')

        $('#social-badge').removeClass('social-out')
        $('#social-badge').addClass('social-in')

        $('#github-link').removeClass('rotate1')
        $('#facebook-link').removeClass('rotate2')
        $('#email-link').removeClass('rotate3')
        $('#twitter-link').removeClass('rotate4')
        $('#linkedin-link').removeClass('rotate5')
    }
})
