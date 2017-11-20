program xpeHb;
uses GraphABC;

begin
  
  Line(138,170,227,170);  
  Line(139,169,180,231);  
  Line(178,230,272,230);  
  Line(225,169,271,231);
  FloodFill(177, 200 ,clGreen);

  Line(178,10,242,10); 
  Line(178,10,138,60);
  Line(138,60,202,60);
  Line(242,10,202,60);
  FloodFill(178, 20 ,clGreen);
  
  Line(410,50,460,50);
  Line(320,100,410,50);
  Line(460,50,410,100);
  Line(410,100,440,150);
  Line(440,150,320,120);
  Line(320,100,320,120);
  FloodFill(390, 100 ,clGreen);
  
  SetPenColor(clRed);
  SetBrushColor(clRosyBrown);
  Ellipse(35, 55, WindowWidth - 300, WindowHeight - 300); 
  Circle(60,105, 25);
  SetPenColor(clBlue);
  SetBrushColor(clYellow);
  Circle(55,100, 8);  
  Line(50,120,63,120);
  

end.