function sendSearchRequest(keyword){
    const resultContainer = document.getElementById('search-container')
    const url = `/tool/?keyword=${encodeURIComponent(keyword.value)}`;
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

function searchDevTool() {
    const searchBtn = document.getElementById('search-btn');
    const keyword = document.getElementById('search-bar');
    const keywordInput = document.getElementById('keyword-input');
    searchBtn.addEventListener('click', ()=>{       
        keywordInput.value = keyword.value;
        sendSearchRequest(keyword);
    });
    keyword.addEventListener('input', ()=>{
        keywordInput.value = keyword.value;
        sendSearchRequest(keyword);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    searchDevTool();
});