def check(cmd):
    if 'read' in cmd:
        return(1)
    elif 'log out' in cmd:
        return(1)
    elif 'reload' in cmd:
        return(1)
    elif 'compose' in cmd:
        return(1)
    elif 'address' in cmd:
        return(1)
    elif 'subject' in cmd:
        return(1)
    elif 'message' in cmd:
        return(1)
    elif 'send' in cmd:
        return(1)
    elif 'attach' in cmd:
        return(1)
    elif 'inbox' in cmd:
        return(1)
    elif 'sent mails' in cmd:
        return(1)
    elif 'delete' in cmd:
        return(1)
    elif 'search' in cmd:
        return(1)
    elif 'open' in cmd:
        return(1)
    elif 'discard draft' in cmd:
        return(1)
    elif 'aap' in cmd:
        return(1)
    elif 'down' in cmd:
        return(1)
    elif 'open' in cmd:
        return(1)
    elif 'go back' in cmd:
        return(1)
    elif 'new' in cmd:
        return(1)
    elif 'close' in cmd:
        return(1)
    else:
        return(0)
    
