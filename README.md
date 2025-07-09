# Hackathon Challenge Description

In this challenge, we train a Machine Learning Interatomic Potential (MLIP)
model using the [mlip](https://github.com/instadeepai/mlip) library.

The model will be trained on the dataset located in `train.xyz`. This dataset consists
of 500 conformations of a molecule called 3-(benzyloxy)pyridin-2-amine (abbreviated 
as 3BPA) sampled with Molecular Dynamics at a temperature of 300 Kelvin.

For a detailed tutorial on how to train an MLIP model on such a dataset, see
[this](https://github.com/instadeepai/mlip/blob/main/tutorials/model_training_tutorial.ipynb)
Jupyter notebook provided with the mlip library. As explained in the notebook, one can
then save a final model in a zip archive format supported by the library. Also
see the deep-dive tutorial 
on [model training](https://instadeepai.github.io/mlip/user_guide/training.html) and
on the [models](https://instadeepai.github.io/mlip/user_guide/models.html) 
themselves to understand how to adapt the hyperparameters of the training
process and the models, respectively.

The model will be tested on its ability to predict the energies of new conformations
of the same molecule. However, to test the generalization
capabilities of the model, these conformations are sampled at higher temperature,
i.e., 1200 Kelvin. The test conformations are located in the
`test_public.xyz` file. You can predict energies for them with a model saved in the
zip format with the mlip library's batched inference functionality, described
[here](https://instadeepai.github.io/mlip/user_guide/simulations.html#batched-inference)
in the mlip documentation or explained in section 2 of 
[mlip's simulation tutorial](https://github.com/instadeepai/mlip/blob/main/tutorials/simulation_tutorial.ipynb).
The target energies are located in the `test_public.csv` file. The metric the 
predictions will be scored on is root-mean-square error (RMSE).

The private test set for which to submit predictions is located in the
`test_private.xyz` file. It contains more conformations, also sampled at the higher
temperature.

Build the Docker image with the following command:

```bash
docker build -t mlip-hackathon .
``` 

Then, run the container with the following command:

```bash
docker run -p 8888:8888 --gpus all -v "$(pwd)":/app mlip-hackathon
```