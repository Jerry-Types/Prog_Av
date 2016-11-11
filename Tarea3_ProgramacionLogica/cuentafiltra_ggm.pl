filtra([],[]).
filtra([H|T],S):-esMiembro(H,T),!,filtra(T,S).
filtra([H|T],[H|S]):-filtra(T,S).

esMiembro(X,[X|_]).
esMiembro(X,[_|T]):- esMiembro(X,T). 

cuenta([H|T],N):-
filtra([H|T],S),
length(S,R),
N==R
.
