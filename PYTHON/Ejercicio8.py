import random
import time

random.seed(time.time_ns())
palabras = ['PIEDRA', 'PAPEL', 'TIJERAS']
			# 0          1         2

icon = ['✊', '✋', '✂️']

print('OPCIONES:')
for i, x in enumerate(palabras):
	print(f'\t{i + 1} - {palabras[i]}')

contador_maquina = 0
contador_jugador = 0
contador_empates = 0

try:
	jugadas=int(input('Cuantas rondas quieres jugar???: '))
except:
	print('Este programa solo funciona con números enteros!!')
	exit(1)

while (jugadas > 0):
	jugadas -= 1
	maquina = random.randint(0, 2)
	jugador = int(input('\nIntroduce tu elección [1-3]: '))

	if jugador < 1 or jugador > 3:
		print('Elección no válida')
		jugadas += 1
		continue
	jugador -= 1
	if jugador == maquina:
		print(f'🤖 MAQUINA: {palabras[maquina]} {icon[maquina]} VS {icon[jugador]} {palabras[jugador]} :JUGADOR 🤠, RESULTADO: Empate!!')
		contador_empates += 1
	elif jugador == 0 and maquina == 2:
		print(f'🤖 MAQUINA: {palabras[maquina]} {icon[maquina]} VS {icon[jugador]} {palabras[jugador]} :JUGADOR 🤠, RESULTADO: Has ganado 🎉')
		contador_jugador += 1
	elif jugador == 2 and maquina == 0:
		print(f'🤖 MAQUINA: {palabras[maquina]} {icon[maquina]} VS {icon[jugador]} {palabras[jugador]} :JUGADOR 🤠, RESULTADO: Has perdido 🙁')
		contador_maquina += 1
	elif jugador > maquina:
		print(f'🤖 MAQUINA: {palabras[maquina]} {icon[maquina]} VS {icon[jugador]} {palabras[jugador]} :JUGADOR 🤠, RESULTADO: Has ganado 🎉')
		contador_jugador += 1
	else:
		print(f'🤖 MAQUINA: {palabras[maquina]} {icon[maquina]} VS {icon[jugador]} {palabras[jugador]} :JUGADOR 🤠, RESULTADO: Has perdido 🙁')
		contador_maquina += 1

print(f'\nRESULTADO FINAL: {"🎉 HAS GANADOOO!!! 🎉" if contador_jugador > contador_maquina else "🙁 HAS PERDIDOOO 🙁!!"}')
print('\t🤖 MAQUINA: ', contador_maquina)
print('\t🤠 JUGADOR: ', contador_jugador)
print('\tEMPATES: ', contador_empates)
