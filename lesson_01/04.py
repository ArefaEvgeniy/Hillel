text = 'sdgh sdfg hlk n,jdngbl  "lkjsdfgklsd"  lkbdgkljsd dgsenlk'
text2 = "sdgh sdfg hlk n,jdngbl  lkjsd'fgklsd  lkbdgkljsd dgsenlk"
text3 = "sdgh sdfg hlk n,jdngbl  \"lkjsd'fgklsd\"  lkbdgkljsd dgsenlk"
text4 = """sdgh sdfg hlk n,jdngbl  "lkjsd'fgklsd"  lkbdgkljsd dgsenlk"""
text5 = """
sdgh sdfg hlk n,
jdngbl  
"lkjsd'fgklsd"  
lkbdgkljsd dgsenlk
"""

print(text)
print(text2)
print(text3)
print(text4)
print(text5)
print(text == text2)
