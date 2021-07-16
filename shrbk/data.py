import numpy as np
import galsim
from scipy.ndimage import rotate


def rotate_image(data, angle):

    data_centre = np.array(data.shape) // 2
    rot_data = np.abs(np.around(rotate(data, angle, reshape=False)))

    return rot_data


def make_ellipse(a, b, theta):

    x = np.linspace(-10, 10, 45)
    y = np.linspace(-10, 10, 45)[:, None]
    ellipse = ((x/a)**2 + (y/b)**2 <= 1).astype(int)

    return rotate_image(ellipse, theta)


hline = np.zeros((5, 5))
hline[2, 1:4] += 1
vline = rotate_image(hline, 90)
diag_up = rotate_image(hline, 45)
diag_down = rotate_image(hline, -45)
circle = hline + vline
circle_off = np.roll(np.roll(circle, 1), 1, axis=0)

data_dict = {'Horizontal Line': hline,
             'Vertical Line': vline,
             'Diagonal Line (Up)': diag_up,
             'Diagonal Line (Down)': diag_down,
             'Circle': circle,
             'Circle (Off-Centre)': circle_off}

def get_galaxy_image(gal_flux,gal_r0,g1,g2,psf_beta,psf_re,pixel_scale,shift_x=0,shift_y=0):
    gal = galsim.Exponential(flux=gal_flux, scale_radius=gal_r0)
    gal = gal.shear(g1=g1, g2=g2)
    gal = gal.shift(shift_x,shift_y)
    psf = galsim.Moffat(beta=psf_beta, flux=1., half_light_radius=psf_re)
    gal_psf = galsim.Convolve([gal, psf])
    image_gal_psf = galsim.ImageF(256,256)
    image_gal_psf = gal_psf.drawImage(image_gal_psf,scale=pixel_scale)
    image_psf = psf.drawImage(scale=pixel_scale)
    return image_gal_psf,image_psf
