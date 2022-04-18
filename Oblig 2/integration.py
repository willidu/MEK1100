from plots import *

def circulation_line_integral(u, v, p):
    """
    Calculates the circulation around rectangle over field F = ui + vj with positive orientation.

    Parameters
    ----------
    u : Array-like
        x component of field
    v : Array-like
        y component of field
    p : 4-tuple
        corners of rectangle (x1, y1, x2, y2)
    """
    x1, y1, x2, y2 = p
    dt = 0.50

    parts = np.zeros(4)
    parts[0] = np.sum(u[x1:x2+1, y1]*dt)
    parts[1] = np.sum(v[x2, y1:y2+1]*dt)
    parts[2] = -np.sum(u[x1:x2+1, y2]*dt)
    parts[3] = -np.sum(v[x1, y1:y2+1]*dt)

    return parts, np.sum(parts)

def circulation_surface_integral(u, v, p):
    """
    Calculates the circulation around rectangle over field F = ui + vj using curl.

    Parameters
    ----------
    u : Array-like
        x component of field
    v : Array-like
        y component of field
    p : 4-tuple
        corners of rectangle (x1, y1, x2, y2)
    """
    x1, y1, x2, y2 = p
    dt = 0.50
    curl_z = np.gradient(v, dt, axis=0) - np.gradient(u, dt, axis=1)

    return np.sum(curl_z[x1:x2+1, y1:y2+1]*dt**2)

def flux_line_integral(u, v, p):
    """
    Calculates the integrated flux around rectangle over field F = ui + vj.

    Parameters
    ----------
    u : Array-like
        x component of field
    v : Array-like
        y component of field
    p : 4-tuple
        corners of rectangle (x1, y1, x2, y2)
    """
    x1, y1, x2, y2 = p
    dt = 0.50

    parts = np.zeros(4)
    parts[0] = -np.sum(v[x1:x2+1, y1]*dt)
    parts[1] = np.sum(u[x2, y1:y2+1]*dt)
    parts[2] = np.sum(v[x1:x2+1, y2]*dt)
    parts[3] = -np.sum(u[x1, y1:y2+1]*dt)

    return parts, np.sum(parts)

if __name__ == '__main__':

    print(f'--------------------------------------------')

    for i, rec in enumerate(indicies, start=1):
        sides, total = circulation_line_integral(u, v, rec)
        surf = circulation_surface_integral(u, v, rec)
        sides_flux, flux = flux_line_integral(u, v, rec)
        
        print(f'Rectangle {i}\n')
        print(f'Circulation, line integral:     {total:.2f}')

        for j, side in enumerate(sides, start=1):
            print(f'Circulation side {j}:             {side:.2f}')

        print(f'\nCirculation, surface integral:  {surf:.2f}')
        print(f'Percentage error:               {(total-surf)/(total)*100:.2f} %\n')
        print(f'Integrated flux:                {flux:.2f}')

        for k, side in enumerate(sides_flux, start=1):
            print(f'Flux side {k}:                    {side:.2f}')

        print(f'--------------------------------------------')
