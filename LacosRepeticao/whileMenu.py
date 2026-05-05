Confirmar = "S"
contaTotal = 0
Pagar = "S"
while Pagar != "P":
    if contaTotal > 0:
                      Pagar = input("Digite P se deseja pagar ").upper()
                      if Pagar =="P":
                       print(f"\n Total a pagar:{contaTotal}")
                       ConfirmarCompra = input( "Digite C para confirmar a compra: ").upper()
    print("MENU: \n 1.Lanche\n 2.Bebida\n 3.Sobremesa\n 4.Sair")
   


    Menu = int(input("Escolha um numero do menu:"))
  
    match Menu:
        case 1:
            print("\nLanches:\n 1.X-vida - 11.00$\n 2.Dogão - 9.00$")
            MenuLanche = int(input("\nEscolha um numero do menu lanches:"))
            match MenuLanche:
                case 1:
                    Quantidade = int(input(f"Quantidade a ser pedida: "))
                    Confirmar =  str(input(f" Selecionado: {Quantidade} itens\n Preço total: {Quantidade*11}$\n Digite S para confirmar a compra: ").upper())
                    if Confirmar != "S":
                     print("Compra cancelada")
                    else:
                     print(f" {Quantidade} X-vida adicionados")
                     contaTotal += Quantidade*11
                        

                case 2:
                    Quantidade = int(input(f"Quantidade a ser pedida: "))
                    Confirmar = str(input(
                        f" Selecionado: {Quantidade} itens\n Preço total: {Quantidade * 9}$\n Digite S para confirmar a compra: ").upper())
                    if Confirmar != "S":
                        print(" Compra cancelada")
                    else:
                     print(f" {Quantidade} Dogão adicionados")
                     contaTotal += Quantidade*9
                    
                   

        case 2:
            print("\nBebidas:\n 1.Suco de abacaxi - 8.00$\n 2.Refrigerante - 7.00$")
            MenuBebida = int(input("\nEscolha um numero do menu bebidas:"))
            match MenuBebida:
                case 1:
                    Quantidade = int(input(f"Quantidade a ser pedida: "))
                    Confirmar = str(input(
                        f" Selecionado: {Quantidade} itens\n Preço total: {Quantidade * 8}$\n Digite S para confirmar a compra: ").upper())
                    if Confirmar != "S":
                         print(" Compra cancelada")
                    else:
                     print(f"{Quantidade} Suco de abacaxi adicionados")
                     contaTotal += Quantidade*8
                    
                   

                case 2:
                    Quantidade = int(input(f"Quantidade a ser pedida: "))
                    Confirmar= str(input(
                        f" Selecionado: {Quantidade} itens\n Preço total: {Quantidade * 7}$\n Digite S para confirmar a compra: ").upper())
                    if Confirmar != "S":
                         print(" Compra cancelada")
                    else:
                     print(f"{Quantidade} Refrigerante adicionados")
                     contaTotal += Quantidade*7
                    
                    
        case 3:
            print("\nSobremesas:\n 1.Sorvete de chocolate - 7.00$\n 2.Pudim - 6.00$")
            MenuSobremesa = int(input("\nEscolha um numero do menu sobremesas:"))
            match MenuSobremesa:
                case 1:
                    Quantidade = int(input(f"Quantidade a ser pedida: "))
                    Confirmar = str(input(
                        f" Selecionado: {Quantidade} itens\n Preço total: {Quantidade * 7}$\n Digite S para confirmar a compra: ").upper())
                    if Confirmar != "S":
                         print(" Compra cancelada")
                    else:
                     print(f"{Quantidade} Sorvete de chocolate adicionados")
                     contaTotal += Quantidade*7
                    
                    

                case 2:
                    Quantidade = int(input(f"Quantidade a ser pedida: "))
                    Confirmar = str(input(
                        f" Selecionado: {Quantidade} itens\n Preço total: {Quantidade * 6}$\n Digite S para confirmar a compra: ").upper())
                    if Confirmar != "S":
                         print(" Compra cancelada")
                    else:
                     print(f"{Quantidade} Pudim adicionados")
                     contaTotal += Quantidade*6
                    
              
        case 4:
            print("Obrigado pela visita!")
        case _:
            print("\nOpção inválida")