# Towards learning Lattice Boltzmann collision operators

In this repository we provide a set of jupyter notebooks which allows to reproduce the results presented in [arxiv.2212.06124](https://arxiv.org/abs/2212.06124):

1.  [create_trainset.ipynb](create_trainset.ipynb) allows to generate a training dataset (see Algorithm 1 in [arxiv.2212.06124](https://arxiv.org/abs/2212.06124) ). The training set consists of pre and post collision distribution functions generated using the LBGK collisional operator.
2.  [train_network.ipynb](train_network.ipynb) makes use of the training data to train a neural network mapping 9 pre-collisional distribution functions (input) to 9 post-collisional distribution functions (output). Conservation laws and symmetries are embedded in the network architecture ( 
using the dataset generated  
3.  [lbml_simulation.ipynb](lbml_simulation.ipynb) Implements a LBM simulation of a Taylor-Green vortex flow, where the BGK operator is replaced by a Neural Network

![image](https://github.com/agabbana/learning_lbm_collision_operator/assets/90458863/7c9b7e56-819b-4bf6-adb2-1e32184d2711)


### How to cite this work

```
@article{toward-learning-lattice-boltzmann-collision-operators,
  title={Towards learning Lattice Boltzmann collision operators},
  author={Corbetta, Alessandro and Gabbana, Alessandro and Gyrya, Vitaliy and Livescu, Daniel and Prins, Joost and Toschi, Federico},
  journal={The European Physical Journal E},
  volume={46},
  number={3},
  pages={10},
  year={2023},
  publisher={Springer},
  doi = {10.1140/epje/s10189-023-00267-w},
}
```
