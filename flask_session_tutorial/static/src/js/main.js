// Remove Alert on Close
let alertButton = document.querySelector('.alert button');

if (alertButton){
  alertButton.addEventListener('click', function (event) {

  	// If the clicked element doesn't have the right selector, bail
    alertbutton.parentNode.style.display = 'none';

  	// Don't follow the link
  	event.preventDefault();

  }, false);
}
