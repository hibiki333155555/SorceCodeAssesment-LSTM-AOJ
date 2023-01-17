#include <iostream>
using namespace std;

void printArray(int A[], int N) {
    for (int i = 0; i < N; i++) {
        if (i != 0) cout << " ";
        cout << A[i];
    }
    cout << endl;
}

void insertionSort(int A[], int N) {
    printArray(A, N);
    for (int i = 1; i <= N - 1; i++) {
        int v = A[i];
        int j;
        for (j = i - 1; j >= 0 && A[j] > v; j--) {
            A[j + 1] = A[j];
        }
        A[j + 1] = v;
        printArray(A, N);
    }

}

int main() {
    int N;
    cin >> N;
    int A[N];
    for (int i = 0; i < N; i++) cin >> A[i];

    insertionSort(A, N);
    return 0;
}
