#include <assert.h>
#include <string.h>
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

void Image::sauver(const string filename) const {
    ofstream fichier (filename.c_str());
    assert(fichier.is_open());
    fichier << "P3" << endl;
    fichier << dimx << " " << dimy << endl;
    fichier << "255" << endl;
    for(unsigned int y=0; y<dimy; ++y)
        for(unsigned int x=0; x<dimx; ++x) {
            Pixel& pix = getPix(x++,y);
            fichier << +pix.r << " " << +pix.g << " " << +pix.b << " ";
        }
    cout << "Sauvegarde de l'image " << filename << " ... OK\n";
    fichier.close();
}

void Image::ouvrir(const string filename) {
    ifstream fichier (filename.c_str());
    assert(fichier.is_open());
	char r,g,b;
	string mot;
	dimx = dimy = 0;
	fichier >> mot >> dimx >> dimy >> mot;
	assert(dimx > 0 && dimy > 0);
	if (tab != NULL) delete [] tab;
	tab = new Pixel [dimx*dimy];
    for(unsigned int y=0; y<dimy; ++y)
        for(unsigned int x=0; x<dimx; ++x) {
            fichier >> r >> b >> g;
            getPix(x,y).setRouge(r);
            getPix(x,y).setVert(g);
            getPix(x,y).setBleu(b);
        }
    fichier.close();
    cout << "Lecture de l'image " << filename << " ... OK\n";
}

void Image::afficherConsole(){
    cout << dimx << " " << dimy << endl;
    for(unsigned int y=0; y<dimy; ++y) {
        for(unsigned int x=0; x<dimx; ++x) {
            Pixel& pix = getPix(x,y);
            cout << +pix.getRouge() << " " << +pix.getVert() << " " << +pix.getBleu() << " ";
        }
        cout << endl;
    }
}