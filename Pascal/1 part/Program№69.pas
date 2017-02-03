﻿{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-16-2
  [*] Вариант: 16
  [*] Задание: 69
  [*] Часовая стрелка образует угол φ с лучом, проходящим через центр 
  и через точку,соответствующую 12 часам на циферблате,0 < φ ≤ 2π . 
  Определить значение угла для минутной стрелки, 
  а также количество часов и полных минут.      
}
program XpeHb;
var fi,grad:real;
    hour,minute:word;
begin
  repeat
    writeln('Угол часовой стрелки от 0 до ',2*180,'.');
    write('Угол часовой стрелки = ');
    readln(fi);
  until(fi>=0)and(fi<=2*180);
  
  minute:=trunc(fi*2);
  hour:=minute div 60;
  writeln('Часов=',hour);
  
  minute:=minute mod 60;
  writeln('Минут=',minute);
  
  grad:=minute*6;
  write('Угол минутной стрелки = ',grad:0:1,' град.');
end.