import numpy as np
from plots import u, v, indicies

def circulation_line_integral(
        u: np.ndarray,
        v: np.ndarray,
        p: tuple[tuple[int, int, int, int], ...]
    ) -> tuple[list[float], float]:
    """
    Calculates the circulation around rectangle over field F = ui + vj 
    with positive orientation as four line integrals.

    Parameters
    ----------
    u : np.ndarray
        x component of field
    v : np.ndarray
        y component of field
    p : tuple[tuple[int, int, int, int], ...]
        Nested n-tuple with indicies for coordinates

    Returns
    -------
    parts : list[float]
        Circulation over each line
    total_circulation : float
        Total circulation around rectangle
    """
    x1, y1, x2, y2 = p
    dt = 0.50

    parts = np.zeros(4)
    parts[0] = np.sum(u[x1:x2+1, y1]*dt)
    parts[1] = np.sum(v[x2, y1:y2+1]*dt)
    parts[2] = -np.sum(u[x1:x2+1, y2]*dt)
    parts[3] = -np.sum(v[x1, y1:y2+1]*dt)

    return parts, np.sum(parts)

def circulation_surface_integral(
        u: np.ndarray,
        v: np.ndarray,
        p: tuple[tuple[int, int, int, int], ...]
    ) -> float:
    """
    Calculates the circulation around rectangle over field F = ui + vj 
    with positive orientation as a single surface integral.

    Parameters
    ----------
    u : np.ndarray
        x component of field
    v : np.ndarray
        y component of field
    p : tuple[tuple[int, int, int, int], ...]
        Nested n-tuple with indicies for coordinates

    Returns
    -------
    circulation : float
        Total circulation around rectangle
    """
    x1, y1, x2, y2 = p
    dt = 0.50
    curl_z = np.gradient(v, dt, axis=0) - np.gradient(u, dt, axis=1)

    return np.sum(curl_z[x1:x2+1, y1:y2+1]*dt**2)

def flux_line_integral(
        u: np.ndarray,
        v: np.ndarray,
        p: tuple[tuple[int, int, int, int], ...]
    ) -> float:
    """
    Calculates the integrated flux of the velocity field v = ui + vj 
    with positive orientation as four line integrals.

    Parameters
    ----------
    u : np.ndarray
        x component of field
    v : np.ndarray
        y component of field
    p : tuple[tuple[int, int, int, int], ...]
        Nested n-tuple with indicies for coordinates

    Returns
    -------
    parts : list[float]
        Flux over each line
    flux : float
        Total flux around rectangle
    """
    x1, y1, x2, y2 = p
    dt = 0.50

    parts = np.zeros(4)
    parts[0] = -np.sum(v[x1:x2+1, y1]*dt)
    parts[1] = np.sum(u[x2, y1:y2+1]*dt)
    parts[2] = np.sum(v[x1:x2+1, y2]*dt)
    parts[3] = -np.sum(u[x1, y1:y2+1]*dt)

    return parts, np.sum(parts)

def main():
    with open('integration_out.txt', 'w') as file:

        for i, rec in enumerate(indicies, start=1):
            sides, total = circulation_line_integral(u, v, rec)
            surf = circulation_surface_integral(u, v, rec)
            sides_flux, flux = flux_line_integral(u, v, rec)
            
            file.write(f'--------------------------------------------\n')
            file.write(f'Rectangle {i}\n')

            file.write('\n')
            file.write(f'Circulation, line integral:     {total:.2f}\n')

            for j, side in enumerate(sides, start=1):
                file.write(f'Circulation side {j}:             {side:.2f}\n')

            file.write('\n')
            file.write(f'Circulation, surface integral:  {surf:.2f}\n')
            file.write(f'Percentage error:               {(total-surf)/(total)*100:.2f} %\n')

            file.write('\n')
            file.write(f'Integrated flux:                {flux:.2f}\n')

            for k, side in enumerate(sides_flux, start=1):
                file.write(f'Flux side {k}:                    {side:.2f}\n')

        file.write(f'--------------------------------------------')

if __name__ == '__main__':
    main()