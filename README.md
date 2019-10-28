# Sucrilhos\_bot

O bot do Sucrilhos. Muitas funções, pouca utilidade.

para rodar, tenha certeza de ter instalado:

- python3
- sqlite3
- screen

Além disso, também serão necessários vários módulos para python3:

- telebot
- json
- requests

TODO: descrever como criar a base de dados no sqlite e rodar o script para criar as tabelas

Depois de tudo isso você precisa setar o token do seu bot. Este token é a identificação do bot,
qualquer um que o tenha pode controlar seu bot, inclusive ler as mensagens que ele recebe.
Por isso, o token não estpa nesse repositório git e, se você quiser rodar este código no
seu computador, terá que conseguir um token para você. O Google é seu amigo.

Com o token em mãos, crie um arquivo keys.py e crie um dicionário, onde a chave será  o nome do
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


Salve e rode o `beta_start.sh` (pode precisar dare permissão (use chmod))
```
./beta_start.sh
```

Vai abrir uma outra screen no seu terminal, rodando o bot. Para sair dela **sem** matar o bold
use Ctrl + a + D. Ctrl + D irá matar o processo.
O screen gera um arquivo de log no mesmo diretório, o `screenlog.0`.De uma olhada lá para saber o que
 aconteceu.
Para saber se o bot está rodando:
```
ps -aux | grep pythpn3
```

Note que estaremos rodando um outro programa por cima que tentará ressubir o bot sempre que ele cair.

Para terminar o processo do Bot: estude sobre Screen ou Kill/Sigterm.

Mais Updates?

Caio Hirakawa 27/10/2019
