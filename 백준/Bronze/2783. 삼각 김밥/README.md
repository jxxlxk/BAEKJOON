# [Bronze III] 삼각 김밥 - 2783 

[문제 링크](https://www.acmicpc.net/problem/2783) 

### 성능 요약

메모리: 113112 KB, 시간: 140 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2023년 4월 18일 15:46:59

### 문제 설명

<p>The National Supermarket Chain (NSC) likes to boast that it has the lowest price for mortadella in the country. In fact, if a customer manages to find cheaper mortadella in any other chain, the NSC will match the price for that customer.</p>

<p>Matej and Filip decided to accept that challenge. They will visit N different supermarket chains in order to find mortadella not only cheaper than the one in NSC, but the cheapest on the market. If they are successful, they will be able to buy the cheapest mortadella in an NSC branch close to their school.</p>

<p>NSC was hoping that no one would be able to find cheaper mortadella since all supermarket chains (including NSC) express mortadella prices in a convoluted way: X dollars for Y grams of mortadella.</p>

<p>Write a program to, given mortadella prices in NSC as well as the remaining N chains, determine the price that Matej and Filip will have to pay for 1000 grams of mortadella in the NSC close to their school.</p>

### 입력 

 <p>The first line of input contains two positive integers X<sub>NSC</sub> (1 ≤ X<sub>NSC</sub> ≤ 100) and Y<sub>NSC</sub> (1 ≤ Y<sub>NSC</sub> ≤ 1000), where X<sub>NSC</sub> is the price of Y<sub>NSC</sub> grams of mortadella in the NSC chain.</p>

<p>The second line of input contains the positive integer N (1 ≤ N ≤ 100), the number of supermarket chains (excluding NSC). </p>

<p>Each of the following N lines contains two positive integers X<sub>i</sub> (1 ≤ X<sub>i</sub> ≤ 100) and Y<sub>i</sub> (1 ≤ Y<sub>i</sub> ≤ 1000), i=1..N, where X<sub>i</sub> is the price of Y<sub>i</sub> grams of mortadella in the i<sup>th</sup> supermarket chain.</p>

### 출력 

 <p>The first and only line of output must contain the requested real number (price). It is allowed to differ at most 0.01 from the exact solution.</p>

