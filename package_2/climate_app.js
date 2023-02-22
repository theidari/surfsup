// queries input function (as searcher function)
function searcher() {
    const starty = document.getElementById('start_date');
    const endy = document.getElementById('end_date');
    let btnOpen = document.querySelector('button_1');
    if (starty.value==""){
        alert("Please Input Start Date!")
    }
    else if (endy.value==""){
        window.open('http://127.0.0.1:5000/api/v1.0/'+starty.value, '_blank', 'height=600px, width=600px');
    }
    else { 
        window.open('http://127.0.0.1:5000/api/v1.0/'+starty.value+'/'+endy.value, '_blank', 'height=600px, width=600px');
    }}
btnOpen.addEventListener('click', searcher()); 

// dropdown function by getting elementby id (as searcher droppy)
function droppy() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
        }
    }
    }
}