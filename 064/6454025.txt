#define reps(i, s, n) for (int i = (s); i < (int)(n); ++i)
#include <bits/stdc++.h>
using namespace std;

int main() {
    while (true) {
        int n, x;
        cin >> n >> x;
        if (n == 0 && x == 0) return 0;
        int ans = 0;
        reps (a, 1, n+1) reps (b, a+1, n+1) {
            int c = x - a - b;
            if (b < c && c <= n) ++ans;
        }
        cout << ans << endl;
    }
    return 0;
}
