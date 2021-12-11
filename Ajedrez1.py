tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
tablero = []
for i in tablero_inicial.split('\n'):
        tablero.append(i.split('\t'))
f = open(tablero, 'w')
for i in tablero:
        f.write('\t'.join(i) + '\n')
f.close()
movimiento = 0

while True:
    continuar = input('Deseas hacer otro movimiento (s/n): ')
    if continuar != 's':
        break
    