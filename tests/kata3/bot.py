


def start(update, context):
    #update.message.reply_text('Hola, Geeks!')    
    return 'Hola, Geeks!'

def help(update, context):
    #update.message.reply_text('Ayudame!')    
    return 'Ayudame!'

def mayus(update, context):
    #update.message.reply_text(context.args[0].upper())    
    return context.args[0].upper()

def alreves(update, context):
    #update.message.reply_text(context.args[0][::-1])
    return update.message.text[::-1]


