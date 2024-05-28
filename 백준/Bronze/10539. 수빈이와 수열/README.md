# [Bronze II] 수빈이와 수열 - 10539 

[문제 링크](https://www.acmicpc.net/problem/10539) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

사칙연산, 수학

### 제출 일자

2023년 12월 5일 15:56:54

### 문제 설명

<p>Mirko is practicing arithmetic operations in an interesting way during math class. First, he writes a sequence of integers A. Then, underneath the first sequence, he writes another sequence of integers B which he gets by replacing every number from the sequence A with the average value of all the numbers before the current one. including it.</p>

<p>For example, if the first sequence of integers A is equal to</p>

<p style="text-align:center">1, 3, 2, 6, 8, </p>

<p>then the second sequence of integers B is going to be </p>

<p style="text-align:center">1/1, (1+3)/2, (1+3+2)/3, (1+3+2+6)/4, (1+3+2+6+8)/5, </p>

<p>in other words </p>

<p style="text-align:center">1, 2, 2, 3, 4.</p>

<p>You are given the second sequence of integers B. Determine the first sequence of integers A to check Mirko's calculations. </p>

### 입력 

 <p>The first line of input contains the integer N (1 ≤ N ≤ 100), the length of sequence B. </p>

<p>The second line of input contains the sequence of N space-separated integers B<sub>i</sub> (1 ≤ B<sub>i</sub> ≤ 10<sup>9</sup>). </p>

### 출력 

 <p>The first and only line of output must contain a sequence of N space-separated integers A<sub>i</sub>.</p>

<p>Please note : the input data will be such that the elements from the sequence A are integers (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>). </p>

