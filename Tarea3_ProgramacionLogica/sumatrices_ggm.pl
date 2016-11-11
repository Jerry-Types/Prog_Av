sumamatriz([],[],[]).
sumamatriz([X|Y],[W|Z],[R|Rs]):-
	sumaPorRenglon(X,W,R),
	sumamatriz(Y,Z,Rs)
	.

sumaPorRenglon([],[],[]).
sumaPorRenglon([X|Y],[W|Z],[R|Rs]):-
	R is X+W,
	sumaPorRenglon(Y,Z,Rs).