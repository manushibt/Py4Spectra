The Code read the spectra and remove the bad spectral values in 970 to 980nm channels and stitch back to the origanl spectra. After stitching, Savitsky Golay filter with 11 window size and second polyorder has been applied to smooth out the spectra with 0.001 precision (except 340nm channel). (See image below)

To access the code : https://github.com/manushibt/Py4Spectra/blob/main/Spectral_Stitching_Smoothing/Spectral_Smoothing.py

![spetra](Spectra.PNG)
![spetra_zoom](Zoomed_Spectra.PNG)
