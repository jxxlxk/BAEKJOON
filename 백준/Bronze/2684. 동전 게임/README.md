# [Bronze I] 동전 게임 - 2684 

[문제 링크](https://www.acmicpc.net/problem/2684) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현, 문자열

### 제출 일자

2023년 9월 5일 15:45:50

### 문제 설명

<p>Penney’s game is a simple game typically played by two players. One version of the game calls for each player to choose a unique three-coin sequence such as HEADS TAILS HEADS (HTH). A fair coin is tossed sequentially some number of times until one of the two sequences appears. The player who chose the first sequence to appear wins the game.</p>

<p>For this problem, you will write a program that implements a variation on the Penney Game. You will read a sequence of 40 coin tosses and determine how many times each three-coin sequence appears. Obviously there are eight such three-coin sequences: TTT, TTH, THT, THH, HTT, HTH, HHT and HHH. Sequences may overlap. For example, if all 40 coin tosses are heads, then the sequence HHH appears 38 times.</p>

### 입력 

 <p>The first line of input contains a single integer P, (1 ≤ P ≤ 1000), which is the number of data sets that follow. Each data set consists of 2 lines. The first line contains the data set number N. The second line contains the sequence of 40 coin tosses. Each toss is represented as an upper case H or an upper case T, for heads or tails, respectively. There will be no spaces on any input line.</p>

### 출력 

 <p>For each data set there is one line of output. It contains the data set number followed by a single space, followed by the number of occurrences of each three-coin sequence, in the order shown above, with a space between each one. There should be a total of 9 space separated decimal integers on each output line.</p>

