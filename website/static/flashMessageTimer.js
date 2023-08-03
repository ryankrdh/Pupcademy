// Function to hide the flash message
function hideFlashMessage() {
	var flashMessage = document.querySelector('.alert');
	if (flashMessage) {
		flashMessage.style.display = 'none';
	}
}

// Function to show flash messages with optional duration parameter
function showFlashMessage(duration = 3000) {
	var flashMessage = document.querySelector('.alert');
	if (flashMessage) {
		flashMessage.style.display = 'block';
		setFlashTimer(duration);
	}
}

// Timer to hide flash message
function setFlashTimer(duration) {
	setTimeout(hideFlashMessage, duration);
}

// Call the showFlashMessage function when the page loads
document.addEventListener('DOMContentLoaded', function () {
	showFlashMessage();
});
