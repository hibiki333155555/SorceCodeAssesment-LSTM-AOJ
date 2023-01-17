#include <iostream>

using namespace std;

const int N = 200010;

int q[N];
int n;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> q[i];
    int low = q[0];
    int res = -1e9;
    for (int i = 1; i < n; i++) {
        res = max(res, q[i] - low);
        low = min(low, q[i]);
    }
    cout << res << endl;
    return 0;
}
