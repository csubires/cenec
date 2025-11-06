
IVA = 0.21

def iva(importe):
    print(f'El importe es {importe:.1f} el iva es {(IVA * 100)} y el total es {importe + (importe * IVA)}')

# iva(100)

def comprar():
    iva(float(input('¿Cual es el importe?: ')))

comprar()
