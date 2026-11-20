# BYD için araç uygulaması nasıl seçilir? Kontrol listesi

Araç ekranına kuracağınız uygulama kameralarınıza, konumunuza ve aracınızın verilerine erişir. Seçerken yalnız özellik listesine değil, aşağıdaki sekiz soruya bakın. Her soru için Yoldaş'ın cevabı da yazılı; böylece kendi ölçütlerinizle karşılaştırabilirsiniz.

Son güncelleme: 15 Ekim 2026

## 1. Hangi araçta, hangi özellik çalışıyor?

Uygulamanın her BYD'de aynı çalışmasını beklemeyin. Araç ekranının yazılım sürümüne göre kamera, kadran ya da cam komutları açılır ya da kapanır. İyi bir uygulama bunu model bazında açıkça yazar.

- **Sorun:** Modelim ve yazılım sürümüm için hangi özellikler listeleniyor, hangileri yok?
- **Yoldaş'ta:** her modelin sayfasında desteklenen özellikler tablosu var. Sürüm numarasının ne anlama geldiği için [DiLink rehberine](https://yoldas.io/rehber/byd-dilink-3-4-5) bakın.

## 2. Kayıt güvenilir mi?

Kayıt uygulamasının asıl sınavı, ihtiyaç duyduğunuz anda kaydın orada olmasıdır. Birkaç saatlik park, araç kapanıp açılması ve dolu alan senaryolarını kendiniz deneyin.

- **Sorun:** Kayıt aralıksız mı? Araç yeniden açılınca kendiliğinden başlıyor mu? Alan dolunca hangi kayıt silinir, önemli klibi koruyabilir miyim?
- **Yoldaş'ta:** sürüşte kayıt varsayılan olarak sürekli, parçalar hâlinde alınır (parkta varsayılan kapalıdır; nöbetçi algılayınca ya da sürekli olarak açabilirsiniz). Alan dolunca korumadığınız en eski kayıt silinir. Ani frende varsayılan olarak öncesi 15 ve sonrası 15 saniye kendiliğinden korunur (5–30 saniye ayarlanır). Ayrıntılar [Dashcam sayfasında](https://yoldas.io/ozellikler/dashcam).

## 3. Veri nerede duruyor?

Kamera kayıtları en hassas veridir. Kaydın araçta mı, bir sunucuda mı durduğunu, canlı izlemenin saklanıp saklanmadığını ve şasi numarası gibi kimlik verilerinin gidip gitmediğini sorun.

- **Sorun:** Kayıtlar kendiliğinden bir sunucuya yükleniyor mu? Canlı görüntü saklanıyor mu? Şasi numarası ya da konum gönderiliyor mu? Verimi silebilir miyim?
- **Yoldaş'ta:** kayıtlar araçta kalır, telefonda istediğinizde alınır. Canlı görüntü sunucudan geçer, saklanmaz. Şasi numarası araçtan çıkmaz. Konum ayrı onayla gönderilir. Telefon uygulamasındaki "Bu aracın geçmişini sil" ile sunucudaki veriler silinir. Ayrıntılar [Güvenlik sayfasında](https://yoldas.io/guvenlik).

## 4. Dil ve birimler

- **Sorun:** Araç ekranı ve telefon uygulaması kendi dilimde mi? Kilometre ve mil, °C ve °F gibi birimleri seçebiliyor muyum?
- **Yoldaş'ta:** Türkçe, İngilizce, Almanca, Fransızca, İspanyolca, Portekizce, Hollandaca, Lehçe, Rusça, Arapça, Korece, Tayca ve Basitleştirilmiş Çince; Arapça sağdan sola yazılır. Birimler (km veya mil, °C veya °F, kW, PS veya hp, bar, kPa veya psi) ayarlanır.

## 5. Kurulum kaç adımda ve kaynağı belli mi?

- **Sorun:** Kurulum için bilgisayar gerekiyor mu? Dosyayı nereden alıyorum? Dosyanın özeti yayımlanıyor mu?
- **Yoldaş'ta:** APK her zaman [indirme sayfasından](https://yoldas.io/indir) alınır; özeti orada yayımlanır ve [nasıl doğrulanacağı](https://yoldas.io/rehber/apk-sha256-dogrulama) anlatılır. Kurulum [USB bellekle](https://yoldas.io/rehber/byd-usb-ile-apk-yukleme) ya da ADB ile yapılır; yardımcı bileşen araç ekranından, bilgisayarsız kurulur.

## 6. Güncelleme güvenli mi?

