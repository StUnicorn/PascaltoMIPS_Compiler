
program fibonacci;

func fib(n:integer): integer;
start
    if (n <= 2) then
	start
        	fib := 1;
	stop;
    if (n > 2) then
	start
        	fib := fib(n-1) + fib(n-2);
	stop;
stop;

var
    i:integer;
    e:integer;
    s:string;
    out : integer;

start
    for i := 1 to 20 do
    start
        out := fib(i);
        writeln(out);
	writeln(' ');
    stop
stop.
