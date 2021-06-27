edad = input('Teclea joven si es menor a 12 meses, y adulto si es mayor a 12 meses: ')
peso = int(input('Cual es el peso ideal del perro: '))

def calculadora_barf(edad, peso):
    if edad == 'joven':
        actividad = input('Teclea "a" si es de 2-4 meses, "b" si es de 5-6 meses, "c" si es 7-8 meses, "d" si es de 9-10 meses y e si es de 11-12 meses: ')
        if actividad == 'a':
          porcentaje = .1
        elif actividad == 'b':
          porcentaje = .08
        elif actividad == 'c':
          porcentaje = .06
        elif actividad == 'd':
          porcentaje = .04
        else:
          porcentaje = .03
        
    elif edad == 'adulto':
        actividad = input('Teclea "a" si sedentario o esterilizado, "b" si es normal, "c" deportista: ')
        if actividad == 'a':
          porcentaje = .02
        elif actividad == 'b':
          porcentaje = .025
        elif actividad == 'c':
          porcentaje = .03
    else:
        print('Favor de teclear joven o adulto')
    print('teclea como quieres ver los calculos \na - diario \nb - semanal \nc - quincenal \nd - mensual')
    frec = input()
    if frec == 'a':
      nfrec = 1
      duracion = 'diarios'
    elif frec =='b':
      nfrec = 7      
      duracion = 'a la semana'
    elif frec =='c':
      nfrec = 15
      duracion = 'a la quincena'
    else:
      nfrec = 30
      duracion = 'al mes'
    # calculos de consumo diario, huesos carnosos, carnes y pescados, 
    # víceras y organos, vegetales y verduras y fruta
    cd = peso * porcentaje * nfrec
    hc = cd * .5
    cp = cd * .3
    vo = cd * .1
    vv = cd * .06
    ft = cd * .04

    print('El perro deberá de comer: '+ str(round(cd,2))+ ' Kilogramos '+duracion+ ', de los cuales: \nHuesos carnosos: ' + str(round(hc,2))+ '\nCarnes y pescado: ' + str(round(cp,2)) + '\nVíceras y órganos: ' + str(round(vo,2))+'\nVegetales y verduras: ' + str(round(vv,2))+'\nFruta: ' + str(round(ft,2)))

calculadora_barf(edad, peso)