{
  [*] ������� ������� ������������
  [*] ���-17-1
  [*] �������: 16
  [*] �������: 53
  [*] ���� �������������� ����� a, b, c, d, e, f, g, h. 
  �������� ��� ����� (e, f) � (g, h) ��������. 
  �������� �����, ��� ����� (a, b) � (c, d) �� ����� �� ������ L, ���������� 
  ����� ����� (e, f) � (g, h).
  
  ������ L ��������� ������������ ��������� �� ��� �������������. 
  ��������, ����� ��, ��� ����� (a, b) � (c, d) ����������� ����� 
  � ��� �� �������������.
}
program Number53;

var a,b,c,d,e,f,g,h:real;
  f1, f2:real;
  
begin
  repeat
    write('������� a: ');  readln(a);  
    write('������� b: ');  readln(b);  
    write('������� c: ');  readln(c);  
    write('������� d: ');  readln(d);  
    write('������� e: ');  readln(e);  
    write('������� f: ');  readln(f);  
    write('������� g: ');  readln(g);  
    write('������� h: ');  readln(h);
    
    if (e = g) or (f = h) then writeln('����� e,f,g,h ������ ����������!');
   
  until not(e = g) or not(f = h);
  
  //��������� ������ f=0: f=(X-e)*(h-f)-(Y-f)*(g-e)
  f1:=(a-e)*(h-f)-(b-f)*(g-e);
    writeln('F1:', f1);
  f2:=(c-e)*(h-f)-(d-f)*(g-e);
    writeln('F2:', f2);
  
  if ((f1 > 0) and (f2 > 0)) or ((f1 < 0) and (f2 < 0)) then
    write('�����������')
  else
    write('�� �����������')
end.
  
  