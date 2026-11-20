# BYD'ye USB bellekle uygulama (APK) yükleme

BYD'nin multimedya ekranı Android ile çalışır ve uygulamalar APK dosyasıyla kurulur. En kolay yol APK'yı bilgisayarda bir USB belleğe kopyalayıp araç ekranında açmaktır. Bu rehber o yolu adım adım anlatır.

Son güncelleme: 15 Ekim 2026

## Başlamadan önce

- **Bir bilgisayar ve bir USB bellek.** APK'yı bilgisayarda belleğe kopyalarsınız.
- **Güncel APK.** Dosya her zaman [yoldas.io/indir](https://yoldas.io/indir) adresindedir. Başka bir kaynaktan aldığınız dosyayı kurmayın.
- **Aracınızın yazılım sürümü.** Hangi özelliklerin açılacağını sürümün ilk basamakları belirler. Nasıl öğrenileceği için [DiLink rehberine](https://yoldas.io/rehber/byd-dilink-3-4-5) bakın.
- **Araç P'de.** Kurulum sırasında ekrana dokunmanız gerekir.

## Adım adım

1. **APK'yı bilgisayarınıza indirin**

[İndirme sayfasından](https://yoldas.io/indir) Yoldaş araç APK'sının güncel sürümünü bilgisayarınıza indirin. Dilerseniz [SHA-256 özetini doğrulayın](https://yoldas.io/rehber/apk-sha256-dogrulama).
2. **Dosyayı USB belleğe kopyalayın**

APK dosyasını bir USB belleğe kopyalayın. Kopyalama bitince belleği bilgisayardan güvenli biçimde çıkarın.
3. **Aracı P'ye alın ve belleği takın**

Aracı park konumunda (P) tutun ve belleği aracın USB girişine takın. Kurulum sırasında ekrana dokunmanız gerekir.
4. **Dosyalar uygulamasında APK'yı açın**

Araç ekranındaki dosya yöneticisinde (Dosyalar) USB belleği bulun ve APK dosyasına dokunun.
5. **Kuruluma izin verin**

"Bilinmeyen kaynaklardan yüklemeye izin ver" sorusu çıkarsa izin verin, sonra "Yükle"ye dokunun.
6. **Yoldaş'ı açıp izinleri verin**

Yoldaş ilk açılışta kamera ve ses izinlerini ayrı ayrı sorar. Kullanacağınız özelliklerin izinlerini verin.
7. **Telefonu eşleyin**

Telefonda app.yoldas.io adresini açın, ana ekrana ekleyin ve araç ekranındaki karekodu okutun.

## "Yükle" düğmesi çıkmıyorsa

APK'ya dokunduğunuzda kurulum penceresi açılmıyor ya da "Yükle" düğmesi görünmüyorsa ikinci yolu kullanın: bilgisayardan ADB ile kurulum. Gerekli geliştirici ayarları ve komutlar [BYD'ye uygulama yükleme rehberinde](https://yoldas.io/byd-uygulama-yukleme) (Yol 2) anlatılıyor. Aynı sayfada kurulumdan sonraki ilk ayarlar da var.

## Kurulumdan sonra

- **Arka planda çalışma:** Yoldaş'ta **Sistem › Arka planda çalışma** kartından "Pil kısıtlaması dışında" ve "Otomatik başlatma desteği" ayarlarını açın. Böylece veriler kesintisiz gelir.
- **Yoldaş yardımcısı:** kadrana aktarım, özel alt çubuk ve nöbet ekran uyarısı için araç ekranından, bilgisayarsız kurulur. [Ayrıntılar](https://yoldas.io/byd-uygulama-yukleme#yardimci)
- **Hangi özellikler açık?** Modelinizin sayfasında yazar: [Seal](https://yoldas.io/byd-seal), [Atto 3](https://yoldas.io/byd-atto-3), [Dolphin](https://yoldas.io/byd-dolphin), [Seal U DM-i](https://yoldas.io/byd-seal-u-dm-i) ve diğerleri.

## Sık karşılaşılan sorunlar

### "Uygulama yüklenmedi" hatası

Dosya yarım kopyalanmış ya da yarım inmiş olabilir. APK'yı indirme sayfasından yeniden indirip belleğe yeniden kopyalayın. Aynı adlı bir uygulama başka bir kaynaktan kurulmuşsa önce onu kaldırın.

### Araç belleği görmüyor

Belleği çıkarıp yeniden takın ya da başka bir USB bellek deneyin. Yine olmazsa ADB yolunu kullanın.

### BYD güncellemesinden sonra uygulama kayboldu

Bazı BYD güncellemeleri sonradan kurulan uygulamaları kaldırır. Yoldaş'ı yeniden kurup telefonunuzla yeniden eşleyin. Sunucuya yedeklenen geçmişiniz ve tercihleriniz yerinde durur.

## Sık sorulan sorular

### USB bellekle yükleme her BYD'de çalışır mı?

Araç yazılım sürümüne göre değişir. Dosyalar uygulamasında APK'ya dokunduğunuzda "Yükle" düğmesi çıkmıyorsa bilgisayardan ADB ile kurmanız gerekir; adımlar [uygulama yükleme rehberinde](https://yoldas.io/byd-uygulama-yukleme).

### BYD'de neden Google Play yok?

Türkiye'de satılan BYD'lerin multimedya ekranında Google Play yoktur. Uygulamalar APK dosyası olarak kurulur.

### Kurulum ne kadar sürer?

Araç ekranından kurulum birkaç dakika sürer. Telefonla eşleme dahil yaklaşık 10 dakikada bitirirsiniz.

### USB ile kurduktan sonra güncellemeler nasıl gelir?

Yoldaş yeni sürümü Wi-Fi'de ya da aracın kendi mobil verisinde kendisi indirir ve imzasını denetler; dolaşımdayken mobil veriyle indirmez. "Onay sormadan kur" açıksa dokunmanız gerekmez, kapalıysa araç ekranında "Yükle"ye bir kez dokunursunuz. Sonrasında Yoldaş kendiliğinden yeniden başlar. USB belleği yeniden takmanız gerekmez.

## Diğer rehberler

### [BYD DiLink 3, 4 ve 5 nedir?](https://yoldas.io/rehber/byd-dilink-3-4-5)

DiLink neslini ve yazılım sürümünüzü nasıl öğrenirsiniz; sürümün ilk basamakları Yoldaş'ta neyi belirler.

### [BYD'ye APK yüklenmiyor](https://yoldas.io/rehber/byd-apk-yuklenmiyor)

Hata mesajları ne anlama gelir, 2310 sonrası sürümlerde ne değişti ve kilitli ekrana uygulama nasıl kuruluyor.

### [Sealion 7 ve DiLink 5'e kurulum](https://yoldas.io/rehber/sealion-7-dilink-5-uygulama-kurma)

DiLink 5'i nasıl tanırsınız, BYD sahiplerinin kullandığı iki kurulum yolu ve kurulumdan sonra açılması gereken ayarlar.

### [BYD güncellemesinden önce ve sonra](https://yoldas.io/rehber/byd-yazilim-guncellemesi)

BYD güncellemesi gelince yüklü uygulamalara ne olabilir, kurmadan önce neyi kaydetmelisiniz, sonra Yoldaş'ı nasıl geri getirirsiniz.

### [BYD'de nöbetçi modu var mı?](https://yoldas.io/rehber/byd-nobetci-modu-var-mi)

BYD'nin kendi nöbetçi modu hangi pazarda var, hangisinde yok; park hâlindeki aracı Yoldaş'la izlemek.

### [BYD kameraları kayıt yapıyor mu?](https://yoldas.io/rehber/byd-kamera-kayit-yapiyor-mu)

BYD'nin kendi kayıt cihazı hangi modelde var, 360° kameralar neden kaydetmiyor ve ek dashcam almadan dört kamerayla kayıt.

### [BYD ekran döndürme](https://yoldas.io/rehber/byd-ekran-dondurme)

Döner ekranı yatay ve dikeye almanın yolları, hangi modellerde ekran döner ve direksiyonda tuşu olmayan araçlar için kısayol.

### [BYD lastik basıncı](https://yoldas.io/rehber/byd-lastik-basinci)

Model model önerilen soğuk lastik basınçları (bar, kPa, psi) ve basıncı ekranda ya da telefonda görmenin yolu.

### [BYD uygulaması bağlanmıyor](https://yoldas.io/rehber/byd-uygulamasi-baglanmiyor)

Resmî BYD uygulamasında araç ekleme, bağlantı ve servis hatalarına karşı denenecekler; BYD'den bağımsız telefon uygulaması.

### [APK dosyasının SHA-256 özeti nasıl doğrulanır?](https://yoldas.io/rehber/apk-sha256-dogrulama)

İndirdiğiniz APK'nın özetini bilgisayarda hesaplayıp indirme sayfasındaki değerle karşılaştırın.

### [BYD için araç uygulaması nasıl seçilir?](https://yoldas.io/rehber/byd-icin-arac-uygulamasi-secimi)

Kayıt güvenilirliği, verinin nerede durduğu, dil, kurulum ve güncelleme imzası için kontrol listesi.

### [Otomasyonlar: ne işe yarar, nasıl kullanılır](https://yoldas.io/rehber/otomasyonlar-nasil-kullanilir)

Tetik, koşul ve adımların ne demek olduğunu, ilk otomasyonun nasıl kurulacağını ve dosyadan nasıl alınacağını öğrenin.

### [Şarj fiyatı ve yolculuk maliyeti](https://yoldas.io/rehber/sarj-fiyati-ve-yolculuk-maliyeti)

Her şarja kendi fiyatını girin, yolculuk maliyetini şarj fiyatlarınıza göre görün.

[Debug modu ve Yoldaş yardımcısı](https://yoldas.io/byd-uygulama-yukleme#debug-kurulumu)
