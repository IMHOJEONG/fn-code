;; defn 함수 - 인수로부터 새로운 함수를 정의
;; 정의되는 함수의 이름 fibs-work, fibs
;; [n i fs], [n] -> 함수 이름의 인수를 묶음
(defn fibs-work [n i fs]
;; if p a b => 인수 3개를 사용 (첫 번째 인수가 진위 함수, 진위 함수가 참이면 두 번째 인수를 반환, 그렇지 않으면 세 번째를 반환)
    (if (= i n)
        fs
        ;; conj - 수를 추가 (두 개 인수 사용) (벡터, 해당 벡터에 추가할 값)
        ;; take-last - 숫자 n과 리스트를 사용 - 리스트 인수의 마지막 n개의 요소를 포함하는 리스트를 반환
        (fibs-work n (inc i) (conj fs (apply + (
            take-last 2 fs
        ))))
    )
)

;; fibs 함수는 cond가 반환한 값을 반환함
;; cond -> (predicate 진위함수) (해당 진위 함수가 참일 경우 반환값)
(defn fibs [n]
    (cond 
        (< n 1) []
        (= n 1) [1]
        :else (fibs-work n 2 [1 1])
    )
)