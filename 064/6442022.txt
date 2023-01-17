#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define fore(i,a) for(auto &i:a)

const ll INF = 1LL << 60;

struct Edge {
  int to;
  ll w;
  Edge(int to, ll w) : to(to), w(w) {}
};

typedef vector<vector<Edge> > Graph;

template<class T> bool chmin(T &a, T b) {
  if (a > b) {
    a = b;
    return true;
  }
  else return false;
}

int main() {
  int V,E,r;
  cin >> V >> E >> r;
  
  Graph G(V);
  rep(i,0,E) {
    int s,t,d;
    cin >> s >> t >> d;
    G.at(s).push_back(Edge(t,d));
  }
  
  vector<bool> used(V, false);
  vector<ll> dist(V, INF);
  dist.at(r) = 0;
  
  rep(iter,0,V) {
    int min_v = -1;
    ll min_dist = INF;
    rep(i,0,V) {
      if (!used.at(i) && dist.at(i) < min_dist) {
        min_dist = dist.at(i);
        min_v = i;
      }
    }
    
    if (min_v == -1) break;
    
    for (int ite=0; ite < G.at(min_v).size(); ite++) {
      Edge e = G.at(min_v).at(ite);
      chmin(dist.at(e.to), dist.at(min_v) + e.w);
    }
    
    used.at(min_v) = true;
  }
  
  rep(i,0,V) {
    if (dist.at(i) == INF) cout << "INF" << endl;
    else cout << dist.at(i) << endl;
  }
}

