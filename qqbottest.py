from qqbot import _bot as bot


bot.Login(['-q', '3391775316'])

bot.Update('buddy')

g = bot.List('buddy', 'imp')    # 直接输入qq号不行
g = g[0]
print([g, type(g), g.qq, g.name, g.uin, g.mark])
bot.SendTo(g, 'hello')
