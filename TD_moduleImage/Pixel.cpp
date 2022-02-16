#include <iostream>
#include "Pixel.h"

using namespace std;

Pixel::Pixel() {
    r = 255;
    g = 255;
    b = 255;
}

Pixel::Pixel(int nr, int ng, int nb) {
    r = nr;
    g = ng;
    b = nb;
}

int Pixel::getRouge() {
    return r;
}

int Pixel::getVert() {
    return g;
}

int Pixel::getBleu() {
    return b;
}

void Pixel::setRouge(int nr) {
    r = nr;
}

void Pixel::setVert(int ng) {
    g = ng;
}

void Pixel::setBleu(int nb) {
    b = nb;
}

bool Pixel::isPixel(Pixel p) {
    if(r == p.getRouge() && g == p.getVert() && b == p.getBleu())
        return true;
    else 
        return false;
}


