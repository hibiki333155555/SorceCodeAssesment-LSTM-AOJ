#include<iostream>
using namespace std;

int main()
{
  int N,h,count=0;

  cin >> N;
  int A[N];

  for(int i=1;i<=N;i++)
    {
      cin >> A[i];
    }

  for(int i=1;i<=N;i++)
    {
      for(int j=N;j>=i+1;j--)
	{
	  if(A[j] < A[j-1])
	    {
	      h = A[j];
	      A[j] = A[j-1];
	      A[j-1] = h;
	      count++;
	    }
	}
    }

  for(int i=1;i<=N;i++)
    {
      cout << A[i];    
      if(i != N)cout << " ";
    }
  cout << endl << count << endl;


  return 0;
}
