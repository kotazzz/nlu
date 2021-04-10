
import lzma
s = '''
import lzma
s = 'Hello world!'

lzc = lzma.LZMACompressor()
cs = lzc.compress(s.encode())

print(f'{s} - {len(s)}')
print(f'{cs} - {len(cs)}')
'''

lzc = lzma.LZMACompressor()
cs = lzc.compress(s.encode())

print(f'{s} - {len(s)}')
print(f'{cs} - {len(cs)}')