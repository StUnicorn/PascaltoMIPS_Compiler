program summa;

var n, sum, mult: integer;
start
    n:= 23;
    sum := 0;
    mult := 1;
    repeat
        sum := sum + n mod 10;
        mult := mult * (n mod 10);
        n := n div 10;
    until (n > 0);
    writeln('Sum of digits = ', sum);
    writeln('Multiplication of digits = ', mult);
stop.