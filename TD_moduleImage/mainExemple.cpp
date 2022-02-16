#include "Image.h"

 
int main() {
 
    Pixel blanc (255, 255, 255);
    Pixel vert (4, 200, 10);
    Pixel bleu (0, 128, 255);
 
    Image image1 (64,48);
    image1.effacer(vert);
    image1.dessinerRectangle(10, 40, 20, 44, blanc);
    image1.setPix(2,9,bleu);
    image1.setPix(15,42,bleu);
    image1.sauver("./data/image1.ppm");
    image1.afficherConsole();
 
    Image image2;
    image2.ouvrir("./data/image1.ppm");
    image2.dessinerRectangle(4, 14, 20, 43, blanc);
    image2.dessinerRectangle(32, 4, 50, 8, bleu);
    image2.sauver("./data/image2.ppm");
    return 0;
}