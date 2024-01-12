document.addEventListener('DOMContentLoaded', function() {
  var openingAnimation = document.querySelector('.opening-animation');

  openingAnimation.addEventListener('animationend', function() {
    openingAnimation.classList.add('visible');
  });
});
