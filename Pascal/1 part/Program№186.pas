{
  [*] Ìèãóíîâ Âèòàëèé Âëàäèìèğîâè÷
  [*] ÈÂÒ-17-1
  [*] Âàğèàíò: 16
  [*] Çàäàíèå: 186
  [*] Âû÷èñëèòü
}
program matrix2;
const max = 999;
type matrix = array [1..max] of real;
var mass : matrix;
    res: real;
    n, fact: integer;
begin
 repeat
    write('Ââåäèòå ğàçìåğ ìàññèâà: ');
    readln(n);
  until (n > 0) and (n <= max);
  
  fact:=1;
  res:=1;
  for var i:=1 to n do
  begin
    write('Ââåäèòå çíà÷åíèå ìàññèâà [',i,'] = ');
    readln(mass[i]);   
    
    writeln('Ñîñòàâ ìàññèâà [', i, '] = ', mass[i]);
    fact := fact * i;
    if(i+1 < mass[i]) and (mass[i] < fact) then
      res := res * mass[i];
  end;
  
  write('Ğåçóëüòàò = ', abs(1/res));
end.