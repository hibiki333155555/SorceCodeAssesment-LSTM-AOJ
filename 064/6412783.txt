#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
typedef pair<ll,ll> pll;
typedef long double D;
//typedef complex<D> P;
#define F first
#define S second
const ll MOD=1000000007;
//const ll MOD=998244353;

template<typename T,typename U>istream & operator >> (istream &i,pair<T,U> &A){i>>A.F>>A.S; return i;}
template<typename T>istream & operator >> (istream &i,vector<T> &A){for(auto &I:A){i>>I;} return i;}
template<typename T,typename U>ostream & operator << (ostream &o,const pair<T,U> &A){o<<A.F<<" "<<A.S; return o;}
template<typename T>ostream & operator << (ostream &o,const vector<T> &A){int i=A.size(); for(auto &I:A){o<<I<<(--i?" ":"");} return o;}
template<typename T,typename U>T & chmax(T &a,const U &b){if(a<b){a=b;} return a;}
template<typename T,typename U>T & chmin(T &a,const U &b){if(b<a){a=b;} return a;}

ll N,M,K,S,T,s,t;
vector<ll> V;
vector<vector<ll>> edge1,edge2;
vector<ll> cmp,cut;
vector<ll> SIZE,BLOCK;

namespace decomp{ 
  vector<ll> depth,tmp;
  int SZ=0;

  int dfs(int u,int d){
    //cout<<"dfs "<<u<<" "<<d<<endl;
    depth[u]=d;
    int mi=d;
    int cutp=0;
    tmp.push_back(u);
    auto add_point=[&](){if(cutp==0){cutp=1; cut[SZ]=1; SIZE[SZ]=1; cmp[u]=SZ++;}};
    auto add_edge=[&](int a,int b){edge2[a].push_back(b); edge2[b].push_back(a);};
    auto add_comp=
      [&](int v){
        //cout<<"add comp "<<u<<"  "<<tmp<<endl;
        add_point();
        if(tmp.back()==u){return;}
        SIZE[SZ]=0;
        add_edge(SZ,cmp[u]);
        int n=0;
        while(n==0){
          if(tmp.back()==v){n=1;}
          int b=tmp.back();
          if(cmp[b]==-1){cmp[b]=SZ; SIZE[SZ]++;}
          else{add_edge(SZ,cmp[b]);}
          tmp.pop_back();
        }
        SZ++;
      };
    for(auto &v:edge1[u]){
      if(depth[v]!=-1){
        if(depth[v]!=d-1){chmin(mi,depth[v]);}
        continue;
      }
      int a=dfs(v,d+1);
      chmin(mi,a);
      if(a==d){
        add_comp(v);
      }else if(a>d){
        assert(a==d+1);
        add_point();
        add_edge(cmp[v],cmp[u]);
      }
    }
    if(mi==d){add_comp(u); tmp.pop_back();}
    return mi;
  }

  void build(){
    dfs(0,0);
    /*
    {
      int a=cmp[0],b=edge2[a][0];
      if(cut[a]==1 && edge2[a].size()==1 && cut[b]==0){
        //cout<<"erase "<<a<<" "<<b<<"  "<<edge2[a]<<endl;
        cmp[0]=b;
        for(auto I=edge2[b].begin();I!=edge2[b].end();++I){
          if(*I==a){edge2[b].erase(I); break;}
        }
        SIZE[b]++;
      }
    }
    */
    s=cmp[S]; t=cmp[T];
    for(auto &u:V){BLOCK[cmp[u]]++;}
    BLOCK[s]--;
  }
};

int dfs1(int u,int p,ll b){
  b+=BLOCK[u];
  for(auto &v:edge2[u]){
    if(v==p){continue;}
    b=dfs1(v,u,b);
  }
  BLOCK[u]=min(SIZE[u],b);
  return b-BLOCK[u];
}

void bfs2(int s,vector<ll> &dist){
  dist.resize(2*N,1e15);
  dist[s]=0;
  queue<int> Q; Q.push(s);
  while(!Q.empty()){
    int u=Q.front(); Q.pop();
    for(auto &v:edge2[u]){
      if(dist[v]>dist[u]+1){dist[v]=dist[u]+1; Q.push(v);}
    }
  }
}

int dfs3(int u,int p){
  int ret=-1;
  if(SIZE[u]>BLOCK[u]){ret=u;}
  for(auto &v:edge2[u]){
    if(v==p){continue;}
    int tmp=dfs3(v,u);
    if(tmp!=-1){ret=tmp;}
  }
  return ret;
}

void input(){
  cin>>N>>M;
  edge1.resize(N);
  edge2.resize(2*N);
  decomp::depth.resize(N,-1);
  cmp.resize(N,-1);
  cut.resize(2*N,0);
  SIZE.resize(2*N,0);
  BLOCK.resize(2*N,0);
  for(int i=0;i<M;i++){
    int a,b;
    cin>>a>>b; a--; b--;
    edge1[a].push_back(b);
    edge1[b].push_back(a);
  }
  cin>>K;
  V.resize(K);
  cin>>V>>S>>T;
  for(auto &I:V){I--;}
  S--; T--;
}

void solve(){
  input();
  if(S==T){cout<<"Yes"<<endl; return;}
  if(K==N){cout<<"No"<<endl; return;}
  decomp::build();
  /*
  cout<<cmp<<endl;
  cout<<SIZE<<endl;
  for(int i=0;i<decomp::SZ;i++){
    cout<<i<<"  "<<edge2[i]<<endl;
  }
  //*/
  dfs1(s,-1,0);
  vector<ll> distS,distT;
  bfs2(t,distT);

  {
    int tmp;
    for(auto &v:edge2[s]){
      if(distT[v]>distT[s]){
        tmp=dfs3(v,s);
        if(tmp!=-1){s=tmp; break;}
      }
    }
  }
  bfs2(s,distS);
  if(s==t){cout<<"Yes"<<endl; return;}
  int mx=0;
  {
    int len=1;
    do{
      for(auto &v:edge2[s]){
        if(distT[v]<distT[s]){s=v; break;}
      }
      len++;
      int dif=0;
      bool re= s==t || cut[s]==0;
      for(auto &v:edge2[s]){
        if(distS[v]+distT[v]==distS[t]){continue;}
        else if(!re){re=true; dif=1;}
      }
      if(re){chmax(mx,len+dif); len=1+dif;}
    }while(s!=t);
  }
  cout<<(K-1+mx<=N?"Yes":"No")<<endl;
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);

  solve();

  return 0;
}
