#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<long long> seg;

    Solution(int n) {
        seg.resize(4 * n); // Correctly size the segment tree array
    }

    long long build(int ind, int low, int high, int arr[]) {
        if (low == high) {
            seg[ind] = arr[low];
            return seg[ind];
        }
        int mid = (low + high) >> 1;
        return seg[ind]= min(build(2 * ind + 1, low, mid, arr), build(2 * ind + 2, mid + 1, high, arr));
    }

    long long summ(int ind, int low, int high, int l, int r) {
        if (r < low || l > high) {
            return 1e9; // Outside the range
        }
        if (l <= low && r >= high) {
            return seg[ind]; // Completely within the range
        }
        int mid = (low + high) >> 1;
        return min(summ(2 * ind + 1, low, mid, l, r) , summ(2 * ind + 2, mid + 1, high, l, r));
    }
};

int main() {
    int n, q;
    cin >> n >> q;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution st(n);
    st.build(0, 0, n - 1, arr);
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << st.summ(0, 0, n - 1, l - 1, r - 1) << endl;
    }
    return 0;
}
