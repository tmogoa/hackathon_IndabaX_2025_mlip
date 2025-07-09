from ase.io import read as ase_read
import pandas as pd
import numpy as np

from mlip.models.model_io import load_model_from_zip
from mlip.models import Visnet
from mlip.inference import run_batched_inference


force_field = load_model_from_zip(Visnet, "hackathon/model.zip")
structures = ase_read("hackathon/test_public.xyz", index=":")

results = run_batched_inference(structures, force_field, batch_size=16)
energies = np.array([result.energy for result in results])

reference = np.array(pd.read_csv("hackathon/test_public.csv")["energy"])

rmse = np.sqrt(np.mean((reference - energies) ** 2))
