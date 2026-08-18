def calculo_cp(cp1:float, cp2:float, cp3:float) -> float:
    notasCP = [cp1,cp2,cp3]
    notasCP.sort()
    notasCP.pop(0)
    mediaCP = ((notasCP[0] + notasCP[1]) / 2) * 0.2
    return mediaCP

def calculo_sp(sp1:float, sp2:float) -> float:
    mediaSP = ((sp1 + sp2) / 2) * 0.2
    return mediaSP

def calculo_gs(gs:float) -> float:
    mediaGS = gs * 0.6
    return mediaGS

def calculo_medias(mediaCP:float, mediaSP:float, mediaGS:float) -> float:
    mediaGeral = (mediaCP + mediaSP + mediaGS) * 0.4
    return mediaGeral


cp1 = float(input('Cp1: '))
cp2 = float(input('Cp2: '))
cp3 = float(input('Cp3: '))
sp1 = float(input('Sprint 1: '))
sp2 = float(input('Sprint 2: '))
gs = float(input('GS: '))

mediaCP = calculo_cp(cp1,cp2,cp3)
mediaSP = calculo_sp(sp1,sp2)
mediaGS = calculo_gs(gs)
mediaGeral = calculo_medias(mediaCP,mediaSP,mediaGS)
print(f'Media do 1a semestre: {mediaGeral}')





