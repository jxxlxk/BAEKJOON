#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;

#define MAX 101010

pii dp[MAX];

int findSample(int N, int confidence[], int host[], int protocol[]) {
	int i;
	for (i = 0; i < N; i++) dp[i].first = confidence[i];
	for (i = N - 1; i > 0; i--) {
		if (protocol[i] == 0) {
			dp[host[i]].first += dp[i].second;
			dp[host[i]].second += max(dp[i].first, dp[i].second);
		}
		else if (protocol[i] == 1) {
			dp[host[i]].first = max(dp[host[i]].first + max(dp[i].first, dp[i].second), dp[host[i]].second + dp[i].first);
			dp[host[i]].second += dp[i].second;
		}
		else {
			dp[host[i]].first = max(dp[host[i]].first + dp[i].second, dp[host[i]].second + dp[i].first);
			dp[host[i]].second += dp[i].second;
		}
	}
	return max(dp[0].first, dp[0].second);
}

#include <cstdio>
#include <cassert>
#define __MAXSIZE__ 100002
using namespace std;

// Confidence
int confidence[__MAXSIZE__];

// Host
int host[__MAXSIZE__];

// Protocol
int protocol[__MAXSIZE__];

// Main
int main(void)
{
	int n, i;

	// Number of people
	assert(scanf("%d", &n) == 1);

	// Confidence
	for (i = 0; i < n; i++)
		assert(scanf("%d", &confidence[i]) == 1);

	// Host and Protocol
	for (i = 1; i < n; i++)
		assert(scanf("%d %d", &host[i], &protocol[i]) == 2);

	// Answer
	printf("%d\n", findSample(n, confidence, host, protocol));
	return 0;
}