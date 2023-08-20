/*
 * File: HFractal.cpp
 * ------------------
 * This program draws an H-fractal on the graphics window.int main() {
 */

#include "HFractal.h"


void drawHFractal(GWindow & gw, double x, double y, double size, int order){
    gw.setColor("Black");
    gw.setExitOnClose(true);
    gw.drawLine(x - 0.5*size, y - 0.5*size, x - 0.5*size, y + 0.5*size);
    gw.drawLine(x - 0.5*size, y, x + 0.5*size, y);
    gw.drawLine(x + 0.5*size, y - 0.5*size, x + 0.5*size, y + 0.5*size);
    if (order != 0) {
        drawHFractal(gw, x - 0.5*size, y - 0.5*size, 0.5*size, order - 1);
        drawHFractal(gw, x - 0.5*size, y + 0.5*size, 0.5*size, order - 1);
        drawHFractal(gw, x + 0.5*size, y - 0.5*size, 0.5*size, order - 1);
        drawHFractal(gw, x + 0.5*size, y + 0.5*size, 0.5*size, order - 1);
    }
}
