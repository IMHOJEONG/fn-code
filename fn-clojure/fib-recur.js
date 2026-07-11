function fib(n) {
    if (n < 1) {
        return null;
    } else if (n <= 2) {
        return 1;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}

function fibs(n) {
    return Array.from({
        length: n
    }, (_, i) => fib(i + 1))
}