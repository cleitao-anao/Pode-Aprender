(function () {
    const moments = [
        { year: '2010', title: 'A primeira ideia', paragraphs: ['A vontade de ampliar o acesso à educação nasceu das conversas com jovens e famílias da comunidade. Era o começo de um projeto construído a partir da escuta.', 'As primeiras ações mostraram que aprender em conjunto poderia abrir caminhos e fortalecer sonhos.'], images: ['photo-1529390079861-591de354faf5', 'photo-1517486808906-6ca8b3f04846', 'photo-1523240795612-9a054b0db644', 'photo-1529156069898-49953e39b3ac'] },
        { year: '2015', title: 'Onde tudo começou', paragraphs: ['A Pode Aprender nasceu do desejo de aproximar jovens da educação e da tecnologia. Em 2015, os primeiros encontros reuniram pessoas dispostas a compartilhar conhecimento e criar novas oportunidades dentro da comunidade.', 'O que começou pequeno cresceu com a força de alunos, voluntários e parceiros.'], images: ['photo-1529390079861-591de354faf5', 'photo-1529156069898-49953e39b3ac', 'photo-1531482615713-2afd69097998', 'photo-1522202176988-66273c2fd55f'] },
        { year: '2017', title: 'Novos caminhos', paragraphs: ['Com novas turmas e mais voluntários, ampliamos as atividades e incluímos formações voltadas ao desenvolvimento pessoal e profissional.', 'A comunidade cresceu e cada encontro passou a conectar mais talentos, experiências e oportunidades.'], images: ['photo-1523240795612-9a054b0db644', 'photo-1522202176988-66273c2fd55f', 'photo-1531482615713-2afd69097998', 'photo-1516321318423-f06f85e504b3'] },
        { year: '2019', title: 'Educação que transforma', paragraphs: ['A tecnologia ganhou ainda mais espaço em nossos cursos. Novas parcerias ajudaram a oferecer experiências práticas e próximas das necessidades do mercado.', 'Seguimos valorizando o protagonismo dos alunos e o impacto positivo de cada conquista.'], images: ['photo-1516321318423-f06f85e504b3', 'photo-1531482615713-2afd69097998', 'photo-1522202176988-66273c2fd55f', 'photo-1523240795612-9a054b0db644'] },
        { year: '2025', title: 'O futuro é agora', paragraphs: ['Celebramos uma trajetória feita por alunos, educadores, voluntários e parceiros que acreditam no poder do conhecimento.', 'Continuamos criando oportunidades para que mais pessoas aprendam, compartilhem e transformem suas histórias.'], images: ['photo-1573164713988-8665fc963095', 'photo-1529156069898-49953e39b3ac', 'photo-1522202176988-66273c2fd55f', 'photo-1529390079861-591de354faf5'] }
    ];
    const timeline = document.querySelector('.timeline');
    const items = [...document.querySelectorAll('.timeline li')];
    const story = document.querySelector('.history-story');
    if (!timeline || !story) return;
    let current = 1;

    function render(index) {
        current = (index + moments.length) % moments.length;
        const moment = moments[current];
        story.classList.add('is-changing');
        window.setTimeout(function () {
            story.querySelector('.story-year').textContent = moment.year;
            story.querySelector('h2').textContent = moment.title;
            story.querySelectorAll('.history-copy p').forEach((p, i) => { p.textContent = moment.paragraphs[i]; });
            story.querySelectorAll('img').forEach((img, i) => { img.src = `https://images.unsplash.com/${moment.images[i]}?auto=format&fit=crop&w=800&q=85`; });
            items.forEach((item, i) => {
                item.classList.toggle('active', i === current);
                item.querySelector('button').toggleAttribute('aria-current', i === current);
            });
            timeline.style.setProperty('--timeline-progress', `${current * 25}%`);
            story.classList.remove('is-changing');
        }, 200);
    }

    items.forEach((item, index) => item.querySelector('button').addEventListener('click', () => render(index)));
    document.querySelector('.history-prev').addEventListener('click', () => render(current - 1));
    document.querySelector('.history-next').addEventListener('click', () => render(current + 1));
    document.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowLeft') render(current - 1);
        if (event.key === 'ArrowRight') render(current + 1);
    });
})();
