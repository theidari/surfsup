let btnOpen = document.querySelector('button');
let input = document.querySelector('input');
btnOpen.addEventListener('click', () => {
    window.open('http://127.0.0.1:5000/api/v1.0/'+input.value, '_blank', 'height=600px, width=600px');
});
