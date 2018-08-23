#lang racket

(define (collatz n)
  (cond
    [(<= n highest) n]
    [(= 0 (remainder n 2)) (collatz (/ n 2))]
    [else (collatz (add1 (* 3 n)))]))

(define START 100000000)
(define END   1000000000)
(define highest START)

(for ([i (in-range 1 (add1 END))])
  (collatz i)
  (set! highest i))

(display "Verified from ")
(display START)
(display " to ")
(display END)
