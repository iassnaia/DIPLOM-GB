import whisper
import re

print("Welcome to the stressDisorderClassification!")
numberOfStory = input("Please, write number of the story: ")
print("Here we go. Wait a few minutes to get the result.")

architecture = whisper.load_model("small")
story = architecture.transcribe(f"in/stories/story{numberOfStory}/client/client2.mp3")

sentences = re.split('[.!?]', story["text"])
countOfSentences = len(sentences)
firstParameters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
secondParameters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def sigmoid_function(x):
    return 1/(1+2.718281828**(-x))

for i in range(countOfSentences):
    currentSentence = sentences[i]
    currentSentence = currentSentence.lower()

    if (currentSentence.find("головная боль") >= 0) | (currentSentence.find("головные боли") >= 0) | (currentSentence.find("болит голова") >= 0) | (currentSentence.find("боль в голове") >= 0):
        firstParameters[1] = 1
    if (currentSentence.find("нервозность") >= 0) | (currentSentence.find("проблемы с нервами") >= 0) | (currentSentence.find("истерика") >= 0) | (currentSentence.find("раздраженность") >= 0):
        firstParameters[2] = 1
    if (currentSentence.find("набор мыслей") >= 0) | (currentSentence.find("каша в голове") >= 0) | (currentSentence.find("повторяющиеся мысли") >= 0) | (currentSentence.find("теже самые мысли") >= 0):
        firstParameters[3] = 1
    if (currentSentence.find("головокружение") >= 0) | (currentSentence.find("голова кружится") >= 0) | (currentSentence.find("в глазах двоится") >= 0) | (currentSentence.find("кружащаяся голова") >= 0) | (currentSentence.find("слабость") >= 0):
        firstParameters[4] = 1
    if (currentSentence.find("не встает") >= 0) | (currentSentence.find("не поднимается") >= 0) | (currentSentence.find("секса не хочется") >= 0) | (currentSentence.find("потеря сексуального влечения") >= 0):
        firstParameters[5] = 1
    if (currentSentence.find("я грубый") >= 0) | (currentSentence.find("я недоволен") >= 0) | (currentSentence.find("выражаю свое недовольство") >= 0) | (currentSentence.find("я зол") >= 0):
        firstParameters[6] = 1
    if (currentSentence.find("мысли управляемы") >= 0) | (currentSentence.find("управление мыслью") >= 0) | (currentSentence.find("мысли контролируются") >= 0) | (currentSentence.find("подбрасывает мысли") >= 0):
        firstParameters[7] = 1
    if (currentSentence.find("они виноваты") >= 0) | (currentSentence.find("они провинились") >= 0) | (currentSentence.find("нехорошие люди") >= 0) | (currentSentence.find("непиятности от людей") >= 0):
        firstParameters[8] = 1
    if (currentSentence.find("забываю") >= 0) | (currentSentence.find("забыл") >= 0) | (currentSentence.find("не помню") >= 0) | (currentSentence.find("проблемы с памятью") >= 0) | (currentSentence.find("память дырявая") >= 0):
        firstParameters[9] = 1
    if (currentSentence.find("я неряха") >= 0) | (currentSentence.find("я неряшливый") >= 0) | (currentSentence.find("я небрежный") >= 0) | (currentSentence.find("внимание рассеянно") >= 0):
        firstParameters[10] = 1
    if (currentSentence.find("я раздражительный") >= 0) | (currentSentence.find("обидно") >= 0) | (currentSentence.find("досадно") >= 0) | (currentSentence.find("жаль") >= 0):
        firstParameters[11] = 1
    if (currentSentence.find("болит сердце") >= 0) | (currentSentence.find("болит грудь") >= 0) | (currentSentence.find("болит грудная клетка") >= 0) | (currentSentence.find("сердце ноет") >= 0):
        firstParameters[12] = 1
    if (currentSentence.find("голоса") >= 0) | (currentSentence.find("я один слышу") >= 0) | (currentSentence.find("послышалось") >= 0) | (currentSentence.find("откуда звук") >= 0):
        firstParameters[16] = 1
    if (currentSentence.find("я никому не верю") >= 0) | (currentSentence.find("я недоверчивый") >= 0) | (currentSentence.find("доверие нужно заслужить") >= 0) | (currentSentence.find("боюсь доверять") >= 0):
        firstParameters[18] = 1
    if (currentSentence.find("краснею при разговоре с противоположным полом") >= 0) | (currentSentence.find("смущаюсь при разговоре с противоположным полом") >= 0) | ((currentSentence.find("я очень застенчивый человек") >= 0) & (currentSentence.find("речь идет о лицах противоположного пола") >= 0)) | (currentSentence.find("дыхание спирает при разговоре с противоположным полом") >= 0) | (currentSentence.find("с противоположным полом общаюсь скованно") >= 0):
        firstParameters[21] = 1
    if (currentSentence.find("я пойман") >= 0) | (currentSentence.find("я в западне") >= 0) | (currentSentence.find("накрыли меня медным тазом") >= 0) | (currentSentence.find("попался я в ловушку") >= 0):
        firstParameters[22] = 1
    if (currentSentence.find("страх овладевает мной") >= 0) | (currentSentence.find("беспричинный страх") >= 0) | (currentSentence.find("неожиданный страх") >= 0) | (currentSentence.find("страшно") >= 0):
        firstParameters[23] = 1
    if (currentSentence.find("я во многом виноват") >= 0) | (currentSentence.find("чувство вины") >= 0) | (currentSentence.find("я виноват") >= 0) | (currentSentence.find("я согрешил") >= 0):
        firstParameters[26] = 1
    if (currentSentence.find("плохое настроение") >= 0) | (currentSentence.find("подавленное настроение") >= 0) | (currentSentence.find("я расстроен") >= 0) | (currentSentence.find("я грущу") >= 0):
        firstParameters[30] = 1
    if (currentSentence.find("меня не понимают") >= 0) | (currentSentence.find("мне не сочувствуют") >= 0) | (currentSentence.find("меня не любят") >= 0) | (currentSentence.find("мной не интересуются") >= 0) | (currentSentence.find("жду сочувствия") >= 0) | (currentSentence.find("не понимают меня") >= 0):
        firstParameters[35] = 1
    if (currentSentence.find("на меня странно посматривают") >= 0) | (currentSentence.find("люди недружелюны") >= 0) | (currentSentence.find("я ненравлюсь людям") >= 0) | (currentSentence.find("люди злые") >= 0):
        firstParameters[37] = 1
    if (currentSentence.find("спешка может навредить") >= 0) | (currentSentence.find("еду тихо, дальше буду") >= 0) | (currentSentence.find("тише едешь, дальше будешь") >= 0) | (currentSentence.find("ошибок не наделать") >= 0):
        firstParameters[38] = 1
    if (currentSentence.find("сердце колотится") >= 0) | (currentSentence.find("сердце из груди вырывается") >= 0) | (currentSentence.find("сердце быстро бьется") >= 0) | (currentSentence.find("гудит сердце") >= 0):
        firstParameters[39] = 1
    if (currentSentence.find("мышцы болят") >= 0) | (currentSentence.find("тяжело напягать мышцы") >= 0) | (currentSentence.find("боль в мышцах") >= 0) | (currentSentence.find("боли в мышцах") >= 0):
        firstParameters[42] = 1
    if (currentSentence.find("плохо сплю") >= 0) | (currentSentence.find("сон неспокойный") >= 0) | (currentSentence.find("трудно засыпать") >= 0) | (currentSentence.find("трудно засыпаю") >= 0):
        firstParameters[44] = 1
    if (currentSentence.find("боюсь ездить на автобусе") >= 0) | (currentSentence.find("боюсь ездить на метро") >= 0) | (currentSentence.find("боюсь ездить на поездах") >= 0) | (currentSentence.find("стах езды на поездах") >= 0):
        firstParameters[47] = 1
    if (currentSentence.find("комок в горле") >= 0) | (currentSentence.find("комки в горле") >= 0) | (currentSentence.find("дышать трудно") >= 0) | (currentSentence.find("комочек в горле") >= 0):
        firstParameters[53] = 1
    if (currentSentence.find("будущее безнадежно") >= 0) | (currentSentence.find("будущее нехорошее") >= 0) | (currentSentence.find("света белого не увижу") >= 0) | (currentSentence.find("синица в руках, журавлем в небе окажется") | (currentSentence.find("судьба нелегкая предначертана")) >= 0):
        firstParameters[54] = 1
    if (currentSentence.find("я напряжен") >= 0) | (currentSentence.find("я на взводе") >= 0) | (currentSentence.find("я взвинчен") >= 0) | (currentSentence.find("могу вспыхнуть") >= 0):
        firstParameters[57] = 1
    if (currentSentence.find("в голове чужие мысли") >= 0) | (currentSentence.find("мысли не свои") >= 0) | (currentSentence.find("мысли не мои") >= 0) | (currentSentence.find("не мыслил так никогда") >= 0):
        firstParameters[62] = 1
    if (currentSentence.find("могу ударить") >= 0) | (currentSentence.find("делаю больно") >= 0) | (currentSentence.find("грубо прикасаюсь") >= 0) | ((currentSentence.find("боль") >= 0) & (currentSentence.find("улыбки") >= 0)) | (currentSentence.find("подумывал свести счеты с жизнью") >= 0) | (currentSentence.find("я вредитель") >= 0):
        firstParameters[63] = 1
    if (currentSentence.find("бессонница по утрам") >= 0) | (currentSentence.find("утром не спится") >= 0) | (currentSentence.find("утром не сплю") >= 0) | (currentSentence.find("утренняя бессонница") | (currentSentence.find("ранним утром не спится")) >= 0):
        firstParameters[64] = 1
    if (currentSentence.find("стесняюсь при общении") >= 0) | (currentSentence.find("смущаюсь при общении") >= 0) | (currentSentence.find("краснею при общении") >= 0) | (currentSentence.find("свою застенчивость") >= 0)| (currentSentence.find("отварачиваюсь при общении") >= 0):
        firstParameters[69] = 1
    if (currentSentence.find("избегаю людные места") >= 0) | (currentSentence.find("мне не нравятся людные места") >= 0) | (currentSentence.find("не люблю шум от людей") >= 0) | (currentSentence.find("от людей столько шума") >= 0):
        firstParameters[70] = 1
    if (currentSentence.find("ужас") >= 0) | (currentSentence.find("паника") >= 0) | (currentSentence.find("приступ паники") >= 0) | (currentSentence.find("приступ ужаса") >= 0):
        firstParameters[72] = 1
    if (currentSentence.find("стыдно есть на людях") >= 0) | (currentSentence.find("стыдно пить на людях") >= 0) | (currentSentence.find("всегда питаюсь в уединении") >= 0) | (currentSentence.find("не люблю, когда на меня смотрят, когда я ем") | (currentSentence.find("я ем один")) >= 0):
        firstParameters[73] = 1
    if (currentSentence.find("чувство одиночества") >= 0) | (currentSentence.find("одиночество") >= 0) | (currentSentence.find("одинокий человек") >= 0):
        firstParameters[77] = 1
    if (currentSentence.find("ощущение никчемности") >= 0) | (currentSentence.find("я никчемный человек") >= 0) | (currentSentence.find("я гноблю себя") >= 0) | (currentSentence.find("я занимаюсь самобичеванием") >= 0):
        firstParameters[79] = 1
    if (currentSentence.find("я швыряюсь вещами") >= 0) | (currentSentence.find("я часто кричу") >= 0) | (currentSentence.find("могу даже закричать") >= 0) | (currentSentence.find("я неспокойный человек") >= 0) | (currentSentence.find("я могу вспылить") >= 0):
        firstParameters[81] = 1
    if (currentSentence.find("боюсь упасть в обморок") >= 0) | (currentSentence.find("не хочу упать в обморок на людях") >= 0) | ((currentSentence.find("боюсь") >= 0) & (currentSentence.find("в обморок") >= 0)) | (currentSentence.find("не хочу беспокоить людей своим слабым здоровьем") >= 0) | (currentSentence.find("боюсь упасть на людях в обморок") >= 0):
        firstParameters[82] = 1
    if (currentSentence.find("люди злоупотребляют моим доверие") >= 0) | (currentSentence.find("я позволяю другим людям злоупотреблять моим доверием") >= 0) | (currentSentence.find("я доверчивый человек") >= 0) | (currentSentence.find("меня легко обмануть") >= 0):
        firstParameters[83] = 1
    if (currentSentence.find("мое тело странное") >= 0) | (currentSentence.find("мое тело не в порядке") >= 0) | (currentSentence.find("необычное у меня тело") >= 0) | (currentSentence.find("у меня странное тело") | (currentSentence.find("мое тело не в норме")) >= 0):
        firstParameters[87] = 1
    if (currentSentence.find("с моим рассудком что-то аномальное") >= 0) | (currentSentence.find("у меня помутнился рассудок") >= 0) | (currentSentence.find("голова как чугун") >= 0) | (currentSentence.find("что-то неладное с моим рассудком") >= 0):
        firstParameters[90] = 1

