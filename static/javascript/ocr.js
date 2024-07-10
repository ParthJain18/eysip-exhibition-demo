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
        const data = { imagePath: src };
    
        // Attempt to load the image to check if it's present
        const testImage = new Image();
        testImage.onload = () => {
            // If the image loads successfully, send the data to the /api/ocr endpoint
            fetch('/api/ocr', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('OCR result:', data);
                document.getElementById('ocrText').innerHTML = data.text;
                // Display the OCR result or do further processing
            })
            .catch(error => {
                console.error('Error during fetch:', error);
            });
    
            // Since the image is present, update the displayed image
            displayedImage.src = src;
        };
        testImage.onerror = () => {
            // If the image fails to load, do not attempt to display it
            console.error('Selected image could not be loaded.');
        };
    
        // Set the src to attempt to load the image
        testImage.src = src;
    };

    function displayImage(file) {
        console.log(file);
        const formData = new FormData();
        formData.append('file', file);
        const image = file;

        fetch('/api/ocr-from-file', {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('OCR result:', data);
            // Display the OCR result or do further processing
            document.getElementById('ocrText').innerHTML = data.text;

        })
        .catch(error => {
            console.error('Error during fetch:', error);
        });
        
        // displayedImage.src = file;

        // const image = ocr(file);
        const reader = new FileReader();
        reader.onload = (event) => {
            displayedImage.src = event.target.result;
        };
        reader.readAsDataURL(image);
    }
});
