import iris
from pathlib import Path

# pathlib note
# `path.parents[1]` is the same as `path.parent.parent`
# `path.parents[2]` is the same as `path.parent.parent.parent`

CMA = Path(__file__).resolve().parents[1]
CMASCIENCE = Path(__file__).resolve().parents[2]

def print_input_files():
    print(CMA)
    print(CMASCIENCE)
    data = CMASCIENCE / 'data' / 'reference' / 'tos_O1_2001-2002.nc'
    print(data)
    cube = iris.load(str(data))
    cube2 = iris.load_cube(str(data))
    print(cube)
    print(cube2)
    #infile =

print_input_files()