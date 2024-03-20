pragma circom 2.0.0;

template QAP() {
    signal input x1;
    signal input x2;
    signal output out;
    signal x3;
    signal x4;

    x3 <== x1 * x1;
    x4 <== x1 * x2;

    out <== x3 + 4 * x2 * x4 - 2;
}

component main = QAP();