import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def plot_psf(psf_img, cmap='gist_stern'):
    fig = plt.figure(figsize=(18,4))

    ax = fig.add_subplot(131)
    im = ax.imshow(psf_img, interpolation='none', origin='lower', cmap=cmap)
    ax.set_xlabel('x [pixels]')
    ax.set_ylabel('y [pixels]')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im, cax=cax, orientation='vertical')
    ax.set_title('PSF')


    ax = fig.add_subplot(132)
    im = ax.imshow(np.log(abs(psf_img)), interpolation='none', origin='lower', cmap=cmap)
    ax.set_xlabel('x [pixels]')
    ax.set_ylabel('y [pixels]')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im, cax=cax, orientation='vertical')
    ax.set_title('log(PSF)')

    ax = fig.add_subplot(133)
    im = ax.imshow(abs(np.fft.fftshift(np.fft.fft2(psf_img))), interpolation='none', origin='lower', cmap=cmap)
    ax.set_xlabel('x [freq]')
    ax.set_ylabel('y [freq]')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im, cax=cax, orientation='vertical')
    ax.set_title('abs(FFT(PSF))')

    plt.show()
