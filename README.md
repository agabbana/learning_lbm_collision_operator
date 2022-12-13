# Towards learning Lattice Boltzmann collision operators

In this repository we provide a set of jupyter notebooks which allows to reproduce the results presented in [arxiv.2212.06124](https://arxiv.org/abs/2212.06124):

1.  [create_trainset.ipynb](create_trainset.ipynb) allows to generate a training dataset (see Algorithm 1 in [arxiv.2212.06124](https://arxiv.org/abs/2212.06124) ). The training set consists of pre and post collision distribution functions generated using the LBGK collisional operator.
2.  [train_network.ipynb](train_network.ipynb) makes use of the training data to train a neural network mapping 9 pre-collisional distribution functions (input) to 9 post-collisional distribution functions (output). Conservation laws and symmetries are embedded in the network architecture ( 
using the dataset generated  
3.  [lbml_simulation.ipynb](lbml_simulation.ipynb) Implements a LBM simulation of a Taylor-Green vortex flow, where the BGK operator is replaced by a Neural Network



### How to cite this work

```
@misc{https://doi.org/10.48550/arxiv.2212.06124,
  author = {Corbetta, Alessandro and Gabbana, Alessandro and Gyrya, Vitaliy and Livescu, Daniel and Prins, Joost and Toschi, Federico},
  title = {Towards learning Lattice Boltzmann collision operators},
  publisher = {arXiv},
  year = {2022},
  url = {https://arxiv.org/abs/2212.06124},
  doi = {10.48550/ARXIV.2212.06124},
}
```
