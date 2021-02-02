import specdal
import glob, os
from scipy.signal import savgol_filter
import numpy as np
import pandas as pd

#Set your input path
inputpath= "C:/Users/manus/Downloads/Justine_Mych_Lansing/Justine_Mych_Lansing/raw_data/"

#Set your file type
search_criteria= "*.sig"

#List all files of interests
q = os.path.join(inputpath, search_criteria)
files = glob.glob(q)

#Empty list of spectras
spectras = []

#Loop through each files
for file in files:
    #Read the spectra
    s = specdal.Spectrum(filepath=file)

    #Interpolate the spectra
    s.interpolate(method='linear')

    #Get its measurements
    s1 = s.measurement

    #Remove the duplicated spectral channels and Stitch it back
    index_duplicated = s1.index.duplicated()
    s2 = s1[index_duplicated==False]

    #Smooth the spectra and add into the list
    smooth_spectra = savgol_filter(s2, 11, polyorder = 2, deriv=0)
    smooth_spectra = np.round(smooth_spectra, 4)
    smooth_spectra_list = smooth_spectra.tolist()
    smooth_spectra_list.insert(0, file[-30:])
    spectras.append(smooth_spectra_list)

#Set Columns and Create Dataframe
cols = s2.index.to_list()
cols.insert(0, "samples")
df = pd.DataFrame(spectras,columns=cols)

#Write as a CSV
df.to_csv(inputpath + "smoothed_spectra.csv")
