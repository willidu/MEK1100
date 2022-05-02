from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import scipy.io
import numpy as np

# Reading data
f = scipy.io.loadmat('data.mat')
x, y, u, v, xit, yit = (f[index].transpose() for index in ['x', 'y', 'u', 'v', 'xit', 'yit'])

# Checking dimension of data
for arr in (x, y, u, v):
    assert arr.shape == (194, 201), 'Wrong dimension'

for arr in (xit, yit):
    assert arr.shape == (194, 1), 'Wrong dimension'

assert (y[0,1]-y[0,0], x[1,0]-x[0,0]) == (0.5, 0.5), 'Wrong dx or dy'

assert (y[-1,0], y[-1,-1]) == (-50.0, 50.0), 'Wrong range of y'

# Indicies of rectangles
indicies = ((34, 159, 69, 169), (34, 84, 69, 99), (34, 49, 69, 59))

def draw_rectangles(
        indicies: tuple[tuple[int, int, int, int], ...],
        x: np.ndarray,
        y: np.ndarray,
        ax: plt.Axes
    ) -> None:
    """
    Draws the rectangles with lower left corner (x[x1,y1], y[x1,y1])
    and upper right corner (x[x2,y2], y[x2,y2]).

    Parameters
    ----------
    indicies : tuple[tuple[int, int, int, int], ...]
        Nested n-tuple with indicies for coordinates
    x : np.ndarray
        x component of xy-meshgrid
    y : np.ndarray
        y component of xy-meshgrid
    ax : plt.Axes
        Axes object where the rectangle is drawn.
    """
    for x1, y1, x2, y2 in indicies:
        x1, y1, x2, y2 = x[x1,y1], y[x1,y1], x[x2,y2], y[x2,y2]
        ax.plot([x1, x2], [y1, y1], color='r')
        ax.plot([x2, x2], [y1, y2], color='g')
        ax.plot([x1, x2], [y2, y2], color='b')
        ax.plot([x1, x1], [y1, y2], color='k')

def main():
    # Plotting speed as contourplot
    v_mag = np.sqrt(u**2 + v**2)

    fig, ax = plt.subplots(2, 1, sharex=True, sharey=True)

    clines = np.linspace(0, 500, 101)
    cs = ax[0].contourf(x, y, v_mag, clines, vmin=0)
    ax[0].plot(xit, yit, 'r-')
    ax[0].set_ylabel('y [mm]')
    ax[0].set_title('Speed in water [mm s$^{-1}$]', fontsize=11)
    plt.colorbar(cs, ax=ax[0])

    clines = np.linspace(0, 5000, 101)
    cs = ax[1].contourf(x, y, v_mag, clines)
    ax[1].plot(xit, yit, 'r-')
    ax[1].set_xlabel('x [mm]')
    ax[1].set_ylabel('y [mm]')
    ax[1].set_title('Speed in air [mm s$^{-1}$]', fontsize=11)
    plt.colorbar(cs, ax=ax[1])

    plt.savefig('figures/task_b.png', dpi=1200)

    # Plotting velocity as quiverplot
    fig, ax = plt.subplots()

    skip = (slice(None, None, 10), slice(None, None, 10))
    ax.quiver(x[skip], y[skip], u[skip], v[skip])
    ax.plot(xit, yit, 'r-')

    draw_rectangles(indicies, x, y, ax)

    ax.set(
        xlabel='x [mm]',
        ylabel='y [mm]',
        xlim=(0, np.max(x)),
        ylim=(-51., 51.),
        title='Velocity in xy-plane'
    )

    plt.savefig('figures/task_c.png', dpi=1200)

    # Calculating divergence
    dudx = np.gradient(u, 0.5, axis=0)
    dvdy = np.gradient(v, 0.5, axis=1)
    div = dudx + dvdy

    # Plotting divergence as contourplot
    fig, ax = plt.subplots()
    cs = ax.contourf(x, y, div)
    plt.colorbar(cs, ax=ax)
    ax.plot(xit, yit, 'r-')

    draw_rectangles(indicies, x, y, ax)

    ax.set(
        xlabel='x [mm]',
        ylabel='y [mm]',
        xlim=(0, np.max(x)),
        ylim=(-50., 50.),
        title='Divergence in $xy$-plane'
    )

    plt.savefig('figures/task_d.png', dpi=1200)

    # Calculating curl
    dvdx = np.gradient(v, 0.5, axis=0)
    dudy = np.gradient(u, 0.5, axis=1)
    curl_z = dvdx - dudy

    # Plotting curl in z direction and streamlines as contourplot
    fig, ax = plt.subplots()
    cs = ax.contourf(x, y, curl_z)
    plt.colorbar(cs, ax=ax)
    ax.plot(xit, yit, 'r-')
    ax.streamplot(
        x.transpose(),
        y.transpose(),
        u.transpose(),
        v.transpose(),
        color=u.transpose()
    )

    draw_rectangles(indicies, x, y, ax)

    ax.set(
        xlabel='x [mm]',
        ylabel='y [mm]',
        xlim=(0, np.max(x)),
        ylim=(-50., 50.),
        title='Curl in $z$-direction'
    )

    plt.savefig('figures/task_e.png', dpi=1200)

if __name__ == '__main__':
    main()
    plt.show()
