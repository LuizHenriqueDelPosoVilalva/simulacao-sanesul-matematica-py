consumo = int(input("digite o valor do consumo no mês: "))
tarifa_fixa = 13.47

def encontrar_posicao(valor, array):
    try:
        posicao = array.index(valor)
        return posicao
    except ValueError:
        return len(array) - 1
      
      
if consumo >= 1:
    array = [0,1,2,3,4,5,6,7,8,9,10]
    resultado1 = encontrar_posicao(consumo, array)
    tarifa_de_esgoto1 = 2.56
    tarifa_agua1 =  5.13
    valor_da_agua1 = resultado1*tarifa_agua1+tarifa_de_esgoto1
    total_a_pagar = valor_da_agua1+ tarifa_fixa


if consumo >= 11:  
    array2 = [10,11,12,13,14,15]
    resultado2 = encontrar_posicao(consumo, array2)
    tarifa_de_esgoto2 = 3.03
    tarifa_agua2 = 6.06
    valor_da_agua2 = resultado2*tarifa_agua2+tarifa_de_esgoto2
    total_a_pagar = valor_da_agua1 + valor_da_agua2+ tarifa_fixa

if consumo >= 16:
    array3 = [15,16,17,18,19,20]
    resultado3 = encontrar_posicao(consumo, array3)
    tarifa_agua3 = 6.99
    tarifa_de_esgoto3 = 3.50
    valor_da_agua3 = resultado3*tarifa_agua3+tarifa_de_esgoto3
    total_a_pagar = valor_da_agua1 + valor_da_agua2 + valor_da_agua3+ tarifa_fixa

if consumo >= 21:
    array4 = [20,21,22,23,24,25]
    resultado4 = encontrar_posicao(consumo, array3)
    tarifa_agua4 = 8.09
    tarifa_de_esgoto4 = 4.05
    valor_da_agua4 = resultado4*tarifa_agua4 + tarifa_de_esgoto4
    total_a_pagar = valor_da_agua1 + valor_da_agua2 + valor_da_agua3 + valor_da_agua4+ tarifa_fixa

if consumo >= 26:
    array5 = [25,26,27,28,29,30]
    resultado5 = encontrar_posicao(consumo, array3)
    tarifa_agua5 = 10.20
    tarifa_de_esgoto5 = 5.10
    valor_da_agua5 = resultado5*tarifa_agua5 + tarifa_de_esgoto5
    total_a_pagar = valor_da_agua1 + valor_da_agua2 + valor_da_agua3 + valor_da_agua4 + valor_da_agua5+ tarifa_fixa

if consumo >= 31:
    array6 = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    resultado6 = encontrar_posicao(consumo, array3)
    tarifa_agua6 = 12.09
    tarifa_de_esgoto6 = 6.05
    valor_da_agua6 = resultado6*tarifa_agua6 + tarifa_de_esgoto6
    total_a_pagar = valor_da_agua1 + valor_da_agua2 + valor_da_agua3 + valor_da_agua4 + valor_da_agua5 + valor_da_agua6+ tarifa_fixa

if consumo > 50:
    tarifa_agua7 = 13.34
    tarifa_de_esgoto7 = 6.67
    valor_da_agua7 = resultado6* + tarifa_de_esgoto7 + tarifa_agua7
    total_a_pagar = valor_da_agua7+ tarifa_fixa

print(f"Valor total a pagar é: R${total_a_pagar:.2f}")