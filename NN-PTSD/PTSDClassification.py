import whisper
import re

architecture = whisper.load_model("small")
result = architecture.transcribe("in/stories/story4/client/client2.mp3")

sentences = re.split('[.!?]', result["text"])
countOfSentences = len(sentences)
parameters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(countOfSentences):
    currentSentence = sentences[i]
    currentSentence = currentSentence.lower()

    if (currentSentence.find("головная боль") >= 0) | (currentSentence.find("головные боли") >= 0) | (currentSentence.find("болит голова") >= 0) | (currentSentence.find("боль в голове") >= 0):
        parameters[1] = 1
    if (currentSentence.find("нервозность") >= 0) | (currentSentence.find("проблемы с нервами") >= 0) | (currentSentence.find("истерика") >= 0) | (currentSentence.find("раздражённость") >= 0):
        parameters[2] = 1
    if (currentSentence.find("набор мыслей") >= 0) | (currentSentence.find("каша в голове") >= 0) | (currentSentence.find("повторяющиеся мысли") >= 0) | (currentSentence.find("теже самые мысли") >= 0):
        parameters[3] = 1
    if (currentSentence.find("головокружение") >= 0) | (currentSentence.find("голова кружится") >= 0) | (currentSentence.find("в глазах двоится") >= 0) | (currentSentence.find("кружащаяся голова") >= 0) | (currentSentence.find("слабость") >= 0):
        parameters[4] = 1
    if (currentSentence.find("не встаёт") >= 0) | (currentSentence.find("не поднимается") >= 0) | (currentSentence.find("секса не хочется") >= 0) | (currentSentence.find("потеря сексуального влечения") >= 0):
        parameters[5] = 1
    if (currentSentence.find("я грубый") >= 0) | (currentSentence.find("я недоволен") >= 0) | (currentSentence.find("выражаю своё недовольство") >= 0) | (currentSentence.find("я зол") >= 0):
        parameters[6] = 1
    if (currentSentence.find("мысли управляемы") >= 0) | (currentSentence.find("управление мыслью") >= 0) | (currentSentence.find("мысли контролируются") >= 0) | (currentSentence.find("подбрасывает мысли") >= 0):
        parameters[7] = 1
    if (currentSentence.find("они виноваты") >= 0) | (currentSentence.find("они провинились") >= 0) | (currentSentence.find("нехорошие люди") >= 0) | (currentSentence.find("непиятности от людей") >= 0):
        parameters[8] = 1
    if (currentSentence.find("забываю") >= 0) | (currentSentence.find("забыл") >= 0) | (currentSentence.find("не помню") >= 0) | (currentSentence.find("проблемы с памятью") >= 0) | (currentSentence.find("память дырявая") >= 0):
        parameters[9] = 1
    if (currentSentence.find("я неряха") >= 0) | (currentSentence.find("я неряшливый") >= 0) | (currentSentence.find("я небрежный") >= 0) | (currentSentence.find("внимание рассеянно") >= 0):
        parameters[10] = 1
    if (currentSentence.find("я раздражительный") >= 0) | (currentSentence.find("обидно") >= 0) | (currentSentence.find("досадно") >= 0) | (currentSentence.find("жаль") >= 0):
        parameters[11] = 1
    if (currentSentence.find("болит сердце") >= 0) | (currentSentence.find("болит грудь") >= 0) | (currentSentence.find("болит грудная клетка") >= 0) | (currentSentence.find("сердце ноет") >= 0):
        parameters[12] = 1
    if (currentSentence.find("голоса") >= 0) | (currentSentence.find("я один слышу") >= 0) | (currentSentence.find("послышалось") >= 0) | (currentSentence.find("откуда звук") >= 0):
        parameters[16] = 1
    if (currentSentence.find("я никому не верю") >= 0) | (currentSentence.find("я недоверчивый") >= 0) | (currentSentence.find("доверие нужно заслужить") >= 0) | (currentSentence.find("боюсь доверять") >= 0):
        parameters[18] = 1
    if (currentSentence.find("краснею при разговоре с противоположным полом") >= 0) | (currentSentence.find("смущаюсь при разговоре с противоположным полом") >= 0) | (currentSentence.find("дыхание спирает при разговоре с противоположным полом") >= 0) | (currentSentence.find("с противоположным полом общаюсь скованно") >= 0):
        parameters[21] = 1
    if (currentSentence.find("я пойман") >= 0) | (currentSentence.find("я в западне") >= 0) | (currentSentence.find("накрыли меня медным тазом") >= 0) | (currentSentence.find("попался я в ловушку") >= 0):
        parameters[22] = 1
    if (currentSentence.find("страх овладевает мной") >= 0) | (currentSentence.find("беспричинный страх") >= 0) | (currentSentence.find("неожиданный страх") >= 0) | (currentSentence.find("страшно") >= 0):
        parameters[23] = 1
    if (currentSentence.find("я во многом виноват") >= 0) | (currentSentence.find("чувство вины") >= 0) | (currentSentence.find("я виноват") >= 0) | (currentSentence.find("я согрешил") >= 0):
        parameters[26] = 1
    if (currentSentence.find("плохое настроение") >= 0) | (currentSentence.find("подавленное настроение") >= 0) | (currentSentence.find("я расстроен") >= 0) | (currentSentence.find("я грущу") >= 0):
        parameters[30] = 1
    if (currentSentence.find("меня не понимают") >= 0) | (currentSentence.find("мне не сочувствуют") >= 0) | (currentSentence.find("меня не любят") >= 0) | (currentSentence.find("мной не интересуются") >= 0):
        parameters[35] = 1
    if (currentSentence.find("на меня странно посматривают") >= 0) | (currentSentence.find("люди недружелюны") >= 0) | (currentSentence.find("я ненравлюсь людям") >= 0) | (currentSentence.find("люди злые") >= 0):
        parameters[37] = 1
    if (currentSentence.find("спешка может навредить") >= 0) | (currentSentence.find("еду тихо, дальше буду") >= 0) | (currentSentence.find("тише едешь, дальше будешь") >= 0) | (currentSentence.find("ошибок не наделать") >= 0):
        parameters[38] = 1
    if (currentSentence.find("сердце колотится") >= 0) | (currentSentence.find("сердце из груди вырывается") >= 0) | (currentSentence.find("сердце быстро бьётся") >= 0) | (currentSentence.find("гудит сердце") >= 0):
        parameters[39] = 1
    if (currentSentence.find("мышцы болят") >= 0) | (currentSentence.find("тяжело напягать мышцы") >= 0) | (currentSentence.find("боль в мышцах") >= 0) | (currentSentence.find("боли в мышцах") >= 0):
        parameters[42] = 1
    if (currentSentence.find("плохо сплю") >= 0) | (currentSentence.find("сон неспокойный") >= 0) | (currentSentence.find("трудно засыпать") >= 0) | (currentSentence.find("трудно засыпаю") >= 0):
        parameters[44] = 1
    if (currentSentence.find("боюсь ездить на автобусе") >= 0) | (currentSentence.find("боюсь ездить на метро") >= 0) | (currentSentence.find("боюсь ездить на поездах") >= 0) | (currentSentence.find("стах езды на поездах") >= 0):
        parameters[47] = 1
    if (currentSentence.find("комок в горле") >= 0) | (currentSentence.find("комки в горле") >= 0) | (currentSentence.find("дышать трудно") >= 0) | (currentSentence.find("комочек в горле") >= 0):
        parameters[53] = 1
    if (currentSentence.find("будущее безнадёжно") >= 0) | (currentSentence.find("будущее нехорошее") >= 0) | (currentSentence.find("света белого не увижу") >= 0) | (currentSentence.find("синица в руках, журавлём в небе окажется") | (currentSentence.find("судьба нелёгкая предначертана")) >= 0):
        parameters[54] = 1
    if (currentSentence.find("я напряжён") >= 0) | (currentSentence.find("я на взводе") >= 0) | (currentSentence.find("я взвинчен") >= 0) | (currentSentence.find("могу вспыхнуть") >= 0):
        parameters[57] = 1
    if (currentSentence.find("в голове чужие мысли") >= 0) | (currentSentence.find("мысли не свои") >= 0) | (currentSentence.find("мысли не мои") >= 0) | (currentSentence.find("не мыслил так никогда") >= 0):
        parameters[62] = 1
    if (currentSentence.find("могу ударить") >= 0) | (currentSentence.find("делаю больно") >= 0) | (currentSentence.find("грубо прикасаюсь") >= 0) | (currentSentence.find("подумывал свести счеты с жизнью") >= 0) | (currentSentence.find("я вредитель") >= 0):
        parameters[63] = 1
    if (currentSentence.find("бессонница по утрам") >= 0) | (currentSentence.find("утром не спится") >= 0) | (currentSentence.find("утром не сплю") >= 0) | (currentSentence.find("утренняя бессонница") | (currentSentence.find("ранним утром не спится")) >= 0):
        parameters[64] = 1
    if (currentSentence.find("стесняюсь при общении") >= 0) | (currentSentence.find("смущаюсь при общении") >= 0) | (currentSentence.find("краснею при общении") >= 0) | (currentSentence.find("свою застенчивость") >= 0)| (currentSentence.find("отварачиваюсь при общении") >= 0):
        parameters[69] = 1
    if (currentSentence.find("избегаю людные места") >= 0) | (currentSentence.find("мне не нравятся людные места") >= 0) | (currentSentence.find("не люблю шум от людей") >= 0) | (currentSentence.find("от людей столько шума") >= 0):
        parameters[70] = 1
    if (currentSentence.find("ужас") >= 0) | (currentSentence.find("паника") >= 0) | (currentSentence.find("приступ паники") >= 0) | (currentSentence.find("приступ ужаса") >= 0):
        parameters[72] = 1
    if (currentSentence.find("стыдно есть на людях") >= 0) | (currentSentence.find("стыдно пить на людях") >= 0) | (currentSentence.find("всегда питаюсь в уединении") >= 0) | (currentSentence.find("не люблю, когда на меня смотрят, когда я ем") | (currentSentence.find("я ем один")) >= 0):
        parameters[73] = 1
    if (currentSentence.find("чувство одиночества") >= 0) | (currentSentence.find("одиночество") >= 0) | (currentSentence.find("одинокий человек") >= 0):
        parameters[77] = 1
    if (currentSentence.find("ощущение никчёмности") >= 0) | (currentSentence.find("я никчёмный человек") >= 0) | (currentSentence.find("я гноблю себя") >= 0) | (currentSentence.find("я занимаюсь самобичеванием") >= 0):
        parameters[79] = 1
    if (currentSentence.find("я швыряюсь вещами") >= 0) | (currentSentence.find("я часто кричу") >= 0) | (currentSentence.find("я неспокойный человек") >= 0) | (currentSentence.find("я могу вспылить") >= 0):
        parameters[80] = 1
    if (currentSentence.find("боюсь упасть в обморок") >= 0) | (currentSentence.find("не хочу упать в обморок на людях") >= 0) | (currentSentence.find("не хочу беспокоить людей своим слабым здоровьем") >= 0) | (currentSentence.find("боюсь упасть на людях в обморок") >= 0):
        parameters[82] = 1
    if (currentSentence.find("люди злоупотребляют моим доверие") >= 0) | (currentSentence.find("я позволяю другим людям злоупотреблять моим доверием") >= 0) | (currentSentence.find("я доверчивый человек") >= 0) | (currentSentence.find("меня легко обмануть") >= 0):
        parameters[83] = 1
    if (currentSentence.find("моё тело странное") >= 0) | (currentSentence.find("моё тело не в порядке") >= 0) | (currentSentence.find("необычное у меня тело") >= 0) | (currentSentence.find("у меня странное тело") | (currentSentence.find("моё тело не в норме")) >= 0):
        parameters[87] = 1
    if (currentSentence.find("с моим рассудком что-то аномальное") >= 0) | (currentSentence.find("у меня помутнился рассудок") >= 0) | (currentSentence.find("голова как чугун") >= 0) | (currentSentence.find("что-то неладное с моим рассудком") >= 0):
        parameters[90] = 1

print(parameters[1])

print(parameters[77])
print(parameters[26])
print(parameters[30])
print(parameters[16])
print(parameters[63])
print(parameters[69])

print(parameters[21])
print(parameters[23])
print(parameters[82])
print(parameters[81])
print(parameters[79])
print(parameters[63])
print(parameters[35])
print(parameters[72])
