function startTypingEffects() {
    const heroTitle = document.querySelector('.hero-title');
    const heroSubtitle = document.querySelector('.hero-subtitle');
    
    if (!heroTitle || !heroSubtitle) return;
    const titleText = 'Leticia Fontes';
    const subtitleText = 'Desenvolvedora Backend';
    
    let titleIndex = 0;
    let subtitleIndex = 0;
    heroTitle.textContent = '';
    heroSubtitle.textContent = '';
    function typeTitle() {
        if (titleIndex < titleText.length) {
            heroTitle.textContent += titleText.charAt(titleIndex);
            titleIndex++;
            setTimeout(typeTitle, 100);
        } else {
            setTimeout(typeSubtitle, 500);
        }
    }

    function typeSubtitle() {
        if (subtitleIndex < subtitleText.length) {
            heroSubtitle.textContent += subtitleText.charAt(subtitleIndex);
            subtitleIndex++;
            setTimeout(typeSubtitle, 80);
        }
    }

    setTimeout(typeTitle, 1000);
}

document.addEventListener('DOMContentLoaded', function() {

    startTypingEffects();
    
    console.log('JavaScript carregado com sucesso! 🚀');
});