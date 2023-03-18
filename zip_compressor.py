import os
import zipfile

# Turn this directory into a zip file. It will be saved in the same directory as the script. 
# It is named raspberry_pi_data.zip
# Manually Upload to Google Drive and Open on Google Colab. 
# There, run the machine learning script.
zipf = zipfile.ZipFile('raspberry_pi_data.zip', 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk('raspberry_pi_data'):
    for file in files:
        zipf.write(os.path.join(root, file))
zipf.close()