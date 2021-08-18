import CriptografiaSegundo
import contas
import firulas

opcmenu = 0
senha = "ykycvwatgyiblokgyqbt"
senha_inserida_criptografada = " "


while senha_inserida_criptografada != "ykycvwatgyiblokgyqbt":
    firulas.pulalinhas()
    senha_inserida = str(input('Digite a senha para continuar: '))
    senha_inserida_criptografada = CriptografiaSegundo.principal(senha_inserida)
    if senha == senha_inserida_criptografada:
        print("Entrando...")
    else:
        print("A senha inserida anteriormente está errada")
        firulas.printLinhaSimples()
        continuar = input('Você deseja retornar ao menu ou encerrar o programa [R/E]: ').upper()
        if continuar == "E":
            senha_inserida_criptografada = "ykycvwatgyiblokgyqbt"
            opcmenu = 4

while opcmenu != 4:
    firulas.pulalinhas()
    print('\033[0;31m|                       Sistema de Gerenciamento de RH - SAG-RH                   |\033[m')
    firulas.printLinhaSimples()
    print('[1] Cálculo do Salário \n[2] Cálculo das Férias \n[3] Cálculo do 13° Salário \n[4] Sair')
    firulas.printLinhaSimples()
    opcmenu = int(input('O que você deseja fazer agora? '))
    if opcmenu == 1:
        firulas.printLinhaDupla()
        print('\033[1;46m                                Cálculo do Salário                                 \033[m')
        nomeFun = input('Por favor, insira o nome do funcionário: ')
        setor = input('Em qual setor o funcionário trabalha? ')
        salario_bruto = float(input('Agora, insira o salário bruto mensal do funcionário: R$ '))
        dependentes = int(input('Digite o número de dependentes do funcionário: '))
        bonus = float(input('Por fim, insira o valor do bonus, caso o usuário vá receber: R$ '))
        listaImpresaoSalario = []
        listaImpresaoSalario = contas.calculoSalarioLiquido(nomeFun, salario_bruto, dependentes, bonus, setor)

        print()
        firulas.printLinhaDupla()
        print('\033[1;32m|                                    SUCESSO!                                     |\033[m')
        firulas.printLinhaSimples()
        print(f'|Funcionário: {listaImpresaoSalario[0]}| Setor: {listaImpresaoSalario[-1]}|')
        firulas.printLinhaSimples()
        print(f'|Salário Bruto: R$:{listaImpresaoSalario[1]:.2f} | Bônus: {listaImpresaoSalario[3]:.2f} | N° de Dependentes: {listaImpresaoSalario[2]}|')
        firulas.printLinhaSimples()
        print(f'|{listaImpresaoSalario[4]}| Desconto Fixo: R${abs(listaImpresaoSalario[5]):.2f}| Total.: R${listaImpresaoSalario[6]:.2f}|')
        firulas.printLinhaSimples()
        print(f'|{listaImpresaoSalario[7]}| Desconto Fixo: R${listaImpresaoSalario[8]:.2f}| Total.: R${listaImpresaoSalario[9]:.2f}|')
        firulas.printLinhaSimples()
        print(f"|Total.: R${listaImpresaoSalario[10]:.2f}| % Desc. {listaImpresaoSalario[11]:.2f}%| Salário Líquido.: R${listaImpresaoSalario[12]:.2f}|")
        firulas.printLinhaDupla()
        input('\n\033[1;43m Aperte qualquer tecla para voltar ao menu: \033[m')

    elif opcmenu == 2:
        print()
        firulas.printLinhaDupla()
        print('\033[1;46m                                Cálculo Férias Líquido                             \033[m')
        nome_func = input('Por favor, insira o nome do funcionário: ')
        setor = input('Em qual setor o funcionário trabalha? ')
        salario_bruto = float(input('Agora, insira o salário bruto mensal do funcionário: R$ '))
        dependentes = int(input('Digite a quantidade de Dependentes: '))

        listaImpresaoFerias = []
        listaImpresaoFerias = contas.calculoFeriasLiquida(nome_func, salario_bruto, dependentes, setor)

        print()
        firulas.printLinhaDupla()
        print('\033[1;32m|                                    SUCESSO!                                     |\033[m')
        firulas.printLinhaSimples()
        print(f'|Funionário.: {listaImpresaoFerias[0]}| Setor: {listaImpresaoFerias[-1]}|')
        firulas.printLinhaSimples()
        print(f'|Salário Bruto: R$:{listaImpresaoFerias[1]:.2f} |                  N° de Dependentes: {listaImpresaoFerias[2]}|')
        firulas.printLinhaSimples()
        print(f'|{listaImpresaoFerias[3]}| Desconto Fixo: R${abs(listaImpresaoFerias[4]):.2f}| Total.: R${listaImpresaoFerias[5]:.2f}|')
        firulas.printLinhaSimples()
        print(f'|{listaImpresaoFerias[6]}| Desconto Fixo: R${listaImpresaoFerias[7]:.2f}| Total.: R${listaImpresaoFerias[8]:.2f}|')
        firulas.printLinhaSimples()
        print(f'|Férias Líquido: R${listaImpresaoFerias[12]:.2f}')
        firulas.printLinhaSimples()
        print(f"|Valor Total do Desconto: R${listaImpresaoFerias[9]:.2f} | {listaImpresaoFerias[10]:.2f}%|    Férias Líquido Total: R${listaImpresaoFerias[11]:.2f}|")
        firulas.printLinhaSimples()
        input('\n\033[1;43m Aperte qualquer tecla para voltar ao menu: \033[m')

    elif opcmenu == 3:
        print()
        firulas.printLinhaDupla()
        print('\033[1;46m                             Cálculo do 13° Salário                                \033[m')
        nomeFun = input('Por favor, insira o nome do funcionário: ')
        setor = input('Em qual setor o funcionário trabalha? ')
        salarioBruto = float(input("Insira o valor do salário bruto: R$ "))
        mesesTrabalhados = int(input("Por favor insira o número de meses trabalhados: "))
        dependentes = int(input('Digite a quantidade de Dependentes: '))

        listaImpresaoDecTerceiro = []
        listaImpresaoDecTerceiro = contas.calculoDecimoTerceiLiquido(nomeFun, salarioBruto, dependentes, mesesTrabalhados, setor)
        print(listaImpresaoDecTerceiro)

        print()
        firulas.printLinhaDupla()
        print('\033[1;32m|                                    SUCESSO!                                     |\033[m')
        firulas.printLinhaSimples()
        print(f'|Funcionário: {listaImpresaoDecTerceiro[0]}| N° de Dependentes: {listaImpresaoDecTerceiro[1]}| Setor: {listaImpresaoDecTerceiro[-1]}|')
        firulas.printLinhaSimples()
        print(f'|{listaImpresaoDecTerceiro[2]}| Desconto Fixo: R${abs(listaImpresaoDecTerceiro[3]):.2f}| Total.: R${listaImpresaoDecTerceiro[4]:.2f}|')
        firulas.printLinhaSimples()
        print(f'|{listaImpresaoDecTerceiro[5]}| Desconto Fixo: R${listaImpresaoDecTerceiro[6]:.2f}| Total.: R${listaImpresaoDecTerceiro[7]:.2f}|')
        firulas.printLinhaSimples()
        print(f"Valor do 13° Salário Líquido.: R${listaImpresaoDecTerceiro[-2]:.2f}|")
        firulas.printLinhaDupla()

        input('\n\033[1;43m Aperte qualquer tecla para voltar ao menu: \033[m')
    elif opcmenu == 4:
        print()
    else:
        print("\033[1;33m Valor digitado é inválido!\033[m")
        input('\n\033[1;31m Aperte qualquer tecla para voltar ao menu: \033[m')