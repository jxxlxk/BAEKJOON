# [Bronze II] 폭죽쇼 - 1773 

[문제 링크](https://www.acmicpc.net/problem/1773) 

### 성능 요약

메모리: 130604 KB, 시간: 232 ms

### 분류

브루트포스 알고리즘, 구현, 수학

### 제출 일자

2023년 8월 22일 15:58:41

### 문제 설명

<p>It's Independence Day, and Farmer John has taken the cows to the fireworks show. Bessie wonders how much of the show the cows will be able to see since they might not be able to stay for the entire display.</p>

<p>The show features C (1 ≤ C ≤ 100) fireworks cannons conveniently numbered 1..C. Cannon i shoots fireworks every Ti (1 ≤ Ti ≤ N) seconds (all times in this task are integer seconds). In a spectacular opening, all cannons first shoot at time 0. Fireworks are visible only during the second in which they are launched from the cannon. The cows will stay at the show from time 1 through time N (1 ≤ N ≤ 2,000,000).</p>

<p>Help Bessie figure out how many different times the cows will be able to see fireworks during the time period that they are at the show.</p>

### 입력 

 <p>* Line 1: Two space-separated integers: C and N.</p>

<p>* Lines 2..C + 1: Line i+1 contains the single integer Ti.</p>

### 출력 

 <p>* Line 1: A single integer that is the number of distinct seconds in the time interval from 1 through N that the cows will be able to see fireworks.</p>

<p> </p>

