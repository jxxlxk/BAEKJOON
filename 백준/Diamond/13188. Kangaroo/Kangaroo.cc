# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
# pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
const ll mod = 1e9+7;
const int MxN = 1e5;
const int inf = INT_MAX;
#define REP0(i,n) for(int i=0; i<n; i++)
#define REP1(i,n) for(int i=1; i<=n; i++)
#define REP(i,a,b) for(int i=a; i<=b; i++)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(), (v).end()
#define compress(v) sort(all(v)); v.erase(    unique(all(v)) , v.end()   )
#define reset(X) memset(X, 0, sizeof(X))
#define pb push_back
#define fi first
#define se second
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vint vector<int>
#define vll vector<ll>
#define vpii vector<pair<int, int>>
#define vpll vector<pair<ll,ll>>
#define endl "\n"
#define LOG 18

ll dp[2001][2001][2];
ll onedir[2001][2001];

void solve()
{
    int n,s,f; cin>>n>>s>>f;
    s; f;
    if(s>f)swap(s,f);  //s<f

    //onedir dp
    onedir[1][1]=1;
    for(int i=2; i<=n;i++)
    {
        for(int j=i-1; j>=1;j--)
        {
            onedir[i][j] = onedir[i][j+1] + onedir[i-1][i-j];
            onedir[i][j] %=mod;
        }
    }
    //initialize dp
    for(int i = n-f+2; i<=n ; i++)
    {
        int parity = (i-1)%2;
        int startpos = i-1-(n-f);
        if(parity == 0)dp[i][1][0] = onedir[i-1][startpos];
        else dp[i][1][0] = onedir[i-1][i-startpos];
    }
    //fill in dp
    for(int i = n-f+3; i<=n; i++)
    {
        for(int j = 2; j<=min(f-n+i-1,s); j++)
        {
            dp[i][j][0] = dp[i][j-1][0] - dp[i-1][j-1][1];
            dp[i][j][1] = dp[i][j-1][1] + dp[i-1][j-1][0];

            dp[i][j][0] %= mod; dp[i][j][0]+=mod; dp[i][j][0]%=mod;
            dp[i][j][1] %= mod;

        }
    }
    cout<< (dp[n][s][0] + dp[n][s][1])%mod <<endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; t=1;
    while(t--)
    {
        solve();
    }
}
