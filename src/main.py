import whisper
# model = whisper.load_model("base")
model = whisper.load_model("small")
result = model.transcribe("./audio/input.m4a",fp16=False)
print(result["text"])

f = open('./transcription/output.txt', 'w')

f.write(result["text"])

f.close()
