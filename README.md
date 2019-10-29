# Sucrilhos\_bot

O bot do Sucrilhos. Muitas funções, pouca utilidade. AGORA DOCKERIZADO

para rodar, tenha certeza de ter instalado:

- docker
- docker-compose

Além disso, não é necessário mais nada :) Vamos instalar tudo o que for necessário
direto no container!

Para buildar o container:
```
docker-compose build
```
Para saber o que esse comando faz, leia o arquivo `Dockerfile`.

Antes de subir o container, entretanto, é necessário setar o token do bot. Este token é a identificação do bot,qualquer um que o tenha pode controlar seu bot, inclusive ler as mensagens que ele recebe.
Por isso, o token não estpa nesse repositório git e, se você quiser rodar este código no
seu computador, terá que conseguir um token para você. O Google é seu amigo.

Com o token em mãos, crie um arquivo ./src/keys.py e crie um dicionário, onde a chave será  o nome do
bot e o valor será o token. ex:
```
keys = {}
keys['nome_do_bot'] = '461489414:AAgfrdomgfdmp156rge1g6r156dsf'
```

Não se esqueça de não publicar este arquivo, proteja seu token!

Depois, procure o arquivo beta-sucribot.py. Há uma linha onde ele seta o token do bot,
algo parecido com 
```
bot = telebot.TeleBot(keys.keys['sucrilhos_bot'])
```

Troque `sucrilhos_bot` pelo nome do bot em `keys`


Salve e vamos subir com container com
```
./docker-compose up
```
Por algum bug na imagem alpine que usamos, vai ficar parado com um output
```
Creating sucrilhos_bot ... done
Attaching to sucrilhos_bot
```
Isso significa que deu certo, seu bot já deve estar no ar. Abra seu Telegram e
mande um `/start` para ele.

Para entrar no container e ver como estão as coisas com os próprios olhos:
abra outro terminal e digite
```
docker exec -it sucrilho_bot sh
```

(note que isso irá abrir a shell do alpine, que é bem mais simples que o bash. Vim 
não está disponível, porém Vi sim)

TODO: 
- Separar bancos para chats diferentes?
- Alguma maneira de descer e subir o bot sem ter que descer e subir o container
- Verificar alguma outra biblioteca para que o bot mande mensagens com triggers de horário
- Melhorar a interface para criar objetos compostos como `event`. Provavelmente seria melhor 
fazer uma máquina de estados que permitisse o usuário digitar campos diferentes (nome, data, local, descrição)
 em mensagens diferentes.
 
Caio Hirakawa 29/10/2019
