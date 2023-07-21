def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    vt = [vertex[0], vertex[1], vertex[2], 1]

    vt_temp = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            vt_temp[i] += modelMatrix[i][j] * vt[j]

    vt = vt_temp[:3]

    return vt

def fragmentShader(**kwargs):
    color = [1, 1, 1]
    return color
