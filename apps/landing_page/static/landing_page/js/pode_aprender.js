




// ------ AREA DO CARROSSEL DE CURSOS ------

const track = document.getElementById('track');
const cards = Array.from(document.querySelectorAll('.course-card'));
const btnPrev = document.getElementById('btn-prev');
const btnNext = document.getElementById('btn-next');

let currentIndex = 0;
const totalCards = cards.length;

// Configurações da curva
let spacing = window.innerWidth <= 768 ? 260 : 380;
const curveStrength = 30;
const scaleDropoff = 0.15;
const opacityDropoff = 0;
const rotationMultiplier = 3.5;

window.addEventListener('resize', () => {
    let newSpacing = window.innerWidth <= 768 ? 260 : 380;
    if (newSpacing !== spacing) {
        spacing = newSpacing;
        updateCarousel();
    }
});

// Função auxiliar para normalizar o índice no range [0, totalCards)
function wrapIndex(index) {
    return ((index % totalCards) + totalCards) % totalCards;
}

function updateCarousel(offset = 0) {
    cards.forEach((card, index) => {
        let relativePosition = index - currentIndex - offset;
        
        // Tratamento para efeito infinito (wrap-around)
        let half = totalCards / 2;
        if (relativePosition > half) relativePosition -= totalCards;
        if (relativePosition < -half) relativePosition += totalCards;

        const absDistance = Math.abs(relativePosition);

        const translateX = relativePosition * spacing;
        const translateY = Math.pow(absDistance, 2) * curveStrength;
        const scale = Math.max(0.4, 1 - (absDistance * scaleDropoff));
        const rotateZ = relativePosition * -rotationMultiplier;
        const zIndex = 100 - Math.round(absDistance * 10);
        const opacity = Math.max(0, 1 - (absDistance * opacityDropoff));

        card.style.transform = `translateX(${translateX}px) translateY(${translateY}px) scale(${scale}) rotateZ(${rotateZ}deg)`;
        card.style.zIndex = zIndex;
        card.style.opacity = opacity;
        
        if(absDistance > 3) {
            card.style.pointerEvents = 'none';
            card.style.visibility = 'hidden';
        } else {
            card.style.pointerEvents = 'auto';
            card.style.visibility = 'visible';
        }
    });
}

updateCarousel();

function moveNext() {
    currentIndex = wrapIndex(currentIndex + 1);
    updateCarousel();
}

function movePrev() {
    currentIndex = wrapIndex(currentIndex - 1);
    updateCarousel();
}

btnNext.addEventListener('click', moveNext);
btnPrev.addEventListener('click', movePrev);

let isDown = false;
let startX;
let startCurrentIndex;
let dragOffset = 0;

track.addEventListener('mousedown', (e) => {
    isDown = true;
    track.classList.add('dragging');
    startX = e.pageX;
    startCurrentIndex = currentIndex;
    dragOffset = 0;
});

window.addEventListener('mouseleave', () => {
    if(isDown) snapToCard();
});

window.addEventListener('mouseup', () => {
    if(isDown) snapToCard();
});

track.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    
    const x = e.pageX;
    const diffX = x - startX;
    dragOffset = diffX / spacing; 

    updateCarousel(-dragOffset);
});

function snapToCard() {
    isDown = false;
    track.classList.remove('dragging');
    
    currentIndex = wrapIndex(startCurrentIndex - Math.round(dragOffset));
    updateCarousel();
}

track.addEventListener('touchstart', (e) => {
    isDown = true;
    track.classList.add('dragging');
    startX = e.touches[0].pageX;
    startCurrentIndex = currentIndex;
    dragOffset = 0;
}, {passive: true});

track.addEventListener('touchmove', (e) => {
    if (!isDown) return;
    const x = e.touches[0].pageX;
    const diffX = x - startX;
    dragOffset = diffX / spacing; 

    updateCarousel(-dragOffset);
}, {passive: false});

track.addEventListener('touchend', () => {
    if(isDown) snapToCard();
});



// ------ FIM DA AREA DO CARROSSEL DE CURSOS ------








(function () {
    const AUTOPLAY_INTERVAL_MS = 5000;

    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.carousel-indicators span');
    const prevButton = document.querySelector('.hero-arrow-prev');
    const nextButton = document.querySelector('.hero-arrow-next');

    if (!slides.length || !dots.length) {
        return;
    }

    let currentIndex = 0;
    let autoplayTimer = null;

    function goToSlide(index) {
        slides[currentIndex].classList.remove('active');
        dots[currentIndex].classList.remove('active');

        currentIndex = (index + slides.length) % slides.length;

        slides[currentIndex].classList.add('active');
        dots[currentIndex].classList.add('active');
    }

    function nextSlide() {
        goToSlide(currentIndex + 1);
    }

    function prevSlide() {
        goToSlide(currentIndex - 1);
    }

    function startAutoplay() {
        stopAutoplay();
        autoplayTimer = setInterval(nextSlide, AUTOPLAY_INTERVAL_MS);
    }

    function stopAutoplay() {
        if (autoplayTimer) {
            clearInterval(autoplayTimer);
            autoplayTimer = null;
        }
    }

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            goToSlide(index);
            startAutoplay();
        });
    });

    if (prevButton) {
        prevButton.addEventListener('click', () => {
            prevSlide();
            startAutoplay();
        });
    }

    if (nextButton) {
        nextButton.addEventListener('click', () => {
            nextSlide();
            startAutoplay();
        });
    }

    startAutoplay();
})();













