#line 1 "test/data/lazy_segment_tree_RSQ_RAQ.test.cpp"
#define PROBLEM "https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_G"
#line 2 "core/stdlib.hpp"
#ifndef LOCAL
#define NDEBUG
#endif

#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace bys {
using std::array, std::vector, std::string, std::set, std::map, std::pair;
using std::cin, std::cout, std::endl;
using std::min, std::max, std::sort, std::reverse, std::abs, std::pow;

// alias
using ll = long long int;
using ld = long double;
using Pa = pair<int, int>;
using Pall = pair<ll, ll>;
using ibool = std::int8_t;
template <class T>
using uset = std::unordered_set<T>;
template <class S, class T>
using umap = std::unordered_map<S, T>;
}  // namespace bys
#line 3 "core/const.hpp"

namespace bys {
constexpr int MOD = 998244353;
constexpr int MOD7 = 1000000007;
constexpr int INF = std::numeric_limits<int>::max() / 2;
constexpr ll LINF = std::numeric_limits<ll>::max() / 2;
}  // namespace bys
#line 4 "core/types.hpp"
#include <utility>

namespace bys {
template <class, class = void>
struct has_lshift_to_ostream : std::false_type {};
template <class T>
struct has_lshift_to_ostream<T, std::void_t<decltype(std::declval<std::ostream&>() << std::declval<T&>())>> : std::true_type {};

template <class, class = void>
struct has_rshift_from_istream : std::false_type {};
template <class T>
struct has_rshift_from_istream<T, std::void_t<decltype(std::declval<std::istream&>() >> std::declval<T&>())>> : std::true_type {};

template <class T, class = void>
struct has_tuple_interface : std::false_type {};
template <class T>
struct has_tuple_interface<T, std::void_t<decltype(std::tuple_size<T>())>> : std::true_type {};

template <class, class = void>
struct has_iterator : std::false_type {};
template <class T>
struct has_iterator<T, std::void_t<typename T::iterator>> : std::true_type {};

struct Int1 {};
}  // namespace bys
#line 4 "core/printer.hpp"

namespace bys {
struct Printer {
    Printer(std::ostream& os_) : os(os_) {}
    ~Printer() { os << std::flush; }

    template <class T>
    void cat(T&& v) {
        if constexpr (has_lshift_to_ostream<std::decay_t<T>>::value) {
            os << v;
        } else if constexpr (has_iterator<std::decay_t<T>>::value) {
            string sep2;
            if constexpr (has_iterator<std::decay_t<typename std::decay_t<T>::value_type>>::value) {
                sep2 = _end;
            } else {
                sep2 = _sep;
            }
            for (auto &&itr = std::begin(v), end = std::end(v); itr != end; ++itr) {
                cat(*itr);
                if (std::next(itr) != end) cat(sep2);
            }
        } else if constexpr (has_tuple_interface<std::decay_t<T>>::value) {
            print_tuple(std::forward<T>(v), std::make_index_sequence<std::tuple_size_v<std::decay_t<T>>>());
        } else {
            static_assert([] { return false; }(), "type error");
        }
    }
    void print() { cat(_end); }
    template <class T>
    void print(T&& top) {
        cat(std::forward<T>(top));
        cat(_end);
    }
    template <class T, class... Ts>
    void print(T&& top, Ts&&... args) {
        cat(std::forward<T>(top));
        cat(_sep);
        print(std::forward<Ts>(args)...);
    }
    template <class... Ts>
    void operator()(Ts&&... args) {
        print(std::forward<Ts>(args)...);
    }

    void flush() { os << std::flush; }
    template <class... Ts>
    void send(Ts&&... args) {
        print(std::forward<Ts>(args)...);
        flush();
    }

    Printer set(string sep_ = " ", string end_ = "\n") {
        _sep = sep_;
        _end = end_;
        return *this;
    }
    void lf() { cat(_end); }

   private:
    std::ostream& os;
    std::string _sep = " ", _end = "\n";
    template <std::size_t I, class T>
    inline void print_tuple_element(T&& elem) {
        if constexpr (I != 0) cat(_sep);
        cat(std::forward<T>(elem));
    }
    template <class Tp, std::size_t... I>
    inline void print_tuple(Tp&& tp, std::index_sequence<I...>) {
        (print_tuple_element<I>(std::forward<decltype(std::get<I>(tp))>(std::get<I>(tp))), ...);
    }
};
}  // namespace bys
#line 4 "core/scanner.hpp"

namespace bys {
struct Scanner {
    Scanner(std::istream& is_) : is(is_){};

    template <class... Ts>
    void scan(Ts&... args) {
        (is >> ... >> args);
    }

