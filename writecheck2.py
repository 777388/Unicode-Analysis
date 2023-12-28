import sys
class instantiate:
    instance = []
for i in range(1114112):
    if (i < 57344):
        pass
    else:
        instantiate.instance.append(chr(i))
with open(sys.argv[1], "w") as g:
    topography = lambda node: print(str(g.write(node)) + node, end="") 
    (list(map(topography, instantiate.instance)))