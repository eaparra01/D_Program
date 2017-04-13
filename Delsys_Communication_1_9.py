import decimal
import socket

from ConnectionDelsys_1_1 import *
import threading

import numpy
import time
import psutil, os

p = psutil.Process(os.getpid())
p.nice(psutil.HIGH_PRIORITY_CLASS)



#def DecodificationData(event1, event2, barrier, sensor):
#    global value
#    global dataEMGbytes

 #   powFraction = numpy.array(
  #      [[2 ** -1], [2 ** -2], [2 ** -3], [2 ** -4], [2 ** -5], [2 ** -6], [2 ** -7], [2 ** -8], [2 ** -9], [2 ** -10],
 #        [2 ** -11], [2 ** -12], [2 ** -13], [2 ** -14], [2 ** -15], [2 ** -16], [2 ** -17], [2 ** -18], [2 ** -19],
#         [2 ** -20], [2 ** -21], [2 ** -22], [2 ** -23]])

 #   while (True):
 #       event1.wait()
 #       dataDevice = dataEMGbytes[sensor * 4:(sensor + 1) * 4]
 #       dataInt = numpy.fromstring(dataDevice, dtype=numpy.uint8)
        # print(dataInt)
#        dataBinary = numpy.unpackbits(dataInt)

#        fractionInt = numpy.add(1, numpy.dot(dataBinary[9:33], powFraction))

#        value[sensor] = numpy.prod([numpy.power((-1), int(numpy.array(dataBinary[0]))), fractionInt[0],
#                                    numpy.power(2, int(numpy.packbits(dataBinary[1:9])) - 127, dtype=float)])
        # print(barrier.n_waiting)
#        barrier.wait()
#        event2.set()
#        event1.clear()


def saveData(event1):

    global f
    global value_pass

    #f = open('datosEMG.txt', 'a')  # Con el archivo .txt creado coloca filas para cada dato nuevo, opción 'a'

    #while (True):
     #   event1.wait()
     #   val = '' + str(toc - tic) + '     ' + str(value[0]) + '     ' + str(value[1]) + '     ' + str(
     #       value[2]) + '     ' + str(value[3]) + '     ' + str(value[4]) + '     ' + str(value[5]) + '     ' + str(
     #       value[6]) + '     ' + str(value[7]) + '\n'
     #   f.write(val)
     #   event1.clear()

    while(True):
        event1.wait()
        #tic=time.perf_counter()
        #print(_array)
        with open('datosEMG.txt','a') as f:
            f.write("\n".join(" ".join(map(str, x)) for x in (value_pass)))
            f.write('\n')
            value_pass = 0
        #print('Tiempo guardar %f' % (time.perf_counter()-tic))
        event1.clear()
     # return value


TCP_IP = "192.168.42.254"
DEVICE_PORT = 50040
EMG_PORT = 50041
ACC_PORT = 50042
BUFFER_SIZE_DEVICE = 64
BUFFER_SIZE_EMG = 64
BUFFER_SIZE_ACC = 192

valueIni64 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

sDEVICE = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sEMG = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sACC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sDEVICE.connect((TCP_IP, DEVICE_PORT))
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print(dataDEVICE)

# time.sleep(2) # delays for 1 seconds
sEMG.connect((TCP_IP, EMG_PORT))
sACC.connect((TCP_IP, ACC_PORT))
# dataEMG = sEMG.recv(BUFFER_SIZE)
# print(dataEMG )

