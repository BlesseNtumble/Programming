{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 114a
  [*] Вычислить 
}
program XpeHb;
var i:byte; 
  count:real;
begin
  count :=0;
  for i:=1 to 100 do
  begin
     count += 1 / sqr(i);
  end;  
  write(count);
end.