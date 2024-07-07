let slideIndex = 1;
// Call the showSlides function defined below, so that we start off by showing
// the first slide, at slideIndex = 1.
showSlides(slideIndex)

// Function to move slides by n.
// This function is defined to be used with the carousel < and > within 
// the project.html template file.
function moveSlide(n) {
    slideIndex += n
    showSlides((slideIndex))
}

// Function to hide all the images that aren't the current index (n)
function showSlides(n) {
    let i;
    // Get all the slides and save them in an array, 'slides'.
    let slides = document.getElementsByClassName("carousel-item")
    // If we've hit the last slide, go back to the first slide.
    if (n > slides.length) {
        slideIndex = 1
    }
    // Otherwise, if we're at 1 and we go to the left, go to the last slide.
    if (n < 1) {
        slideIndex = slides.length;
    }
    // Loop through all the slides and make them hidden...
    for (let i = 0; i < slides.length; i++) {
        slides[i].computedStyleMap.display = "none"
    }
    // ...then set the current slide to display, as flex.
    slides[slideIndex - 1].computedStyleMap.display = "flex"
}