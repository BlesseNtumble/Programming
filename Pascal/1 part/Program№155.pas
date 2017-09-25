{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 155
}
program matrix2;
const max = byte.MaxValue;
type matrix = array [1..max] of real;
var res  : real; 
    mass : matrix;
    n    : integer;
begin
  repeat
    write('Введите количество элементов последовательности (Не больше ', max,' и не меньше 2): ');
    readln(n);
  until (n >= 2) and (n <= max);

  res := 1;
  for var x:=1 to n do
  begin
    mass[x] :=  x;
    if (x >= 2) then 
    begin
      res := res * (1/abs(mass[x-1] + 1)) + mass[x];      
    end;
  end;
  writeln('x = ', res)
end.