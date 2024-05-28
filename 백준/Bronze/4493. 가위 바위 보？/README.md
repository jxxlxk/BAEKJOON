# [Bronze III] 가위 바위 보? - 4493 

[문제 링크](https://www.acmicpc.net/problem/4493) 

### 성능 요약

메모리: 117240 KB, 시간: 292 ms

### 분류

구현

### 제출 일자

2023년 1월 30일 20:52:04

### 문제 설명

<p>Rock, Paper, Scissors is a two player game, where each player simultaneously chooses one of the three items after counting to three. The game typically lasts a pre-determined number of rounds. The player who wins the most rounds wins the game. Given the number of rounds the players will compete, it is your job to determine which player wins after those rounds have been played. </p>

<p>The rules for what item wins are as follows: </p>

<ul>
	<li>Rock always beats Scissors (Rock crushes Scissors) </li>
	<li>Scissors always beat Paper (Scissors cut Paper) </li>
	<li>Paper always beats Rock (Paper covers Rock) </li>
</ul>

### 입력 

 <p>The first value in the input file will be an integer t (0 < t < 1000) representing the number of test cases in the input file. Following this, on a case by case basis, will be an integer n (0 < n < 100) specifying the number of rounds of Rock, Paper, Scissors played. Next will be n lines, each with either a capital R, P, or S, followed by a space, followed by a capital R, P, or S, followed by a newline. The first letter is Player 1’s choice; the second letter is Player 2’s choice.</p>

### 출력 

 <p>For each test case, report the name of the player (Player 1 or Player 2) that wins the game, followed by a newline. If the game ends up in a tie, print TIE. </p>

