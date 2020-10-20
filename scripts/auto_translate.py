from googletrans import Translator
translator = Translator()

enUS_path = "en_US.lang"
destinations = ["us","gb","de","es","mx"]
rawTranslations = []

for line in open(enUS_path):
    lineToRemove = ""
    for c in line:
        lineToRemove += c
        if c == "=":
            break
    rawTranslations.append(line.strip(lineToRemove))

for i in range(0, len(destinations)):
    try:
        translations = translator.translate(rawTranslations, dest=destinations[i])
    except ValueError:
        print(destinations[i], "is a invalid lang code for google translate")

    for translation in translations:
        print(translation.text)
