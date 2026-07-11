(declare fib)

(defn fib-w [n]
    (cond
        (< n 1) nil
        (<= n 2) 1
        :else (+ (fib (dec n)) (fib (- n 2)))
    )
)

(def fib (memoize fib-w))

;; rest 함수 - 리스트에서 첫 번째 요소를 뺀 나머지 해당 리스트를 반환 (range 함수가 옴)
;; range 함수 - 수행을 지연
(defn lazy-fibs []
    (map fib (rest (range)))
)

;; 지연 리스트 - 다음 값을 계산하는 방법을 아는 객체 = 리스트인 척하는 반복자
    ;; 다음 요소를 계산하는 방법을 아는 반복자일 뿐
    ;; 계산이 수행되면 메모리가 할당되고 값이 실제 리스트에 배치됨
    ;; 무한하지 않고, 특정한 크기로 고정되어 있지 않을 뿐

;; take - 처음 n개 요소를 포함하는 리스트를 반환
(prn (take 10 (lazy-fibs)))

(def list-of-fibs (lazy-fibs))

(prn (take 5 list-of-fibs))

;; 최종 결과에 접근할 때까지 어떤 계산도 수행되지 않음

(def real-list-of-fibs (doall (take 50 (lazy-fibs))))

;; (fib 1 ~ fib 499) 까지가 가비지 컬렉션 되었을 가능성이 높다 
;; 리스트 자체를 유지하지 않음
(prn (nth (lazy-fibs) 50))