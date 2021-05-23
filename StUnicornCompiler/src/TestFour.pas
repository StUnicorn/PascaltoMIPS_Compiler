program pwr;

func power(numb,pow:integer):integer;
var i,res:integer;
start
    res:= 1;
    for i:= 1 to pow do
    start
        res:= res*numb;
    stop;
    power:= res;
stop;

var a,b,c:integer;
start
    a:= 4;
    b:= 3;
    c:= power(a,b);
    writeln(c);
stop.