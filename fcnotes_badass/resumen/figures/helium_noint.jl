using Gadfly
using DataFrames

noint = DataFrame(yintercept=[-68,-108.8],Interacción="Indep.")
int = DataFrame(yintercept=[-60,-59,-58,-78.8],Interacción="No ind.")

draw(PNG("helium_noint.png", 20cm, 15cm),
        plot(vcat(noint,int),yintercept=:yintercept,xgroup=:Interacción,
            Geom.subplot_grid(Geom.hline),
            Guide.ylabel("Energía (eV)"),
            Theme(major_label_font_size=28pt,
                minor_label_font_size=28pt,
                line_width=2pt),
            )
        )

