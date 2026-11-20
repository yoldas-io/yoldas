# BYD DiLink 3, 4 ve 5 nedir? Hangi modelde hangi sürüm?

DiLink, BYD'nin araç ekranındaki Android tabanlı platformun adıdır. "3", "4" ve "5" bu platformun nesilleridir. Bu rehber nesillerin ne anlama geldiğini, sürümünüzü nasıl öğreneceğinizi ve Yoldaş'ın sürüm numarasına göre ne yaptığını kaynaklarıyla anlatır.

Son güncelleme: 19 Kasım 2026

## Önce bilmeniz gereken: model adı sürümü kesin belirlemez

BYD, resmî DiLink destek sayfasında nesil ve model eşleşmesini veren bir tablo yayımlamıyor; sayfa yalnız platformun genel özelliklerini ve DiLink'li modelleri sayıyor. Topluluk kaynakları da aynı model için üretim yılına göre farklı nesiller listeliyor. Bu yüzden bu rehber model adına bakıp "şu modelde şu sürüm vardır" demez. Doğru yol, aracınızın kendi yazılım sürümünü okumaktır; aşağıda nasıl yapıldığını bulursunuz. Her modelin kendi sayfasında ise Yoldaş'ın o model için bildiği platform ve ekran bilgisi yer alır.

## DiLink nedir?

DiLink, BYD araçlarındaki dokunmatik multimedya ekranının yazılım platformudur. Android üzerine kuruludur; araç ayarları, uygulamalar, kamera görüntüleri ve BYD'nin bulut hizmetleri bu platformdan geçer. BYD'nin kendi destek sayfası platformu Android tabanlı akıllı sistem, bölünebilen uygulama ekranı, açık ve koyu tema ile bulut üzerinden araç kontrolü gibi başlıklarla tanıtır. Yoldaş da bu ekrana kurulan bir Android uygulamasıdır.

## 3, 4 ve 5: nesiller

Bir topluluk tablosuna göre nesiller şöyle ayrılıyor. Resmî bir tablo olmadığı için bunu kesin değil, yön gösterici olarak okuyun.
NesilAndroid sürümüArayüz sürümü DiLink 3.0Android 104.0 ve 5.0 DiLink 4.0Android 104.0 DiLink 5.0Android 12L5.0

Tabloda 3.0 ve 4.0'ın aynı Android sürümünü kullanması dikkat çekicidir: iki nesil arasındaki fark çoğunlukla arayüz ve işlemcidedir. Yoldaş nesil adına değil yazılım sürümünün başına bakar: 13 ile başlayanı DiLink 3, 51 ile başlayanı DiLink 5 olarak tanır. DiLink 4 için ayrı bir yol yoktur.

## Sürümünüzü nasıl öğrenirsiniz?

İki ayrı numara vardır ve sık karıştırılır:

- **Nesil (3, 4, 5):** BYD'nin platform adı. Aracın ekranında çoğu zaman yazmaz.
- **Yazılım sürümü:** araç ayarlarının sistem bilgisi bölümünde yazan uzun numara. Örnek biçim: `13.1.33.2606100.1`. İlk basamaklar platform grubunu gösterir; son basamaklar yapım tarihini ve sürüm sırasını taşır.

