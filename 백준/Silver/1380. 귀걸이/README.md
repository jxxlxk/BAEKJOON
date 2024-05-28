# [Silver V] 귀걸이 - 1380 

[문제 링크](https://www.acmicpc.net/problem/1380) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

구현, 문자열

### 제출 일자

2023년 11월 21일 15:40:18

### 문제 설명

<p>At Pascal High School, lots of young girls insist on trying to get away with wearing nonregulation earrings. Mr Sneddon, the Associate Principal, sees red every time he spots a pair of long dangly earrings and confiscates them.</p>

<p>He keeps a numbered list of the girls from whom he has confiscated earrings. As he takes them, he uses a permanent marker to record the number of the owner on the back of each earring. Being a bit of a control freak, he also adds a letter to each one—A or B.</p>

<p>At the end of each term and after completing after-school detentions, the girls are to come and collect their earrings. Unfortunately one day Mr Sneddon dropped the envelope he keeps the earrings in and at the end of the term there is one earring that he cannot find.</p>

<p>Please tell him the name of the angry girl who only gets one earring back.</p>

### 입력 

 <p>Input will consist of a number of scenarios. Each scenario will contain:</p>

<ul>
	<li>A number n (1 ≤ n ≤ 100) on a line on its own, which is the number of girls he has confiscated earrings from.</li>
	<li>n lines each containing a girl’s full name (at most 60 characters in length).</li>
	<li>2n − 1 lines of data with a girl’s number followed by a space then either an ‘A’ or a ‘B’. These lines represent the earrings in the envelope: the number represents the position of the girl in Mr Sneddon’s list, with 1 being the first girl. A girl’s number will occur twice at most, with a different letter (A or B) for each number.</li>
</ul>

<p>The last line of input will be a ‘0’ on a line by itself. This line should not be processed.</p>

### 출력 

 <p>Output should consist of the scenario number followed by the girl’s name whose earring is missing, separated from the scenario number by a single space.</p>

