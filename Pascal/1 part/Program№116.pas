{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-16-2
  [*] Вариант: 16
  [*] Задание: 116б
  [*] Даны натурально число n, действительное число x. Вычислить:
}
program XpeHb;
const one = 1;
var
  n, fac: integer;
  x, all: real;
 
begin
  repeat
  writeln('Введите натуральное число: ');
  readln(n);
  until (n > 0);
  writeln('Введите действительное число: ');
  readln(x);
  fac := one;
  all := 0;
  for var i := one to n do
  begin    
    all += (one / fac) + sqrt(abs(x));  
    fac := fac * i;
  end;  
  write(all);
end.