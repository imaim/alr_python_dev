"""
bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio
"""
import re


url = "https://www.bytebank.com.br/cambio"
padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao_url.match(url)

if not match:
    raise ValueError("A url não é valida")

print("A url é valida")
