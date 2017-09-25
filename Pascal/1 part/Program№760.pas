{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 760в
  [*] TODO ????????????????????????????????????
}
program XpeHb;
const max = byte.maxValue;
type massive = array [1..max] of real;
var x, fac:real;
    mass:massive;
    n:integer;
begin 
  Readln(x);
  Randomize;
  n:= Random(20) + 10;
  fac:=1;
  Writeln('n = ', n);
  for var i:=10 to n do
  begin
    fac:= fac * (Sqrt(i)*(i+2));
    mass[i] := x / fac;
    
    if(mass[i+1] < Power(10, -6)) then Writeln(mass[i],' | ', i);
  end;
  
  end.