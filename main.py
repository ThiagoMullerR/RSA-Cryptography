import rsa
from tkinter import filedialog

def gera_chaves():
    public_key, private_key = rsa.newkeys(1024)

    with open("chave_publica.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("chave_privada.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

def ler_chave_publica():
    print("Selecione a chave pública")
    chave_publica = filedialog.askopenfilename(title="Chave Pública")
    print("Lendo chave publica...")
    with open(chave_publica, "rb") as f:
        return rsa.PublicKey.load_pkcs1(f.read())

def ler_chave_privada():
    print("Selecione a chave privada")
    chave_privada = filedialog.askopenfilename(title="Chave Privada")
    print("Lendo chave privada...")
    with open(chave_privada, "rb") as f:
        return rsa.PrivateKey.load_pkcs1(f.read())

print("\n-- Bem-vindo(a) à criptografia RSA --\n")

gera_chave = input("Deseja gerar chaves? (s/n) ")
if gera_chave == 's':
    gera_chaves()

crip_ou_descrp = input("Deseja criptografar uma mensagem (1) ou descriptografar (0)? ")

if crip_ou_descrp == '1':
    mensagem = input("Digite uma mensagem: ")
    chave_publica = ler_chave_publica()
    mensagem_encript = rsa.encrypt(mensagem.encode(), chave_publica)
    print("Mensagem criptografada:")
    print(mensagem_encript)
    descrip = input("Deseja descriptografá-la? (s/n) ")
    if descrip == 'n':
        exit()

else:
    mensagem_encript = input("Informe a mensagem criptografada: ")
    mensagem_encript = eval(mensagem_encript)


chave_privada = ler_chave_privada()
msg_descript = rsa.decrypt(mensagem_encript, chave_privada)

print("\nMensagem descriptografada:")
print(msg_descript.decode())