"""Exercise installed components; run after installing the built GXpy wheel."""
from importlib import import_module
from importlib.metadata import version

print(f"GXpy {version('gxpy')}")
for distribution, module in (
    ("pyAMPP", "pyampp"),
    ("pyGXRender", "gxrender"),
    ("pyEUVTools", "pyeuvtools"),
    ("pyCHMP", "pychmp"),
):
    imported = import_module(module)
    print(f"{distribution} {version(distribution)}: {imported.__file__}")

from gxrender.radio import GXRadioImageComputing

renderer = GXRadioImageComputing()
print("Native radio renderer initialized")
