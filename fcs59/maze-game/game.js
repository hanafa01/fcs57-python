//Initialized variables
let is_game_running = false;
let score = 0;
let bonus = 0;
const MainTimer = 6;
let sound1 = new Audio("./sound1.mp3");
let sound2 = new Audio("./sound2.mp3");

//Declared variables
let end;
let start;
let boundaries;
let status_display;
let timer;
let coins;
let bonusEl;
let reset;

document.addEventListener("DOMContentLoaded", loadPage);

function displayScore(message) {
  if (message != "")
    status_display.innerHTML = message + "<br/>" + "Your Score is: " + score;
}

function gameOver() {
  if (is_game_running) {
    for (let i = 0; i < boundaries.length; i++)
      boundaries[i].style.backgroundColor = "rgb(243, 159, 159)";
    if (score > 0) score = score - 1;
    displayScore("Game Over!");
    sound2.pause()
    sound1.pause()
    sound1.currentTime = 0
    sound2.currentTime = 0
    sound1.play();
    is_game_running = false;
  }
}

function startGame() {
  displayScore("");
  is_game_running = true;
  startTimer();
  bonus = 0
  bonusEl = document.getElementById("bonus").innerHTML = bonus;
  for (let i = 0; i < boundaries.length; i++)
    boundaries[i].style.backgroundColor = "#eeeeee";

  for (let i = 0; i < coins.length; i++) {
    coins[i].style.display = "block";
  }
}

function endGame() {
  if (is_game_running) {
    for (let i = 0; i < boundaries.length; i++)
      boundaries[i].style.backgroundColor = "rgb(113 225 141)";
    score = score + 5 + bonus;
    displayScore("You Won!");
    sound1.pause();
    sound2.pause();
    sound1.currentTime = 0
    sound2.currentTime = 0
    sound1.play();
    for (let i = 0; i < coins.length; i++) {
      this.style.display = "block";
    }
    is_game_running = false;
  }
}

function startTimer() {
  timerSecond = MainTimer;
  const countDown = setInterval(function () {
    if (!is_game_running || timerSecond <= 0) {
      clearInterval(countDown);
      if (timerSecond <= 0) {
        document.getElementById("timer").innerHTML = "Time is out!";
      }
      gameOver();
    } else {
      changeTime(timerSecond);
    }
    timerSecond -= 1;
  }, 1000);
}

function changeTime(time) {
  const minutes = Math.floor(time / 60);
  const seconds = time - minutes * 60;
  timer.innerHTML =
    ("0" + minutes).slice(-2) + " : " + ("0" + seconds).slice(-2);
}

function loadPage() {
  end = document.getElementById("end");
  start = document.getElementById("start");
  boundaries = document.getElementsByClassName("boundary");
  status_display = document.getElementById("status");
  timer = document.getElementById("timer");
  coins = document.getElementsByClassName("coin-img");
  reset = document.getElementById("reset");

  changeTime(MainTimer);

  end.addEventListener("mouseover", endGame);
  start.addEventListener("mousedown", startGame);
  for (let i = 0; i < boundaries.length; i++) {
    boundaries[i].addEventListener("mouseover", gameOver);
  }

  for (let i = 0; i < coins.length; i++) {
    coins[i].addEventListener("mouseover", function () {
      if (is_game_running) {

        sound2.pause();
        sound2.currentTime = 0
        sound2.play();
        this.style.display = "none";
        bonus += 6;
        bonusEl = document.getElementById("bonus").innerHTML = bonus;
      }
    });
  }

  reset.addEventListener("click", function () {
    is_game_running = false;
    score = 0;
    bonus = 0;
    bonusEl = document.getElementById("bonus").innerHTML = bonus;

    status_display.innerHTML = 'Begin by moving your mouse over the "S".';
    for (let i = 0; i < boundaries.length; i++)
      boundaries[i].style.backgroundColor = "#eeeeee";
    changeTime(MainTimer);
  });
}
