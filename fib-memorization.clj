;; declare 함수 - 바인딩되지 않은 심벌 생성, 
;; 해당 함수가 정의되어 바인딩 되기 전 다른 함수에서 사용 가능
(declare fib)

(defn fib-w [n]
    (cond 
        (< n 1) nil
        (<= n 2) 1
        :else (+ (fib (dec n)) (fib (- n 2)))
    )
)

;; memoize - 함수인 인수 f를 받아 새로운 함수 g를 반환
(def fib (memoize fib-w))