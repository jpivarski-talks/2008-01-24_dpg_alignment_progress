import svgfig

svgfig.canvas(svgfig.Frame(-0.2, 1.2, 0, 3, svgfig.Line(0, 0.20, 1, 1.65), svgfig.Line(0, 1.7, 1, 2.26), xticks={0:"tuned APEs", 1:"infinite APEs"}, xminiticks=[], height=35, yticks=-7).SVG(), viewBox="0 0 100 35").save("statsyst.svg")

