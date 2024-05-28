# [Bronze III] 일반 화학 실험 - 4766 

[문제 링크](https://www.acmicpc.net/problem/4766) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 4월 9일 15:21:15

### 문제 설명

<p>Your chemistry lab instructor is a very enthusiastic graduate student who clearly has forgotten what their undergraduate Chemistry 101 lab experience was like. Your instructor has come up with the brilliant idea that you will monitor the temperature of your mixture every minute for the entire lab. You will then plot the rate of change for the entire duration of the lab.</p>

<p>Being a promising computer scientist, you know you can automate part of this procedure, so you are writing a program you can run on your laptop during chemistry labs. (Laptops are only occasionally dissolved by the chemicals used in such labs.) You will write a program that will let you enter in each temperature as you observe it. The program will then calculate the difference between this temperature and the previous one, and print out the difference. Then you can feed this input into a simple graphing program and ﬁnish your plot before you leave the chemistry lab.</p>

### 입력 

 <p>The input is a series of temperatures, one per line, ranging from -10 to 200. The temperatures may be speciﬁed up to two decimal places. After the final observation, the number 999 will indicate the end of the input data stream. All data sets will have at least two temperature observations.</p>

### 출력 

 <p>Your program should output a series of differences between each temperature and the previous temperature. There is one fewer difference observed than the number of temperature observations (output nothing for the ﬁrst temperature). Differences are always output to two decimal points, with no leading zeroes (except for the ones place for a number less than 1, such as 0.01) or spaces.</p>

<p>After the ﬁnal output, print a line with “End of Output”</p>

