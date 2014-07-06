import numpy as numpy


def readDHTable(path):

    DHTableFile = open(path, "r")
    
    DHTable = DHTableFile.read().strip()
    DHTable = DHTable.replace('\r\n', ';')
    DHTable = DHTable.replace('\n', ';')
    DHTable = DHTable.replace('\r', ';')
    
    return numpy.matrix(DHTable)


def matrixTJ(fis0, j):

    matTJ = numpy.zeros(shape=(4,4))
    
    if j == 9:
        matTJ[0][0] = 1
        matTJ[0][3] = 1.56
        matTJ[1][1] = 1
        matTJ[2][2] = 1
        matTJ[3][3] = 1
    else:
        phi = fis0[j]*(numpy.pi/180)
        l = 2.0

        if j == 0:
            l = 0.0
        
        matTJ[0][0] = numpy.cos(phi)
        matTJ[0][1] = -numpy.sin(phi)
        matTJ[0][3] = l
        matTJ[1][0] = numpy.sin(phi)
        matTJ[1][1] = numpy.cos(phi)
        matTJ[2][2] = 1
        matTJ[3][3] = 1
    
    return matTJ


def matrixJTemp(fis0, j):

    matJTemp = numpy.zeros(shape=(4,4))
    phi = fis0[j]*(numpy.pi/180)
    
    matDTJ = numpy.zeros(shape=(4,4))
    matDTJ[0][0] = -numpy.sin(phi)
    matDTJ[0][1] = -numpy.cos(phi)
    matDTJ[1][0] = numpy.cos(phi)
    matDTJ[1][1] = -numpy.sin(phi)
    
    if j == 0:
        matJTemp = matDTJ
    else:
        matJTemp = matrixTJ(fis0, 0)
        
    for j2 in range(1,10):

        if j2 == j:
            matJTemp = numpy.dot(matJTemp, matDTJ)
        else:
            matJTemp = numpy.dot(matJTemp, matrixTJ(fis0, j2))
    
    return matJTemp
    

def matrixJ(fis0):
    
    matJ = numpy.zeros(shape=(3,9))
        
    for j in range(0, 9):
        matJTemp = matrixJTemp(fis0, j)
        
        matJ[0][j] = matJTemp[0][3]
        matJ[1][j] = matJTemp[1][3]
        matJ[2][j] = matJTemp[0][0]
        
    return matJ


def matrixJInv(matJ):

    matJT = numpy.transpose(matJ)
    matJTJ = numpy.dot(matJ, matJT)
    
    return numpy.dot(matJT, numpy.linalg.inv(matJTJ))
    

if __name__ == '__main__':
    
    DHTable = readDHTable("DHtable")
    
    fis0 = DHTable[:,3]
    
    matJ = matrixJ(fis0)
    matJInv = matrixJInv(matJ)
    
    print matJInv
    
    
    


    
