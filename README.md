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
import beautiful_tools
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
beautiful_tools.approximation_display(qc)
```
You will be able to ouput figures like these ones:

![2d_dialset](images/2d_dialset.png?raw=true "Title")
![color_bar](images/color_bar.png?raw=true "Title")
![3d_dialset](images/3d_dialset.png?raw=true "Title")
![entanglement](images/entanglement.png?raw=true "Title")

Please note that all of these tools might not be implemented yet when you will be reading these lines.

## TODO

* Add the doc to the repo
* Add exemples
* Fix approximation.py
* Make this repo into a real package
* Add all the vizualisation tools

