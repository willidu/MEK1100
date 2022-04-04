% 4.9.a
t = linspace(-5, 5);
[x, y] = meshgrid(t);
psi = x.*y;
contour(x, y, psi);
axis square

%% 
% 4.9.b
t = linspace(-5, 5);
[x, y] = meshgrid(t);
psi = 2*log(sqrt(x.^2 + y.^2));
contour(x, y, psi);
axis square

%% 
% 4.9.b
t = linspace(-6, 6);
[x, y] = meshgrid(t);
psi = y ./ (x.^2 + y.^2);
contour(x, y, psi,  [-1 -.5 -.35 -.2 0 .2 .35 .5 1]);
axis square
