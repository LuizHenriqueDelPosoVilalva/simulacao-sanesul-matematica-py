# informações de tarifas nesse site https://agencia.sanesul.ms.gov.br/Content/TARIFAS.pdf : Residencia normal

litros = float(input("Digite a quantidade de litros comsumida de água, com ponto e não virgula: "))

def calculo(m):
    tarifa_fixa = 13.47

    if m >= 1 and m <=10:
        tarifa_da_agua= 5.13
        tarifa_do_esgoto = 2.56
        total_a_pagar = m*(tarifa_da_agua+tarifa_do_esgoto+tarifa_fixa)
    else:
        if m >= 11 and m <= 15:
            tarifa_da_agua = 6.06
            tarifa_do_esgoto = 3.03
            total_a_pagar = m*(tarifa_da_agua+tarifa_do_esgoto+tarifa_fixa)
        else:
            if m >= 16 and m <= 20:
                tarifa_da_agua = 6.99
                tarifa_do_esgoto = 3.50
                total_a_pagar = m*(tarifa_da_agua+tarifa_do_esgoto+tarifa_fixa)
            else:
                if m >= 21 and m <= 25:
                    tarifa_da_agua = 8.09
                    tarifa_do_esgoto = 4.05
                    total_a_pagar = m*(tarifa_da_agua+tarifa_do_esgoto+tarifa_fixa)
                else:
                    if m >= 26 and m <= 30:
                        tarifa_da_agua = 10.20
                        tarifa_do_esgoto = 5.10
                        total_a_pagar = m*(tarifa_da_agua+tarifa_do_esgoto+tarifa_fixa)
                    else:
                        if m >= 31 and m <= 50:
                            tarifa_da_agua = 12.09
                            tarifa_do_esgoto = 6.05
                            total_a_pagar = m*(tarifa_da_agua+tarifa_do_esgoto+tarifa_fixa)
                        else:
                            if m > 50:
                                tarifa_da_agua = 13.34
                                tarifa_do_esgoto = 6.67
                                total_a_pagar = m*(tarifa_da_agua+tarifa_do_esgoto+tarifa_fixa)
                            else:
                                print("Digite um valor maior que 1000 litros")
    
    return total_a_pagar
      
litros_para_metros_cubicos = litros/1000;
resultado = calculo(litros_para_metros_cubicos)
print(f"O valor total a pagar é {resultado:.2f}")