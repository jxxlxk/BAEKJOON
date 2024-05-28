# [Bronze I] 전화 요금 - 3226 

[문제 링크](https://www.acmicpc.net/problem/3226) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 4월 16일 15:37:01

### 문제 설명

<p>Ivica is worried about amount of money he spend for phone bill for surfing on Internet. </p>

<p>One minute of surfing in the period between 7:00 and 19:00 costs 10 cents, and in period between 19:00 and 7:00 costs 5 cents (the price is the same for all days in the months). </p>

<p>Start and end of one connection to Internet is always rounded to minute (not seconds), and one connection lasts at most 60 minutes. </p>

<p>You are given a list of connections, write a program which will calculate the total amount of money spent on Internet. </p>

### 입력 

 <p>In the first line of input file there is integer N, number of connections, 1 ≤ N ≤ 100. </p>

<p>In each of next N lines there is description of one connection, in the following format: </p>

<pre>HH:MM DD </pre>

<p>with HH:MM denotes hour and minute of start of connection, and DD denotes for duration of connection (in minutes, maximum 60). Between MM and DD there is one space character. </p>

<p>If hour or minute of start of connection or duration is one-digit number, then there is a leading zeroin front of that number. </p>

<p>Times are denoted from 00:00 till 23:59. </p>

### 출력 

 <p>You have to write total amount of money (in cents) in only line in output file. </p>

<p> </p>

