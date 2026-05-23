(ns prime-factors-spec
  (:require [prime-factors :refer [prime-factors-of]]
            [speclj.core :refer :all]))

(describe "prime factors"
  (it "returns no factors for 1"
    (should= [] (prime-factors-of 1)))

;; 2번째 테스트
  (it "returns 2"
    (should= [2] (prime-factors-of 2)))    

;; 3번째 테스트 
  (it "return 3"
    (should= [3] (prime-factors-of 3)))

;; 4번째 테스트
  (it "test 4"
    (should= [2 2] (prime-factors-of 4)))
  
;; 5,6,7,8번째 테스트
  (it "test 5,6,7,8"
    (should= [5] (prime-factors-of 5))
    (should= [2 3] (prime-factors-of 6))
    (should= [7] (prime-factors-of 7))
    (should= [2 2 2] (prime-factors-of 8))
  )

)
