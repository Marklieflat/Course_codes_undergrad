clc;

%% Nurse scheduling problem

cvx_solver gurobi;
cvx_begin
integer variables x1 x2 x3 x4 x5 x6 x7
    minimize x1 + x2 + x3 + x4 + x5 + x6 +x7
    subject to 
        x1           + x4 + x5 + x6 + x7 >= 13
        x1 + x2           + x5 + x6 + x7 >= 15
        x1 + x2 + x3           + x6 + x7 >= 15
        x1 + x2 + x3 + x4           + x7 >= 16
        x1 + x2 + x3 + x4 + x5           >= 12
             x2 + x3 + x4 + x5 + x6      >= 6
                  x3 + x4 + x5 + x6 + x7 >= 7
        [x1,  x2,  x3,  x4,  x5,  x6,  x7] >= 0
cvx_end

[x1, x2, x3, x4, x5, x6, x7]


