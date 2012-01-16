"""
Talker-style communication and commands
"""

@listen('input')
def input_command(e):
    e.stop()

    if e.input.startswith("'"):
        cmd = 'say'
        input = e.input[1:]
    elif e.input.startswith(';'):
        cmd = 'emote'
        input = e.input[1:]
    elif ' ' in e.input:
        (cmd, input) = e.input.split(' ', 1)
    else:
        cmd = e.input
        input = ''
    
    # Find and run command
    if not commands.has_key(cmd):
        write(e.user, 'That command was not recognised')
        return
    
    e.input = input
    commands[cmd](e)

