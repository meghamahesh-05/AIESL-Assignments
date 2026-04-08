:- dynamic answer/2.

% Ask all questions
ask_all :-
    ask('Do you like math'),
    ask('Do you enjoy logical thinking'),
    ask('Do you like technology'),
    ask('Do you like biology'),
    ask('Do you want to help people'),
    ask('Are you creative'),
    ask('Do you like drawing'),
    ask('Do you like computers'),
    ask('Do you enjoy problem solving'),
    ask('Do you like managing people'),
    ask('Are you interested in finance'),
    ask('Do you like debating'),
    ask('Are you interested in justice').

% Ask predicate
ask(Q) :-
    write(Q), write(' (yes/no): '),
    read(A),
    assert(answer(Q, A)).

% Career rules

career(engineering) :-
    answer('Do you like math', yes),
    answer('Do you enjoy logical thinking', yes),
    answer('Do you like technology', yes).

career(medical) :-
    answer('Do you like biology', yes),
    answer('Do you want to help people', yes).

career(arts) :-
    answer('Are you creative', yes),
    answer('Do you like drawing', yes).

career(it) :-
    answer('Do you like computers', yes),
    answer('Do you enjoy problem solving', yes).

career(business) :-
    answer('Do you like managing people', yes),
    answer('Are you interested in finance', yes).

career(law) :-
    answer('Do you like debating', yes),
    answer('Are you interested in justice', yes).

% Main rule
start :-
    retractall(answer(_,_)),
    ask_all,
    career(X),
    write('Suggested career is: '), write(X), nl, !.

start :-
    write('No suitable career found.'), nl.