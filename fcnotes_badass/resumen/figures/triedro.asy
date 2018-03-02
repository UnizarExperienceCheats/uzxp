settings.outformat="pdf";
settings.prc=false;
settings.render=0;
import three;




// Colors
pen red = rgb("C42A2A");
pen green = rgb("41C42A");
pen blue = rgb("4D55AB");
pen purple = rgb("C844E6");



size(10cm,0);

real a = 1.5; // x
real b = 2.5; // y
real c = 2.0; // z

real as = 2.7; // scaler for angle markings

triple R = (a,b,c);


// Proyections (first to avoid hiding of labels)
path p = box((0,0),(a,b));
draw(R--(a,b,0),gray+dashed);
draw((a,0,0)--(a,b,0),gray+dashed);
draw((0,b,0)--(a,b,0),gray+dashed);
draw(O--(a,b,0),gray);

// Axis
draw(O--(1.3*a,0,0), gray, arrow=Arrow3(), 
     L=Label("$\mathrm{\mathbf{\Pi}}_1$"
	     , position=EndPoint
	     , filltype=Fill(white)));
draw(O--(0,1.3*b,0), gray, arrow=Arrow3(), 
     L=Label("$\mathrm{\mathbf{\Pi}}_2$"
	     , position=EndPoint
	     , filltype=Fill(white)));
draw(O--(0,0,1.3*c), gray, arrow=Arrow3(), 
     L=Label("$\hat{k}=\mathbf{k}/|\mathbf{k}|$"
	     , position=EndPoint
	     , filltype=Fill(white)));

// Main line
draw(O--R
     , arrow=Arrow3()
     , p=linewidth(1pt)
     , L=Label("$\mathbf{R}$"
	       , position=EndPoint
	       , filltype=Fill(white))
     , light=currentlight);


// Angles

real Rnorm = sqrt(a*a+b*b+c*c);

draw(arc(O, Z*Rnorm/as, R/as), red, 
     L=Label("$\theta'$"
	     , position=MidPoint
	     , filltype=Fill(white)));
draw(arc(O, X*Rnorm/as, R/as), green, 
     L=Label("$\theta'_1$"
	     , position=MidPoint
	     , filltype=Fill(white)));
draw(arc(O, Y*Rnorm/as, R/as), blue, 
     L=Label("$\theta'_2$"
	     , position=MidPoint
	     , filltype=Fill(white)));
draw(arc(O, X*Rnorm/as, (a/as, b/as, 0/as)), purple, 
     L=Label("$\varphi'$"
	     , position=MidPoint
	     , filltype=Fill(white)));
