
import numpy

class ConnectionDelsys_1_1():


    def __init__(self):
        self.powFraction=numpy.array([[2**-1],[2**-2],[2**-3],[2**-4],[2**-5],[2**-6],[2**-7],[2**-8],[2**-9],[2**-10],[2**-11],[2**-12],[2**-13],[2**-14],[2**-15],[2**-16],[2**-17],[2**-18],[2**-19],[2**-20],[2**-21],[2**-22],[2**-23]])
        #self.powFraction = numpy.array([[0.5], [0.25], [0.125], [0.0625], [0.03125], [0.01562], [0.007812], [0.003906], [0.001953], [0.0009765],[0.0004882], [0.0002441], [0.0001220], [6.1035e-05], [3.0517e-05], [1.5258e-05], [7.6293e-06],[3.8146e-06], [1.9073e-06], [9.536e-07], [4.7683e-07], [2.3841e-07], [1.1920e-07]])
        #self.value1 = 0 #numpy.zeros(8)


        pass

    def DecodificationData(self,dataDevice):

        #dataInt = numpy.fromstring(dataDevice, dtype=numpy.uint8)
        #print(dataInt)
        #dataBinary = numpy.unpackbits(dataInt)

        dataBinary = numpy.unpackbits(numpy.fromstring(dataDevice, dtype=numpy.uint8))

        #fractionInt = numpy.add(1,numpy.dot(dataBinary[9:33],self.powFraction))
        #self.value1 = numpy.prod([ numpy.power((-1),int(numpy.array(dataBinary[0]))),fractionInt[0] ,numpy.power(2,int(numpy.packbits(dataBinary[1:9])) - 127,dtype=float)])
        #tic = time.perf_counter()
        value1 = numpy.prod([ numpy.power((-1),int(numpy.array(dataBinary[0]))),numpy.add(1,numpy.dot(dataBinary[9:33],self.powFraction)) ,numpy.power(2,int(numpy.packbits(dataBinary[1:9])) - 127,dtype=float)])
        #print(time.perf_counter() - tic)
        return value1
        pass








