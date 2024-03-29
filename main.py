import pymorphy2
morph = pymorphy2.MorphAnalyzer()

# 1) методами строк очистить текст от знаков препинания;
print()
print('1) без знаков препинания: ')
print()

text_str = '''Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему.
Все смешалось в доме Облонских. Жена узнала, что муж был в связи с бывшею в их доме француженкою-гувернанткой, и объявила мужу, что не может жить с ним в одном доме. Положение это продолжалось уже третий день и мучительно чувствовалось и самими супругами, и всеми членами семьи, и домочадцами. Все члены семьи и домочадцы чувствовали, что нет смысла в их сожительстве и что на каждом постоялом дворе случайно сошедшиеся люди более связаны между собой, чем они, члены семьи и домочадцы Облонских. Жена не выходила из своих комнат, мужа третий день не было дома. Дети бегали по всему дому, как потерянные; англичанка поссорилась с экономкой и написала записку приятельнице, прося приискать ей новое место; повар ушел вчера со двора, во время самого обеда; черная кухарка и кучер просили расчета.
На третий день после ссоры князь Степан Аркадьич Облонский — Стива, как его звали в свете, — в обычный час, то есть в восемь часов утра, проснулся не в спальне жены, а в своем кабинете, на сафьянном диване. Он повернул свое полное, выхоленное тело на пружинах дивана, как бы желая опять заснуть надолго, с другой стороны крепко обнял подушку и прижался к ней щекой; но вдруг вскочил, сел на диван и открыл глаза.
«Да, да, как это было? — думал он, вспоминая сон. — Да, как это было? Да! Алабин давал обед в Дармштадте; нет, не в Дармштадте, а что-то американское. Да, но там Дармштадт был в Америке. Да, Алабин давал обед на стеклянных столах, да, — и столы пели: Il mio tesoro 1 и не Il mio tesoro, а что-то лучше, и какие-то маленькие графинчики, и они же женщины», — вспоминал он.
Глаза Степана Аркадьича весело заблестели, и он задумался, улыбаясь. «Да, хорошо было, очень хорошо. Много еще что-то там было отличного, да не скажешь словами и мыслями даже наяву не выразишь». И, заметив полосу света, пробившуюся сбоку одной из суконных стор, он весело скинул ноги с дивана, отыскал ими шитые женой (подарок ко дню рождения в прошлом году), обделанные в золотистый сафьян туфли, и по старой, девятилетней привычке, не вставая, потянулся рукой к тому месту, где в спальне у него висел халат. И тут он вспомнил вдруг, как и почему он спит не в спальне жены, а в кабинете; улыбка исчезла с его лица, он сморщил лоб.
«Ах, ах, ах! Ааа!..» — замычал он, вспоминая все, что было. И его воображению представились опять все подробности ссоры с женою, вся безвыходность его положения и мучительнее всего собственная вина его.
«Да! она не простит и не может простить. И всего ужаснее то, что виной всему я, виной я, а не виноват. В этом-то вся драма, — думал он. — Ах, ах, ах!» — приговаривал он с отчаянием, вспоминая самые тяжелые для себя впечатления из этой ссоры.
Неприятнее всего была та первая минута, когда он, вернувшись из театра, веселый и довольный, с огромною грушей для жены в руке, не нашел жены в гостиной; к удивлению, не нашел ее и в кабинете и, наконец, увидал ее в спальне с несчастною, открывшею все, запиской в руке.
Она, эта вечно озабоченная, и хлопотливая, и недалекая, какою он считал ее, Долли, неподвижно сидела с запиской в руке и с выражением ужаса, отчаяния и гнева смотрела на него.
— Что это? это? — спрашивала она, указывая на записку.
И при этом воспоминании, как это часто бывает, мучало Степана Аркадьича не столько самое событие, сколько то, как он ответил на эти слова жены.
С ним случилось в эту минуту то, что случается с людьми, когда они неожиданно уличены в чем-нибудь слишком постыдном. Он не сумел приготовить свое лицо к тому положению, в которое он становился перед женой после открытия его вины. Вместо того чтоб оскорбиться, отрекаться, оправдываться, просить прощения, оставаться даже равнодушным — все было бы лучше того, что он сделал! — его лицо совершенно невольно («рефлексы головного мозга», — подумал Степан Аркадьич, который любил физиологию), совершенно невольно вдруг улыбнулось привычною, доброю и потому глупою улыбкой.
Эту глупую улыбку он не мог простить себе. Увидав эту улыбку, Долли вздрогнула, как от физической боли, разразилась, со свойственною ей горячностью, потоком жестоких слов и выбежала из комнаты. С тех пор она не хотела видеть мужа.'''

# знаки препинания
# точка (.), вопросительный знак (?), восклицательный знак (!), многоточие (...),
# запятая (,), точка с запятой (;), двоеточие (:), тире (-), скобки (круглые) ( ), кавычки (" ")

no_sign = ''
sign_list = '. ? ! , ; : \' — ( ) " « »'.split()

for i in sign_list:
    text_str = text_str.replace(i, no_sign)

print(text_str)
print()


# 2) сформировать list со словами (split);

print('2) Список:')
print()

text_list = text_str.split()
print(text_list)
print()


# 3) привести все слова к нижнему регистру (map);
# 5) дополнительно к приведению к нижнему регистру выполнить лемматизацию

print('3) Нижний регист: \n5) Лемматизация:')
print()

text_lower = list(map(lambda x: x.lower(), text_list))

lem_list = []

for a in text_lower:
    lem_list.append(morph.parse(a)[0].normal_form)
print(lem_list)
print()


#3) получить из list пункта 3 dict, ключами которого являются слова,
# а значениями их количество появлений в тексте;

print('4) Словарь: ')
print()

#text_dict = {a: text_lower.count(a) for a in text_lower}
text_dict = {a: lem_list.count(a) for a in lem_list}
#print(text_dict)
for keys, values in text_dict.items():
    print(keys, values)

print()


# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set);

print('5 наиболее часто встречающихся слов:')
print()
# 5 наиболее часто встречающихся слов

popular_words = []
for a in text_dict.values():
    popular_words.append(a)
popular_words.sort()

popular_5words = popular_words[-5:]

for keys, values in text_dict.items():
    if values in popular_5words:
        print(keys, values)

print()

#количество разных слов в тексте
differ_words = set(text_dict)
print('Количество разных слов в тексте: ', len(differ_words))
