#include <iostream>
#include <string>
using namespace std;

int N, nums[100];

void insertionSort(int nums[100]){
  for(int k = 0; k < N; k++){
    cout << nums[k];
    if(k < N - 1) cout << ' ';
    else cout << endl;
  }
  for(int i = 1; i < N; i++){
    int v = nums[i];
    int j = i - 1;
    while(j >= 0 && nums[j] > v){
      nums[j + 1] = nums[j];
      j--;
      nums[j+1] = v;
    }
    for(int k = 0; k < N; k++){
      cout << nums[k];
      if(k < N - 1) cout << ' ';
      else cout << endl;
    }
  }
}

int main(){
  cin >> N;
  for(int i = 0; i < N; i++){
    cin >> nums[i];
  }
  insertionSort(nums);
  return 0;
}
