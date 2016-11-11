ackermann(0, N, Ans) :- Ans is N+1.
ackermann(M, 0, Ans) :- M>0, X is M-1, ackermann(X, 1, Ans).
ackermann(M, N, Ans) :- M>0, N>0, X is M-1, Y is N-1, ackermann(M, Y, Ans2), ackermann(X, Ans2, Ans),!.