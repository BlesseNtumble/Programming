{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 338д
}
program matrix2;
const max = 15;
type matrix = array [1..max] of integer;
var mass, mass2 : matrix;
    n: integer;
    o, debug: boolean;
    sposob: string;
    label test;
begin
  debug := true;
  n:=Random(max) + 1; 
  repeat
    writeln('Выберите способ ввода:');
    writeln('1 = ручной');
    writeln('2 = автоматический');
    write('Способ ввода: ');
    readln(sposob);
  until (sposob = '1') or (sposob = '2');

test:
  if(debug) then writeln('Размер массива: ', n);
  for var k:=1 to 2 do
    for var i:=1 to n do
      begin
        if(sposob = '1') then          
          if (k = 1) then
          begin
            write('Введите значение первого массива [',i,'] = ');
            readln(mass[i]);
          end
          else
          begin
            write('Введите значение второго массива [',i,'] = ');
            readln(mass2[i]);
          end        
        else
          begin
            if(k = 1) then 
            begin
              mass[i] := Random(999) - 666;
              if(debug) then writeln('[DEBUG] Результат = ', mass[i]);
            end
            else 
            begin
              mass2[i] := Random(999) - 666;
              if(debug) then writeln('[DEBUG] Результат 2 = ', mass2[i]);
            end;
          end;
      end; 

  for var i:=2 to n do
  begin
    if(mass[i-1] = mass[i]) or (mass2[i-1] = mass[i]) then 
    begin
      writeln('Введеные вами цифры повторяются один или несколько раз.');
      writeln('Пожалуйста повторите попытку.');
      goto test;
    end;
  end;
  
  o:= false;
  for var i:=1 to n do
  begin    
    if(mass[i] = mass2[i]) then
    begin
      o:= true;
      writeln(mass[i], '|', mass2[i]);
    end;
  end;
  if (o = false) then writeln('Нет')
  else writeln('Да');
end.