let fib;

function fibW(n) {
    if (n < 1) {
        return null;
    } else if (n <= 2) {
        return 1;
    } else {
        return fib(n - 1) + fib(n - 2)
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

fib = memoize(fibW);

function* lazyFibs() {
    let n = 1;

    while (true) {
        yield fib(n);
        n += 1;
    }
}

const fibs = lazyFibs();
console.log(
    [...Array(10)].map(() => fibs.next().value)
);
console.log(
    [...Array(20)].map(() => fibs.next().value)
);