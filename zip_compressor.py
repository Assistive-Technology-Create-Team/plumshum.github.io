import os
import zipfile

# Turn this directory into a zip file. It will be saved in the same directory as the script. 
# It is named raspberry_pi_data.zip
# Manually Upload to Google Drive and Open on Google Colab. 
# There, run the machine learning script.
zipf = zipfile.ZipFile('raspberry_pi_data.zip', 'w', zipfile.ZIP_DEFLATED)

print(os.getcwd())

#go through file in this directory and add them to the zip file
for root, dirs, files in os.walk('.'):
    for file in files:
        print("new file: ", file)
        zipf.write(os.path.join(root, file))
zipf.close()