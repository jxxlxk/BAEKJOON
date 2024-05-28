# [Silver IV] 페이지 세기 - 4821 

[문제 링크](https://www.acmicpc.net/problem/4821) 

### 성능 요약

메모리: 117064 KB, 시간: 360 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2023년 10월 3일 15:36:28

### 문제 설명

<p>When you execute a word processor's print command, you are normally prompted to specify the pages you want printed. You might, for example, enter:</p>

<p>10-15,25-28,8-4,13-20,9,8-8</p>

<p>The expression you enter is a list of print ranges, separated by commas.</p>

<p>Each print range is either a single positive integer, or two positive integers separated by a hyphen. In the latter case we call the first integer low and the second one high. A print range for which low > high is simply ignored. A print range that specifies page numbers exceeding the number of pages is processed so that only the pages available in the document are printed. Pages are numbered starting from 1.</p>

<p>Some of the print ranges may overlap. Pages which are common to two or more print ranges will be printed only once. (In the example given, pages 13, 14 and 15 are common to two print ranges.)</p>

### 입력 

 <p>The input will contain data for a number of problem instances. For each problem instance there will be two lines of input. The first line will contain a single positive integer: the number of pages in the document. The second line will contain a list of print ranges, as defined by the rules stated above. End of input will be indicated by 0 for the number of pages. The number of pages in any book is at most 1000. The list of print ranges will be not be longer than 1000 characters.</p>

### 출력 

 <p>For each problem instance, the output will be a single number, displayed at the beginning of a new line. It will be the number of pages printed by the print command.</p>

