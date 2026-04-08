import os;

os.chmod("/tmp/exercicio", 0o755);

# Módulo principal
def main():
  i: int = 1;
  div: float = 0;
  res: float = 1;
  
  n = int(input("Insira o número: "));
  
  while i <= n:
    if i == 1: # print do 1o número da somatória já incluso na variável res
      gravaArquivo(str(1.0));

    div = calcDiv(i);
    res += div;
    i += 1;
    gravaArquivo(str(div));
  
  gravaArquivo("Resultado: " + str(res));

# Calcula e retorna a divisão de 1 pelo fatorial de fat
def calcDiv(fat):
  return 1 / calcFat(fat);

# Calcula o fatorial do parâmetro f
def calcFat(f):
  j: int = 1;
  fat: int = 1;
  
  while j <= f:
    fat = fat * j;
    j += 1;
  
  return fat;

# Função para escrever no arquivo
def gravaArquivo(linha):
  arq: str = "ex36.txt";
  dir: str = "/tmp/exercicio/";
  
  file: str = "";
  enc: str = "";
  tipo: str = "";
  
  if (os.path.exists(dir) and os.path.isdir(dir)):
    file = dir + arq;
    enc = "utf-8";
    tipo = "w";
    
    if (os.path.exists(file)):
      tipo = "a";
    
    with open(file, tipo, encoding=enc) as arquivo:
      arquivo.write(linha + "\n");
  else:
    print("Diretório não existe!");

if __name__ == "__main__":
  main();