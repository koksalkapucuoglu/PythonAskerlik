# -*- coding: utf-8 -*-
while 1:
	egitim = int(input("lise ve altı için -> 1\nön lisans için -> 2\nlisans ve üstü için -> 3 giriniz:  "))
	if egitim == 3:
		cevap_1 = input("Bedelli yapmak ister misiniz?(E/H)")
		if cevap_1 =='h' or cevap_1 == 'H':
			cevap_2 = input("Yedek Subay olmak ister misin?(E/H)")
			if cevap_2 == 'E' or cevap_2 == 'e':
				print("Askerlik tarifeniz : 2 ay temel eğitim(Harçlık) + 10 ay Kıt'a(Maaş)\n----------------------------------------------------------------------------------------")
			else:
				print("Askerlik tarifeniz : 1 ay temel eğitim(Harçlık) + 5 ay Kıt'a(Harçlık)\n---------------------------------------------------------------------------------------- ")
		else: print("Askerlik tarifeniz : 1 ay temel askerlik(harçlık) + 32 bin lira bedelli ücreti\n----------------------------------------------------------------------------------------")


	if egitim == 2:
		cevap_1 = input("Bedelli yapmak ister misiniz?(E/H)")
		if cevap_1 == 'H' or cevap_1 == 'h':
			cevap_2 = input("Yedek Astsubay olmak ister misin?(E/H)")
			if cevap_2 == 'E' or cevap_2 == 'e':
				print("Askerlik tarifeniz : 2 ay temel eğitim(Harçlık) + 10 ay Kıt'a(Maaş)\n----------------------------------------------------------------------------------------")
			else:
				print("Askerlik tarifeniz : 1 ay temel eğitim(Harçlık) + 5 ay Kıt'a(Harçlık) \n----------------------------------------------------------------------------------------")
		else: print("Askerlik tarifeniz : 1 ay temel askerlik(harçlık) + 32 bin lira bedelli ücreti\n----------------------------------------------------------------------------------------")

	if egitim == 1:
		cevap_1 = input("Bedelli yapmak ister misiniz?(E/H)")
		if cevap_1 == 'H' or cevap_1 == 'h':
			print("Askerlik tarifeniz : 1 ay temel eğitim(Harçlık) + 5 ay askerlik(Harçlık)\n----------------------------------------------------------------------------------------")
			cevap_2  = input("Toplam 6 ay askerliğin ardından 6 ay daha askerde kalmak ister misiniz?(E/H)")
			if cevap_2 == 'E' or cevap_2 == 'e':
				print("Askerlik tarifeniz : 1 ay temel eğitim(Harçlık) + 5 ay askerlik(Harçlık) + 6 ay ek askerlik(Maaş)\n----------------------------------------------------------------------------------------")
			else:
				print("Askerlik tarifeniz : 1 ay temel eğitim(Harçlık) + 5 ay askerlilk(Harçlık))\n----------------------------------------------------------------------------------------")
		else: print("Askerlik tarifeniz : 1 ay temel askerlik(harçlık) + 32 bin lira bedelli ücreti\n----------------------------------------------------------------------------------------")
	else: print("Lütfen belirtilen seçeneklerden birini seçiniz.\n")
