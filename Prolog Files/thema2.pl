s --> np, vp.
np --> det, noun.
vp --> verb, np.
vp --> verb, np, pp.
pp --> prep, np.


det --> [the].
verb --> [brought].
noun --> [waiter].
noun --> [meal].
noun --> [table].
prep --> [to].

%s([the, waiter, brought, the, meal, to, the, table],[]).


s(s(NP,VP))  --> np(NP), vp(VP).
np(np(D,N))  --> det(D), noun(N).
vp(vp(V,NP,PP)) --> verb(V), np(NP), pp(PP).
pp(pp(P,NP)) --> prep(P), np(NP).
det(det(the)) --> [the].
verb(verb(brought)) --> [brought].
noun(noun(waiter)) --> [waiter].
noun(noun(meal)) --> [meal].
noun(noun(table)) --> [table].
prep(prep(to)) --> [to].

%s(S,[the,waiter,brought,the,meal,to,the,table],[]).