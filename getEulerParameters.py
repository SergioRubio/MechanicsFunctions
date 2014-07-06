import numpy as NP


def readRotationMatrix(path):
    
    rijxcolumns = open(path, "w+")
    rijxcolumnsBak = open(path + ".bak").readline()

    matrixR = NP.zeros(shape=(3,3))
    i = j = 0
    
    for elem in rijxcolumnsBak.split(","):
        matrixR[i][j] = float(elem.strip())
            
        i += 1

        if i == 3:
            i = 0
            j += 1
            
    for j in range(3):
        for i in range(3):
            rijxcolumns.write(str(matrixR[i][j]))

            if i != 3 and j != 3:
                rijxcolumns.write(", ")
                
    return matrixR


def generateRotationMatrix(path):
    
    rijxcolumns = open(path, "w+")
    
    v1 = NP.array([0.0514352967826213, 0.10869082075020531, 0.017050320602514768])
    c1 = v1/(NP.linalg.norm(v1))
    v2 = NP.array([0.6619543690108294, 0.9785558011717996, 0.8985397123574375])
    
    v2Parallel = NP.dot(c1, v2) * c1
    v2Transverse = v2 - v2Parallel
    c2 = v2Transverse/(NP.linalg.norm(v2Transverse))
    
    c3 = NP.cross(c1, c2)
    
    matrixR2 = NP.zeros(shape=(3,3))
    matrixR2[0][0] = c1[0]
    matrixR2[1][0] = c1[1]
    matrixR2[2][0] = c1[2]
    matrixR2[0][1] = c2[0]
    matrixR2[1][1] = c2[1]
    matrixR2[2][1] = c2[2]
    matrixR2[0][2] = c3[0]
    matrixR2[1][2] = c3[1]
    matrixR2[2][2] = c3[2]
    
    for j in range(3):
        for i in range(3):
            rijxcolumns.write(str(matrixR2[i][j]))

            if i != 3 and j != 3:
                rijxcolumns.write(", ")
            
    return matrixR2


def eulerParametrization1(matrixR):

    euler1 = NP.zeros(shape=(2,3))
    
    beta1 = NP.arcsin(-matrixR[2][0])
    beta2 = NP.pi - beta1
    
    alpha1 = NP.arccos((matrixR[0][0])/NP.cos(beta1))
    alpha2 = NP.arccos((matrixR[0][0])/NP.cos(beta2))
    
    gamma1 = NP.arccos((matrixR[2][2])/NP.cos(beta1))
    gamma2 = NP.arccos((matrixR[2][2])/NP.cos(beta2))

    euler1[0][0] = alpha1
    euler1[0][1] = beta1
    euler1[0][2] = gamma1
    
    euler1[1][0] = alpha2
    euler1[1][1] = beta2
    euler1[1][2] = gamma2
    
    return euler1


def eulerParametrization2(matrixR):

    euler2 = NP.zeros(shape=(2,3))
    
    beta1 = NP.arccos(matrixR[2][2])
    beta2 = NP.pi - beta1
    
    alpha1 = NP.arcsin((matrixR[0][2])/NP.sin(beta1))
    alpha2 = NP.arcsin((matrixR[0][2])/NP.sin(beta2))
    
    gamma1 = NP.arcsin((matrixR[2][0])/NP.sin(beta1))
    gamma2 = NP.arcsin((matrixR[2][0])/NP.sin(beta2))
    
    euler2[0][0] = alpha1
    euler2[0][1] = beta1
    euler2[0][2] = gamma1
    
    euler2[1][0] = alpha2
    euler2[1][1] = beta2
    euler2[1][2] = gamma2
    
    return euler2
    

if __name__ == '__main__':
    
    matrixR = readRotationMatrix("rijxcolumns")
    #matrixR = generateRotationMatrix("rijxcolumns")
        
    fisef = open("fisef", "w+")
    
    eulerParam = eulerParametrization1(matrixR)
    #eulerParam = eulerParametrization2(matrixR)
        
    fisefString = str((180*eulerParam[0][0])/NP.pi) + ", " + str((180*eulerParam[0][1])/NP.pi) + ", " + str((180*eulerParam[0][2])/NP.pi)
    fisef.write(fisefString)
    
    print(fisefString)
    
    
    
