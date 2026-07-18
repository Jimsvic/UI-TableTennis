document.addEventListener("DOMContentLoaded", function() {
  let slides = document.querySelector('.slides');
  let currentSlide = 0;

  function showSlide(index) {
    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === index);
    });
  }

  function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
  }

  // Initialize the first slide
  showSlide(currentSlide);

  // Set interval to change slides every 3 seconds
  setInterval(nextSlide, 3000);

   // Register button
   document.getElementById('register-btn').addEventListener('click', function() {
    alert('Register now to participate in the tournament!');
  });

  // Responsive menu
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');

  menuToggle.addEventListener('click', () => {
    nav.classList.toggle('active');
  });
});