# import sentencepiece as spm
 
# # 加载模型
# sp = spm.SentencePieceProcessor(model_file='content/TinyLLM/data/tok4096.model')
 
# # 文本编码
# encoded_text = sp.encode('This is a test txt')
# print("Encoded:", encoded_text)
 
# # 解码回原文
# decoded_text = sp.decode(encoded_text)
# print("Decoded:", decoded_text)














import sentencepiece as spm

sp = spm.SentencePieceProcessor(model_file="content/TinyLLM/data/tok4096.model")

test_txt="hello, this is a test text."
encoded_text = sp.encode(test_txt)
print("encode:", encoded_text)

decoded_text = sp.decode(encoded_text)
print("decode:", decoded_text)
