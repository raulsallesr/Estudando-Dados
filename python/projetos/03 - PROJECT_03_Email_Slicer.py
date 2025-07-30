# criando o sistema

# 1. Perguntar ao usuario seu email
# 2. Cortar o email c/ o username e o dominio de email
# 3. Username é antes do @ e o email dps e antes do .
# 4. tentar fazer sozinho hehe


email = input("Olá, qual seu e-mail? ").strip()

username = (email[:email.index("@")])
dominio_email = (email[email.index("@") + 1 :email.index(".")])
print(f"Seu usuário é {username} e seu domínio de e-mail é o {dominio_email}")



#uhuullll - solo de boas
# esqueci de colocar o .strip no final do input
# Ensinou a colocar o +1 dps do dominio do email, p nao pegar o @