# [Silver IV] 진짜 메시지 - 9324 

[문제 링크](https://www.acmicpc.net/problem/9324) 

### 성능 요약

메모리: 110884 KB, 시간: 208 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2024년 4월 2일 15:43:11

### 문제 설명

<p>To communicate with HQ, spies send electronic messages over the Information Superhighway using a protocol called SMTP (Secret Message Translation Protocol). To ensure that these messages are genuine and have not, for example, been sent by an evil adversary, every message  is modiﬁed in such a way that it looks like there was noise on the communication line, or the sender was very nervous while typing the message. However, the mutation algorithm is carefully crafted such that an imposter is very unlikely to replicate this particular effect, and it is also easy for ﬁeld agents to intentionally insert a “mistake” if they are forced at gunpoint to write a message.</p>

<p>In a correctly mutated message every third appearance of each letter is duplicated. For example, “<code>HELLOTHEREEWELLLBEFINEE</code>” is the correct mutation if the agent wanted to send “<code>HELLOTHEREWELLBEFINE</code>”. For the past few decades these messages have been checked by highly trained monkeys. Since the number of messages arriving at the HQ has greatly increased recently, they have tasked you with writing an automated program that can alert HQ when a message is deﬁnitely fake and not sent by our agent.</p>

### 입력 

 <p>On the ﬁrst line one positive number: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>one line with a string M (1 ≤ length(M) ≤ 100 000), consisting of uppercase letters only: the incoming message to check.</li>
</ul>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>one line with either “<code>OK</code>” or “<code>FAKE</code>”, indicating whether or not the message M can be the result of a correctly applied mutation to some (unspeciﬁed) original message.</li>
</ul>

