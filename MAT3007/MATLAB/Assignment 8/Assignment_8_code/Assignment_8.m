%% Problem 1

xl = 1.5;
xr = 4.5;
while xr - xl > 10^(-5)
    xm = 0.5 * (xl + xr);
    if ((-5*(xm^(3)))+3*(xm^(2))+xm+2*((xm+1)^(2))*xm*log(xm)+1)/(((xm-1)^(3))*xm*((xm+1)^2)) < 0
        xl = xm;
    else
        xr = xm;
    end
end
solution = xm
value = -1/(xm-1)^2 * (log(xm) - (2*xm-2)/(xm+1))

%% Problem 2_back

grad_des_back([3;3], 10^(-5), 0.5, 0.1,'.k','-k')
grad_des_back([-3;3], 10^(-5), 0.5, 0.1,'.b','-b')
grad_des_back([3;-3], 10^(-5), 0.5, 0.1,'.r','-r')
grad_des_back([-3;-3], 10^(-5), 0.5, 0.1,'.g','-g')

%% Problem 2_exact

grad_des_exact([3;3], 10^(-5), '.k','-k')
grad_des_exact([-3;3], 10^(-5), '.b','-b')
grad_des_exact([3;-3], 10^(-5), '.r','-r')
grad_des_exact([-3;-3], 10^(-5), '.g','-g')

%% Problem 3

adagrad_back([3;3], 10^(-5), 0.5, 0.1, 10^(-6), 25, '.k', '-k')
adagrad_back([-3;3], 10^(-5), 0.5, 0.1, 10^(-6), 25, '.b', '-b')
adagrad_back([3;-3], 10^(-5), 0.5, 0.1, 10^(-6), 25, '.r', '-r')
adagrad_back([-3;-3], 10^(-5), 0.5, 0.1, 10^(-6), 25, '.g', '-g')

%% Problem 4a_grad

rosen_grad([-1; -0.5], 10^(-7), 0.5, 10^(-4))

%% Problem 4a_newton

rosen_newton([-1; -0.5], 10^(-7), 0.5, 10^(-4), 10^(-6), 0.1)

%% Problem 4b

newton_p23([3; 3], 10^(-5), 0.5, 0.1, 10^(-6), 0.1, '.k','-k')
newton_p23([-3; 3], 10^(-5), 0.5, 0.1, 10^(-6), 0.1, '.b','-b')
newton_p23([3; -3], 10^(-5), 0.5, 0.1, 10^(-6), 0.1, '.r','-r')
newton_p23([-3; -3], 10^(-5), 0.5, 0.1, 10^(-6), 0.1, '.g','-g')

