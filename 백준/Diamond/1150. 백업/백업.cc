#pragma GCC optimize ("O3")
#pragma GCC optimize ("Ofast")
#pragma GCC optimize ("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")
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
#define lpl pair<ll, pair<ll,ll> >

void solve()
{
    int n,k; cin>>n>>k;
    vll pos(n);
    REP0(i,n)cin>>pos[i];
    vll sum(n);
    sum[1] = pos[1] - pos[0];
    for(int i =2; i<n; i++)
    {
        sum[i] = sum[i-2] + pos[i]-pos[i-1];
    }


    priority_queue<lpl, vector<lpl>, greater<lpl>> minheap;
    int left = k;
    REP0(i, n-1)minheap.push({pos[i+1] - pos[i], {i, i+1}});

    bool used[n];
    reset(used);
    ll ans = 0;

    set<int> leftover;
    REP0(i,n)leftover.insert(i);
    leftover.insert(-1);
    leftover.insert(n);

    while(left > 0 )
    {
        left --;
        while(used[minheap.top().se.fi]!=false || used[minheap.top().se.se]!=false)
        {
            minheap.pop();
        }
        int l = minheap.top().se.fi; int r = minheap.top().se.se;
        used[l] = true; used[r] = true;
        ans += minheap.top().fi;
        minheap.pop();

        leftover.erase(l);
        leftover.erase(r);
        
        int newr= *(leftover.upper_bound(r));
        int newl= *(--leftover.lower_bound(l));
        if(newr!=n && newl!=-1)minheap.push(    {pos[newr]-pos[newl] - 2*(sum[newr-1]-sum[newl]), {newl, newr}}    );

        


    }
    
    cout<<ans<<endl;

    
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

