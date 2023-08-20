W = [0, 10, 12, 17, 34;
    10, 0, 18, 8, 46;
    12, 18, 0, 9, 27;
    17, 8, 9, 0, 20;
    34, 46, 27, 20, 0];
a = [115;385;410;480;610];
b = [200;500;800;200;300];

cvx_begin
variables x(5, 5)
    minimize sum(sum(W .* x))
    subject to
        sum(x,2) == a;
        sum(x)' == b;
        sum(sum(x)) == 2000;
        x >= 0;
cvx_end
x
optval = cvx_optval
    
    
    
    
    
    