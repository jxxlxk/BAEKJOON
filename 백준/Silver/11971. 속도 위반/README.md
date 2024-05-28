# [Silver V] 속도 위반 - 11971 

[문제 링크](https://www.acmicpc.net/problem/11971) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

구현

### 제출 일자

2023년 10월 24일 16:06:41

### 문제 설명

<p>Always the troublemaker, Bessie the cow has stolen Farmer John's tractor and taken off down the road!</p>

<p>The road is exactly 100 miles long, and Bessie drives the entire length of the road before ultimately being pulled over by a police officer, who gives Bessie a ticket for exceeding the speed limit, for having an expired license, and for operating a motor vehicle while being a cow. While Bessie concedes that the last two tickets are probably valid, she questions whether the police officer was correct in issuing the speeding ticket, and she wants to determine for herself if she has indeed driven faster than the speed limit for part of her journey.</p>

<p>The road is divided into \(N\) segments, each described by a positive integer length in miles, as well as an integer speed limit in the range \(1 \ldots 100\) miles per hour. As the road is 100 miles long, the lengths of all \(N\) segments add up to 100. For example, the road might start with a segment of length 45 miles, with speed limit 70, and then it might end with a segment of length 55 miles, with speed limit 60.</p>

<p>Bessie's journey can also be described by a series of segments, \(M\) of them. During each segment, she travels for a certain positive integer number of miles, at a certain integer speed. For example, she might begin by traveling 50 miles at a speed of 65, then another 50 miles at a speed of 55. The lengths of all \(M\) segments add to 100 total miles. Farmer John's tractor can drive 100 miles per hour at its fastest.</p>

<p>Given the information above, please determine the maximum amount over the speed limit that Bessie travels during any part of her journey.</p>

### 입력 

 <p>The first line of the input contains \(N\) and \(M\), separated by a space.</p>

<p>The next \(N\) lines each contain two integers describing a road segment, giving its length and speed limit.</p>

<p>The next \(M\) lines each contain two integers describing a segment in Bessie's journey, giving the length and also the speed at which Bessie was driving.</p>

### 출력 

 <p>Please output a single line containing the maximum amount over the speed limit Bessie drove during any part of her journey. If she never exceeds the speed limit, please output 0.</p>

