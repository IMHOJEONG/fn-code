(defn fib [n]
    (cond
        (< n 1) nil
        (<= n 2) 1
        ;; fib에 대한 호출은 함수의 꼬리 부분에 있지 않음 
        ;; else 절에 의해 마지막으로 실행되는 것은 + 함수 
        ;; -> recur 함수를 사용하지 못해 꼬리 호출 최적화가 불가능 
        :else (+ (fib (dec n)) (fib (- n 2)))
    )
)

(defn fibs [n]
;; range - 두 개의 인수 a,b를 사용해 a에서 b-1까지 모든 정수 리스트를 반환
;; map - f,l이라는 두 개의 인수를 사용 - f 인수는 함수 / l 인수는 리스트여야 함
    ;; l의 각 멤버마다 f를 호출한 결과를 리스트로 반환
    (map fib (range 1 (inc n)))
)

(defn ifib
    (
        [n a b]
        if (= 0 n)
            b
            (recur (dec n) b (+ a b))
    )

    (
        [n]
        (cond
            (< n 1) nil
            (<= n 2) 1
            :else (ifib (- n 2) 1 1)
        )
    )
)