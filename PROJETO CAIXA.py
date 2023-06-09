senha_c = "2987"
tentativas = 3
brk = 1

while tentativas >= 0:
    senha = input("Digite a senha para abrir o caixa: ")
    if senha == senha_c:
        print("Caixa aberto!")
        break
    else:
        tentativas -= 1
        if tentativas == 2:
            print("SENHA INCORRETA,\nVocê tem direito a mais DUAS tentativas....\n");
            tentativas -= 1
        else:
            if tentativas == 0:
                print("SENHA INCORRETA,\nVocê tem direito a mais UMA tentativa....\n")
            else:
                brk -= 1
                print("SENHA INCORRETA,\nSistema tem que ser reinicializado!!!!!\n")

troco_disp = 1280

notas_200 = 2
notas_100 = 4
notas_50 = 6
notas_10 = 10
notas_5 = 10
moedas_1 = 20
moedas_0_5 = 20

fechamento_caixa = 0
fechamento_vendas = 0

confirmacao = 0

while True:
    if brk == 0:
        break
            
    print()            
    valor_venda = 1
    quantidade_vendas = 0
    total_vendido = 0
    num_item = 1

    while valor_venda != 0:
      valor_venda = input(f"Digite o valor do item {num_item} (0 para finalizar, -1 para corrigir): ")
      if valor_venda == "-1":
          if quantidade_vendas > 0:
                total_vendido -= ultima_venda
                quantidade_vendas -= 1
                ultima_venda = 0
                num_item -= 1
                print("\nÚltimo item removido.\n")
          else:
                print("Não há itens a serem removidos.")
      else:
          valor_venda = float(valor_venda)
          if valor_venda != 0:
              quantidade_vendas += 1
              total_vendido += valor_venda
              ultima_venda = valor_venda
              num_item += 1

      if valor_venda == 0:
        confirmacao = int(input("\nDeseja realmente finalizar? (1 - Sim / 2 - Não): "))
        fechamento_caixa = fechamento_caixa + quantidade_vendas
        fechamento_vendas = fechamento_vendas + total_vendido
        if confirmacao == 1:
          print("Fim da compra")
          break
        else:
          confirmacao = confirmacao + 2

    if confirmacao > 1:
      print("COMPRA CANCELADA, REINICIE O SISTEMA!")
      break


    print("\n\t**************************************")
    print("\t********* RELATÓRIO DE VENDA *********")
    print("\t**************************************")
    print(f"\t    Venda finalizada com {num_item-1} itens.   ")
    print("\t    Número total de vendas: {}       " .format(quantidade_vendas))
    print("\t    Valor total vendido: R${}     " .format(total_vendido))
    print("\t**************************************")
    print()


    while True:
        valor_pago = float(input("Digite o valor pago pelo cliente: \n"))
        troco = valor_pago - total_vendido
        a = troco_disp - troco
        troco = valor_pago - total_vendido
        if troco > troco_disp:
            print("Valor pago excede o troco disponível. Caixa fechando.")
            break
        else:
            a = troco_disp - troco
            if a <= 0:
                print("Limite máximo de troco alcançado. Caixa fechado.")
                break

        while troco > 0:
          print("\nTroco a ser devolvido: R$", "{:.2f}".format(troco))

          qtd_ced = troco // 200
          if qtd_ced >= 1:
            if notas_200 < qtd_ced:
              qtd_ced = notas_200
            notas200 = min(int(qtd_ced), notas_200)
            print("Notas de R$ 200:", notas200)
            troco -= notas200 * 200
            notas_200 -= notas200

          qtd_ced = troco // 100
          if qtd_ced >= 1:
            if notas_100 < qtd_ced:
              qtd_ced = notas_100
            notas100 = min(int(qtd_ced), notas_100)
            print("Notas de R$ 100:", notas100)
            troco -= notas100 * 100
            notas_100 -= notas100

          qtd_ced = troco // 50
          if qtd_ced >= 1:
            if notas_50 < qtd_ced:
              qtd_ced = notas_50
            notas50 = min(int(troco // 50), notas_50)
            print("Notas de R$ 50:", notas50)
            troco -= notas50 * 50
            notas_50 -= notas50

          qtd_ced = troco // 10
          if qtd_ced >= 1:
            if notas_10 < qtd_ced:
              qtd_ced = notas_10
            notas10 = min(int(troco // 10), notas_10)
            print("Notas de R$ 10:", notas10)
            troco -= notas10 * 10
            notas_10 -= notas10

          qtd_ced = troco // 5
          if qtd_ced >= 1:
            if notas_5 < qtd_ced:
              qtd_ced = notas_5
            notas5 = min(int(troco // 5), notas_5)
            print("Notas de R$ 5:", notas5)
            troco -= notas5 * 5
            notas_5 -= notas5

          qtd_ced = troco // 1
          if qtd_ced >= 1:
            if moedas_1 < qtd_ced:
              qtd_ced = moedas_1
            moedas1 = min(int(troco // 1), moedas_1)
            print("Moedas de R$ 1:", moedas1)
            moedas_1 -= moedas1

          qtd_ced = troco // 0.5
          if qtd_ced >= 1:
            if moedas_0_5 < qtd_ced:
              qtd_ced = moedas_0_5
            moedas_0_5_troco = min(int((troco % 1) / 0.5), moedas_0_5)
            print("Moedas de R$ 0.5:", moedas_0_5_troco)
            moedas_0_5 -= moedas_0_5_troco * 0.5

          while True:
              fechar_caixa = int(input("\nDeseja fechar o caixa? (1 - Sim / 2 - Não) "))
              if fechar_caixa == 1:
                break
              else:
                break

          if fechar_caixa == 1:
            break
        break

    if fechar_caixa == 1:
      print("\n\t**************************************")
      print(f"\t*********** CAIXA FECHADO ************")
      print("\t**************************************")
      print("\t    NÚMERO TOTAL DE VENDAS: {}       " .format(fechamento_caixa))
      print("\t    VALOR TOTAL VENDIDO R${:.2f}     " .format(fechamento_vendas))
      print("\t**************************************")
      print()
      break

          
    
                                                          
    

    

