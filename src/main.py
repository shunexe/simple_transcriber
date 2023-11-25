import whisper
# model = whisper.load_model("base")
model = whisper.load_model("small")
result = model.transcribe("./audio/test.m4a",fp16=False)
print(result["text"])

f = open('output.txt', 'w')

f.write(result["text"])

f.close()
