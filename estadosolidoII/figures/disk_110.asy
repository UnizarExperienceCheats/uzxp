settings.outformat="pdf";
settings.prc=false;
settings.render=0;
import three;
currentprojection=perspective(0.5,0.7,1);


triple H = rotate(angle=90-45, u=(0,0,0),v=(1,1,0))*(0,0,1.2);

// Colors
pen main = rgb("64B5CD");
pen secondary = rgb("CCB974");


size(5cm,0);

// Circle
path3 c = circle((0,0,0), 1.0);
draw(rotate(angle=90, u=(0,0,0), v=(1.4,-1.4,0))*c, secondary);

// Angles and vectors
draw(arc(O, 0.75*(0.707,-0.707,0), 0.75*H), gray,
     L=Label("$\theta$"
	     , position=MidPoint
	     , filltype=Fill(white)));

draw(O--H, main, arrow=Arrow3(),
     L=Label("$\mathbf{H}$"
	     , position=EndPoint
	     , filltype=Fill(white)));

// Axis
draw(O--(1/sqrt(2),1/sqrt(2),0), gray, arrow=Arrow3(),
     L=Label("[110]"
	     , position=EndPoint
	     , filltype=Fill(white)));
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
draw(O--(0.707,-0.707,0), gray);
draw(O--(-0.707,+0.707,0), gray);
draw(O--(0,0,-1), gray);
