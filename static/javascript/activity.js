document.addEventListener('DOMContentLoaded', function () {
    const quizContainer = document.getElementById('quiz-container');
    const scoreElement = document.getElementById('score');
    let questions = [];

    function loadQuestions() {
        const csvUrl = document.querySelector('script[data-csv-url]').getAttribute('data-csv-url');
        // Use csvUrl in your fetch call
        fetch(csvUrl)
            .then(response => response.text())
            .then(text => {
                const lines = text.split('\n');
                lines.forEach(line => {
                    const parts = line.split(',');
                    const question = {
                        question: parts[0],
                        choices: parts.slice(1, 5),
                        correct: parseInt(parts[5], 10) - 1 // Adjusting index to be 0-based
                    };
                    questions.push(question);
                });
                displayAllQuestions();
            });
    }

    function displayAllQuestions() {
        questions.forEach((question, questionIndex) => {
            const questionElement = document.createElement('div');
            questionElement.className = 'question';
            questionElement.innerHTML = `<h3>Q${questionIndex + 1}: ${question.question}</h3>`;
            const choicesElement = document.createElement('ul');
            question.choices.forEach((choice, index) => {
                const li = document.createElement('li');
                const button = document.createElement('button');
                button.textContent = choice;
                button.className = 'choice-button';
                button.addEventListener('click', () => selectAnswer(questionIndex, index));
                li.appendChild(button);
                choicesElement.appendChild(li);
            });
            questionElement.appendChild(choicesElement);
            quizContainer.appendChild(questionElement);
        });
        addNavigationButtons();
    }

    function selectAnswer(questionIndex, choiceIndex) {
        // Logic to mark an answer as selected
    }

    function addNavigationButtons() {
        const submitButton = document.createElement('button');
        submitButton.textContent = 'Submit';
        submitButton.id = 'submit-btn';
        submitButton.addEventListener('click', calculateScore);
        quizContainer.appendChild(submitButton);

        // Optionally, add a back button here
    }

    function calculateScore() {
        // Calculate and display score
    }

    loadQuestions();
});
// function checkAnswer1() {
//     var selected = document.querySelector('input[name="q1"]:checked');
//     if (selected) {
//         if (selected.value === "yes") {
//             document.getElementById("q1-correct").style.display = "block";
//             document.getElementById("q1-wrong").style.display = "none";
//         } else {
//             document.getElementById("q1-correct").style.display = "none";
//             document.getElementById("q1-wrong").style.display = "block";
//         }
//     } else {
//         alert("Please select an answer.");
//     }
// }

// function checkAnswer2() {
//     var selected = document.querySelector('input[name="q2"]:checked');
//     if (selected) {
//         if (selected.value === "no") {
//             document.getElementById("q2-correct").style.display = "block";
//             document.getElementById("q2-wrong").style.display = "none";
//         } else {
//             document.getElementById("q2-correct").style.display = "none";
//             document.getElementById("q2-wrong").style.display = "block";
//         }
//     } else {
//         alert("Please select an answer.");
//     }
// }