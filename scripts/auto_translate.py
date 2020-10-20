from googletrans import Translator

enUS_path = "en_US.lang"

for line in open(enUS_path, "R"):
    print(line)
    
translator = Translator()
print(translator.translate("Hei verden!", dest='sw'))