Yoldaş'ın kurulum rehberi de önce yazılım sürümünüzü öğrenmenizi ister: [BYD'ye uygulama yükleme](https://yoldas.io/byd-uygulama-yukleme). Yoldaş kuruluysa **Sistem › Tanılama ve kayıt** bölümündeki Uyumluluk raporu platformu, yazılım sürümünü ve ekran bilgilerini tek yerde toplar. Rapor şasi numarası, seri numarası ya da konum içermez.

## Sürüm numarasının ilk basamakları Yoldaş'ta neyi belirler?

Yoldaş platformu önce yazılım sürümünün başına bakarak belirler. Gözlenen örnekler:

- **13.1.33 ile başlayan:** Yoldaş'ın geliştirildiği BYD Seal'de okunan grup (13.1.33.2606100.1).
- **13.1.32 ile başlayan:** Dolphin için yayımlanmış bir teknik incelemede bu grup görülür (13.1.32.2507250.1). Atto 3 ve Dolphin sahipleri çoğunlukla bu gruptadır.
- **51 ile başlayan:** Yoldaş bunu DiLink 5 olarak tanır ve DiLink 5 yolunu kullanır. Sealion 7 ve yeni üretim bazı modeller bu platformdadır.
Sürüm numarasıKamera, dashcam, nöbetçiCam ve diğer uzaktan komutlarKadrana aktarım 13 ile başlıyor (DiLink 3)VarVarVar 51 ile başlıyor (DiLink 5)VarVarVar

Özellikler aracın donanımına ve yazılım sürümüne göre küçük farklar gösterebilir. Bir şey beklediğiniz gibi çalışmazsa bize yazın.

## Modelinize göre ayrıntı

Platform, yazılım grubu, ekran ve desteklenen özellikler her model sayfasında ayrı yazılıdır:

- [BYD Seal](https://yoldas.io/byd-seal), [Seal U EV](https://yoldas.io/byd-seal-u-ev) ve [Seal U DM-i](https://yoldas.io/byd-seal-u-dm-i)
- [Atto 3](https://yoldas.io/byd-atto-3), [Atto 2](https://yoldas.io/byd-atto-2) ve [Dolphin](https://yoldas.io/byd-dolphin)
- [Han](https://yoldas.io/byd-han) ve [Tang](https://yoldas.io/byd-tang)
- [Sealion 7](https://yoldas.io/byd-sealion-7)

Kadran özelliğinin ne yaptığı için [Kadrana aktarım](https://yoldas.io/ozellikler/kadrana-harita) sayfasına bakın. Uygulamayı kurmaya hazırsanız [USB bellekle yükleme rehberi](https://yoldas.io/rehber/byd-usb-ile-apk-yukleme) ve [indirme sayfası](https://yoldas.io/indir) sıradaki adımdır.

## Kaynaklar

- BYD resmî DiLink destek sayfası (platform tanıtımı; nesil tablosu içermez): [byd.com/en-ma/support/dilink](https://www.byd.com/en-ma/support/dilink)
- DiLink nesilleri için topluluk tablosu (Android ve arayüz sürümleri): [bydhack.com/en/systems](https://bydhack.com/en/systems)
- Dolphin multimedya ünitesi teknik incelemesi (DiLink 3.0, Android 10, yazılım sürümü örneği): [github.com/wheregoes/byd-dolphin-hacking](https://github.com/wheregoes/byd-dolphin-hacking)
- Yoldaş'ın geliştirme aracından alınan ölçümler (Seal, yazılım 13.1.33.2606100.1).

## Sık sorulan sorular

### DiLink 3, 4 ve 5 aynı şey mi?

Hayır. Üçü de BYD'nin Android tabanlı multimedya platformunun nesilleridir. Nesil numarası arayüzü, Android sürümünü ve işlemciyi etkiler. Aynı model adı üretim yılına ve pazara göre farklı nesille gelebilir; bu yüzden kesin bilgi aracınızın kendi sistem bilgisindedir.

### BYD'mde DiLink sürümünü nereden görürüm?

Araç ayarlarının sistem bilgisi bölümünde multimedya yazılım sürümü yazar (ör. 13.1.33.2606100.1 biçiminde). Menü adları modele ve yazılıma göre değişebilir. Yoldaş'ta Sistem › Tanılama ve kayıt bölümündeki Uyumluluk raporu da platformu ve yazılım sürümünü gösterir.

### Yazılım sürümüm 13 ile başlıyor. Yoldaş çalışır mı?

Evet. 13 ile başlayan sürümlerde Yoldaş DiLink 3 yolunu kullanır: kameralar, dashcam, nöbetçi, kadrana aktarım ve telefondan kontrol çalışır.

### Yazılım sürümüm 51 ile başlıyor. Ne olur?

Yoldaş bu sürümü DiLink 5 olarak tanır ve DiLink 5 yolunu kullanır. Kameralar, dashcam, nöbetçi, kadrana aktarım ve telefondan kontrol bu platformda da çalışır.

## Diğer rehberler

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

### [BYD'ye USB bellekle APK yükleme](https://yoldas.io/rehber/byd-usb-ile-apk-yukleme)

APK'yı bilgisayarda USB belleğe kopyalayıp araç ekranında açın. Adım adım, izin sorusu ve sık sorunlarla.

### [APK dosyasının SHA-256 özeti nasıl doğrulanır?](https://yoldas.io/rehber/apk-sha256-dogrulama)

İndirdiğiniz APK'nın özetini bilgisayarda hesaplayıp indirme sayfasındaki değerle karşılaştırın.

### [BYD için araç uygulaması nasıl seçilir?](https://yoldas.io/rehber/byd-icin-arac-uygulamasi-secimi)

Kayıt güvenilirliği, verinin nerede durduğu, dil, kurulum ve güncelleme imzası için kontrol listesi.

### [Otomasyonlar: ne işe yarar, nasıl kullanılır](https://yoldas.io/rehber/otomasyonlar-nasil-kullanilir)

Tetik, koşul ve adımların ne demek olduğunu, ilk otomasyonun nasıl kurulacağını ve dosyadan nasıl alınacağını öğrenin.

### [Şarj fiyatı ve yolculuk maliyeti](https://yoldas.io/rehber/sarj-fiyati-ve-yolculuk-maliyeti)

Her şarja kendi fiyatını girin, yolculuk maliyetini şarj fiyatlarınıza göre görün.
