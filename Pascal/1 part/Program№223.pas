program matrix2;
const max = 20;
type matrix = array [1..max] of integer;
var mass : matrix;
    n,res: integer;
    sposob: char;
begin
  n:=Random(max) + 1; 
  repeat
    writeln('�������� ������ �����:');
    writeln('1 = ������');
    writeln('2 = ��������������');
    write('������ �����: ');
    readln(sposob);
  until (sposob >= '1') and (sposob <= '2');
    
  res := 0;
  for var i:=1 to n do
  begin    
    if(sposob = '1') then
    begin
      if(i > 1) and (mass[i-1] < 0) then break;
      repeat      
        write('������� �������� ������� [',i,'] = ');
        readln(mass[i]);      
      until (mass[1] > 0)
    end
    else
    begin
      mass[i] := Random(999);
      if(i >= 2) then mass[i] := Random(999) - 666
    end;
    if (mass[i] mod 2 = 0) and (mass[i] mod 4<>0) then res += 1;
  end;
  
  for var i:=1 to n do
  begin    
    writeln('������ ������� [',i,'] = ', mass[i]);
    if(i = n) then writeln('���������� �������� = ', n);
    if (mass[i] < 0) then break;
  end;
  writeln('��������� = ', res);
end.