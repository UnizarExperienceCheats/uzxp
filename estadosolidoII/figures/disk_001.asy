settings.outformat="pdf";
settings.prc=false;
settings.render=0;
import three;
currentprojection=perspective(1,1,1);


triple H = 2*(0.2,0.7,0);
triple M = 2*(0.3,0.5,0);

// Colors
pen main = rgb("64B5CD");
pen secondary = rgb("CCB974");


size(5cm,0);

// Circle
path3 c = circle((0,0,0), 1.0);
draw(c, secondary);

// Angles and vectors
draw(arc(O, 0.75*(1,0,0), 0.75*M), gray,
     L=Label("$\varphi$"
	     , position=MidPoint
	     , filltype=Fill(white)));

draw(O--M, main, arrow=Arrow3(),
     L=Label("$\mathbf{M}$"
	     , position=EndPoint
	     , filltype=Fill(white)));

draw(arc(O, 0.25*(1,0,0), 0.25*H), gray,
     L=Label("$\theta$"
	     , position=MidPoint
	     , filltype=Fill(white)));

draw(O--H, main, arrow=Arrow3(),
     L=Label("$\mathbf{H}$"
	     , position=EndPoint
	     , filltype=Fill(white)));

// Axis
draw(O--(1,0,0), black, arrow=Arrow3(),
     L=Label("[100]"
	     , position=EndPoint
	     , filltype=Fill(white)));
draw(O--(0,1,0), black, arrow=Arrow3(),
     L=Label("[010]"
	     , position=EndPoint
	     , filltype=Fill(white)));
draw(O--(0,0,1), black, arrow=Arrow3(),
     L=Label("[001]"
	     , position=EndPoint
	     , filltype=Fill(white)));
