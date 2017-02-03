program matrix2;
const max = 999;
type matrix = array [1..max] of real;
var res  : real; 
    mass : matrix;
    n    : integer;
begin
 repeat
    write('Ââåäèòå ğàçìåğ ìàññèâà: ');
    readln(n);
  until (n >= 1) and (n <= max);
  
  for var i:=1 to n do
  begin
    write('Ââåäèòå çíà÷åíèå ìàññèâà [',i,'] = ');
    readln(mass[i]);    
    if (mass[i] < 0) then mass[i] := 0;
  end;
  res:=0;
  for var i:=1 to n do
  begin
    res += mass[i]
  end;
  write(res*2);
end.