import os;

arq: str = "ex38.txt";
dir: str = "/tmp/exercicio/";

os.chmod("/tmp/exercicio", 0o755);

def main():
  leArquivo();

def leArquivo():
  global arq;
  global dir;

  if (os.path.exists(dir) and os.path.isdir(dir)):
    file: str = dir + arq;

    if (os.path.isfile(file)):
      with open(file) as arquivo:
        for linha in arquivo:
          if not("Menor" in linha) or not("Maior" in linha):
            num: int = int(linha);

            if num % 5 == 0:
              gravaArquivo(str(num));
    else:
      print("Arquivo não existe!");
  
  else:
    print("Diretório não existe!");

def gravaArquivo(n):
  global dir
  arq: str = "ex38_2.txt";

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
      arquivo.write(n + "\n");
  else:
    print("Diretório não existe!");

if __name__ == "__main__":
  main();