{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-16-2
  [*] Вариант: 16
  [*] Задание: 139и
}
program matrix2;
const max = 20;
type matrix = array [1..max] of real;
var res  : real; 
    mass : matrix;
    fact : word;
    n    : integer;
begin
  repeat
    write('Введите количество элементов последовательности (Не больше ', max,'): ');
    readln(n);
  until (n <= max);
  fact := 1;
  res := 0;
  for var i:=1 to n do
  begin
    fact := fact * i;
    res += 1/fact;
    mass[i] :=  i*res;
    writeln('b','[',i,'] = ', mass[i])
  end;
end.