# Surface Evolver

## Introduction

**Surface Evolver** (or **Evolver**) is an interactive program for the modelling of liquid surfaces written by Ken Brakke.
It can be used to model minimal surfaces spanning a given boundary (soap films!).
Here is a summary of the files you can find here:

* `install.sh`:: An installation script for **Evolver**. It should work on Linux provided that the **FreeGLUT** library is installed. The Debian/Ubuntu repositories also provides **Evolver**.
* `blender-evolver.py`:: A script for **Blender** which is designed to export a selected mesh to the data file format of **Evolver**. To use it, open the text editor with `Shift-F11` in **Blender**. Open the script and run it with `Alt-p`.
* `data/*` :: Data files for **Evolver**.
* `blender/*`:: Surfaces in `.stl` format (without tickness) and `.blend` format (with thickness).
* `expo/expo.pdf`:: A very short presentation of **Evolver**.

## How to export a STL file from the evolver console?

Before launching **Evolver**, make sure that an environment variable `$EVOLVERPATH` is pointing to a folder containing the file `stl.cmd` (it should be `/usr/share/evolver` for a system install or a `$HOME/.local/share/evolver` for a local install).
In an **Evolver** session, type

```
read "stl.cmd"
binary_stl >>> "filename.stl"
```

However, the surface is exported as a mesh without thickness.
To print the model, it is left to add thickness with a modelisation software such as **Blender**...

## Links

* [Some nice minimal surfaces to visualize](http://www.mas.ucy.ac.cy/~clabou01/galerie.html)
* [Web page of Ken Brakke, the author of Surface Evolver](https://facstaff.susqu.edu/brakke/)
* [Official documentation](http://facstaff.susqu.edu/brakke/evolver/html/evolver.htm)
* [A tutorial to modelize and print the surface "Trefunknot"](https://www.thingiverse.com/thing:1559227)
