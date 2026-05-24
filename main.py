from modelo.persona import Persona
from modelo.caja_atencion import CajaAtencion

def main():
    caja = CajaAtencion()
    
    print(" SIMULADOR DE GESTIÓN DE TURNOS - OFICINA DE ATENCIÓN ")
    
    personas = [
        Persona("Christian Mora", "1094728192"),
        Persona("Migel Hernandez", "1018374829"),
        Persona("Jose Delgado", "1032847192"),
        Persona("Marlon Bejarano", "1074839201")
    ]
    
    print("\n[+] REGISTRANDO LLEGADA DE ESTUDIANTES:")
    for persona in personas:
        turno = caja.agregar_persona(persona)
        print(f"  - Registrado: {persona} : {turno}")
        
    print(f"\nEstado de la cola: ¿Está vacía?: {caja.esta_vacia()}")
    
    print("\n[+] ATENDIENDO ESTUDIANTES (FIFO - First In, First Out):")
    for i in range(2):
        turno_atendido = caja.atender_siguiente()
        if turno_atendido:
            print(f"  * Atendido: {turno_atendido}")
        else:
            print("  * No hay personas esperando en la cola.")

    print("\n[+] CONSULTANDO SIGUIENTE TURNO EN ESPERA:")
    proximo = caja.proximo_turno()
    if proximo:
        print(f"  Siguiente turno a atender: {proximo}")
    else:
        print("  No hay más personas en la cola.")
        
    print("=" * 60)

if __name__ == "__main__":
    main()

