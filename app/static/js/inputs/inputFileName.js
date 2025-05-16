const fileInput = document.getElementById('file-input');
const fileNameSpan = document.getElementById('file-name');

fileInput.addEventListener('change', function() {
    if (this.files.length > 0) {
    fileNameSpan.textContent = this.files[0].name;
    } else {
    fileNameSpan.textContent = '';
    }
});