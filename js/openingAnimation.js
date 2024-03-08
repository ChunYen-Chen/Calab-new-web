function fade(x) {
    y = 1-x; // 1~0 => 0~1
    // return ( Math.cos(y*Math.PI) + 1 ) / 2;
    // return 1 - y*y;
    return 1-y;
}

setInterval(function(){
    // select video element
    var vid = document.getElementById('halo-mp4-2');
    var vid_div = document.getElementById('halo-div-2');
    var rect = vid.getBoundingClientRect();
    var rect2 = vid_div.getBoundingClientRect();
    var barOffset = 0;
    var fade_percent = 0.95;
    var cur_percent = (-rect2.top) / (rect2.height - rect.height);
    if ( isNaN(cur_percent) ) { cur_percent = 0; }
    if ( cur_percent <= 0 ) {
        vid.style.position = "absoulte";
        vid.currentTime = 0;
        vid.style.opacity = 1.0;
    } else if ( cur_percent <= fade_percent ) {
        vid.style.position = "sticky";
        vid.style.top = 0;
        vid.style.opacity = 1.0;
        var vid_percent = (-rect2.top) / (rect2.height - rect.height) / fade_percent;
        if ( isNaN(vid_percent) ) { vid_percent = 0; }
        vid.currentTime = vid.duration * vid_percent;
    } else if ( cur_percent <= 1.0 ) {
        vid.style.position = "sticky";
        vid.style.top = 0;
        vid.style.opacity = fade( (1-cur_percent) / (1-fade_percent) );
        vid.currentTime = vid.duration;
    } else {
        vid.style.position = "absoulte";
        vid.currentTime = vid.duration;
        vid.style.opacity = 0.0;
    }
}, 40);


