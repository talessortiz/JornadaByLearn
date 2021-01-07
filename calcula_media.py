def calcularMedia(notas):
  qtd = len(notas)
  soma = sum(notas)
  media = soma / qtd
  return media

def verificarAprovacao(media):
  print(f'A média do aluno é:', media)
  if media > 7:
    print('Aluno aprovado!')
  else:
    print('Aluno reprovado!')

notas = [5,8,5,7]
media = calcularMedia(notas)
verificarAprovacao(media)