const GREEN = '#00FF00';

const checkAnswer = (selectedAnswer) => {
    // Get the correct answer from the JavaScript variable
    const correctAnswerFromJS = correctAnswer;

    // Get all option buttons
    const optionButtons = document.querySelectorAll('.option');
    const confetti = new JSConfetti();
    // Loop through each option button
    optionButtons.forEach((button) => {
        // Check if the button's text matches the selected answer
        if (button.textContent === selectedAnswer) {
            // If the selected answer is correct
            if (selectedAnswer === correctAnswerFromJS) {
                // Color the button green
                button.style.backgroundColor = GREEN; 
                confetti.addConfetti({
                    emojis: ['🌈', '⚡️', '💥', '✨', '💫', '🌸'],
                })

                confetti.addConfetti();
            } else {
                // If the selected answer is incorrect, color the button red
                button.style.backgroundColor = '#FF0000'; // Red
            }
        }
        // If the button's text matches the correct answer, color it green
        if (button.textContent === correctAnswerFromJS) {
            button.style.backgroundColor = GREEN;
        }
        // Disable further clicks on buttons
        button.disabled = true;
    });

    // Wait for 2 seconds before redirecting
    setTimeout(() => {
        window.location.href = '/game'; // Redirect to the /game route
    }, 1500); // 1500 milliseconds = 1.5 seconds
}