- **Sorun:** Güncelleme HTTPS ile mi iniyor? Kurulmadan önce imza ve paket adı denetleniyor mu? Eski bir sürüm yeniymiş gibi kurulabilir mi?
- **Yoldaş'ta:** bütün sürümler aynı anahtarla imzalanır. Güncelleme yalnız HTTPS üzerinden, Wi-Fi'de ya da aracın kendi mobil verisinde iner (dolaşımdayken mobil veriyle inmez); kurmadan önce bütünlük, paket adı, sürüm numarası ve imza denetlenir. Eski sürüm yeniymiş gibi kurulmaz.

## 7. İzinler ne kadar ve neden?

- **Sorun:** Hangi izinleri istiyor ve her birinin açık bir gerekçesi var mı? Mikrofon ve konum ayrı onayla mı?
- **Yoldaş'ta:** kamera, mikrofon, konum, diğer uygulamaların üzerinde gösterme ve bildirim izinleri tek tek listelenir. Mikrofon kabin sesini dinleme ya da konuşmayı açarsanız ve sesli dashcam kaydında kullanılır; konum ayrı onayla kullanılır.

## 8. Park hâlinde aracın enerjisini koruyor mu?

Park hâlinde çalışan uygulama 12 V aküyü ve çekiş bataryasını tüketebilir. Uygulamanın bir alt sınırı olmalı.

- **Sorun:** Pil ya da 12 V akü düşünce uygulama kendini durduruyor mu?
- **Yoldaş'ta:** park hâlinde bağlantı desteğinde varsayılan olarak pil ve 12 V akü sınırı yoktur ("Sınır yok"). İsterseniz pil için %10–60, akü için 11–13 V arasında bir alt sınır koyarsınız; sınırın altına inince bağlantı bırakılır. Şarj kablosu takılıyken sınır aranmaz. Ayrıntılar [kurulum rehberinde](https://yoldas.io/byd-uygulama-yukleme).

## Kurduktan sonra üç günlük kısa test

1. **İlk gün**

Kurulumu bitirin, izinleri verin ve bir kısa sürüş kaydı alın. Kaydı telefonda açın.
2. **İkinci gün**

Aracı birkaç saat park edin. Dönünce park kaydının ve bildirimlerin gelip gelmediğine bakın.
3. **Üçüncü gün**

Aracı kapatıp açın, uygulamanın kendiliğinden başladığını ve kaydın sürdüğünü görün. Araç aküsünü ve pil yüzdesini park öncesi ve sonrası karşılaştırın.

Sorularınız için [iletisim@yoldas.io](mailto:iletisim@yoldas.io) adresine yazabilirsiniz. Yoldaş'ın özellikleri için [Özellikler](https://yoldas.io/ozellikler) sayfasına bakın.

## Sık sorulan sorular

### BYD için araç uygulamasını nasıl seçerim?

Önce uygulamanın aracınızın yazılım sürümünde ve modelinde neyi desteklediğine bakın, sonra kaydın güvenilirliğini, verinin nerede durduğunu, dil desteğini ve güncellemelerin imzalı olup olmadığını kontrol edin. Aşağıdaki liste bu ölçütleri soru olarak sıralar.

### Kayıt güvenilirliğini nasıl sınarım?

Aracı park edip birkaç saat bırakın; dönünce kayıtların kesintisiz olup olmadığına bakın. Aracı kapatıp açın ve kaydın kendiliğinden sürüp sürmediğini görün. Kayıt alanı dolunca eski kayıtlara ne olduğunu ve önemli klibi koruyabildiğinizi denetleyin.

### Bir araç uygulamasının güvenli olduğunu nasıl anlarım?

İzin listesine bakın ve her iznin gerekçesi var mı kontrol edin. Güncellemenin HTTPS ile indiğini, imzasının denetlendiğini ve kurulum dosyasının özetinin yayımlandığını doğrulayın. Gizlilik sayfasında hangi verinin toplandığı ve nasıl silineceği yazılı olmalı.

## Diğer rehberler

### [BYD kameraları kayıt yapıyor mu?](https://yoldas.io/rehber/byd-kamera-kayit-yapiyor-mu)

BYD'nin kendi kayıt cihazı hangi modelde var, 360° kameralar neden kaydetmiyor ve ek dashcam almadan dört kamerayla kayıt.

### [BYD için en iyi uygulamalar](https://yoldas.io/rehber/byd-icin-en-iyi-uygulamalar)

