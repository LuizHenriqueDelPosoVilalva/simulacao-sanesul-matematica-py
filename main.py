consumo = int(input("digite o valor do consumo a o mês: "))

if consumo >= 1 and consumo <= 50:
  def encontrar_posicao1(valor, array):
      try:
          posicao = array.index(valor)
          return posicao
      except ValueError:
          return len(array) - 1
      

  
  def encontrar_posicao2(valor, array):
      try:
          posicao = array.index(valor)
          return posicao
      except ValueError:
          return len(array) - 1
      
  def encontrar_posicao3(valor, array):
      try:
          posicao = array.index(valor)
          return posicao
      except ValueError:
          return len(array) - 1
      
  if consumo >= 1 or consumo <= 10 :
    array = [0,1,2,3,4,5,6,7,8,9,10]
    resultado1 = encontrar_posicao1(consumo, array)
    tarifa_de_esgoto1 = 2.56
    tarifa_agua1 =  5.13
    valor_da_agua1 = resultado1*tarifa_agua1+tarifa_de_esgoto1
    
    

  if consumo >= 11 or consumo <= 15:  
    array2 = [10,11,12,13,14,15]
    resultado2 = encontrar_posicao2(consumo, array2)
    tarifa_de_esgoto2 = 3.03
    tarifa_agua2 = 6.06
    valor_da_agua2 = resultado2*tarifa_agua2+tarifa_de_esgoto2

  if consumo >= 16 or consumo <= 20:
    array3 = [15,16,17,18,19,20]
    resultado3 = encontrar_posicao3(consumo, array3)
    tarifa_agua3 = 6.99
    tarifa_de_esgoto3 = 3.50
    valor_da_agua3 = resultado3*tarifa_agua3+tarifa_de_esgoto3
