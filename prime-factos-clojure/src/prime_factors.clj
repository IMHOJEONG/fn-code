(ns prime-factors)

;; (defn factors-of [n]
;;   (if (<= n 1)
;;     []
;;     (throw (UnsupportedOperationException.
;;              "Prime factorization is not implemented yet."))))

;; 1번째 (defn prime-factors-of [n] [])

;; 2번째 
;; (defn prime-factors-of [n] 
;;   (if (> n 1) [2] []))

;; 3번째
;; (defn prime-factors-of [n] 
;;   (if (> n 1) [n] []))

;; 4번째 
;; (defn prime-factors-of [n] 
;;   (if (> n 1) 
;;     (if (zero? (rem n 2))
;; ;; cons 함수 - prime-factors-of에서 반환된 리스트의 시작 부분에 2를 추가
;;       (cons 2 (prime-factors-of (quot n 2)))
;;       [n])
;;   [])
;; )

;; 
(defn prime-factors-of [n] 
;; loop - 즉석에서 새로운 익명 함수 생성
  (loop [n n 
        divisor 2
        factors []]
    (if (> n 1) 
      (if (zero? (rem n divisor))
        ;; conj 함수 - factors에 값을 추가
        (recur (quot n divisor) divisor (conj factors divisor))
        (recur n (inc divisor) factors))
      factors
    [])
  )
)

