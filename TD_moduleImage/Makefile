all: mainExemple.out

mainExemple.out: mainTest.o Image.o Pixel.o
	g++ mainTest.o Image.o Pixel.o -o mainExemple.out
	
Pixel.o: Pixel.cpp Pixel.h
	g++ -Wall -c Pixel.cpp

Image.o: Image.cpp Image.h Pixel.h
	g++ -Wall -c Image.cpp

mainTest.o: mainTest.cpp Image.h Pixel.h
	g++ -Wall -c mainTest.cpp

clean:
	rm *.o && rm *.out
