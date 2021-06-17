from twitchio.ext import commands
# Fiz esse repositório pois não achei conteúdo sobre twitchio em português, e foi dificil eu enteder o conteúdo gringo para dar os primeiros passos
# Bom, vamos lá...
# Crie uma conta para seu bot e ative a verificação de duas etapas
# Você pode usar a sua também, mas recomendo criar uma separada
# Com a conta do bot, pegue o token em https://twitchapps.com/tmi/
# Cuidado, o token muda sempre que você pega ele de novo, o meu estava invalido, só peguei outro e funcionou
# Crie uma aplicação em https://dev.twitch.tv/console/apps/create
# "oauth" é o token que você pegou, mas a twitch mudou algumas coisas então bote https://localhost
# Na "categoria" coloque Chat Bot
# Para criar uma aplicação você precisa ter a verificação de duas etapas
# Agora, segue o código
token = "oauth:TOKEN AQUI"
clientid= "CLIENT ID AQUI"
bot = commands.Bot(
    irc_token=token,
    client_id=clientid,
    nick='seunick',
    prefix='!', #prefixo (exemplo: !teste)
    initial_channels=['canal'], # canais para entrar, pode ser mais de um
)

@bot.command(name='teste', aliases=['t']) #name= nome do comando, aliases: apelidos, a função sera chamada pelo nome e os apelidos. aliases não é obrigatorio nos parâmetros 
async def funcao_teste(ctx): # o nome da função pode ser qualquer um
    await ctx.send(f'Teste passado! Parabéns {ctx.author.name}') #envia a mensagem, o bot só pode enviar mensagens de 30-35 segundos, eu realmente não sei o motivo, esse time só se aplica ao envio de mensagens pelo o que eu testei. Não sei como corrigir.

if __name__ == "__main__": # esse "if" é para rodar o bot quando o código estiver pronto para ser executado
    print("Rodando...")
    bot.run() # roda o bot
    
# Se der essa exceção: asyncio.exceptions.timeouterror: request to join the channel has timed out. make sure the channel exists.
# É só entrar em https://twitchapps.com/tmi/ e pegar o novo token, provavelmente vai dar certo.
