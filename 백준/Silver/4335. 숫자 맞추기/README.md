# [Silver V] 숫자 맞추기 - 4335 

[문제 링크](https://www.acmicpc.net/problem/4335) 

### 성능 요약

메모리: 110612 KB, 시간: 168 ms

### 분류

구현

### 제출 일자

2024년 4월 30일 16:03:46

### 문제 설명

<p>Stan and Ollie are playing a guessing game. Stan thinks of a number between 1 and 10 and Ollie guesses what the number might be. After each guess, Stan indicates whether Ollie's guess is too high, too low, or right on.</p>

<p>After playing several rounds, Ollie has become suspicious that Stan cheats; that is, that he changes the number between Ollie's guesses. To prepare his case against Stan, Ollie has recorded a transcript of several games. You are to determine whether or not each transcript proves that Stan is cheating.</p>

### 입력 

 <p>Standard input consists of several transcripts. Each transcript consists of a number of paired guesses and responses. A guess is a line containing single integer between 1 and 10, and a response is a line containing "too high", "too low", or "right on". Each game ends with "right on". A line containing 0 follows the last transcript.</p>

### 출력 

 <p>For each game, output a line "Stan is dishonest" if Stan's responses are inconsistent with the final guess and response. Otherwise, print "Stan may be honest".</p>

