%% Relaxation of Original Problem

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval

%% S1

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 <= 1;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval


%% S2

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 >= 2;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval

%% S3

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 <= 1;
        x1 <= 1;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval


%% S4

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 <= 1;
        x1 >= 2;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval


%% S5

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 <= 1;
        x1 <= 1;
        x2 <= 0;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval

%% S6

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 <= 1;
        x1 <= 1;
        x2 >= 1;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval


%% S7

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 <= 1;
        x1 >= 2;
        x4 <= 1;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval


%% S8

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 <= 1;
        x1 >= 2;
        x4 >= 2;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval


%% S9

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 <= 1;
        x1 >= 2;
        x4 <= 1;
        x2 <= 0;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval


%% S10

cvx_begin quiet
    variables x1 x2 x3 x4
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
        x3 <= 1;
        x1 >= 2;
        x4 <= 1;
        x2 >= 1;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval


%% Original Problem

cvx_solver mosek
cvx_begin quiet
    variable x1 integer
    variable x2 integer
    variable x3 integer
    variable x4 integer
    maximize 2*x1 + 3*x2 + 4*x3 + 7*x4
    subject to
        4 * x1 + 6 * x2 - 2 * x3 + 8 * x4 == 20;
        x1 + 2 * x2 - 6 * x3 + 7 * x4 == 10;
        [x1 x2 x3 x4] >= 0;
cvx_end
x = [x1 x2 x3 x4]
optval = cvx_optval