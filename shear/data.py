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

data_list = {'Horizontal Line': hline,
             'Vertical Line': vline,
             'Diagonal Line (Up)': diag_up,
             'Diagonal Line (Down)': diag_down,
             'Circle': circle,
             'Circle (Off-Centre)': circle_off}
