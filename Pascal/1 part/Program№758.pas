{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 758з
}
program XpeHb;
const e = Power(10, -6);
var x, count:real;
    i, fac:integer;
begin
  Write('Введите X: '); Read(x);
  count:=0;
  i:=0;
  fac:=1;
  while (count < e) do
  begin
    i+= 1;
    fac:= fac * (2*i+1);
    count += (Power(-1, i+1) / fac) * (Power(x / 3, 4*i+2));
  end;
Write(count);
end.