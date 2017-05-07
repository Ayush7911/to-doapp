window.addEventListener('load', handleLoad);

function handleLoad() {
    var form = document.querySelector('form.create-form');

    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
}

function handleFormSubmit(e) {
    var titleInput = document.querySelector('#input-todo-title');
    var title = titleInput.value.trim();

    if (!title || title === '') {
        alert('Please enter the title.');
        titleInput.focus();
        e.preventDefault();
    }
}