    template <class T, class... Us>
    decltype(auto) read() {
        if constexpr (sizeof...(Us) == 0) {
            if constexpr (has_rshift_from_istream<T>::value) {
                T res;
                is >> res;
                return res;
            } else if constexpr (has_tuple_interface<T>::value) {
                auto res = read_tuple<T>(std::make_index_sequence<std::tuple_size_v<T>>());
                return res;
            } else if constexpr (std::is_same_v<T, Int1>) {
                int res;
                is >> res;
                --res;
                return res;
            } else if constexpr (has_iterator<T>::value) {
                //! TODO: 一行読んでsplit
                static_assert([] { return false; }(), "NotImplementedError");
            } else {
                static_assert([] { return false; }(), "TypeError");
            }
        } else {
            return std::tuple{read<T>(), read<Us>()...};
        }
    }

    template <class T, std::size_t N, typename R = std::conditional_t<std::is_same_v<T, Int1>, int, T>>
    std::array<R, N> read() {
        std::array<R, N> res;
        for (auto&& e : res) e = read<T>();
        return res;
    }

    template <class T, typename R = std::conditional_t<std::is_same_v<T, Int1>, int, T>>
    vector<R> readvec(int n) {
        vector<R> res(n);
        for (auto&& e : res) e = read<T>();
        return res;
    }
    template <class T, typename R = std::conditional_t<std::is_same_v<T, Int1>, int, T>>
    vector<vector<R>> readvec(int n, int m) {
        vector<vector<R>> res(n);
        for (auto&& e : res) e = readvec<T>(m);
        return res;
    }

    template <class Lambda = std::function<int(std::string)>,
              typename T = std::invoke_result_t<std::decay_t<Lambda>, std::string>>
    std::vector<T> readln(
        Lambda f = [](string x) { return std::stoi(x); }, char sep = ' ') {
        std::ws(is);
        std::string elem;
        std::getline(is, elem);
        std::stringstream ss{elem};
        std::vector<T> res;
        while (std::getline(ss, elem, sep)) res.emplace_back(f(elem));
        return res;
    }
    std::string getline(bool skip_ws = true) {
        if (skip_ws) std::ws(is);
        std::string res;
        std::getline(is, res);
        return res;
    }

   private:
    std::istream& is;
    template <class Tp, std::size_t... I>
    inline decltype(auto) read_tuple(std::index_sequence<I...>) {
        return Tp{read<typename std::tuple_element_t<I, Tp>>()...};
    }
};
}  // namespace bys
#line 5 "core/io.hpp"

namespace bys {
__attribute__((constructor)) void setup_io() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout << std::fixed << std::setprecision(11);
    std::cerr << std::fixed << std::setprecision(11);
    std::cerr << std::boolalpha;
}

Printer print(std::cout), debug(std::cerr);
Scanner scanner(std::cin);
}  // namespace bys
#line 2 "core/macro.hpp"
// clang-format off
/**
 * @brief マクロ
 */
#ifdef LOCAL
//! @brief デバッグ用出力 ジャッジ上では何もしない。
#define DEBUG(...) { std::cerr << "[debug] line" << std::setw(4) << __LINE__ << ": "; debug(__VA_ARGS__); }
#else
#define DEBUG(...)
#endif
//! @brief printしてreturnする。
#define EXIT(...) { print(__VA_ARGS__); return; }
#define CONCAT_IMPL(a, b) a##b
#define CONCAT(a, b) CONCAT_IMPL(a, b)
//! @brief [[maybe_unused]]な変数を生成。
#define UV [[maybe_unused]] auto CONCAT(unused_val_, __LINE__)
#define RE std::runtime_error("line: " + std::to_string(__LINE__) + ", func: " + __func__)
// clang-format on
#line 2 "core/solver.hpp"

namespace bys {
struct Solver {
    int IT = 1;
    Solver() {}
    void solve();
    void solve(int rep) {
        for (; IT <= rep; ++IT) solve();
    }
};
}  // namespace bys
#line 4 "data/lazy_segment_tree.hpp"

#line 3 "math/bit.hpp"

