# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kbRR8xTUVGXzoaSXBALC-lfSKi6YblCA

100 katlı bina var 2 adet yumurta ile sadece tek sefer kullanmak şartı en az kaç defada yumurtanın kırılmadığı katı bulabiliriz?
"""

import math
x=1000000
for i in range(2,100):
  m=0
  m+=(math.floor(100/i)+math.floor((i-1)/2)+math.floor((100%i)/2))
  x=min(x,m)
print(x)

"""  
Görüntü işleme aşamlarını sırası ile tarif ediniz.

Elde Etme: Sayısal görüntü sayısal kamera ile elde edilir.

Ön İşleme: Sayısal görüntüyü kullanmadan önce bazı ön işlemlerden geçirmek gerekir.

Bölümleme:Bu kısımda amaç görüntü içerisindeki nesne ve alanların değişik özelliklerinin tespit edilip birbirinden ayrılmasıdır.

Çıkarım: Elde edilen ham bilgilerin, istenilen farklı özelliklerin, ayrıntıların ön plana çıkarılmasıdır.

Yorumlama: Bu son kısımda artık bazı yapay zeka algoritmaları ile işlenen görüntü içerisindeki farklı nesnelerin ve alanların sınıflara ayrılması ve etiketlendirilmesi yapılır.


Feature map veya bir sonraki layerın boyutlarını belirleyen özellikler nelerdir. Açıklayınız.

İnputun boyutlarıyla birlikte Kernel'ın/filtrenin boyutları,Pooling ve/veya Padding yapılması, Stride(adım boyu)/Filtrenin hareket boyu ve dept yani uygulanan filtrenin sayısı sonunda çıkıcak olan Feature Mapin ve sonraki Layerin boyutunu belirleyecektir.

Softmax nedir? Ne işe yarar?

Softmax Fonksiyonu: Çoklu sınıflandırma problemleri için kullanılan bu fonksiyon, verilen her bir girdinin bir sınıfa ait olma olasılığını gösteren [0,1] arası çıktılar üretmektedir.

Aktivasyon fonskiyonlarının kullanım amaçları nedir? 3 adet örnek veriniz. Amaçlarını açıklayınız. Şekillerini çiziniz.

 Yapay sinir ağlarına doğrusal olmayan gerçek dünya özelliklerini tanıtmak için aktivasyon fonksiyonuna ihtiyaç duyarız. Temel olarak basit bir yapay sinir ağında x girdiler,** w** ağırlıklar olarak tanımlanır ve ağın çıkışına aktarılan değere f(x) yani aktivasyon işlemi uygularız. Daha sonra bu, nihai çıkış ya da bir başka katmanın girişi olacaktır.

ReLU (Rectified Linear Unit) Fonksiyonu
Doğrusal (Linear) Fonksiyon
Sigmoid Fonksiyonu

32,32 lik image olduğunu düşünelim 2,2 like Max pooling sonucunda çıktı hangi boyutta olur?  
31.0

Droupout'un amacı nedir?

 Dropout kullanılarak fully-connected layerlardaki bağlar koparılır. Böylece node'lar birbiri hakkında daha az bilgiye sahip olur ve bunun doğal sonucu olarak node'lar birbirlerinin ağırlık değişimlerinden daha az etkilenirler.

Görüntü işleme yöntemleri için kullanılan 3 adet framework belirtiniz.

OpenCV,EmguCV,Tensorflow

Niçin imajlar için ANN yerine CNN kullanıyoruz?

ANN ile somut veri noktaları sağlanmalıdır. CNN kullanırken, bu uzamsal özellikler görüntü girişinden çıkarılır. Öncekilere kıyasla cnn'in en büyük avantajı, önemli özellikleri herhangi bir insan gözetimi olmadan otomatik olarak algılamasıdır. Bu nedenle CNN, bilgisayarla görme ve görüntü sınıflandırma sorunlarına ideal bir çözüm olacaktır.

CNN ağları için dimension reduction mümkünmüdür? Mümkünse nasıl ve hangi katmanlarda uygulanabilir?

Mümkündür. Pooling Layer, CovNet’teki ardışık convolutional katmanları arasına sıklıkla eklenen bir katmandır.r.

5,5 bir imaja 3,3 lük bir filtre uygulandığında stride=1 olacak şekilde o-elde edilen outputun boyutunun 5,5 olması niçin ne yapabiliriz?

(((5-3)+2*X)/1)+1=5 olması  X=1 kalınlığında olması gerekir.
"""