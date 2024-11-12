from machine import deepsleep
with open('/bin/shell.py') as shell:
    exec(shell.read())
deepsleep()