namespace bys {
template <class T>
int bit_width(T x) {
    int bits = 0;
    x = (x < 0) ? (-x) : x;
    for (; x != 0; bits++) x >>= 1;
    return bits;
}
template <class T>
T bit_floor(T x) {
    assert(x >= 0);
    return x == 0 ? 0 : T(1) << (bit_width(x) - 1);
}
template <class T>
T bit_ceil(T x) {
    assert(x >= 0);
    return x == 0 ? 1 : T(1) << bit_width(x - 1);
}

string bin(ll n) {
    assert(n > 0);
    if (n == 0) return "0";
    string res;
    while (n > 0) {
        res.push_back(n & 1 ? '1' : '0');
        n >>= 1;
    }
    std::reverse(res.begin(), res.end());
    return res;
}
inline bool pop(int s, int d) { return s & (1 << d); }
inline bool pop(ll s, int d) { return s & (1LL << d); }
}  // namespace bys
#line 2 "monoid/monoid.hpp"
#include <optional>
namespace bys {
template <class T>
struct Magma {
    using set_type = T;
    static constexpr set_type operation(set_type a, set_type b);
    static constexpr bool commutative{false};
};
template <class T>
struct Add : Magma<T> {
    using typename Magma<T>::set_type;
    static constexpr set_type operation(set_type a, set_type b) { return a + b; }
    static constexpr set_type identity{0};
    static constexpr bool commutative{true};
};
template <class T>
struct Min : Magma<T> {
    using typename Magma<T>::set_type;
    static constexpr set_type operation(set_type a, set_type b) { return std::min(a, b); }
    static constexpr set_type identity{std::numeric_limits<set_type>::max()};
};
template <class T>
struct Max : Magma<T> {
    using typename Magma<T>::set_type;
    static constexpr set_type operation(set_type a, set_type b) { return std::max(a, b); }
    static constexpr set_type identity{std::numeric_limits<set_type>::min()};
};
template <class T>
struct Update : Magma<T> {
    using set_type = std::optional<T>;
    static constexpr set_type operation(set_type a, set_type b) { return b.has_value() ? b : a; }
    static constexpr set_type identity{std::nullopt};
};
}  // namespace bys
#line 3 "monoid/mapping.hpp"
namespace bys {
template <class T, class ActMonoid>
struct MappingToSet {};
template <class T, class S>
struct MappingToSet<T, Add<S>> {
    static constexpr void mapping(T& t, typename Add<S>::set_type u) { t += u; }
};
template <class T, class S>
struct MappingToSet<T, Update<S>> {
    static constexpr void mapping(T& t, typename Update<S>::set_type u) {
        if (u.has_value()) t = u.value();
    }
};
template <class Monoid, class ActMonoid>
struct Mapping {};
template <class T, class S>
struct Mapping<Min<T>, Update<S>> {
    static constexpr void mapping(typename Min<T>::set_type& t, typename Update<S>::set_type s, int) {
        if (s.has_value()) t = s.value();
    }
};
template <class T, class S>
struct Mapping<Add<T>, Add<S>> {
    static constexpr void mapping(typename Add<T>::set_type& t, typename Add<S>::set_type s, int w) { t += s * w; }
};
// template <class T, class S>
// struct Mapping<Min<T>, Add<S>> {
//     static constexpr void mapping(typename Min<T>::set_type& t, typename Add<S>::set_type s, int w);
// };
// template <class T, class S>
// struct Mapping<Add<T>, Update<S>> {
//     static constexpr void mapping(typename Add<T>::set_type& t, typename Update<S>::set_type s, int w);
// };

}  // namespace bys
#line 7 "data/lazy_segment_tree.hpp"
namespace bys {
template <class Monoid, class ActMonoid, class Action = Mapping<Monoid, ActMonoid>>
struct LazySegmentTree {
    using value_type = typename Monoid::set_type;
    using act_type = typename ActMonoid::set_type;
    int _n, n_leaf, logsize;
    std::vector<act_type> lazy;
    std::vector<value_type> data;

    void reload(int p) { data[p] = Monoid::operation(data[p * 2], data[p * 2 + 1]); }
    void push(const int p) {
        int w = n_leaf >> bit_width(p);
        apply_segment(p * 2, lazy[p], w);
        apply_segment(p * 2 + 1, lazy[p], w);
        lazy[p] = ActMonoid::identity;
    }
    void apply_segment(const int p, act_type f, int w) {
        Action::mapping(data[p], f, w);
        if (p < n_leaf) lazy[p] = ActMonoid::operation(lazy[p], f);
    }

