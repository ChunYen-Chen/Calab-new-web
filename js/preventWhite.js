// Prevent the white when too less content
// please add the script when necessary
const section = document.getElementsByClassName("main-section")[0]; // assume to be one main section
const footer  = document.getElementById("footer");

// update the window size
function updateSize() {
  var min_height = window.innerHeight - footer.getBoundingClientRect().height ;
  section.style.minHeight = min_height.toString() + "px";
}

// Add event listener for window resize
window.addEventListener('click', updateSize);
window.addEventListener('resize', updateSize);

// Initial update
updateSize();
