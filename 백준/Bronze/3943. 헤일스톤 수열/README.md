# [Bronze II] 헤일스톤 수열 - 3943 

[문제 링크](https://www.acmicpc.net/problem/3943) 

### 성능 요약

메모리: 119408 KB, 시간: 812 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2023년 9월 12일 16:06:43

### 문제 설명

<p>The hailstone sequence is formed in the following way:</p>

<ul>
	<li>If n is even, divide it by 2 to get n'</li>
	<li>if n is odd, multiply it by 3 and add l to get n'</li>
</ul>

<p>It is conjectured that for any positive integer number n, the sequence will always end in the repeating cycle: 4, 2, 1, 4, 2, 1,.... Suffice to say, when n == 1, we will say the sequence has ended.</p>

<p>Write a program to determine the largest value in the sequence for a given n.</p>

### 입력 

 <p>The first line of input contains a single integer P, (1 ≤ P ≤ 100000), which is the number of data sets that follow. Each data set should be processed identically and independently.</p>

<p>Each data set consists of a single line of input consisting of two space separated decimal integers. The first integer is the data set number. The second integer is n, (l ≤ n ≤ 100, 000), which is the starting value.</p>

### 출력 

 <p>For each data set there is a single line of output consisting of the data set number, a single space, and the largest value in the sequence starting at and including n.</p>

