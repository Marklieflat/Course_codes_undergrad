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

    