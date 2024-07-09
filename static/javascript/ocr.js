document.addEventListener('DOMContentLoaded', () => {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('fileInput');
    const fileSelector = document.getElementById('fileSelector');
    const displayedImage = document.getElementById('displayedImage');

    dropzone.addEventListener('dragover', (event) => {
        event.preventDefault();
        dropzone.classList.add('dragover');
    });

    dropzone.addEventListener('dragleave', () => {
        dropzone.classList.remove('dragover');
    });

    dropzone.addEventListener('drop', (event) => {
        event.preventDefault();
        dropzone.classList.remove('dragover');
        const file = event.dataTransfer.files[0];
        if (file) {
            displayImage(file);
        }
    });

    fileSelector.addEventListener('click', (event) => {
        event.preventDefault();
        fileInput.click();
    });

    fileInput.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            displayImage(file);
        }
    });

    window.selectSampleImage = (src) => {
        // src = "./images/" + src
        displayedImage.src = src;
    };

    function displayImage(file) {
        const reader = new FileReader();
        reader.onload = (event) => {
            displayedImage.src = event.target.result;
        };
        reader.readAsDataURL(file);
    }

    function ocr(file) {
        fetch('/api/ocr', {
            method: 'POST',
            body: file,
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Update the page or show a success message based on 'data'
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle errors here, such as showing an error message
            });
    }
});
