import sys
import os
import contextlib
import subprocess
import glob

from scipy.interpolate import interp1d
import numpy as np

from vebio.FileModifiers import write_file_with_replacements
from vebio.Utilities import yaml_to_dict, dict_to_yaml

def run_script(filename, *args, verbose=True):
    """ Execute the contents of a file.

    This function will attempt to execute the contents of a file specified
    with ``filename`` using the Python ``exec`` function.  No error checking
    is performed on the source file to be executed.

    Args:
        filename (str):
            The filename to execute line by line.
        *args:
            Variable length argument list to be made
            available to the executed file via ``sys.argv[..]``.
        verbose (bool, optional):
            Flag to display the printed outputs
            from the executed file, defaults to ``True``.

    Returns:
        None

    """

    pass

def run_pretreatment(notebookDir, params_filename, fs_options, pt_options, verbose=True):
    """ Run the pretreatment operation.

    This function runs the pretreatment unit model specified in ``ptrun.py``.
    Since this is the first unit operation in the overall conversion process,
    the feedstock properties are integrated during this step.

    Through the ``fs_options`` widgets, the user controls the following
    values:

        * The initial fraction of solids due to xylan (X_X)
        * The initial fraction of solids due to glucan (X_G)
        * The initial porous fraction of the biomass particles

    Through the ``pt_options`` widgets, the user controls the following
    values:

        * Acid Loading (float)
        * Steam Temperature (float)
        * Initial FIS_0 (float)
        * Final Time (float)
        * Show plots (bool)

    Args:
        notebookDir (str):
            The path to the Jupyter Notebook, used to specify the location
            of the input file and reset the working directory after this operation
            is finished.

        params_filename (str):
            The filename for the parameters yaml file including
            extension, e.g., ``'virteng_params.yaml'``

        fs_options (WidgetCollection):
            A ``WidgetCollection`` object containing all of widgets used
            to solicit user input for feedstock properties.

        pt_options (WidgetCollection):
            A ``WidgetCollection`` object containing all of widgets used
            to solicit user input for pretreatment properties.

        verbose (bool, optional):
            Option to show print messages from executed file, default True.

    Returns:
        None

    """

    pass
    
def run_enzymatic_hydrolysis(notebookDir, params_filename, eh_options, hpc_run,
                             verbose=True):
    """ Run the enzymatic hydrolysis operation.

    This function runs the enzymatic hydrolysis unit operation. Three 
    distinct variants are included in the virtual engineering code:
    (1) a two-phase model which makes a well-mixed assumption, (2)
    a pre-trained surrogate model informed from CFD runs, and (3) 
    the CFD simulation itself, where option (3) is accessible only
    with ``hpc_run=True``. The default unit operation is the 
    surrogate model.

    Through the ``eh_options`` widgets, the user controls the following
    values:

        * Model Type
        * Enzymatic Load (float)
        * FIS_0 Target (float)
        * Final Time (float)
        * Show plots (bool)

    Args:
        notebookDir (str):
            The path to the Jupyter Notebook, used to specify the location
            of the input file and reset the working directory after this operation
            is finished.

        params_filename (str):
            The filename for the parameters yaml file including
            extension, e.g., ``'virteng_params.yaml'``

        eh_options (WidgetCollection):
            A ``WidgetCollection`` object containing all of widgets used
            to solicit user input for enzymatic hydrolysis properties.

        hpc_run (bool):
            A flag indicating whether or not the Notebook is being
            run on HPC resources, enable CFD only if True.

        verbose (bool, optional):
            Option to show print messages from executed file, default True.

    Returns:
        None

    """

    pass
    
def run_bioreactor(notebookDir, params_filename, br_options, hpc_run, verbose=True):
    """ Run the aerobic bioreaction operation.

    This function runs the aerobic bioreaction operation using the
    user-specified properties.  Two distinct models exist: (1) a 
    pre-trained surrogate model informed from CFD runs and (2) the
    full CFD simulation itself where option (2) is accessible only
    with ``hpc_run=True``.  The default option is the surrogate model.

    Through the ``br_options`` widgets, the user controls the following
    values:

        * Model Type
        * Final Time (float)

    Args:
        notebookDir (str):
            The path to the Jupyter Notebook, used to specify the location
            of the input file and reset the working directory after this operation
            is finished.

        params_filename (str):
            The filename for the parameters yaml file including
            extension, e.g., ``'virteng_params.yaml'``

        br_options (WidgetCollection):
            A ``WidgetCollection`` object containing all of widgets used
            to solicit user input for bioreaction properties.

        hpc_run (bool):
            A flag indicating whether or not the Notebook is being
            run on HPC resources, enable CFD only if True.

        verbose (bool, optional):
            Option to show print messages from executed file, default True.

    Returns:
        None

    """

    pass
    