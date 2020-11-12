(content:appendix)=
# Appendix

## `data.py` Content

Here we provide the code used to generate the example data for this chapter in
case you want to see it or reuse it.

```{admonition} Click the button to reveal code
:class: dropdown
```python
import numpy as np
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
```

## `plot.py` Content

Here we provide the code used to produce the plots for this chapter in case
you want to see it or reuse it.

```{admonition} Click the button to reveal code
:class: dropdown
```python
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
```
