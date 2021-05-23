program faktorial;
var
n, i, s: integer;

start
  n := 12;
  s := 1;
  for i := 1 to n do
    start
    	s := s * i;
    stop;
writeln(s)
stop.