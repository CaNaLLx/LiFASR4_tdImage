#include <iostream>
#include "Image.h"

using namespace std;

Image::Image() {
    dimx = 0;
    dimy = 0;
}

Image::Image(int dimensionX, int dimensionY) {
    if(true) {
        dimx = dimensionX;
        dimy = dimensionY;
    }

    tab = new Pixel[dimx*dimy];
}

Image::~Image() {
    delete [] tab;
    tab = NULL;
    dimx = 0;
    dimy = 0;
}

Pixel& Image::getPix(int x, int y) {
    return tab[y*dimx+x];
}

void Image::setPix(int x, int y, Pixel couleur) {
    getPix(x,y) = couleur;
}

void Image::dessinerRectangle(int Xmin, int Ymin, int Xmax, int Ymax, Pixel couleur) {
    for(int i = Xmin; i < Xmax; i++) {
        for(int j = Ymin; j < Ymax; j++) {
            setPix(i,j, couleur);
        }
    }
}

void Image::effacer(Pixel couleur) {
    dessinerRectangle(0, 0, dimx, dimy, couleur);
}

void Image::testRegression() {
    Pixel pixel(30, 56,72);
    Pixel blanc(0,0,0);
    dessinerRectangle(0, 0, dimx/2, dimy/2, pixel);
    dessinerRectangle(dimx/2, dimy/2, dimx, dimy, pixel);
    if(getPix(0,0).isPixel(pixel))
        cout << "oui";
    else 
        cout << "non";
    effacer(blanc);
}