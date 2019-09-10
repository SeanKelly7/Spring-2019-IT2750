//Rail cipher
//I wanted to be fancy so its secretum for the encrypt and veritas for the decrypt
//Also yeah most of what's in the code is in latin if you were wondering

def secretum(text):
    etiam = ""
    impar = ""
    count = 0
    for num in text:
        if count % 2 == 0:
            etiam = etiam + num
        else:
            impar = impar + num
        count = count + 1
    cypher = impar + etiam
    return cypher
    
def veritas(cypherIllud):
    halfLength = len(cypherIllud) // 2
    impar = cypherIllud[:halfLength]
    etiam = cypherIllud[halfLength:]
    plainText = ""
   
    for i in range(halfLength):
        plainText = plainText + etiam[i]
        plainText = plainText + impar[i]
   
    if len(impar) < len(etiam):
        plainText = plainText + etiam[-1]
   
    return plainText
