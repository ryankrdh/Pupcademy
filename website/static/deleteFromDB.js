function deleteNote(noteId) {
	fetch('/delete-note', {
		method: 'POST',
		body: JSON.stringify({ noteId: noteId }),
	}).then((_res) => {
		window.location.href = '/';
	});
}
function deleteDog(dogID) {
	fetch('/delete-dog', {
		method: 'POST',
		body: JSON.stringify({ dogID: dogID }),
	}).then((_res) => {
		window.location.href = '/training';
	});
}
