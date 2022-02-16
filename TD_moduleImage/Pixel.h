class Pixel {
    private:
        unsigned int r,g,b; // les composantes du pixel, unsigned char en C++
    public:

        // Constructeur par défaut de la classe: initialise le pixel à la couleur noire
        Pixel();

        // Constructeur de la classe: initialise r,g,b avec les paramètres
        Pixel(int nr, int ng, int nb);


        // Accesseur : récupère la composante rouge du pixel
        int getRouge();

        // Accesseur : récupère la composante verte du pixel
        int getVert();

        // Accesseur : récupère la composante bleue du pixel
        int getBleu();
        
        
        // Mutateur : modifie la composante rouge du pixel
        void setRouge(int nr);

        // Mutateur : modifie la composante verte du pixel
        void setVert(int ng);

        // Mutateur : modifie la composante bleue du pixel
        void setBleu(int nb);

        bool isPixel(Pixel p);
};
