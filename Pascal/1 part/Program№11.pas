{ 
  [*] ������� ������� ������������
  [*] ���-16-2
  [*] �������: 16
  [*] �������: 11�
  [*] ���� x, y, z. ��������� a, b 
}
program number11;
var
  x, y, z: real;  //�������� ����������
  v, resulta, resultb: real; //�������������� ����������

begin
  //----- ������ N ����� ----------------------------
  write('������� �������� X: ');
  readln(x);
  write('������� �������� Y: ');
  readln(y);
  write('������� �������� Z: ');
  readln(z);
  //--------------------------------------------------
  
  //----- �������������� �������� --------------------
  v := (y - sqrt(abs(x))) * (x - (y / (z + sqr(x) / 4)));
  resulta := Ln(abs(v));
  
  resultb := x - sqr(x) / 6 + exp(ln(x)*5) / 120;
  //--------------------------------------------------
  
  //----- ������� ���������� ��������� --------------- 
  writeln('����� a: ', resulta:1:0);
  writeln('����� b: ', resultb:1:0);
  //--------------------------------------------------
  
end.