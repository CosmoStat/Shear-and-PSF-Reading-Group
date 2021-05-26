from ipywidgets.widgets import *
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse


def show_image(data, show_flux=False, centroid=None,
               chi=None, epsilon=None, abt=None):

    limx, limy = data.shape

    def display_image():
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.grid()
        ax.imshow(data, cmap='binary', extent=[0, limx, limy, 0])
        return ax

    if show_flux:
        @interact(data=fixed(data), x=(0, limx-1, 1), y=(0, limy-1, 1))
        def make_plot(data, x, y):
            ax = display_image()
            box = Rectangle((x, y), 1, 1, color='red', alpha=0.5)
            ax.add_patch(box)
            ax.text(limy + limy / 5, limx - 4 * limx / 5,
                    r'$I({}, {})={}$'.format(x, y, data[y, x]), fontsize=18)

    if not isinstance(centroid, type(None)):
        ax = display_image()
        ax.plot(*centroid + 0.5, 'rx', markersize=12, markeredgewidth=2)
        ax.text(limy + limy / 5, limx - 4 * limx / 5,
                r'$\bar x = {}, \bar y = {}$'.format(*centroid), fontsize=18)

    if not isinstance(chi, type(None)):
        ax.text(limy + limy / 5, limx - 3 * limx / 5,
                r'$\chi_1 = {}, \chi_2 = {}$'.format(*chi), fontsize=18)

    if not isinstance(epsilon, type(None)):
        ax.text(limy + limy / 5, limx - 2 * limx / 5,
                r'$\epsilon_1 = {}, \epsilon_2 = {}$'.format(*epsilon),
                fontsize=18)

    if not isinstance(abt, type(None)):
        a, b, theta = abt
        ellipse = Ellipse(centroid + 0.5, a * 5, b * 5, -theta, fill=False,
                          edgecolor='c', linewidth=2)
        ax.add_patch(ellipse)
        ax.text(limy + limy / 5, limx - limx / 5,
                r'$a = {}, b = {}, \theta = {}$'.format(*abt),
                fontsize=18)

    plt.show()

def ellipse_from_measure(measured_shear,ax):
    q = measured_shear.observed_shape.q
    beta = measured_shear.observed_shape.beta
    centroid = (measured_shear.moments_centroid.x+128,measured_shear.moments_centroid.y+128)
    sigma = measured_shear.moments_sigma
    print(sigma)
    ellipse = Ellipse(centroid,sigma*3,sigma*3/q,-beta.deg,color="red",fill=False,label="Measured shape")
    ax.add_patch(ellipse)