jQuery(document).ready(function($){
    $('button').on('click', function() {
        $('.menu_mobile').removeClass('hidden').addClass('active');
    });
    
    $('.close-menu').on('click', function() {
        $('.menu_mobile').removeClass('active');
    });
});