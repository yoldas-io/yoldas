# Sealion 7 ve DiLink 5'e uygulama kurma (APK)

BYD Sealion 7, Tang 2025 ve DiLink 5'li yeni araçlarda uygulama kurma yolu DiLink 3'ten farklıdır. Bu rehber DiLink 5'i nasıl tanıyacağınızı, BYD sahiplerinin kullandığı iki kurulum yolunu ve kurulumdan sonra açmanız gereken ayarları anlatır.

Son güncelleme: 20 Kasım 2026

## Aracınız DiLink 5 mi?

Araç ayarlarının sistem bilgisi bölümündeki multimedya yazılım sürümüne bakın:

- **51 ile başlıyorsa** (örneğin 51.1.2.2411280.1): DiLink 5. Sealion 7 ve Tang 2025 bu gruptadır.
- **23 ile başlıyorsa:** bazı 2025 üretimi Seal ve Seal U'larda görülen DiLink 5 grubu.
- **13 ile başlıyorsa:** DiLink 3; [APK yüklenmiyor rehberine](https://yoldas.io/rehber/byd-apk-yuklenmiyor) bakın.

DiLink 5 araçlar modele göre Android 11 ya da 12 kullanır. Yoldaş iki grupta da çalışır; DiLink 5 yolunu sürüm numarasından kendisi seçer ([DiLink 3, 4 ve 5 rehberi](https://yoldas.io/rehber/byd-dilink-3-4-5)).

## Yol 1: USB klasörü (bilgisayarsız)

BYD sahiplerinin bildirdiğine göre 51 ile başlayan Global ve Türkiye yazılımlarında çalışan yol budur:

1. **Klasörü hazırlayın**

Bir USB belleğin köküne ülke kodunuzla adlandırılmış bir klasör açın: Türkiye için "Third Party Apps 90". Yoldaş APK'sını [indirme sayfasından](https://yoldas.io/indir) alıp bu klasöre koyun.
2. **Belleği takın**

Araç açık ve P'deyken belleği takın. Araç bir şifre sorar; şifre BYD'nin servis bilgisidir, sitede yazmıyoruz. Bilmiyorsanız bize yazın.
3. **Kurulumu bekleyin**

Şifre kabul edilince araç klasördeki uygulamaları kurar. Yoldaş'ı açıp ilk açılış izinlerini verin.

DiLink 5'te kalıcı bir kilit açıcı kurulamadığı bildiriliyor; bu yüzden başka uygulamaları da aynı klasörden kurarsınız.

## Yol 2: Gizli geliştirici sayfası ve kablosuz ADB

Avustralya'daki bir Sealion 7 sahibi, yazılım sürümü ekranındaki fabrika ayarlarına dönme yazısına art arda dokununca gizli bir geliştirici sayfasının açıldığını bildirdi. Aynı menüler Fas ve Almanya'daki araçlarda da görüldü. Bu sayfadan kablosuz ADB açılıp bilgisayardan `adb install` ile kurulum yapılabiliyor.
**Sıfırla düğmelerine dokunmayın**

Gizli sayfadaki iki mavi sıfırlama düğmesi aracı fabrika ayarına döndürür. Yalnız hata ayıklama anahtarlarını kullanın.

Aynı bildirime göre o araçta kablosuz ADB park ettikten sonra kendiliğinden kapanıyor ve ekrandan kurulum "bilinmeyen kaynak" diye reddediliyor; ADB her seferinde yeniden açılmalı.
**Yoldaş DiLink 5'te de çalışır**

Sealion 7 ve diğer DiLink 5'li BYD'lerde Yoldaş'la nöbetçi, aracın kameralarıyla kayıt, kadranda harita ve telefondan kontrol tek uygulamada.

[Yoldaş'ı indir](https://yoldas.io/indir/yoldas-arac-321.apk) [Yoldaş ve Sealion 7](https://yoldas.io/byd-sealion-7)

## Kurulumdan sonra açılması gereken ayarlar

- **Arka planda çalışma:** BYD ayarlarında Yoldaş için arka plan uygulamalarını ve otomatik başlatmayı devre dışı bırakan seçenekler kapalı olmalı. Yoldaş'ta **Sistem › Arka planda çalışma** kartını kontrol edin.
- **Uyku:** DiLink 5 ana ünitesi araç kapandıktan yaklaşık 10 dakika sonra uyur; bu süreden sonra hiçbir uygulama çalışmaz.
- **Mobil veri:** bazı DiLink 5 yazılımlarında sonradan kurulan uygulamaların mobil verisi kısıtlanıyor. Telefon bağlantısı gelmiyorsa aracı Wi-Fi'ye bağlayıp deneyin ve bize yazın.
- **Telefon:** app.yoldas.io'yu açıp araç ekranındaki karekodu okutun.

## Avrupa yazılımı (OTA 3.3)

Avrupa'da satılan ve OTA 3.3 sürümlü Sealion 7'ler için güvenilir bir kurulum bildirimi bulamadık. Aracınız bu gruptaysa ve bir yol denediyseniz ya da takıldıysanız [iletisim@yoldas.io](mailto:iletisim@yoldas.io) adresine yazın; rehberi sizinle birlikte güncelleriz.

## Kaynaklar

- BYD sahiplerinin forumu, Sealion 7'ye uygulama kurma: [byd.forum](https://byd.forum/topic/8-sealion-7-installing-apps/)
- Avustralya'daki Sealion 7 için geliştirici sayfası notları: [github.com/jasoisjaso/byd-sealion7](https://github.com/jasoisjaso/byd-sealion7)

## Sık sorulan sorular

### Sealion 7'ye uygulama kurulabilir mi?

Evet. BYD sahiplerinin bildirdiğine göre 51 ile başlayan yazılımlı Sealion 7 ve Tang'larda (Global ve Türkiye sürümü) USB klasörü yoluyla bilgisayarsız kurulum yapılıyor.

### DiLink 5'te ADB gerekir mi?

USB klasörü yolunda gerekmez. Kablosuz ADB'yi açan bir gizli geliştirici sayfası da bildirildi; ama o sayfadaki sıfırlama düğmeleri aracı fabrika ayarına döndürür, dikkatli olun.

### Yoldaş DiLink 5'te güncellemeleri nasıl alır?

Yoldaş yeni sürümlerini kendisi indirir. Aracınızın yazılımı ekrandan kurulumu reddederse güncellemeyi de aynı USB klasörü yoluyla yaparsınız: yeni APK'yı klasöre koyup belleği takın.

### Avrupa yazılımlı Sealion 7'ye kurulum yapılabiliyor mu?

OTA 3.3 sürümlü Avrupa araçları için güvenilir bir kurulum bildirimi bulamadık. Aracınız bu gruptaysa yazılım sürümünüzle birlikte bize yazın.

## Diğer rehberler

### [BYD DiLink 3, 4 ve 5 nedir?](https://yoldas.io/rehber/byd-dilink-3-4-5)

DiLink neslini ve yazılım sürümünüzü nasıl öğrenirsiniz; sürümün ilk basamakları Yoldaş'ta neyi belirler.

### [BYD'ye APK yüklenmiyor](https://yoldas.io/rehber/byd-apk-yuklenmiyor)

Hata mesajları ne anlama gelir, 2310 sonrası sürümlerde ne değişti ve kilitli ekrana uygulama nasıl kuruluyor.

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
