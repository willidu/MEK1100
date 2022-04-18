from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import scipy.io
import numpy as np

# Reading data
f = scipy.io.loadmat('Oblig 2/data.mat')
x, y, u, v, xit, yit = (f[index].transpose() for index in ['x', 'y', 'u', 'v', 'xit', 'yit'])

# Checking dimension of data
for arr in (x, y, u, v):
    assert arr.shape == (194, 201), 'Wrong dimension'

for arr in (xit, yit):
    assert arr.shape == (194, 1), 'Wrong dimension'

assert (y[0,1]-y[0,0], x[1,0]-x[0,0]) == (0.5, 0.5), 'Wrong dx or dy'

assert (y[-1,0], y[-1,-1]) == (-50.0, 50.0), 'Wrong range of y'

indicies = ((34, 159, 69, 169), (34, 84, 69, 99), (34, 49, 69, 59))

if __name__ == '__main__':
    # Plotting speed as contourplot
    v_mag = np.sqrt(u**2+v**2)

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

    plt.savefig('Oblig 2/figures/task_b.pdf')
    # plt.show()

    # Plotting velocity as quiverplot
    fig, ax = plt.subplots()

    skip = (slice(None, None, 10), slice(None, None, 10))
    ax.quiver(x[skip], y[skip], u[skip], v[skip])
    ax.plot(xit, yit, 'r-')

    for x1, y1, x2, y2 in indicies:
        x1, y1, x2, y2 = x[x1,y1], y[x1,y1], x[x2,y2], y[x2,y2]
        ax.add_patch(Rectangle((x1, y1),
                               width=x2-x1,
                               height=y2-y1,
                               fill=False,
                               ec='g',
                               lw=2.))

    ax.set(xlabel='x [mm]',
           ylabel='y [mm]',
           xlim=(0, np.max(x)),
           ylim=(-51., 51.),
           title='Velocity in xy-plane')

    plt.savefig('Oblig 2/figures/task_c.pdf')
    # plt.show()

    # Calculating divergence
    dudx = np.gradient(u, axis=0)
    dvdy = np.gradient(v, axis=1)
    div = dudx + dvdy

    # Plotting divergence as contourplot
    fig, ax = plt.subplots()
    cs = ax.contourf(x, y, div)
    plt.colorbar(cs, ax=ax)
    ax.plot(xit, yit, 'r-')

    for x1, y1, x2, y2 in indicies:
        x1, y1, x2, y2 = x[x1,y1], y[x1,y1], x[x2,y2], y[x2,y2]
        ax.add_patch(Rectangle((x1, y1),
                               width=x2-x1,
                               height=y2-y1,
                               fill=False,
                               ec='k',
                               lw=2.))

    ax.set(xlabel='x [mm]',
           ylabel='y [mm]',
           xlim=(0, np.max(x)),
           ylim=(-50., 50.),
           title='Divergence in $xy$-plane')

    plt.savefig('Oblig 2/figures/task_d.pdf')
    # plt.show()

    # Calculating curl
    dvdx = np.gradient(v, axis=0)
    dudy = np.gradient(u, axis=1)
    curl_z = dvdx - dudy

    # Plotting curl in z direction and streamlines as contourplot
    fig, ax = plt.subplots()
    cs = ax.contourf(x, y, curl_z)
    plt.colorbar(cs, ax=ax)
    ax.plot(xit, yit, 'r-')
    ax.streamplot(x.transpose(),
                  y.transpose(),
                  u.transpose(),
                  v.transpose(),
                  color=u.transpose())

    for x1, y1, x2, y2 in indicies:
        x1, y1, x2, y2 = x[x1,y1], y[x1,y1], x[x2,y2], y[x2,y2]
        ax.add_patch(Rectangle((x1, y1),
                               width=x2-x1,
                               height=y2-y1,
                               fill=False,
                               ec='k',
                               lw=2.))

    ax.set(xlabel='x [mm]',
           ylabel='y [mm]',
           xlim=(0, np.max(x)),
           ylim=(-50., 50.),
           title='Curl in $z$-direction')

    plt.savefig('Oblig 2/figures/task_e.pdf')
    plt.show()
