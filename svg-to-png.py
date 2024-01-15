import os
import subprocess

for svg in os.listdir('svg'):
    subprocess.run(["inkscape",
                    "svg/" + svg,
                    "-o",
                    "png/" + svg.replace('.svg', '.png'),
                    "--export-width=128"])
