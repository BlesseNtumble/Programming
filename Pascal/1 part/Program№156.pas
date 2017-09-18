{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-16-2
  [*] Вариант: 16
  [*] Задание: 156б
}
program matrix2;
const max = 40;
type matrix = array [1..max] of real;
var res  : real; 
    mass : matrix;
    n    : integer;
begin
  repeat
    write('Введите количество элементов последовательности (Не больше ', max,'): ');
    readln(n);
  until (n >= 3) and (n <= max);

  res := 0;
  for var x:=1 to n do
  begin
    mass[x]:= x;
    if x >= 3 then 
    begin
      res += (mass[x-2] + mass[x-1] + mass[x])*mass[x-1];      
    end;
  end;
  writeln('x = ', res)
end.