x_pert_arb(X, arb(_, X, _)).
x_pert_arb(X, arb(I, _, _)) :- x_pert_arb(X, I).
x_pert_arb(X, arb(_, _, D)) :- x_pert_arb(X, D).

nods_arb(nil,0):-!.
nods_arb(arb(nil,nil,nil),0):-!.
nods_arb(arb(nil,_,nil),1):-!.
nods_arb(arb(A,nil,nil),N):-nods_arb(A,N).
nods_arb(arb(nil,nil,A),N):-nods_arb(A,N).
nods_arb(arb(A,nil,C),N):-nods_arb(A,F),nods_arb(C,D), N is F+D,!. 
nods_arb(arb(A,_,C),N):-nods_arb(A,F),nods_arb(C,D), N is F+D+1,!. 
