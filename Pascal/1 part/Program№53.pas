{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-16-2
  [*] Вариант: 16
  [*] Задание: 53
  [*] Даны действительные числа a, b, c, d, e, f, g, h. 
  Известно что точки (e, f) и (g, h) различны. 
  Известно также, что точки (a, b) и (c, d) не лежат на прямой L, проходящей 
  через точки (e, f) и (g, h).
  
  Прямая L разбивает координатную плоскость на две полуплоскости. 
  Выяснить, верно ли, что точки (a, b) и (c, d) принадлежат одной 
  и той же полуплоскости.
}
program Number53;

var a,b,c,d,e,f,g,h:real;
  f1, f2:real;
  
begin
  write('Введите a: ');
  readln(a);  
  write('Введите b: ');
  readln(b);  
  write('Введите c: ');
  readln(c);  
  write('Введите d: ');
  readln(d);  
  write('Введите e: ');
  readln(e);  
  write('Введите f: ');
  readln(f);  
  write('Введите g: ');
  readln(g);  
  write('Введите h: ');
  readln(h);
  
  if (e = g) or (f = h) then
    begin
      writeln('Точки e,f,g,h должны различатся!');
      exit;
    end;
  
  //Уравнение прямой f=0: f=(X-e)*(h-f)-(Y-f)*(g-e)
  f1:=(a-e)*(h-f)-(b-f)*(g-e);
    writeln('F1:', f1);
  f2:=(c-e)*(h-f)-(d-f)*(g-e);
    writeln('F2:', f2);
  
  if ((f1 > 0) and (f2 > 0)) or ((f1 < 0) and (f2 < 0)) then
    write('Принадлежат')
  else
    write('Не принадлежат')
end.
  
  