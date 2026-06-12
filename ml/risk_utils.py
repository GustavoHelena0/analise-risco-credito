def classificar_risco(predicao, probabilidade):

    if predicao == 1:
        return "alto"

    if probabilidade >= 0.40:
        return "moderado"

    return "baixo"