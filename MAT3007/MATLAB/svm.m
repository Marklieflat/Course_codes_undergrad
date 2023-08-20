cvx_solver mosek
cvx_begin quiet
    variables w1 w2 b
    minimize 1/2 * (w1^2 + w2^2)
    subject to
        -1*(w2 + b) >= 1;
        -1*(w1 + b) >= 1;
        (4*w2 + b) >= 1;
        (4*w1 + b) >= 1;
cvx_end

res = [w1; w2; b]