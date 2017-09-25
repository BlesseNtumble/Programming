{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 201a
  [*] Даны натуральное число n, действительные числа a1,...,an. Получить:
    а) max (a1,...,an);
}
program matrix2;
const max = byte.MaxValue;
type matrix = array [1..max] of real;
var mass : matrix;
    res: real;
    n: integer;
begin
 repeat
    write('Введите размер массива (Не более ', max, '): ');
    readln(n);
  until (n > 0) and (n <= max);
  
  res := 0;
  for var i:=1 to n do
  begin
    write('Введите значение массива [',i,'] = ');
    readln(mass[i]);  
    if(mass[i] > res) then     
      res := mass[i];    
  end;
  write('Результат = ', res);
end.