all: mainExemple.out

mainExemple.out: mainExemple.o Image.o Pixel.o
	g++ mainExemple.o Image.o Pixel.o -o mainExemple.out
	
Pixel.o: Pixel.cpp Pixel.h
	g++ -Wall -c Pixel.cpp

Image.o: Image.cpp Image.h Pixel.h
	g++ -Wall -c Image.cpp

mainExemple.o: mainExemple.cpp Image.h Pixel.h
	g++ -Wall -c mainExemple.cpp

clean:
	rm *.o && rm *.out
