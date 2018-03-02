reset

set term pngcairo size 1200,600
set output "simetry.png"

f(x) = cos(x)
g(x) = x*x

set view map
unset key
set isosamples 150
set samples 1000

unset xtics
unset ytics
unset cbrange
unset cbtics
unset colorbox

set contour

set multiplot layout 1,2

set title "ϕ(x) + ψ(y) (simétrica)" font ",20"

splot f(x)*g(y) + g(x)*f(y) w pm3d

set title "ϕ(x) - ψ(y) (antisimétrica)" font ",20"
splot f(x)*g(y) - g(x)*f(y) w pm3d

unset multiplot
