PROJECT OVERVIEW:
This project basically is ETL and Visualization of US yellow taxi trip daily total amount for the month of February 2023. The implementation is very basic just using miniconda, python and some packages.

SETUP INSTRUCTIONS:
1. Install miniconda and follow steps here: https://docs.anaconda.com/free/miniconda/miniconda-install/
2. Create a virtual environment. Open Anaconda Prompt (Miniconda3) and type: conda create --name myenv. Note: Replace myenv with the desired name for your virtual environment. Conda will create a new environment with the specified name and install a minimal set of packages.
3. Activate your virtual environment by typing below; the name myenv should match the name of the environment you created in the previous step:
a. for Windows: conda activate myenv
b. for macOS and Linux:	source activate myenv

4. Let's install packages, run the following commands:

a. conda install pandas<br>
b. conda install pyarrow
c. conda install sqlite3
d. conda install matplotlib
e. conda uninstall pillow
f. conda install pillow=10.0.1

4. Download the taxi.py file. Still in the conda prompt, make sure to go to the python file and run: python taxi.py
5. A summary breakdown and plot chart will show within 1 minute of running the code.

DISCUSSION:
The approach in python is simple by using pandas, matplotlib and sqlite3 packages only inside a virtual environment in miniconda. At first, there was no plan of using miniconda but I got stuck with wheels package issue when installing pyarrow package so I had to resort to miniconda and virtual environment. Also had an issue with the pillow package so I had to uninstall and install a newer version of it. For the visualization, there are a lot of options but I just preferred a simple implementation as well as for the overall project.
My assumption for the project was that the data will be retrieved via Rest API, and this is also the first time I encounted the parquet file type.

Thank you!

![image](https://github.com/cranemix/ota-taxi-data/assets/7769820/38df74e6-905c-44b7-bc8c-f31079a8da09)

