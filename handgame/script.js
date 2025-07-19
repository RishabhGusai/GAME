document.addEventListener('DOMContentLoaded', () => {
    const choices = document.querySelectorAll('.choice');
    const result = document.getElementById('result');
    const playerScore = document.getElementById('player-score');
    const computerScore = document.getElementById('computer-score');
    const historyList = document.getElementById('history-list');

    let playerPoints = 0;
    let computerPoints = 0;

    const getComputerChoice = () => {
        const choices = ['rock', 'paper', 'scissors'];
        const randomIndex = Math.floor(Math.random() * 3);
        return choices[randomIndex];
    };

    const getEmoji = (choice) => {
        const emojis = {
            rock: '✊',
            paper: '✋',
            scissors: '✌'
        };
        return emojis[choice];
    };

    const determineWinner = (playerChoice, computerChoice) => {
        if (playerChoice === computerChoice) return 'draw';

        if (
            (playerChoice === 'rock' && computerChoice === 'scissors') ||
            (playerChoice === 'paper' && computerChoice === 'rock') ||
            (playerChoice === 'scissors' && computerChoice === 'paper')
        ) {
            return 'win';
        }

        return 'lose';
    };

    const updateHistory = (playerChoice, computerChoice, result) => {
        const li = document.createElement('li');
        const resultText = result === 'win' ? 'Won' : result === 'lose' ? 'Lost' : 'Draw';
        li.textContent = `${getEmoji(playerChoice)} vs ${getEmoji(computerChoice)} - ${resultText}`;
        historyList.insertBefore(li, historyList.firstChild);

        // Keep only last 10 moves
        if (historyList.children.length > 10) {
            historyList.removeChild(historyList.lastChild);
        }
    };

    const updateScore = () => {
        playerScore.textContent = playerPoints;
        computerScore.textContent = computerPoints;
    };

    const playGame = (playerChoice) => {
        const computerChoice = getComputerChoice();
        const gameResult = determineWinner(playerChoice, computerChoice);

        let resultText = '';
        switch (gameResult) {
            case 'win':
                resultText = 'You win! 🎉';
                playerPoints++;
                break;
            case 'lose':
                resultText = 'You lose! 😢';
                computerPoints++;
                break;
            default:
                resultText = "It's a draw! 🤝";
        }

        result.textContent = resultText;
        updateScore();
        updateHistory(playerChoice, computerChoice, gameResult);
    };

    choices.forEach(choice => {
        choice.addEventListener('click', (e) => {
            const playerChoice = e.target.dataset.choice;
            playGame(playerChoice);
        });
    });
});