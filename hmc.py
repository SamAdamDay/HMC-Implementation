import torch
from pyro.infer.mcmc.mcmc_kernel import MCMCKernel

class HMC(MCMCKernel):
    """Hamiltonian Monte Carlo kernel.
    
    Parameters
    ----------
        
    potential_fn : callable
        Potential energy function, a.k.a. `U`

    step_size : int, default=1
        The size of a single step taken while simulating Hamiltonian dynamics

    num_steps
        The number of steps to simulate Hamiltonian dynamics
    """

    def __init__(self, potential_fn, step_size=1, num_steps=10):

        self.potential_fn = potential_fn
        self.step_size = step_size
        self.num_steps = num_steps


    def sample(self, q_current):

        # Position variable
        q = q_current

        # Resample the momentum
        p = p_current = ...