document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("edit-form").addEventListener("submit", function(e) {
        e.preventDefault(); // Prevent the default form submission
        const formData = new FormData(this);
        console.log("I'm here!");

        fetch("/edit", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json()) // Assuming the server responds with JSON
        .then(data => {
            console.log("Success:", data);
            // Update the page or show a success message based on 'data'

            fetch('/api/process-model', {method: 'POST'})
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error in generating process model');
                    }
                    return response.blob();
                })
                .then(blob => {
                    const imageURL = URL.createObjectURL(blob);
                    document.getElementById('process-model').src = imageURL;
                })
                .catch(error => {
                    console.log(error);
                })

        })
        .catch((error) => {
            console.error("Error:", error);
            // Handle errors here, such as showing an error message
        });
    });

    document.querySelectorAll('.delete-row').forEach(button => {
        button.addEventListener('click', function() {
            this.closest('tr').remove();
        });
    });

    document.getElementById('add-row').addEventListener('click', function() {
        const table = document.querySelector('.data tbody');
        const newRow = table.insertRow(-1); // Insert a row at the end of the table
        const cols = document.querySelector('.data thead tr').children.length; // Get number of columns from the header, minus the delete button column
    
        // Define the names of the inputs according to your CSV structure
        const inputNames = ['user_id', 'timestamp', 'activity'];
    
        // Insert new cells (`<td>`) with inputs for each column
        inputNames.forEach((name, i) => {
            const cell = newRow.insertCell(i);
            const input = document.createElement('input');
            input.type = 'text';
            input.name = name; // Use the correct name for each column
            cell.appendChild(input);
        });
    
        // Add a delete button to the new row
        const deleteCell = newRow.insertCell(cols);
        const deleteButton = document.createElement('button');
        deleteButton.type = 'button';
        deleteButton.textContent = 'Delete';
        deleteButton.className = 'delete-row';
        deleteButton.onclick = function() { this.closest('tr').remove(); };
        deleteCell.appendChild(deleteButton);
    });
});