"""Run the code cells in group9_code.ipynb and save every plot to figures/.

The notebook uses a fixed seed, so these figures match a Restart + Run All.
Run from this folder with the venv active:  python export_figures.py
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)

# File names in the order the plots appear in the notebook
NAMES = ["part1_1_chisq", "part1_2_t", "part1_3_F",
         "part2_W_prime", "part2_T_prime", "part3_1_F_prime"]

saved = []
def save_instead_of_show(*args, **kwargs):
    name = NAMES[len(saved)] if len(saved) < len(NAMES) else f"plot{len(saved) + 1}"
    path = OUT / f"{name}.pdf"
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    saved.append(path)

nb = json.loads((HERE / "group9_code.ipynb").read_text(encoding="utf-8"))
namespace = {}
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        exec("".join(cell["source"]), namespace)
        namespace["plt"].show = save_instead_of_show   # set after the import cell runs

for p in saved:
    print("saved", p.relative_to(HERE))
