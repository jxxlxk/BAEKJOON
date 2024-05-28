# [Silver V] 사탕 - 11256 

[문제 링크](https://www.acmicpc.net/problem/11256) 

### 성능 요약

메모리: 110480 KB, 시간: 136 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2023년 10월 17일 15:46:45

### 문제 설명

<p>You are an owner of a candy factory. In each day, you have to pack J jelly beans into boxes for transfer to the stores.</p>

<p>You have some boxes which may be different in dimension. For your convenience, you want to use least boxes as possible. (You do not need to fill up the box, partly fill is acceptable.)</p>

<p>Write a program that get a number of jelly beans you receive from the factory and dimension of each box and find the number of least boxes can be used. We guarantee that there will be sufficient spaces for the jelly beans.</p>

### 입력 

 <p>First line has a number T (1 ≤ T ≤ 10) represent number of test cases. Each test case has a format as follow.</p>

<p>First line has two numbers, J and N (1 ≤ J, N ≤ 1,000) represent number of jelly beans you receive from the factory and number of boxes you have.</p>

<p>For next N lines, each line has two numbers R<sub>i</sub> and C<sub>i</sub> (1 ≤ R<sub>i</sub>, C<sub>i</sub> ≤ 10,000) represent dimension (number of rows and columns) of i-th box (There can be two boxes with the same dimension.) This box can be packed with no more than R<sub>i</sub> * C<sub>i</sub> jelly beans.</p>

### 출력 

 <p>Your output should have T lines. Each line represent the number of least boxes can be used in i-th test case.</p>

