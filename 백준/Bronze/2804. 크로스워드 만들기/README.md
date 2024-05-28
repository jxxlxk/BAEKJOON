# [Bronze I] 크로스워드 만들기 - 2804 

[문제 링크](https://www.acmicpc.net/problem/2804) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

구현, 문자열

### 제출 일자

2023년 12월 12일 15:51:41

### 문제 설명

<p>Since ACTA has entered into force, Slavko has been spending his time offline, solving crosswords. Having solved almost all that he could get his hands on, he wants to make a few crosswords of his own. However, he is too sloppy for such fine work, so he has asked you to help him generate the crosswords.</p>

<p>You are given two words, A and B. The word A must be output horizontally, and the word B vertically, so that the two words cross (i.e. share exactly one letter). The shared letter must be the first letter in A that is also contained in B, more specifically the first occurrence of that letter in each word.</p>

<p>For example, given the words A = “ABBA” and B = “CCBB”, you need to output 4 lines as shown below:</p>

<pre style="text-align: center;">.C..
.C..
ABBA
.B..</pre>

### 입력 

 <p>The first and only line of input contains two words, A and B, not more than 30 characters long, separated by a single space. Both words will contain only uppercase English letters. There will be at least one letter contained in both words.</p>

### 출력 

 <p>Let N be the length of word A, and M the length of word B. The output must contain M lines, each containing N characters. The character grid must contain the two words crossed as described above. All other characters in the grid must be periods (the character „.‟, without quotes), thus padding all lines to the length of N characters.</p>

