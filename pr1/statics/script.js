// JavaScript to handle dropdown functionality
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

// JavaScript to handle dropdown functionality
// Get the dropdown toggle element
const dropdownToggle = document.querySelector('.dropdown-toggle');

// Get the dropdown menu element
const dropdownMenu = document.querySelector('.dropdown-menu');

// Add click event listener to the dropdown toggle
dropdownToggle.addEventListener('click', function(event) {
  // Prevent default link behavior
  event.preventDefault();

  // Toggle the 'show' class on the dropdown menu
  dropdownMenu.classList.toggle('show');
});

// Close the dropdown menu when clicking outside of it
document.addEventListener('click', function(event) {
  if (!event.target.matches('.dropdown-toggle')) {
      const isDropdownOpen = dropdownMenu.classList.contains('show');
      if (isDropdownOpen) {
          dropdownMenu.classList.remove('show');
      }
  }
});
document.querySelector("#contact-form").addEventListener("submit", (e) => {
e.preventDefault();
e.target.elements.name.value = "";
e.target.elements.email.value = "";
e.target.elements.message.value = "";
});