let user = 0;
let computer = 0;

function play(userChoice) {
  let options = ["rock", "paper", "scissors"];
  let computerChoice = options[Math.floor(Math.random() * 3)];
  let result = "";

  if (userChoice === computerChoice) {
    result = "Draw!";
  } else if (
    (userChoice === "rock" && computerChoice === "scissors") ||
    (userChoice === "paper" && computerChoice === "rock") ||
    (userChoice === "scissors" && computerChoice === "paper")
  ) {
    result = "You win!";
    user++;
  } else {
    result = "Computer wins!";
    computer++;
  }

  document.getElementById("result").textContent = result;
  document.getElementById("user").textContent = user;
  document.getElementById("computer").textContent = computer;
}
