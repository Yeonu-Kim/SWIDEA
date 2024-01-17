function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function togglePickBtn() {
    document.body.addEventListener('click', (event) => {
        const button = event.target.closest('.pick-btn');
        if (button) {
            const ideaId = button.getAttribute('button-pk');
            const url = `pick/${ideaId}/`;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({}),
            })
            .then(response => response.json())
            .then(data => {
                if (data.pick_status) {
                    button.classList.add('yellow-star');
                    button.classList.remove('black-star');
                }
                else{
                    button.classList.add('black-star');
                    button.classList.remove('yellow-star');
                }
            });
        }
    });
}

function changeInterest() {
    document.body.addEventListener('click', (event) => {
        const container = event.target.closest('.interest-container');
        if (container) {
            const minusBtn = container.children[0];
            const plusBtn = container.children[2];
            const interestValue = container.children[1];
            const ideaId = container.getAttribute('button-pk');
            const plusUrl = `/idea/${ideaId}/add_interest/`;
            const minusUrl = `/idea/${ideaId}/minus_interest/`;

            if (event.target === plusBtn && parseInt(interestValue.innerText) < 5) {
                fetch(plusUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                    body: JSON.stringify({}),
                })
                .then(response => response.json())
                .then(data => {
                    interestValue.innerText = data.interest_status;
                });
            }

            if (event.target === minusBtn && parseInt(interestValue.innerText) > 0) {
                fetch(minusUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                    body: JSON.stringify({}),
                })
                .then(response => response.json())
                .then(data => {
                    interestValue.innerText = data.interest_status;
                });
            }
        }
    });
}
function sendSortRequest(keyword){
    const resultContainer = document.getElementById('idea-container')
    const sortForm = document.getElementById('sort-form');
    const url = `/?order=${encodeURIComponent(keyword.value)}`;
    fetch(url,{
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        },
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        resultContainer.innerHTML = data.html_from_view;
    })
}

function sortIdea() {
    const sortSelect = document.getElementById('sort-select');
    sortSelect.addEventListener('change', ()=>{        
        sendSortRequest(sortSelect);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    sortIdea();
    togglePickBtn();
    changeInterest();
});
