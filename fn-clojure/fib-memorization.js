function fib_w(n) {
    if (n < 1) {
        return null;
    } else if (n <= 2) {
        return 1;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}

function memoize(fn) {
    const cache = new Map();

    return function (n) {
        if (cache.has(n)) {
            return cache.get(n);
        }

        const result = fn(n);
        cache.set(n, result);
        return result;
    }
}

const fib = memoize(fib_w);

console.log(fib(3));
console.log(fib(5));
console.log(fib(11));
console.log(fib(50));