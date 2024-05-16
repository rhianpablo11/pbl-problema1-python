#coding utf-8
'''
*******************************************************************************

Autor: Rhian Pablo Araujo Almeida
Componente Curricular: Algoritmos I
Concluido em: 10/04/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

******************************************************************************************
'''






'''LISTA DE TIPO DAS PESSOAS''' 
lista_pf = []
lista_pj = []

'''CONTADORES DOS ITENS PF'''
soma_acucar_pf = 0
soma_arroz_pf = 0
soma_sal_pf = 0
soma_feijao_pf = 0
soma_far_trigo_pf = 0
soma_oleo_pf = 0
soma_bolacha_pf = 0
soma_macarrao_pf = 0
soma_extr_tom_pf = 0
soma_cafe_pf = 0
soma_extra_pf = 0

'''INICIALIZANDO CONTADORES DOS ITENS PJ'''
soma_acucar_pj = 0; soma_arroz_pj = 0; soma_sal_pj = 0; soma_feijao_pj = 0; soma_far_trigo_pj = 0; soma_oleo_pj = 0; soma_bolacha_pj = 0; soma_macarrao_pj = 0; soma_extr_tom_pj = 0; soma_cafe_pj = 0; soma_extra_pj = 0

print("Seja bem-vindo(a) ao sistema de doacoes do Dispensario Santana\n")
menu_main = input("Qual opcao deseja realizar?\n1) Registro de novo doador\n2) Registro de nova doacao\n3) Relatorio parcial\n4) Encerrar o programa")
while menu_main != "1" and menu_main != "2" and menu_main != "3" and menu_main != "4":
        print("opcao invalida, por favor tente novamente")
        menu_main = input("Qual opcao deseja realizar?\n1) Registro de novo doador\n2) Registro de nova doacao\n3) Relatorio\n4) Encerrar o programa")
