str_1 = ("Dans la catégorie du film ayant reçu la plus longue ovation (comme si cela confirmait la qualité "
         "d’une œuvre ou l’assurance d’une Palme d’or), le gagnant est Valeur sentimentale, du Norvégien de "
         "naissance danoise Joachim Trier, avec 19 minutes d’applaudissements. Membre de la grande famille "
         "cannoise depuis 2011, année où il a présenté Oslo 31 août à Un certain regard, le réalisateur de Plus "
         "fort que les bombes et de Julie (en 12 chapitres) se retrouve une troisième fois en compétition. "
         "Et plusieurs le voient déjà remporter la plus haute distinction samedi soir lors de la cérémonie de clôture.")

str_2 = ("Truskawka Albion, z najnowszej hodowli wiecznie kwitnących odmian, zaczyna owocować w maju i trwa do "
         "końca października! Każda truskawka może wyprodukować 450 g pysznych owoców rocznie! Truskawka Albion to "
         "kolejny rodzaj truskawki, która rośnie jako pnące pędy z długimi, elastycznymi korzeniami. Bogate, pyszne, "
         "słodkie, ciemnoczerwone jagody mają niepowtarzalny smak, który pozostaje taki sam przez całe lato. Ponadto "
         "ta energiczna odmiana 55 ma zwiększoną odporność na choroby, takie jak werticilioza i zgnilizna korony.")

str_3 = ("大兴“好房子”建面约168-222㎡低密平墅 西红门新品迭代88-139㎡带阳台三至四居 石景山建面约80-130平二至四居售楼处开放 "
         "首付146万起抢西四环全四居临铁公园住区 京西五环 约91-143㎡学府洋房 样板间开放 京西约76-149㎡二至四居全明洋房全线封顶 "
         "良乡大学城芯 99㎡户型加推 少量席位抢藏 长安街新首钢 地铁旁 满配洋房 首开即磬 7-11层洋房+高配置私家会所 现房开盘 顺义主城 "
         "105-188平三居四居钜惠立减38万")


from langdetect import detect


print(detect(str_1))
print(detect(str_2))
print(detect(str_3))

a = 333

