1. Install miniconda and follow steps here: https://docs.anaconda.com/free/miniconda/miniconda-install/
2. Create a virtual environment. Open Anaconda Prompt (Miniconda3) and type: conda create --name myenv. Note: Replace myenv with the desired name for your virtual environment. Conda will create a new environment with the specified name and install a minimal set of packages.
3. Activate your virtual environment by typing below; the name myenv should match the name of the environment you created in the previous step:
a. for Windows: conda activate myenv
b. for macOS and Linux:	source activate myenv
4. Let's install packages, run the following commands:
a. conda install pandas
b. conda install pyarrow
c. conda install sqlite3
d. conda install matplotlib
e. conda uninstall pillow
f. conda install pillow=10.0.1

4. Download the taxi.py file. Still in the conda prompt, make sure to go to the python file and run: python taxi.py
5. A summary breakdown and plot chart will show within 1 minute of running the code.