while menu_main == "1" or menu_main == "2" or menu_main == "3" or menu_main == "4":
    '''REGISTRO DE DOADOR'''
    while menu_main == "1":
        nome_doador = input("Nome completo do doador:").lower()
        while nome_doador == "":
            print("Insira um nome valido")
            nome_doador = input("Nome completo do doador:").lower()
        telefone = input("qual o telefone do doador? \nInserir DDD junto\n")
        while telefone.isdigit() == False:
            print("digite apenas numeros, sem haver espacos ou outros caracteres")
            telefone = input("qual o telefone do doador? \nInserir DDD junto\n")
        pf_pj = input("o doador e pessoa fisica ou pessoa jurica? \nDigite 1 para Pessoa fisica e 2 para pessoa juridica")
        while pf_pj != "1" and pf_pj != "2":
            print("opcao invalida, por favor tente novamente")
            pf_pj = input("o doador e pessoa fisica ou pessoa jurica? \nDigite 1 para Pessoa fisica e 2 para pessoa juridica")
        if pf_pj == "1":
            get_doador_pf = lista_pf.append(nome_doador)
            print("o id desse usuario é:")
            print(lista_pf.index(nome_doador))
        elif pf_pj == "2":
            get_doador_pj = lista_pj.append(nome_doador)
            print("o id desse usuario é:")
            print(lista_pj.index(nome_doador))
        menu_main = input("Qual opcao deseja realizar?\n1) Registro de novo doador\n2) Registro de nova doacao\n3) Relatorio\n4) Encerrar o programa")

    '''REGISTRO DE DOACOES'''
    while menu_main == "2":
        qm_doa = input("Qual o nome do usuario que esta doando?")
        ''' VERIFICACAO DE QUEM ESTA DOANDO '''
        if qm_doa not in lista_pf and qm_doa not in lista_pj:
            print("Usuario nao cadastrado, ou nao encontrado")
            print("Por favor, primeiro acesse o menu para fazer realizar o registro")
        if qm_doa.lower() in lista_pf:
            #BLOCO DOS ALIMENTOS EM QUANTIDADE
            print("escolha qual alimento deseja doar digitando o numero da opcao")
            print("0) outros \n1) açucar \n2) café \n3) óleo \n4) macarrão \n5) farinha de trigo \n6) sal \n7) extrato de tomate \n8) bolacha \n9) arroz \n10) feijao")
            opcao = input("")
            while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6" and opcao != "7" and opcao != "8" and opcao != "9" and opcao != "10":
                print("digite uma opcao valida:")
                opcao = input("")
            if opcao == "0":
                extra_quant = input("qual a quantidade de itens a parte do basico?")
                while extra_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    extra_quant = input("qual a quantidade de itens a parte do basico?")
                if extra_quant.isdigit() == True:
                    soma_extra_pf += int(extra_quant)
            elif opcao == "1":
                acucar_quant = input("qual a quantidade de acucar?")
                while acucar_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    acucar_quant = input("qual a quantidade de acucar?")
                if acucar_quant.isdigit() == True:    
                    soma_acucar_pf += int(acucar_quant)
            elif opcao == "2":
                cafe_quant = input("qual a quantidade de cafe?")
                while cafe_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    cafe_quant = input("qual a quantidade de cafe?")
                if cafe_quant.isdigit() == True:    
                    soma_cafe_pf += int(cafe_quant)
            elif opcao == "3":
                oleo_quant = input("qual a quantidade de oleo?")
                while oleo_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    oleo_quant = input("qual a quantidade de oleo?")
                if oleo_quant.isdigit() == True:    
                    soma_oleo_pf += int(oleo_quant)
            elif opcao == "4":
                mac_quant = input("qual a quantidade de macarrao?")
                while mac_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    mac_quant = input("qual a quantidade de macarrao?")
                if mac_quant.isdigit() == True:
                    soma_macarrao_pf += int(mac_quant)
            elif opcao == "5":
                far_trigo_quant = input("qual a quantidade de farinha de trigo?")
                while far_trigo_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    far_trigo_quant = input("qual a quantidade de farinha de trigo?")
                if far_trigo_quant.isdigit() == True:
                    soma_far_trigo_pf += int(far_trigo_quant)
            elif opcao == "6":
                sal_quant = input("qual a quantidade de sal?")
                while sal_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    sal_quant = input("qual a quantidade de sal?")
                if sal_quant.isdigit() == True:
                    soma_sal_pf += int(sal_quant)
            elif opcao == "7":
                extra_tom_quant = input("qual a quantidade de extrato de tomate?")
                while extra_tom_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    extra_tom_quant = input("qual a quantidade de extrato de tomate?")
                if extra_tom_quant.isdigit() == True:
                    soma_extr_tom_pf += int(extra_tom_quant)
            elif opcao == "8":
                bolacha_quant = input("qual a quantidade de bolacha?")
                while bolacha_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    bolacha_quant = input("qual a quantidade de bolacha?")
                if bolacha_quant.isdigit() == True:
                    soma_bolacha_pf += int(bolacha_quant)
            elif opcao == "9":
                arroz_quant = input("qual a quantidade de arroz?")
                while arroz_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    arroz_quant = input("qual a quantidade de arroz?")
                if arroz_quant.isdigit() == True:
                    soma_arroz_pf += int(arroz_quant)
            elif opcao ==  "10":
                feijao_quant = input("qual a quantidade de feijao?")
                while feijao_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    feijao_quant = input("qual a quantidade de feijao?")
                if feijao_quant.isdigit() == True:
                    soma_feijao_pf += int(feijao_quant)
            nova_doacao = input("Deseja doar algo mais?\ndigite S para sim e N para não")
            while nova_doacao.lower() != "s" and nova_doacao.lower() != "n":
                print("opcao invalida, por favor tente novamente")
                nova_doacao = input("Deseja doar algo mais?\ndigite S para sim e N para não")
            while nova_doacao.lower()[0] == "s":
                opcao = input("escolha a opcao do prox produto")
                while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6" and opcao != "7" and opcao != "8" and opcao != "9" and opcao != "10":
                    print("digite uma opcao valida")
                    opcao = input("")
                if opcao == "0":
                    extra_quant = input("qual a quantidade de itens a parte do basico?")
                    while extra_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        extra_quant = input("qual a quantidade de itens a parte do basico?")
                    if extra_quant.isdigit() == True:
                        soma_extra_pf += int(extra_quant)
                elif opcao == "1":
                    acucar_quant = input("qual a quantidade de acucar?")
                    while acucar_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        acucar_quant = input("qual a quantidade de acucar?")
                    if acucar_quant.isdigit() == True:    
                        soma_acucar_pf += int(acucar_quant)
                elif opcao == "2":
                    cafe_quant = input("qual a quantidade de cafe?")
                    while cafe_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        cafe_quant = input("qual a quantidade de cafe?")
                    if cafe_quant.isdigit() == True:    
                        soma_cafe_pf += int(cafe_quant)
                elif opcao == "3":
                    oleo_quant = input("qual a quantidade de oleo?")
                    while oleo_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        oleo_quant = input("qual a quantidade de oleo?")
                    if oleo_quant.isdigit() == True:    
                        soma_oleo_pf += int(oleo_quant)
                elif opcao == "4":
                    mac_quant = input("qual a quantidade de macarrao?")
                    while mac_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        mac_quant = input("qual a quantidade de macarrao?")
                    if mac_quant.isdigit() == True:
                        soma_macarrao_pf += int(mac_quant)
                elif opcao == "5":
                    far_trigo_quant = input("qual a quantidade de farinha de trigo?")
                    while far_trigo_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        far_trigo_quant = input("qual a quantidade de farinha de trigo?")
                    if far_trigo_quant.isdigit() == True:
                        soma_far_trigo_pf += int(far_trigo_quant)
                elif opcao == "6":
                    sal_quant = input("qual a quantidade de sal?")
                    while sal_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        sal_quant = input("qual a quantidade de sal?")
                    if sal_quant.isdigit() == True:
                        soma_sal_pf += int(sal_quant)
                elif opcao == "7":
                    extra_tom_quant = input("qual a quantidade de extrato de tomate?")
                    while extra_tom_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        extra_tom_quant = input("qual a quantidade de extrato de tomate?")
                    if extra_tom_quant.isdigit() == True:
                        soma_extr_tom_pf += int(extra_tom_quant)
                elif opcao == "8":
                    bolacha_quant = input("qual a quantidade de bolacha?")
                    while bolacha_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        bolacha_quant = input("qual a quantidade de bolacha?")
                    if bolacha_quant.isdigit() == True:
                        soma_bolacha_pf += int(bolacha_quant)
                elif opcao == "9":
                    arroz_quant = input("qual a quantidade de arroz?")
                    while arroz_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        arroz_quant = input("qual a quantidade de arroz?")
                    if arroz_quant.isdigit() == True:
                        soma_arroz_pf += int(arroz_quant)
                elif opcao ==  "10":
                    feijao_quant = input("qual a quantidade de feijao?")
                    while feijao_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        feijao_quant = input("qual a quantidade de feijao?")
                    if feijao_quant.isdigit() == True:
                        soma_feijao_pf += int(feijao_quant)
                nova_doacao = input("Deseja doar algo mais?\ndigite S para sim e N para não")
                while nova_doacao.lower() != "s" and nova_doacao.lower() != "n":
                    print("opcao invalida, por favor tente novamente")
                    nova_doacao = input("Deseja doar algo mais?\ndigite S para sim e N para não")
        elif qm_doa.lower() in lista_pj:
            #BLOCO DOS ALIMENTOS EM QUANTIDADE
            #TROCAR LOCAIS DOS INPUTS
            print("escolha qual alimento deseja doar digitando o numero da opcao")
            print("0) outros \n1) açucar \n2) café \n3) óleo \n4) macarrão \n5) farinha de trigo \n6) sal \n7) extrato de tomate \n8) bolacha \n9) arroz \n10) feijao")
            opcao = input("")
            while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6" and opcao != "7" and opcao != "8" and opcao != "9" and opcao != "10":
                print("digite uma opcao valida:")
                opcao = input("")            
            if opcao == "0":
                extra_quant = input("qual a quantidade de itens a parte do basico?")
                while extra_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    extra_quant = input("qual a quantidade de itens a parte do basico?")
                if extra_quant.isdigit() == True:
                    soma_extra_pj += int(extra_quant)
            elif opcao == "1":
                acucar_quant = input("qual a quantidade de acucar?")
                while acucar_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    acucar_quant = input("qual a quantidade de acucar?")
                if acucar_quant.isdigit() == True:    
                    soma_acucar_pj += int(acucar_quant)
            elif opcao == "2":
                cafe_quant = input("qual a quantidade de cafe?")
                while cafe_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    cafe_quant = input("qual a quantidade de cafe?")
                if cafe_quant.isdigit() == True:    
                    soma_cafe_pj += int(cafe_quant)
            elif opcao == "3":
                oleo_quant = input("qual a quantidade de oleo?")
                while oleo_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    oleo_quant = input("qual a quantidade de oleo?")
                if oleo_quant.isdigit() == True:    
                    soma_oleo_pj += int(oleo_quant)
            elif opcao == "4":
                mac_quant = input("qual a quantidade de macarrao?")
                while mac_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    mac_quant = input("qual a quantidade de macarrao?")
                if mac_quant.isdigit() == True:
                    soma_macarrao_pj += int(mac_quant)
            elif opcao == "5":
                far_trigo_quant = input("qual a quantidade de farinha de trigo?")
                while far_trigo_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    far_trigo_quant = input("qual a quantidade de farinha de trigo?")
                if far_trigo_quant.isdigit() == True:
                    soma_far_trigo_pj += int(far_trigo_quant)
            elif opcao == "6":
                sal_quant = input("qual a quantidade de sal?")
                while sal_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    sal_quant = input("qual a quantidade de sal?")
                if sal_quant.isdigit() == True:
                    soma_sal_pj += int(sal_quant)
            elif opcao == "7":
                extra_tom_quant = input("qual a quantidade de extrato de tomate?")
                while extra_tom_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    extra_tom_quant = input("qual a quantidade de extrato de tomate?")
                if extra_tom_quant.isdigit() == True:
                    soma_extr_tom_pj += int(extra_tom_quant)
            elif opcao == "8":
                bolacha_quant = input("qual a quantidade de bolacha?")
                while bolacha_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    bolacha_quant = input("qual a quantidade de bolacha?")
                if bolacha_quant.isdigit() == True:
                    soma_bolacha_pj += int(bolacha_quant)
            elif opcao == "9":
                arroz_quant = input("qual a quantidade de arroz?")
                while arroz_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    arroz_quant = input("qual a quantidade de arroz?")
                if arroz_quant.isdigit() == True:
                    soma_arroz_pj += int(arroz_quant)
            elif opcao ==  "10":
                feijao_quant = input("qual a quantidade de feijao?")
                while feijao_quant.isdigit()==False:
                    print("digite um numero INTEIRO")
                    feijao_quant = input("qual a quantidade de feijao?")
                if feijao_quant.isdigit() == True:
                    soma_feijao_pj += int(feijao_quant)
            nova_doacao = input("Deseja doar algo mais?\ndigite S para sim e N para não")
            while nova_doacao.lower() != "s" and nova_doacao.lower() != "n":
                print("opcao invalida, por favor tente novamente")
                nova_doacao = input("Deseja doar algo mais?\ndigite S para sim e N para não")
            while nova_doacao.lower()[0] == "s":
                opcao = input("escolha a opção do prox produto")
                while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6" and opcao != "7" and opcao != "8" and opcao != "9" and opcao != "10":
                    print("digite uma opcao valida")
                    opcao = input("")
                if opcao == "0":
                    extra_quant = input("qual a quantidade de itens a parte do basico?")
                    while extra_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        extra_quant = input("qual a quantidade de itens a parte do basico?")
                    if extra_quant.isdigit() == True:
                        soma_extra_pj += int(extra_quant)
                elif opcao == "1":
                    acucar_quant = input("qual a quantidade de acucar?")
                    while acucar_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        acucar_quant = input("qual a quantidade de acucar?")
                    if acucar_quant.isdigit() == True:    
                        soma_acucar_pj += int(acucar_quant)
                elif opcao == "2":
                    cafe_quant = input("qual a quantidade de cafe?")
                    while cafe_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        cafe_quant = input("qual a quantidade de cafe?")
                    if cafe_quant.isdigit() == True:    
                        soma_cafe_pj += int(cafe_quant)
                elif opcao == "3":
                    oleo_quant = input("qual a quantidade de oleo?")
                    while oleo_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        oleo_quant = input("qual a quantidade de oleo?")
                    if oleo_quant.isdigit() == True:    
                        soma_oleo_pj += int(oleo_quant)
                elif opcao == "4":
                    mac_quant = input("qual a quantidade de macarrao?")
                    while mac_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        mac_quant = input("qual a quantidade de macarrao?")
                    if mac_quant.isdigit() == True:
                        soma_macarrao_pj += int(mac_quant)
                elif opcao == "5":
                    far_trigo_quant = input("qual a quantidade de farinha de trigo?")
                    while far_trigo_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        far_trigo_quant = input("qual a quantidade de farinha de trigo?")
                    if far_trigo_quant.isdigit() == True:
                        soma_far_trigo_pj += int(far_trigo_quant)
                elif opcao == "6":
                    sal_quant = input("qual a quantidade de sal?")
                    while sal_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        sal_quant = input("qual a quantidade de sal?")
                    if sal_quant.isdigit() == True:
                        soma_sal_pj += int(sal_quant)
                elif opcao == "7":
                    extra_tom_quant = input("qual a quantidade de extrato de tomate?")
                    while extra_tom_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        extra_tom_quant = input("qual a quantidade de extrato de tomate?")
                    if extra_tom_quant.isdigit() == True:
                        soma_extr_tom_pj += int(extra_tom_quant)
                elif opcao == "8":
                    bolacha_quant = input("qual a quantidade de bolacha?")
                    while bolacha_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        bolacha_quant = input("qual a quantidade de bolacha?")
                    if bolacha_quant.isdigit() == True:
                        soma_bolacha_pj += int(bolacha_quant)
                elif opcao == "9":
                    arroz_quant = input("qual a quantidade de arroz?")
                    while arroz_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        arroz_quant = input("qual a quantidade de arroz?")
                    if arroz_quant.isdigit() == True:
                        soma_arroz_pj += int(arroz_quant)
                elif opcao ==  "10":
                    feijao_quant = input("qual a quantidade de feijao?")
                    while feijao_quant.isdigit()==False:
                        print("digite um numero INTEIRO")
                        feijao_quant = input("qual a quantidade de feijao?")
                    if feijao_quant.isdigit() == True:
                        soma_feijao_pj += int(feijao_quant)
                nova_doacao = input("Deseja doar algo mais?\ndigite S para sim e N para não")
                while nova_doacao.lower() != "s" and nova_doacao.lower() != "n":
                    print("opcao invalida, por favor tente novamente")
                    nova_doacao = input("Deseja doar algo mais?\ndigite S para sim e N para não")
        menu_main = input("Qual opcao deseja realizar?\n1) Registro de novo doador\n2) Registro de nova doacao\n3) Relatorio\n4) Encerrar o programa")

    '''RELATORIO PARCIAL'''
    while menu_main == "3":

        '''SOMADORA DE ITENS TOTAIS'''
        tot_acucar = soma_acucar_pj + soma_acucar_pf
        tot_arroz = soma_arroz_pf + soma_arroz_pj
        tot_cafe = soma_cafe_pj + soma_cafe_pf
        tot_extrato = soma_extr_tom_pf + soma_extr_tom_pj
        tot_sal = soma_sal_pf + soma_sal_pj
        tot_feijao = soma_feijao_pj + soma_feijao_pf
        tot_fartrigo = soma_far_trigo_pf + soma_far_trigo_pj
        tot_oleo = soma_oleo_pf + soma_oleo_pj
        tot_mac = soma_macarrao_pf + soma_macarrao_pj
        tot_bolacha = soma_bolacha_pf + soma_bolacha_pj
        tot_extra = soma_extra_pf + soma_extra_pj
        '''SOMADORA DE ITENS PF E PJ'''
        tot_pf = soma_acucar_pf + soma_arroz_pf + soma_bolacha_pf + soma_cafe_pf + soma_extr_tom_pf + soma_far_trigo_pf + soma_feijao_pf + soma_macarrao_pf + soma_oleo_pf + soma_sal_pf + soma_extra_pf

        tot_pj = soma_acucar_pj + soma_arroz_pj + soma_bolacha_pj + soma_cafe_pj + soma_extr_tom_pj + soma_far_trigo_pj + soma_feijao_pj + soma_macarrao_pj + soma_oleo_pj + soma_sal_pj + soma_extra_pj
        
        '''PRODUCAO DE CESTAS'''
        '''ITENS QUE SOBRARAM É IGUAL A VARIAVEL TOT_NOME DO ITEM, APOS FORMAR AS CESTAS'''
        cestas = 0
        cestas_c_extra = 0
        cestas_s_extra = 0
        for a in range(0, tot_acucar):
            if tot_acucar // 1 and tot_arroz // 4 and tot_cafe // 2 and tot_extrato // 2 and tot_sal // 1 and tot_feijao // 4 and tot_fartrigo // 1 and tot_oleo // 1 and tot_mac // 3 and tot_bolacha // 1:
                tot_acucar -= 1
                tot_arroz -= 4
                tot_cafe -= 2
                tot_extrato -= 2
                tot_sal -= 1
                tot_feijao -= 4
                tot_fartrigo -= 1
                tot_oleo -= 1
                tot_mac -= 3
                tot_bolacha -= 1
                
                cestas += 1

        '''CESTAS BASICAS COM E SEM ITEM EXTRA'''
        if cestas > tot_extra:
            cestas_c_extra = tot_extra
            cestas_s_extra = cestas - tot_extra
            tot_extra = 0
        elif cestas == tot_extra:
            cestas_c_extra = tot_extra
            cestas_s_extra = 0
            tot_extra = 0
        elif cestas < tot_extra:
            cestas_c_extra = cestas
            cestas_s_extra = 0
            tot_extra = tot_extra - cestas
        '''TOTAL DE CADA ITEM'''

        print("Total de itens recebidos:\n")
        print(f"\tacucar: {soma_acucar_pj + soma_acucar_pf} kg")
        print(f"\tarroz: {soma_arroz_pf + soma_arroz_pj} kg")
        print(f"\tcafe: {soma_cafe_pj + soma_cafe_pf} kg")
        print(f"\textrato de tomate: {soma_extr_tom_pf + soma_extr_tom_pj} und")
        print(f"\tmacarrao: {soma_macarrao_pf + soma_macarrao_pj} und")
        print(f"\tbolacha: {soma_bolacha_pf + soma_bolacha_pj} pct")
        print(f"\toleo: {soma_oleo_pf + soma_oleo_pj} l")
        print(f"\tfarinha de trigo: {soma_far_trigo_pf + soma_far_trigo_pj} kg")
        print(f"\tfeijao: {soma_feijao_pj + soma_feijao_pf} kg")
        print(f"\tsal: {soma_sal_pf + soma_sal_pj} kg")
        print(f"\titem extra: {soma_extra_pf + soma_extra_pj} item(ns)\n")

        '''TOTAL DE ITENS DOADOS POR PF E POR PJ'''
        print("Total de itens doados por Pessoas Fisicas e Pessoas Juridicas\n")
        print("\tTotal de itens doados por PF")
        print("\t\t",tot_pf, "\n")
        print("\tTotal de itens doados por PJ")
        print("\t\t",tot_pj)

        '''TOTAL DE CESTAS BASICAS FORMADAS'''
        print("\nTotal de cestas basicas formadas:")
        print("\t",cestas)

        '''CESTAS BASICAS COM ITEM EXTRA'''
        print("\nQuantidade de cestas que receberam um, item extra:")
        print("\t",cestas_c_extra)

        '''CESTAS BASICAS SEM ITEM EXTRA'''
        print("\nQuantidade de cestas basicas sem item extra:")
        print("\t",cestas_s_extra)
        '''ITENS QUE SOBRARAM'''
        print("\nQuantidade de itens que sobraram:\n")
        print(f"\tacucar: {tot_acucar} kg")
        print(f"\tarroz: {tot_arroz} kg")
        print(f"\tcafe: {tot_cafe} kg")
        print(f"\textrato de tomate: {tot_extrato} und")
        print(f"\tmacarrao: {tot_mac} und")
        print(f"\tbolacha: {tot_bolacha} pct")
        print(f"\toleo: {tot_oleo} l")
        print(f"\tfarinha de trigo: {tot_fartrigo} kg")
        print(f"\tfeijao: {tot_feijao} kg")
        print(f"\tsal: {tot_sal} kg")
        print(f"\titem extra: {tot_extra} item(ns)\n\n")
        menu_main = input("Qual opcao deseja realizar?\n1) Registro de novo doador\n2) Registro de nova doacao\n3) Relatorio\n4) Encerrar o programa")
    
    '''VALIDACAO DO MENU'''
    while menu_main != "1" and menu_main != "2" and menu_main != "3" and menu_main != "4":
        print("opcao invalida, por favor tente novamente")
        menu_main = input("Qual opcao deseja realizar?\n1) Registro de novo doador\n2) Registro de nova doacao\n3) Relatorio\n4) Encerrar o programa")
    
    '''ENCERRAMENTO'''
    if menu_main == "4":
        confirmacao = input("deseja mesmo encerrar o programa?\n digite 1 para SIM e 2 para NAO")
        
        if confirmacao == "2":
            menu_main = input("Qual opcao deseja realizar?\n1) Registro de novo doador\n2) Registro de nova doacao\n3) Relatorio\n4) Encerrar o programa")
        elif confirmacao =="1":

            '''SOMADORA DE ITENS TOTAIS'''
            tot_acucar = soma_acucar_pj + soma_acucar_pf
            tot_arroz = soma_arroz_pf + soma_arroz_pj
            tot_cafe = soma_cafe_pj + soma_cafe_pf
            tot_extrato = soma_extr_tom_pf + soma_extr_tom_pj
            tot_sal = soma_sal_pf + soma_sal_pj
            tot_feijao = soma_feijao_pj + soma_feijao_pf
            tot_fartrigo = soma_far_trigo_pf + soma_far_trigo_pj
            tot_oleo = soma_oleo_pf + soma_oleo_pj
            tot_mac = soma_macarrao_pf + soma_macarrao_pj
            tot_bolacha = soma_bolacha_pf + soma_bolacha_pj
            tot_extra = soma_extra_pf + soma_extra_pj
            '''SOMADORA DE ITENS PF E PJ'''
            tot_pf = soma_acucar_pf + soma_arroz_pf + soma_bolacha_pf + soma_cafe_pf + soma_extr_tom_pf + soma_far_trigo_pf + soma_feijao_pf + soma_macarrao_pf + soma_oleo_pf + soma_sal_pf + soma_extra_pf

            tot_pj = soma_acucar_pj + soma_arroz_pj + soma_bolacha_pj + soma_cafe_pj + soma_extr_tom_pj + soma_far_trigo_pj + soma_feijao_pj + soma_macarrao_pj + soma_oleo_pj + soma_sal_pj + soma_extra_pj
            
            '''PRODUCAO DE CESTAS'''
            '''ITENS QUE SOBRARAM É IGUAL A VARIAVEL TOT_NOME DO ITEM, APOS FORMAR AS CESTAS'''
            cestas = 0
            cestas_c_extra = 0
            cestas_s_extra = 0
            for a in range(0, tot_acucar):
                if tot_acucar // 1 and tot_arroz // 4 and tot_cafe // 2 and tot_extrato // 2 and tot_sal // 1 and tot_feijao // 4 and tot_fartrigo // 1 and tot_oleo // 1 and tot_mac // 3 and tot_bolacha // 1:
                    tot_acucar -= 1
                    tot_arroz -= 4
                    tot_cafe -= 2
                    tot_extrato -= 2
                    tot_sal -= 1
                    tot_feijao -= 4
                    tot_fartrigo -= 1
                    tot_oleo -= 1
                    tot_mac -= 3
                    tot_bolacha -= 1
                    
                    cestas += 1

            '''CESTAS BASICAS COM E SEM ITEM EXTRA'''
            if cestas > tot_extra:
                cestas_c_extra = tot_extra
                cestas_s_extra = cestas - tot_extra
                tot_extra = 0
            elif cestas == tot_extra:
                cestas_c_extra = tot_extra
                cestas_s_extra = 0
                tot_extra = 0
            elif cestas < tot_extra:
                cestas_c_extra = cestas
                cestas_s_extra = 0
                tot_extra = tot_extra - cestas
            '''TOTAL DE CADA ITEM'''

            print("Total de itens recebidos:\n")
            print(f"\tacucar: {soma_acucar_pj + soma_acucar_pf} kg")
            print(f"\tarroz: {soma_arroz_pf + soma_arroz_pj} kg")
            print(f"\tcafe: {soma_cafe_pj + soma_cafe_pf} kg")
            print(f"\textrato de tomate: {soma_extr_tom_pf + soma_extr_tom_pj} und")
            print(f"\tmacarrao: {soma_macarrao_pf + soma_macarrao_pj} und")
            print(f"\tbolacha: {soma_bolacha_pf + soma_bolacha_pj} pct")
            print(f"\toleo: {soma_oleo_pf + soma_oleo_pj} l")
            print(f"\tfarinha de trigo: {soma_far_trigo_pf + soma_far_trigo_pj} kg")
            print(f"\tfeijao: {soma_feijao_pj + soma_feijao_pf} kg")
            print(f"\tsal: {soma_sal_pf + soma_sal_pj} kg")
            print(f"\titem extra: {soma_extra_pf + soma_extra_pj} item(ns)\n")

            '''TOTAL DE ITENS DOADOS POR PF E POR PJ'''
            print("Total de itens doados por Pessoas Fisicas e Pessoas Juridicas\n")
            print("\tTotal de itens doados por PF")
            print("\t\t",tot_pf, "\n")
            print("\tTotal de itens doados por PJ")
            print("\t\t",tot_pj)

            '''TOTAL DE CESTAS BASICAS FORMADAS'''
            print("\nTotal de cestas basicas formadas:")
            print("\t",cestas)

            '''CESTAS BASICAS COM ITEM EXTRA'''
            print("\nQuantidade de cestas que receberam um, item extra:")
            print("\t",cestas_c_extra)

            '''CESTAS BASICAS SEM ITEM EXTRA'''
            print("\nQuantidade de cestas basicas sem item extra:")
            print("\t",cestas_s_extra)
            '''ITENS QUE SOBRARAM'''
            print("\nQuantidade de itens que sobraram:\n")
            print(f"\tacucar: {tot_acucar} kg")
            print(f"\tarroz: {tot_arroz} kg")
            print(f"\tcafe: {tot_cafe} kg")
            print(f"\textrato de tomate: {tot_extrato} und")
            print(f"\tmacarrao: {tot_mac} und")
            print(f"\tbolacha: {tot_bolacha} pct")
            print(f"\toleo: {tot_oleo} l")
            print(f"\tfarinha de trigo: {tot_fartrigo} kg")
            print(f"\tfeijao: {tot_feijao} kg")
            print(f"\tsal: {tot_sal} kg")
            print(f"\titem extra: {tot_extra} item(ns)\n\n")

            '''MENSAGEM DE ENCERRAMENTO'''
            print("Programa encerrado!")
            menu_main = 5
            
    
    
    
