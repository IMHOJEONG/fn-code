(defn fibs-work [n i fs]
    (
        if (= i n)
        fs
        ;; 클로저에서는 recur 함수 사용으로 꼬리 호출 최적화를 명시적으로 호출
        ;; recur 함수 = 꼬리 위치에서만 호출 가능 & 스택을 늘리지 않음
        (recur n (inc i) (conj fs (apply + (take-last 2 fs))))
    )
)