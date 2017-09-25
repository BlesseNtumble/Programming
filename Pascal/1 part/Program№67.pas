{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 67г
  [*] Дано натуральное число n (n ≤ 100).
      г) Найти первую цифру числа n.
}
program Number67;

var
  number: integer;

begin
  repeat
    write('Введите число: '); readln(number);
    if(number > 100) then writeln('Число должно быть меньше или равное 100!');    
  until(number <= 100);
  
  if(number >= 10) then 
    number := number div 10
  else if(number = 100) then
    number := number div 100;    
    
  writeln('Первая цифра числа: ', number);
end.