for j in range(91):
    if j not in [3, 4, 5, 7, 8, 12, 16, 18, 21, 22, 37, 47, 54, 79]:
        secondParameters[j] = firstParameters[j]
    else:
        match j:
            case 3:
                secondParameters[3] = sigmoid_function(firstParameters[21]*1 + firstParameters[23]*0.8 + firstParameters[35]*0.6 + firstParameters[63]*0.6 + firstParameters[72]*0.6 + firstParameters[79]*0.6 + firstParameters[81]*0.7 + firstParameters[82]*0.8)
            case 4:
                secondParameters[4] = sigmoid_function(firstParameters[0]*0.7 + firstParameters[16]*0.6 + firstParameters[26]*0.8 + firstParameters[30]*0.7 + firstParameters[63]*0.6 + firstParameters[69]*0.6 + firstParameters[77]*0.7)
            case 5:
                secondParameters[5] = sigmoid_function(firstParameters[9]*0.6 + firstParameters[32]*0.6 + firstParameters[42]*0.8 + firstParameters[47]*0.7 + firstParameters[63]*0.6 + firstParameters[87]*0.7)
            case 7:
                secondParameters[7] = sigmoid_function(firstParameters[16]*0.5 + firstParameters[44]*0.6 + firstParameters[57]*0.6 + firstParameters[70]*0.6)
            case 8:
                secondParameters[8] = sigmoid_function(firstParameters[0]*0.7 + firstParameters[7]*0.5 + firstParameters[62]*0.6)
            case 12:
                secondParameters[12] = sigmoid_function(firstParameters[0]*0.6 + firstParameters[4]*0.7 + firstParameters[16]*0.8 + firstParameters[32]*0.6 + firstParameters[37]*0.6 + firstParameters[39]*0.7 + firstParameters[54]*0.6 + firstParameters[64]*0.9 + firstParameters[73]*0.6)
            case 16:
                secondParameters[16] = sigmoid_function(firstParameters[7]*0.8 + firstParameters[13]*0.6 + firstParameters[35]*0.6 + firstParameters[53]*0.7 + firstParameters[86]*0.5)
            case 18:
                secondParameters[18] = sigmoid_function(firstParameters[7]*0.6 + firstParameters[15]*0.5 + firstParameters[16]*0.5 + firstParameters[17]*0.9 + firstParameters[44]*0.7 + firstParameters[64]*0.5 + firstParameters[72]*0.7 + firstParameters[87]*0.5)
            case 21:
                secondParameters[21] = sigmoid_function(firstParameters[0]*0.8 + firstParameters[3]*0.9 + firstParameters[13]*0.6 + firstParameters[15]*0.6 + firstParameters[16]*0.6 + firstParameters[22]*0.9 + firstParameters[34]*0.6 + firstParameters[43]*0.6 + firstParameters[46]*0.5 + firstParameters[47]*0.7 + firstParameters[49]*0.5 + firstParameters[50]*0.6 + firstParameters[59]*0.8 + firstParameters[61]*0.8 + firstParameters[62]*0.5 + firstParameters[63]*0.5 + firstParameters[64]*0.7 + firstParameters[69]*0.9 + firstParameters[70]*0.7 + firstParameters[74]*0.6 + firstParameters[76]*0.7 + firstParameters[79]*0.9 + firstParameters[81]*0.5 + firstParameters[84]*0.7 + firstParameters[85]*0.5)
            case 22:
                secondParameters[22] = sigmoid_function(firstParameters[0]*0.4 + firstParameters[1]*0.4 + firstParameters[8]*0.4 + firstParameters[38]*0.5 + firstParameters[60]*0.6 + firstParameters[63]*0.4)
            case 37:
                secondParameters[37] = sigmoid_function(firstParameters[0]*0.5 + firstParameters[20]*0.8 + firstParameters[23]*0.5 + firstParameters[25]*0.5 + firstParameters[33]*0.9 + firstParameters[36]*0.7 + firstParameters[41]*0.8 + firstParameters[47]*0.6 + firstParameters[63]*0.6 + firstParameters[70]*0.5 + firstParameters[90]*0.6)
            case 47:
                secondParameters[47] = sigmoid_function(firstParameters[5]*0.5 + firstParameters[13]*0.6 + firstParameters[31]*0.5 + firstParameters[49]*0.5 + firstParameters[51]*0.5 + firstParameters[82]*0.5)
            case 54:
                secondParameters[54] = sigmoid_function(firstParameters[0]*0.8 + firstParameters[22]*0.5 + firstParameters[25]*0.5 + firstParameters[26]*0.6 + firstParameters[49]*0.5 + firstParameters[68]*0.5 + firstParameters[72]*0.5 + firstParameters[79]*0.8 + firstParameters[80]*0.7 + firstParameters[84]*0.6)
            case 79:
                secondParameters[79] = sigmoid_function(firstParameters[0]*0.6 + firstParameters[3]*0.5 + firstParameters[16]*0.7 + firstParameters[41]*0.5 + firstParameters[47]*0.7 + firstParameters[51]*0.6 + firstParameters[54]*0.5 + firstParameters[55]*0.7 + firstParameters[64]*0.6 + firstParameters[71]*0.7 + firstParameters[80]*0.8)

countOfDisorders = 0
sumOfParametersValues = 0
for parameterValue in secondParameters:
    if parameterValue != 0:
        countOfDisorders = countOfDisorders + 1
        sumOfParametersValues = sumOfParametersValues + parameterValue

result = int((round(sumOfParametersValues/countOfDisorders, 2))*100)

f = open("out/results.txt", "a")
f.write(f"Result of story number {numberOfStory} is: {result}%\n")
f.close()

print(f"Result of story number {numberOfStory} is: {result}%")
print("Where 50%-70% is good, 70%-90% is normal, 90%-100% is bad.")
print("To see all yours results: out/results.txt.")


