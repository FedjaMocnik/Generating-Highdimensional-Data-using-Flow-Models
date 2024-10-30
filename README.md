# High-Dimensional Data Generation Using Flow Models

This repository contains the implementation of my project focused on generating high-dimensional data using RealNVP flow models. The project scales from 2D and 4D experiments to a 12-dimensional dataset derived from the [Pierre Auger Observatory](https://opendata.auger.org/) (which is available on this [link](https://zenodo.org/records/10488964) ). While the core RealNVP implementation is complete and functional, the integration of Bayesian Stochastic Variational Inference (SVI) for 12-dimensional data remains a work in progress.

## Project Structure

### 1. Core RealNVP Implementation
The main focus of this project is on the application of RealNVP flow models to different datasets. These models were successfully applied to 2D, 4D, and 12D data with good results for lower dimensions and mediocre for 12-dimensions.

- **[RealNVP.ipynb](12d/RealNVP/RealNVP.ipynb)**: The implementation of the RealNVP model for generating 12-dimensional data. This version does not include Bayesian inference and serves as the primary, most successful approach in this project.
  
### 2. Bayesian SVI Models (In Progress)
The repository also includes early attempts to extend the RealNVP model with Bayesian layers using Pyro's SVI (Stochastic Variational Inference). While these models work in lower dimensions (2D and 4D), they are not fully implemented or functional for the 12D case.

- **BayesianModel12D/**: This folder contains files related to the 12-dimensional model using Bayesian inference. These models use the Pyro library for variational inference, but are still under development and have not yet produced better results than the standard RealNVP approach.
  
- **[PyroFlow2.ipynb](12d/BayesianFlow(RNVP)/PyroFlow2.ipynb)**: This is an example notebook using Pyro to try implement Bayesian layers for flow models, but the Bayesian methods are unimplemented (so it is a standard Pyro flow). It is successful for lower-dimensional data but does not outperform the standard RealNVP in the 12D setting.

## Next Steps
The main challenge lies in the correct implementation of Bayesian SVI for the 12-dimensional data. Future work will focus on resolving these challenges and improving uncertainty estimation using advanced Bayesian techniques.

## Dependencies
This project uses the following libraries:
- `PyTorch`
- `Pyro`
- `numpy`
- `matplotlib`

Please refer to the individual notebooks for more specific dependencies and instructions. For a more in-depth explaination refer to the [report](https://github.com/FedjaMocnik/Generating-Highdimensional-Data-using-Flow-Models/blob/main/Generating-highdim-data-using-flow.pdf).

## Conclusion
While the Bayesian models are still in progress, the regular RealNVP implementation has proven effective in generating 12D data, achieving a KDE overlap of around 40%. Contributions and suggestions for improving the Bayesian SVI model are welcome.
