settings.outformat="pdf";
settings.prc=false;
settings.render=0;
import three;
currentprojection=perspective(1,0.6,0.50);

size(5cm,0);

// Colors
pen main = rgb("64B5CD");
pen secondary = rgb("CCB974");

// Spin description
real Sx = 0.3;
real Sy = 0.3;
real Sz = 0.4;
triple S = (Sx, Sy, Sz);

// Axis
draw(O--(0.5,0,0), gray, arrow=Arrow3());
draw(O--(0,0.5,0), gray, arrow=Arrow3());
draw(O--(0,0,0.65), gray, arrow=Arrow3(),
     L=Label("$\hat{z}$"
	     , position=EndPoint
	     , filltype=Fill(white)));

// Field
draw(O--0.4*Z, main, arrow=Arrow3(), L=Label("$\mathbf{B}_p$", position=EndPoint));

// Projections
draw(S--(Sx,Sy,0), dashed+gray);
draw(X*Sx--(Sx,Sy,0), dashed+gray);
draw(Y*Sy--(Sx,Sy,0), dashed+gray);

// Spin
draw(O--S, main, arrow=Arrow3(),
           L=Label("$\mathbf{S}_p$",
           filltype=Fill(white),
           position=MidPoint));

// Circle
path3 c = circle((0,0,Sz), sqrt(Sx^2 +Sy^2));
draw(c, secondary);
