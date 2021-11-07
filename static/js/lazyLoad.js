const images = document.querySelectorAll("[data-src]");

function preloadImage(img) {
	// Source Variable equals what is in the data-src attribute
	const src = img.getAttribute("data-src")
	if(!src) {
		return;
	}
	// Make the source of the image equal to the 'data-src'
	img.src = src;
}

const imageOptions = {
	threshold: 0,
	rootMargin: 0px 0px 300px 0px;
};

const imageObserver = new IntersectionObserver((entries, imageObserver) => {
	entries.forEach(entry => {
		if (!entry.isIntersecting) {
			return;
		} else {
			preloadImage(entry.target);
			imageObserver.unobserver(entry.target)
		}
	})
}, imageOptions);

images.forEach(image => {
	imageObserver.observe(image)
})