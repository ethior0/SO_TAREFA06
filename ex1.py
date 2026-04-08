import os;

os.chmod("/tmp/exercicio", 0o755);

def main():
  num: float = 0;
  maior: int = 0;
  menor: int = 0;
  linha: str = "";
  
  for i in range(100):
    num = int(input(f"Insira um número ({i+1}º): "));

    if i == 0:
      menor = num;
      maior = num;
    
    if num < menor:
      menor = num;
    if num > maior:
      maior = num;
    
    gravaArquivo(str(num));
  
  linha = "Menor: " + str(menor) + " | Maior: " + str(maior);
  gravaArquivo(linha);

def gravaArquivo(linha):
  file: str = "";
  enc: str = "";
  tipo: str = "";
  
  arq: str = "ex38.txt";
  dir: str = "/tmp/exercicio/";
  
  if (os.path.exists(dir) and os.path.isdir(dir)):
    file = dir + arq;
    enc = "utf-8";
    tipo = "w"; # write
    
    if (os.path.isfile(file)):
      tipo = "a"; # append
    
    with open(file, tipo, encoding=enc) as arquivo:
      arquivo.write(linha + "\n");

if __name__ == "__main__":
  main();