# Vizualisation tools for quantum computing

This repo consists in the results of school project that aimed at creating new vizualisation tools for quantum computing. We worked under the supervision of Rodney Van Meter. We are quite new in the Qiskit community and it is first time we develop a tool. If you notice any bugs, things that can be improved, or if you need further explanation on how to use this package and what is the meaning of the outputs please contact us (clement.lezane@polytechnique.edu or charles.gery@polytechnique.edu). A documentation will be added to this package as soon as possible.

![pyqt_window_exemples](images/pyqt_window_exemples.png?raw=true "Title")

## Getting started

As it is now, this repo is not completely a package. To use our vizualisation tools you'll need to clone this repo in your working folder with:
```
git clone https://github.com/Lezane/PSC-Quantum-visualisation
```
Then you'll need to put the import at the beggining of your code:
```
import PSC_Quantum_visualisation
```
### Prerequisites

You'll need to have these packages installed to use the project:
* matplotlib
* numpy
* PIL
* qiskit
* PyQt5

## How to use the vizualisation tools

To use the vizualisation tools you'll first need to create any quantum circuit with qiskit.
Then you can display the state of your system after running your circuit using one of our tools with:
```
PSC_Quantum_visualisation.<vizualisation_tool>.display(qc)
```

## Description of the tools
### The Dial Set

The Dial Set vizualisation consists in serveral dials with bars. Each dial represents a state of the system, the size of the bar inside the dial is the amplitude of the state, its angle is its phase (0 if the bar is up, 90 if right...).

![2d_dialset](images/2d_dialset.png?raw=true "Title")

### The bar chart

The chart bar vizualisation consists in several bars. Each bar represents a state of the system, the size of the bar is its amplitude, and the color its phase.

![color_bar](images/color_bar.png?raw=true "Title")

### The 3D Dial set

The 3D Dial sets consits in the dials of the dial set vizualisation stacked. The |000...0> dial set is the one at the bottom of the figure, then you have the |0000...01> and it goes on. This vizualisation might help to find patterns linked to the entanglement of the system. Moreover it has intersting geometrical properties.

![3d_dialset](images/3d_dialset.png?raw=true "Title")

### The entanglement vizualisation

**Section that needs to be updated**
Displays a figure that helps understanding if your system is entangled.

![entanglement](images/entanglement.png?raw=true "Title")

### The Vizualisation window

This is a small GUI that contains the tools mentionned above.
## TODO

* Add the doc to the repo
* Add exemples
* Fix approximation.py
* Make this repo into a real package
* Add all the vizualisation tools