Harita, müzik, video, dashcam ve telefondan kontrol için BYD ekranında işe yarayan uygulamalar.

### [BYD'de YouTube, Netflix, Google Maps](https://yoldas.io/rehber/byd-youtube-netflix-google-maps)

BYD ekranında hangi uygulamalar yerleşik, hangileri kurulur; Google Maps'i göstergeye almak, şarjda YouTube izlemek.

### [BYD CarPlay ve Android Auto](https://yoldas.io/rehber/byd-carplay-android-auto)

Hangi BYD'de kablolu ya da kablosuz, nasıl bağlanır ve CarPlay haritasını direksiyonun arkasındaki göstergeye almak.

### [BYD'de nöbetçi modu var mı?](https://yoldas.io/rehber/byd-nobetci-modu-var-mi)

BYD'nin kendi nöbetçi modu hangi pazarda var, hangisinde yok; park hâlindeki aracı Yoldaş'la izlemek.

### [BYD'ye APK yüklenmiyor](https://yoldas.io/rehber/byd-apk-yuklenmiyor)

Hata mesajları ne anlama gelir, 2310 sonrası sürümlerde ne değişti ve kilitli ekrana uygulama nasıl kuruluyor.

### [BYD güncellemesinden önce ve sonra](https://yoldas.io/rehber/byd-yazilim-guncellemesi)

BYD güncellemesi gelince yüklü uygulamalara ne olabilir, kurmadan önce neyi kaydetmelisiniz, sonra Yoldaş'ı nasıl geri getirirsiniz.

### [BYD 360 kamera](https://yoldas.io/rehber/byd-360-kamera)

360° kamerayı açmanın yolları, şeffaf şasi görünümü ve dört kamerayı telefondan canlı izlemek, kaydetmek.

### [BYD 12 V akü bitti](https://yoldas.io/rehber/byd-12v-aku)

12 V akü bitince ne olur, nasıl açılır, BYD aküyü ne zaman kendisi şarj eder ve voltajı her an izlemek.

### [BYD lastik basıncı](https://yoldas.io/rehber/byd-lastik-basinci)

Model model önerilen soğuk lastik basınçları (bar, kPa, psi) ve basıncı ekranda ya da telefonda görmenin yolu.

### [BYD uygulaması bağlanmıyor](https://yoldas.io/rehber/byd-uygulamasi-baglanmiyor)

Resmî BYD uygulamasında araç ekleme, bağlantı ve servis hatalarına karşı denenecekler; BYD'den bağımsız telefon uygulaması.

### [Sealion 7 ve DiLink 5'e kurulum](https://yoldas.io/rehber/sealion-7-dilink-5-uygulama-kurma)

DiLink 5'i nasıl tanırsınız, BYD sahiplerinin kullandığı iki kurulum yolu ve kurulumdan sonra açılması gereken ayarlar.

### [BYD DiLink 3, 4 ve 5 nedir?](https://yoldas.io/rehber/byd-dilink-3-4-5)

DiLink neslini ve yazılım sürümünüzü nasıl öğrenirsiniz; sürümün ilk basamakları Yoldaş'ta neyi belirler.

### [BYD ekran döndürme](https://yoldas.io/rehber/byd-ekran-dondurme)

Döner ekranı yatay ve dikeye almanın yolları, hangi modellerde ekran döner ve direksiyonda tuşu olmayan araçlar için kısayol.

### [BYD'ye USB bellekle APK yükleme](https://yoldas.io/rehber/byd-usb-ile-apk-yukleme)

APK'yı bilgisayarda USB belleğe kopyalayıp araç ekranında açın. Adım adım, izin sorusu ve sık sorunlarla.

### [APK dosyasının SHA-256 özeti nasıl doğrulanır?](https://yoldas.io/rehber/apk-sha256-dogrulama)

İndirdiğiniz APK'nın özetini bilgisayarda hesaplayıp indirme sayfasındaki değerle karşılaştırın.

### [Otomasyonlar: ne işe yarar, nasıl kullanılır](https://yoldas.io/rehber/otomasyonlar-nasil-kullanilir)

Tetik, koşul ve adımların ne demek olduğunu, ilk otomasyonun nasıl kurulacağını ve dosyadan nasıl alınacağını öğrenin.

### [Şarj fiyatı ve yolculuk maliyeti](https://yoldas.io/rehber/sarj-fiyati-ve-yolculuk-maliyeti)

Her şarja kendi fiyatını girin, yolculuk maliyetini şarj fiyatlarınıza göre görün.
