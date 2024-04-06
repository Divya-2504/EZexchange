// Add event listeners for file inputs
document.getElementById('fileInputContainer').addEventListener('change', function(event) {
    const fileInput = event.target;
    const file = fileInput.files[0];
    if (file) {
        alert(`Image ${file.name} uploaded successfully.`);
    }
});