(function () {
    const grid = document.querySelector('#course-grid');
    const category = document.querySelector('#category-filter');
    const sort = document.querySelector('#sort-courses');
    const search = document.querySelector('#course-search');
    const empty = document.querySelector('.empty-courses');
    if (!grid || !category || !sort || !search) return;

    const cards = [...grid.querySelectorAll('.catalog-card')];

    function updateCatalog() {
        const query = search.value.trim().toLocaleLowerCase('pt-BR');
        let visibleCount = 0;

        cards.forEach((card) => {
            const matchesCategory = category.value === 'all' || card.dataset.category === category.value;
            const matchesSearch = card.dataset.title.includes(query);
            card.hidden = !(matchesCategory && matchesSearch);
            if (!card.hidden) visibleCount += 1;
        });

        const sorted = [...cards].sort((a, b) => {
            if (sort.value === 'title') return a.dataset.title.localeCompare(b.dataset.title, 'pt-BR');
            if (sort.value === 'hours-asc') return Number(a.dataset.hours) - Number(b.dataset.hours);
            if (sort.value === 'hours-desc') return Number(b.dataset.hours) - Number(a.dataset.hours);
            return Number(a.dataset.order) - Number(b.dataset.order);
        });
        sorted.forEach((card) => grid.appendChild(card));
        empty.hidden = visibleCount !== 0;
    }

    category.addEventListener('change', updateCatalog);
    sort.addEventListener('change', updateCatalog);
    search.addEventListener('input', updateCatalog);
})();
