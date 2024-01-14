/*!
 * Start Bootstrap - Agnecy Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        var animate_speed = 'easeInOutExpo';
        var animate_duration = 1500;
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, animate_duration, animate_speed);
        event.preventDefault();
    });
});
$(function() {
    $('a.page-scroll-slow').bind('click', function(event) {
        var $anchor = $(this);
        var animate_speed = 'easeInOutExpo';
        var animate_duration = 3000;
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, animate_duration, animate_speed);
        event.preventDefault();
    });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});