sDEVICE.send(b'MASTER\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('Se tomó el MASTER: %s' % dataDEVICE)

sDEVICE.send(b'TRIGGER?\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('El TRIGGER se encuentra en esatdo: %s ' % dataDEVICE)

sDEVICE.send(b'TRIGGER STOP OFF\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('El TRIGGER ahora se encuentra en STOP: %s ' % dataDEVICE)

sDEVICE.send(b'UPSAMPLING?\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('El UPSAMPLIG está en modo: %s ' % dataDEVICE)

sDEVICE.send(b'UPSAMPLE OFF\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('El UPSAMPLE se encendió: %s ' % dataDEVICE)

sDEVICE.send(b'SENSOR 1 TYPE?\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('El SENSOR 1 está en tipo: %s ' % dataDEVICE)

sDEVICE.send(b'SENSOR 1 SERIAL?\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('El SENSOR 1 SERIAL está en: %s ' % dataDEVICE)

sDEVICE.send(b'SENSOR 1 FIRMWARE?\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('El SENSOR 1 FIRMWARE es: %s ' % dataDEVICE)

sDEVICE.send(b'SENSOR 1 PAIRED?\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('La paridad del SENSOR 1 es: %s ' % dataDEVICE)

#sDEVICE.send(b'UPSAMPLE ON\r\n\r\n')
#dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
#print('La cantidad de CHANNELCOUNT del SENSOR 1 es: %s ' % dataDEVICE)

sDEVICE.send(b'SENSOR 1 CHANNEL 1 GAIN?\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('El canal del SENSOR 1 es: %s ' % dataDEVICE)

sDEVICE.send(b'SENSOR 1 CHANNEL 2 UNITS?\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('La unidad del SENSOR 1 es: %s ' % dataDEVICE)

sDEVICE.send(b'ENDIAN BIG\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('ENDIAN BIG del SENSOR 1 es: %s ' % dataDEVICE)

sDEVICE.send(b'ENDIANNESS?\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print('ENDIAN BIG del SENSOR 1 es: %s ' % dataDEVICE)

#sDEVICE.send(b'START\r\n\r\n')
#dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
#print(dataDEVICE)

Delsys1 = ConnectionDelsys_1_1()  # Se crea el objeto Delsys de la clase ConnectionDelsys
# pool = ThreadPool(processes=1)
# sensorThread1 = Thread(target = Delsys.DecodificationData,args=())


event1 = threading.Event()  # Crea el evento que ayuda a ejecutar el loop de la función guarda los datos decodificados un archivo .txt
#event2 = threading.Event()  # Crea el evento que ayuda a ejecutar el loop para la función saveData
#barrier = threading.Barrier(8)  # Crea la barrera y espera que los 8 hilos creados se terminen su ejecución para con el resto del programa

dataEMGbytes = valueIni64

#thread_1 = threading.Thread(target=DecodificationData, args=(event1, event2, barrier, 0))
#thread_2 = threading.Thread(target=DecodificationData, args=(event1, event2, barrier, 1))
#thread_3 = threading.Thread(target=DecodificationData, args=(event1, event2, barrier, 2))
#thread_4 = threading.Thread(target=DecodificationData, args=(event1, event2, barrier, 3))
#thread_5 = threading.Thread(target=DecodificationData, args=(event1, event2, barrier, 4))
#thread_6 = threading.Thread(target=DecodificationData, args=(event1, event2, barrier, 5))
#thread_7 = threading.Thread(target=DecodificationData, args=(event1, event2, barrier, 6))
#thread_8 = threading.Thread(target=DecodificationData, args=(event1, event2, barrier, 7))

  # Tiempo de espera para cuando sale el warning por los 2000Hz de la lectura de datos

#thread_1.start()
#thread_2.start()
#thread_3.start()
#thread_4.start()
#thread_5.start()
#thread_6.start()
#thread_7.start()
#thread_8.start()


elapsed = 0  # Variable que mide los tiempos de los datos
tic = 0  # Variable de inicio de la toma de los datos
toc = 0  # Variable final de la toma de los datos
global _array_in
global f
global value_pass
length = 150000
_array = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0],dtype=numpy.dtype(decimal.Decimal))
value =numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0],dtype=numpy.dtype(decimal.Decimal))     # se tiene 9 datos uno para tiempo y los demás para sensores
value =numpy.zeros((15000,9),dtype=numpy.dtype(decimal.Decimal))     # se tiene 9 datos uno para tiempo y los demás para sensores


f = open('datosEMG.txt', 'w')  # Crea un archivo .txt donde se guardaran los datos, opción 'w'
f.write('   Time        Sensor1     Sensor2     Sensor3     Sensor4     Sensor5     Sensor6     Sensor7     Sensor8\n')
f = open('datosEMG.txt', 'a')  # Con el archivo .txt creado coloca filas para cada dato nuevo, opción 'a'

thread_saved = threading.Thread(target=saveData, args=(event1,))
#thread_saved.start()

sDEVICE.send(b'START\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)
print(dataDEVICE)

time.sleep(5)


level = 0
i=0
tic = time.perf_counter()
print('Comienzo de la lectura de los Sensor')
e = 0
while (e<15000):

    #print(p.cpu_percent())
    #print(p.status())
    #if(e==1):
    #    tic = time.perf_counter()
    #tic1=time.perf_counter()

    dataEMGbytes = sEMG.recv(BUFFER_SIZE_EMG)
    #toc = time.perf_counter()

#    value[1:] = cython.list(map(Delsys1.DecodificationData,(dataEMGbytes[0:4],dataEMGbytes[4:8],dataEMGbytes[8:12],dataEMGbytes[12:16],dataEMGbytes[16:20],dataEMGbytes[20:24],dataEMGbytes[24:28],dataEMGbytes[28:32])))
#    print(dataEMGbytes)
#    print(type(dataEMGbytes))
    value[e,0] = time.perf_counter() - tic
    value[e,1] = Delsys1.DecodificationData(dataEMGbytes[0:4])
    value[e,2] = Delsys1.DecodificationData(dataEMGbytes[4:8])
    value[e,3] = Delsys1.DecodificationData(dataEMGbytes[8:12])
    value[e,4] = Delsys1.DecodificationData(dataEMGbytes[12:16])
    value[e,5] = Delsys1.DecodificationData(dataEMGbytes[16:20])  # Desde acá toma sólo dos datos // Aumenta de a dos seg
    value[e,6] = Delsys1.DecodificationData(dataEMGbytes[20:24])
    value[e,7] = Delsys1.DecodificationData(dataEMGbytes[24:28])  # Desde acá empiezaa cortar la toma d
    value[e,8] = Delsys1.DecodificationData(dataEMGbytes[28:32])
    #value[0] = 0#time.perf_counter() - tic
    #_array = numpy.vstack((_array, value))

    #print('Primer tiempo %f' % (time.perf_counter()-tic1))

    i = i + 1
    if (i == 80):
        #print('Tiempo %f' % (time.perf_counter()-tic1))
        #value_pass = value[level:e,:]
        f.write("\n".join(" ".join(map(str, x)) for x in (value[level:e,:])))
        f.write('\n')

        #value_pass = 0
        #print(value_pass)
        level = e
        i=0
        #print('tiempo %f' % (time.perf_counter() - tic))

        #event1.set()

        # x = round(float(elapsed), 10)
    #val = '' + str(toc - tic) + '     ' + str(v1[0]) + '     ' + str(v1[1]) + '     ' + str(v1[2]) + '     ' + str(v1[3]) + '     ' + str(v1[4]) + '     ' + str(v1[5]) + '     ' + str(v1[6]) + '     ' + str(v1[7]) + '\n'

    #val = '' + str(toc - tic) + '     ' + str(value[0]) + '     ' + str(value[1]) + '     ' + str(value[2]) + '     ' + str(value[3]) + '     ' + str(value[4]) + '     ' + str(value[5]) + '     ' + str(value[6]) + '     ' + str(value[7]) + '\n'
    #f.write(val)
    #print(time.perf_counter()-tic1)

    # barrier = threading.Barrier(8)
    # event1.clear()
    e += 1
#print(type(_array))
#print(value)
tocT = time.clock()
print(tocT - tic)
len(_array)
# f.close()
thread_saved.do_run = False
sDEVICE.send(b'STOP\r\n\r\n')
dataDEVICE = sDEVICE.recv(BUFFER_SIZE_DEVICE)

print(dataDEVICE)
print('Termina en la lectura de los Sensor')
sDEVICE.close()
sEMG.close()
sACC.close()
