let menu = document .querySelector('#menu-icon');
let navbar = document .querySelector('.navbar');

menu.onclick = () => {
    menu.classList .toggle('bx-x');
    navbar.classList .toggle('active');
}

// JavaScript functions to open/close the modal
function openModal() {
    document.getElementById('signupModal').style.display = 'block';
    document.getElementById('signupForm').style.display = 'block';
}

function closeModal() {
    document.getElementById('signupModal').style.display = 'none';
    document.getElementById('signupForm').style.display = 'none';
}
