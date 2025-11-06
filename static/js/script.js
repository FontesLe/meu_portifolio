
let animationInProgress = false;

function startNameAnimation() {
    if (animationInProgress) return;

    animationInProgress = true;

    const nameElement = document.getElementById('dynamic-name');
    const titleElement = document.getElementById('dynamic-title');
    nameElement.innerHTML = '';
    titleElement.innerHTML = '';

    const nameText = 'Leticia Fontes';
    const titleText = 'Desenvolvedora Backend';

    let nameIndex = 0;
    let titleIndex = 0;

    function typeName() {
        if (nameIndex < nameText.length) {
            nameElement.innerHTML += nameText.charAt(nameIndex);
            nameIndex++;
            setTimeout(typeName, 100);
        } else {

            setTimeout(typeTitle, 500);
        }
    }

    function typeTitle() {
        if (titleIndex < titleText.length) {
            titleElement.innerHTML += titleText.charAt(titleIndex);
            titleIndex++;
            setTimeout(typeTitle, 80);
        } else {
            setTimeout(() => {
                animationInProgress = false;
            }, 1000);
        }
    }

    typeName();
}

document.addEventListener('DOMContentLoaded', function () {
    startNameAnimation();

    const homeSection = document.getElementById('home');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animationInProgress) {
                setTimeout(startNameAnimation, 500);
            }
        });
    }, {
        threshold: 0.7
    });

    observer.observe(homeSection);
});

document.querySelector('a[href="#home"]').addEventListener('click', function (e) {
    e.preventDefault();
    document.getElementById('home').scrollIntoView({ behavior: 'smooth' });
    setTimeout(() => {
        if (!animationInProgress) {
            startNameAnimation();
        }
    }, 1000);
});
