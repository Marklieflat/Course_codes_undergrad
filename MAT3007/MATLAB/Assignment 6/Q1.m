x = linspace(-5, 5, 100);
y = linspace(-5, 5, 100);
[X, Y] = meshgrid(x, y);
Z = X + 2/3 * X.^3 + 1/2 * X.^2 - 2 * Y .* X.^2 + 4/3 * Y.^2;
figure;
surf(X, Y, Z);
hold on;
plot3(0, 0, 0, 'rx')
plot3(-1, 3/4, 1/12, 'go')
colorbar();
xlabel('x1');
ylabel('x2');
hold off;
