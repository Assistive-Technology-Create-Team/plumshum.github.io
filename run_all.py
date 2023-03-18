import os

# Run zip_compressor.py
os.system("python zip_compressor.py")

# Run FallAllD_2_PYTHON_Structure_new.py. It is in the folder scripts
os.chdir("scripts")
os.system("python FallAllD_2_PYTHON_Structure_new.py")
os.chdir("..")

# Run (machine learning new.ipynb)
os.system("jupyter nbconvert --to script 'machine learning new.ipynb'")
os.system("python 'machine learning new.py'")

# Run script.py
os.system("python script.py")