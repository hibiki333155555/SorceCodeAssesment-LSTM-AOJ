#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


int main(){

	int N;
	scanf("%d",&N);

	vector<int> V;
	int tmp;

	for(int loop = 0; loop < N; loop++){
		scanf("%d",&tmp);
		V.push_back(tmp);
	}

	int num_query;
	scanf("%d",&num_query);

	for(int loop = 0; loop < num_query; loop++){

		scanf("%d",&tmp);

		printf("%lld\n",lower_bound(V.begin(),V.end(),tmp)-V.begin());
	}

	return 0;
}

