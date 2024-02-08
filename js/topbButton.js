// Reference: https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function scrollToTop() {
  let duration = 1000; // in miliseconds
  const start = window.pageYOffset;
  const startTime = 'now' in window.performance ? performance.now() : new Date().getTime();

  function scroll() {
    const currentTime = 'now' in window.performance ? performance.now() : new Date().getTime();
    const timeElapsed = currentTime - startTime;
    const progress = Math.min(timeElapsed / duration, 1);

    window.scrollTo(0, easeInOutCubic(start, 0, progress));

    if (progress < 1) {
      requestAnimationFrame(scroll);
    }
  }

  // Easing function for smooth scrolling
  function easeInOutCubic(start, end, progress) {
    progress /= 0.5;
    if (progress < 1) return 0.5 * progress * progress * progress * (end - start) + start;
    progress -= 2;
    return 0.5 * (progress * progress * progress + 2) * (end - start) + start;
  }

  requestAnimationFrame(scroll);
}
