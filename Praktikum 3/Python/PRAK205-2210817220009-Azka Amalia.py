A=int(input())
B=int(input())
C=int((B*B)-(A*A))**(1/2)
print("Alas = {} cm".format(int(C)))
print("Tinggi = {} cm".format(int(A)))
keliling=int(A+B+C)
print("Keliling = {} cm".format(int(keliling)))
luas=int((C*A)/2)
print("Luas = {} cm^2".format(int(luas)))