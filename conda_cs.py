# ---------------------------------
# 1. Installing Conda
# ---------------------------------

# Miniconda (lighter version of Anaconda):
# Download from: https://docs.conda.io/en/latest/miniconda.html

# Anaconda (full scientific Python stack):
# Download from: https://www.anaconda.com/products/distribution

# Check Conda version:
conda --version

# ---------------------------------
# 2. Managing Conda Environments
# ---------------------------------

# Create a new environment:
# Syntax: conda create --name env_name [python=x.x]
conda create --name myenv python=3.8

# Activate an environment:
# Syntax: conda activate env_name
conda activate myenv

# Deactivate the current environment:
# Syntax: conda deactivate
conda deactivate

# List all environments:
# Syntax: conda env list
conda env list

# Remove an environment:
# Syntax: conda remove --name env_name --all
conda remove --name myenv --all

# Export an environment to a YAML file:
# Syntax: conda env export > environment.yml
conda env export > environment.yml

# Create environment from a YAML file:
# Syntax: conda env create -f environment.yml
conda env create -f environment.yml

# ---------------------------------
# 3. Managing Packages in an Environment
# ---------------------------------

# Install a package in the active environment:
# Syntax: conda install package_name
conda install numpy

# Install a specific version of a package:
# Syntax: conda install package_name=version
conda install numpy=1.19.2

# Install multiple packages at once:
# Syntax: conda install pkg1 pkg2 pkg3
conda install pandas matplotlib seaborn

# List all installed packages in the active environment:
# Syntax: conda list
conda list

# Search for available packages:
# Syntax: conda search package_name
conda search numpy

# Update a package:
# Syntax: conda update package_name
conda update numpy

# Update all packages in the active environment:
# Syntax: conda update --all
conda update --all

# Uninstall a package:
# Syntax: conda remove package_name
conda remove numpy

# ---------------------------------
# 4. Conda Channels
# ---------------------------------

# Conda channels are package sources.

# Add a new channel:
# Syntax: conda config --add channels channel_name
conda config --add channels conda-forge

# View all channels in your Conda configuration:
# Syntax: conda config --get channels
conda config --get channels

# Set priority of channels:
# Syntax: conda config --add channels channel_name
conda config --add channels defaults

# Install from a specific channel:
# Syntax: conda install -c channel_name package_name
conda install -c conda-forge pandas

# ---------------------------------
# 5. Conda Environment Cloning and Sharing
# ---------------------------------

# Clone an existing environment:
# Syntax: conda create --name new_env_name --clone old_env_name
conda create --name newenv --clone myenv

# Share an environment:
# Export it to a YAML file:
conda env export > environment.yml

# ---------------------------------
# 6. Virtual Environment Comparison: Conda vs Pip
# ---------------------------------

# Install a package using pip in a Conda environment:
# Activate the environment and then use pip.
conda activate myenv
pip install requests

# Use pip to install packages not available in Conda:
# For instance, if a package isn't in the Conda repository, you can use pip:
pip install <package_name>

# ---------------------------------
# 7. Conda Update and Management
# ---------------------------------

# Update Conda itself:
# Syntax: conda update conda
conda update conda

# Install a specific version of Python in the environment:
# Syntax: conda install python=version
conda install python=3.8

# ---------------------------------
# 8. Conda Clean and Maintenance
# ---------------------------------

# Clean up tarballs, cache, and unused packages:
# Syntax: conda clean --all
conda clean --all

# Clean package cache (default is unused packages):
# Syntax: conda clean --packages
conda clean --packages

# Remove unused packages and cached files:
conda clean --all

# ---------------------------------
# 9. Conda Troubleshooting
# ---------------------------------

# If Conda hangs or runs into issues, you can try some of the following:

# Remove a broken environment:
# Syntax: conda env remove --name env_name
conda env remove --name broken_env

# List broken environments or packages:
# Syntax: conda list --explicit
conda list --explicit

# Check Conda configuration:
# Syntax: conda config --show
conda config --show
