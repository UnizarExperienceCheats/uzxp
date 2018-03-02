settings.outformat="pdf";
settings.prc=false;
settings.render=0;
import three;
currentprojection=perspective(0.5,1,0.5);

size(5cm,0);

// Colors
pen main = rgb("64B5CD");
pen secondary = rgb("CCB974");

real Ssize  = 1;
real Nleft  = 15;
real Nwall  = 15;
real Nright = 15;

// Axis
draw((-1,0,0) -- (2,0,0), gray);

// Spins (left)
for(int i=0; i<Nleft; ++i){
  real x = 1.0*i/(Nleft-1) - 1;
  draw((x,0,0) -- (x,0,1), main, arrow=Arrow3());
 }

// Spins (wall)
for(int i=0; i<Nwall; ++i){
  // base of the arrow.
  real x = 1.0*i/(Nwall-1);
  triple A = (x,0,0);
  // Final point.
  real angle = 3.141592 * i / (Nwall-1);
  triple B = (x,sin(angle),cos(angle));
  // Draw it.
  draw(A -- B, main, arrow=Arrow3());
 }

// Spins (right)
for(int i=0; i<Nright; ++i){
  real x = 1.0*i/(Nright-1) + 1;
  draw((x,0,0) -- (x,0,-1), main, arrow=Arrow3());
 }
