triangulo(X,Y,Z):- (((X+Y)<Z)->write("No es posible formar un triangulo.")),!.
triangulo(X,Y,Z):- (((Y+Z)<X)->write("No es posible formar un triangulo.")),!.
triangulo(X,Y,Z):- (((X+Z)<Y)->write("No es posible formar un triangulo.")),!.

triangulo(X,Y,Z):- (X==Y,X==Z,Y==Z->write("Triangulo equilatero.")),!.
triangulo(X,Y,Z):- (X==Y,X\=Z->write("Triangulo isoceles.")),!.
triangulo(X,Y,Z):- (Z==Y,X\=Z->write("Triangulo isoceles.")),!.
triangulo(X,Y,Z):- (X==Z,X\=Y->write("Triangulo isoceles.")),!.
triangulo(X,Y,Z):- (X\=Y,X\=Z,Y\=Z->write("Triangulo escaleno.")),!.