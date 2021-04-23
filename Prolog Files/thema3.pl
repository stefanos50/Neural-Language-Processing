expression(Value) --> number(Value).
expression(Value) --> 
	number(X), [+], expression(V),	{Value is X+V}.
expression(Value) --> 
	number(X), [-], expression(V),	{Value is X-V}.
expression(Value) --> 
	number(X), [*], expression(V),	{Value is X*V}.
expression(Value) --> 
	number(X), [/], expression(V),	{V\=0, Value is X/V}.
expression(Value) --> left_parenthesis, expression(Value), right_parenthesis.
left_parenthesis --> ['('].
right_parenthesis --> [')'].

number(N)   --> digit(D),number(D,N).
number(N,N) --> [].
number(A,N) --> digit(D),{A1 is A*2 + D },number(A1,N).

digit(0) --> [0].
digit(1) --> [1].

dec_bin(0,'0').
dec_bin(1,'1').
dec_bin(N,B):-N>1,X is N mod 2,Y is N//2,dec_bin(Y,B1),atom_concat(B1, X, B).

recognize(Input, VL) :-expression(Value,Input,[]),dec_bin(Value,V),atom_number(V, VL).

%recognize(['(',1,1,+,1,0,+,'(',1,0,1,0,/,1,0,1,')',')'],X).
%recognize([1,0,+,'(',1,0,1,0,/,1,0,1,')'],X).
%recognize([1,+,1],X).