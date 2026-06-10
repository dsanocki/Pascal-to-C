program test1;

var
    x, y : integer;

begin
    x := 5;
    y := x + 10;

    if y > 10 then
    begin
        writeln(y);
        y := y + 1;
    end;
    writeln(y);
end.
