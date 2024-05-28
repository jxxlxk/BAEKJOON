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


ll pow(ll a,ll b)
{
    if(b==0)return 1;
    ll temp = pow(a,b/2);
    temp = temp*temp;
    temp %= mod;

    if(b%2==1)temp *= a;
    temp %= mod;

    return temp;
}

ll inverse(ll a)
{
    return pow(a, mod-2);
}


void solve()
{
    ll r,g,b,k;
    cin>>r>>g>>b>>k;
    ll numerator = 0;
    ll denominator =0;

    numerator += k * (b+g); numerator%=mod;
    numerator *= pow(b+1, k);
    numerator %=mod;

    ll temp = b*r;
    temp %=mod;
    ll temp2 = pow(b+1, k);
    temp2 -= pow(b,k);
    temp2 +=mod+mod;
    temp2 %=mod;
    temp = temp *temp2;
    temp %=mod;
    numerator += temp;
    numerator %=mod;

    denominator += b;
    denominator *= pow(b+1, k);
    denominator %=mod;




    ll ans = numerator * inverse(denominator);
    ans %= mod;
    cout<<ans<<endl;

}



int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin>>t;
    while(t--)
    {
        solve();
    }
}

