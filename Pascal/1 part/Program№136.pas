{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-16-2
  [*] Вариант: 16
  [*] Задание: 136а
  [*] Даны натуральное число n, действительные числа a1,..., an.	Вычислить:
}
program XpeHb;
const n = 65535;
var a:real;
    ar: array [1..n] of real;
    count:integer;
begin
  repeat
    write('Введите кол-во массивов: ');
    readln(count);
  until(count > 0) and (count < n);
  a:=0;
  for var i:=1 to count do 
  begin
    write('Введите массив [',i,']: ');
    readln(ar[i]);
  end;
  for var i:=1 to n do 
  begin
    //a += ar[i];
    a += sqrt(10+ sqr(ar[i]));
  end;
  write('Результат: ', a);
end.
