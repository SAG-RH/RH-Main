def calculoValorLiquido(item_bruto, numero_dependetes):
    if item_bruto <= 1100:
        faixa_inss = "INSS Faixa 1 - 7,5%"
        porc_inss = 7.5
        descon_inss = 0

    elif item_bruto <= 2203.48:
        faixa_inss = "INSS Faixa 2 - 9%"
        porc_inss = 9
        descon_inss = 16.50

    elif item_bruto <= 3305.22:
        faixa_inss = "INSS Faixa 3 - 12%"
        porc_inss = 12
        descon_inss = 82.60

    elif item_bruto <= 6433.57:
        faixa_inss = "INSS Faixa 4 - 14%"
        porc_inss = 14
        descon_inss = 148.70

    elif item_bruto >= 6433.58:
        faixa_inss = "INSS Faixa LIMITE - 0%"
        porc_inss = 0
        descon_inss = -751.97

    au = item_bruto - (item_bruto / 100 * porc_inss)
    inss = (item_bruto - au - descon_inss)
    base_calculo = item_bruto - inss

    if base_calculo <= 0:
        print(" ")
        porcen_base = 0
        deduc = 0
    elif base_calculo <= 1903.98:
        faixa_irrf = "IRRF Faixa 1 - 0%"
        porcen_base = 0
        deduc = 0
    elif base_calculo <= 2826.65:
        faixa_irrf = "IRRF Faixa 2 - 7,5%"
        porcen_base = 7.5
        deduc = 142.80
    elif base_calculo <= 3751.05:
        faixa_irrf = "IRRF Faixa 3 - 15%"
        porcen_base = 15
        deduc = 354.80
    elif base_calculo <= 4664.68:
        faixa_irrf = "IRRF Faixa 4 - 22,5"
        porcen_base = 22.5
        deduc = 636.13
    elif base_calculo >= 4664.69:
        faixa_irrf = "IRRF Faixa Limite - 27,5"
        porcen_base = 27.5
        deduc = 869.36

    base_irrf = item_bruto - inss - (numero_dependetes * 189.59)
    av = base_irrf - (base_irrf / 100 * porcen_base)
    irrf = (base_irrf - av - deduc)
    total_desconto = irrf + inss
    porcen_desconto = (total_desconto * 100 / item_bruto)
    salario_liquido = (item_bruto - inss - irrf)

    devolve_lista = [faixa_inss, descon_inss, inss, faixa_irrf, deduc, irrf, total_desconto, porcen_desconto, salario_liquido]
    return devolve_lista

def calculoSalarioLiquido(nome_funcionario, salario_bruto, depentes, bonus, setor):
    item_bruto = salario_bruto + bonus
    lista_retorno = [nome_funcionario, salario_bruto, depentes, bonus]
    lista_retorno = lista_retorno + calculoValorLiquido(item_bruto, depentes)
    lista_retorno.append(setor)
    return lista_retorno

def calculoDecimoTerceiLiquido(nome_funcionario, salario_bruto, depentes, meses_trabalhados, setor):
    decimoTerceiroBruto = salario_bruto / 12 * meses_trabalhados
    lista_retorno = [nome_funcionario, depentes]
    lista_retorno = lista_retorno + calculoValorLiquido(decimoTerceiroBruto, depentes)
    lista_retorno.append(setor)
    return lista_retorno

def calculoFeriasLiquida(nome_funcionario, salario_bruto, depentes, setor):
    ferias_liquido = 1 / 3 * salario_bruto
    ferias_liquido = salario_bruto + ferias_liquido
    lista_retorno = [nome_funcionario, salario_bruto, depentes]
    lista_retorno = lista_retorno + calculoValorLiquido(ferias_liquido, depentes)
    lista_retorno.append(ferias_liquido)
    lista_retorno.append(setor)
    return lista_retorno




