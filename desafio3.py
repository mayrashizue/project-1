temperatura = 37
frecuencia_cardiaca = 110

if temperatura >= 38 and frecuencia_cardiaca >= 100:
    print("Alerta clínica")
else:
    print("Sin criterios de alerta")

dolor_pecho = False
disnea = False

if dolor_pecho or disnea:
    print("Evaluar urgencia")
else:
    print("Sin síntomas graves")

alergia_penicilina = False

if not alergia_penicilina:
    print("Se puede indicar penicilina")
