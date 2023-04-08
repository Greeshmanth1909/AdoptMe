"""Open FITS file and display image with addititional processing options"""

from astropy.io import fits
from matplotlib import pyplot as plt

# Opening FITS file
file = fits.open("/Users/geechu/Desktop/MAST_2022-12-12T0539/JWST/jw02731-o001_t017_nircam_clear-f187n/jw02731-o001_t017_nircam_clear-f187n_segm.fits")
img_data = file[1].data

print(img_data[1:100, 1:100])
# plt.imshow(img_data)
# plt.show()
print(file[1].header)

