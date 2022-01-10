from datetime import datetime
import instaloader

L = instaloader.Instaloader()
L.login('**Seu Usuario**', '**Sua Senha**')

posts = instaloader.Profile.from_username(L.context, "Perfil da pagina").get_posts()

SINCE = datetime(2022, 1, 1) 
UNTIL = datetime(2022, 2, 1)

for post in posts:
    if(post.date >= SINCE) and (post.date <= UNTIL):
        print(post.date)
        L.download_post(post, "Download Concluido") #Cria a Pasta onde vai esta os Arquivos Baixados
