document.addEventListener('DOMContentLoaded', function() {
  var openingAnimation = document.querySelector('.opening-animation');

  openingAnimation.addEventListener('animationend', function() {
    openingAnimation.classList.add('visible');
  });

  var openingAnimation = document.querySelector('.opening-animation-from-bottom');

  openingAnimation.addEventListener('animationend', function() {
    openingAnimation.classList.add('visible');
  });
});


// select video element
var vid = document.getElementById('halo-mp4');
var vid_div = document.getElementById('halo-div');
var nav = document.getElementById('nav-bar');
//var vid = $('#v0')[0]; // jquery option

// pause video on load
vid.pause();

// pause video on document scroll (stops autoplay once scroll started)
window.onscroll = function(){
    vid.pause();
};

// refresh video frames on interval for smoother playback
setInterval(function(){
    var speed = 10;
    var rect = vid.getBoundingClientRect();
    var rect_nav = nav.getBoundingClientRect();
    var barOffset = 0;
    //var barOffset = rect_nav.bottom;
    //console.log(rect_nav);
    //console.log(window.pageYOffset);
    //console.log(rect);
    //console.log(rect_nav.bottom, rect.top, rect.bottom);
    if ( 0 <= rect.top - barOffset ) {
        vid.currentTime = 0;
        vid.classList.remove('video-fixed');
    } else if ( 0 >= rect.bottom - barOffset ) {
        vid.currentTime = vid.duration;
        vid.classList.remove('video-fixed');
    } else {
        vid.classList.add('video-fixed');
        vid.style.top = barOffset;
        vid.currentTime = (barOffset - rect.top)/speed;
    }
}, 40);


setInterval(function(){
    // select video element
    var vid = document.getElementById('halo-mp4-2');
    var vid_div = document.getElementById('halo-div-2');
    var rect = vid.getBoundingClientRect();
    var rect2 = vid_div.getBoundingClientRect();
    var barOffset = 0;
    var time = (-rect2.top) / (rect2.height - rect.height);
    if ( isNaN(time) ) { time = 0; }
    if ( time <= 0 ) {
        vid.style.position = "absoulte";
        vid.currentTime = 0;
    } else if ( time >= 1 ) {
        vid.style.position = "absoulte";
        vid.currentTime = vid.duration;
    } else {
        vid.style.position = "sticky";
        vid.style.top = 0;
        vid.currentTime = vid.duration * time;
    }
}, 40);