   public:
    LazySegmentTree(int n)
        : _n(n),
          n_leaf(bit_ceil(_n)),
          logsize(bit_width(_n - 1)),
          lazy(n_leaf, ActMonoid::identity),
          data(n_leaf * 2, Monoid::identity) {}
    LazySegmentTree(std::vector<value_type> v)
        : _n(v.size()),
          n_leaf(bit_ceil(_n)),
          logsize(bit_width(_n - 1)),
          lazy(n_leaf, ActMonoid::identity),
          data(n_leaf * 2, Monoid::identity) {
        std::copy(v.begin(), v.end(), data.begin() + n_leaf);
        for (int i = n_leaf - 1; i > 0; --i) {
            data[i] = Monoid::operation(data[i * 2], data[i * 2 + 1]);
        }
    }
    value_type operator[](int p) {
        assert(0 <= p && p < _n);
        p += n_leaf;
        for (int i = logsize; i > 0; --i) push(p >> i);
        return data[p];
    }
    void update(int p, const value_type& x) {
        assert(0 <= p && p < _n);
        p += n_leaf;
        for (int i = logsize; i > 0; --i) push(p >> i);
        data[p] = x;
        for (int i = 1; i <= logsize; ++i) reload(p >> i);
    }
    value_type query(int l, int r) {
        assert(0 <= l);
        assert(l <= r);
        assert(r <= _n);
        if (l == r) return Monoid::identity;

        l += n_leaf;
        r += n_leaf;

        for (int i = logsize; i > 0; i--) {
            if (((l >> i) << i) != l) push(l >> i);
            if (((r >> i) << i) != r) push((r - 1) >> i);
        }

        value_type left = Monoid::identity, right = Monoid::identity;
        for (; l < r; l >>= 1, r >>= 1) {
            if (l & 1) left = Monoid::operation(left, data[l++]);
            if (r & 1) right = Monoid::operation(data[--r], right);
        }
        return Monoid::operation(left, right);
    }

    // value_type query_all() { return data[1]; }
    // void apply(int i, act_type f) { apply(i, i + 1, f); }

    void apply(int l, int r, act_type f) {
        assert(0 <= l);
        assert(l <= r);
        assert(r <= _n);
        if (l == r) return;
        l += n_leaf;
        r += n_leaf;

        for (int i = logsize; i > 0; i--) {
            if (((l >> i) << i) != l) push(l >> i);
            if (((r >> i) << i) != r) push((r - 1) >> i);
        }

        int l2 = l, r2 = r;
        int w = 1;
        while (l2 < r2) {
            if (l2 & 1) apply_segment(l2++, f, w);
            if (r2 & 1) apply_segment(--r2, f, w);
            l2 >>= 1;
            r2 >>= 1;
            w <<= 1;
        }
        // if (l2 & 1) Action::mapping(data[l2++], f, 1);
        // if (r2 & 1) Action::mapping(data[--r2], f, 1);
        // for (l2 >>= 1, r2 >>= 1; l2 < r2; l2 >>= 1, r2 >>= 1) {
        //     if (l2 & 1) {
        //         lazy[l2] = ActMonoid::operation(lazy[l2], f);
        //         ++l2;
        //     }
        //     if (r2 & 1) {
        //         --r2;
        //         lazy[r2] = ActMonoid::operation(lazy[r2], f);
        //     }
        // }

        for (int i = 1; i <= logsize; i++) {
            if (((l >> i) << i) != l) reload(l >> i);
            if (((r >> i) << i) != r) reload((r - 1) >> i);
        }
    }
};
}  // namespace bys
#line 2 "utility/change.hpp"
namespace bys {
template <class T>
inline bool chmax(T& a, const T& b) {
    if (a < b) {
        a = b;
        return 1;
    }
    return 0;
}
template <class T>
inline bool chmin(T& a, const T& b) {
    if (b < a) {
        a = b;
        return 1;
    }
    return 0;
}
}  // namespace bys
#line 2 "utility/range.hpp"

namespace bys {
//! @brief Pythonのrange
template <typename T>
struct Range {
    Range(T start, T stop, T step = 1) : it(start), stop(stop), step(step), dir(step >= 0 ? 1 : -1) {}
    Range(T stop) : it(0), stop(stop), step(1), dir(1) {}
    Range<T> begin() const { return *this; }
    T end() const { return stop; }
    bool operator!=(const T val) const { return (val - it) * dir > 0; }
    void operator++() { it += step; }
    const T& operator*() const { return it; }

   private:
    T it;
    const T stop, step;
    const int dir;

    friend Range reversed(const Range& r) {
        auto new_start = (r.stop - r.dir - r.it) / r.step * r.step + r.it;
        return {new_start, r.it - r.dir, -r.step};
    }
};
template <class T>
Range<T> irange(T stop) {
    return Range(stop);
}
template <class T>
Range<T> irange(T start, T stop, T step = 1) {
    return Range(start, stop, step);
}
}  // namespace bys
#line 7 "test/data/lazy_segment_tree_RSQ_RAQ.test.cpp"

namespace bys {
void Solver::solve() {
    auto [n, q] = scanner.read<int, 2>();
    LazySegmentTree<Add<ll>, Add<ll>> seg(n);
    for ([[maybe_unused]] int i : irange(q)) {
        auto c = scanner.read<int>();
        if (c == 0) {
            auto [s, t, x] = scanner.read<int, 3>();
            seg.apply(s - 1, t, x);
        } else {
            auto [s, t] = scanner.read<int, 2>();
            print(seg.query(s - 1, t));
        }
    }
}
}  // namespace bys

int main() {
    bys::Solver solver;
    solver.solve(/* bys::scanner.read<int>() */);
    return 0;
}

