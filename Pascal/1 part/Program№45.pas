﻿{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-16-2
  [*] Вариант: 16
  [*] Задание: 45
  [*] Даны действительные числа a, b, c, d. 
  [*] Если a ≤ b ≤ c ≤ d, то каждое число заменить наибольшим из них; 
        если a > b > c > d, то числа оставить без изменения; 
        в противном случае все числа заменяются их квадратами.
}
program xpeHb;

var a, b, c, d, max: real;
    
begin
    write('Введите A: ');
    readln(a);
    write('Введите В: ');
    readln(b);
    write('Введите C: ');
    readln(c);
    write('Введите D: ');
    readln(d);
     
    if (a > b) then max := a
    else max := b;
    
    if (c > max) then max := c;
    if (d > max) then max := d;
    
    
       
    writeln('Max: ', max);
    
    if (a <= b) and (b <= c) and (c <= d) then
      begin
        a := max;
        b := max;
        c := max;
        d := max;       
      end
    else if not (a > b) or not(b > c) or not (c > d) then  
      begin
        a := sqr(a);
        b := sqr(b);
        c := sqr(c);
        d := sqr(d);
      end;
    writeln('A: ', a, ', B: ', b, ', C: ', c, ', D: ', d);
end.