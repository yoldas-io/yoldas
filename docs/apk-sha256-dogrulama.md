# APK dosyasının SHA-256 özeti nasıl doğrulanır?

SHA-256 özeti, bir dosyanın parmak izidir. Yoldaş her sürümün özetini indirme sayfasında yayımlar. İndirdiğiniz dosyadan aynı özeti hesaplayıp karşılaştırırsanız, elinizdeki dosyanın yayımlananla birebir aynı olduğunu bilirsiniz.

Son güncelleme: 6 Ekim 2026

## Neden doğrulanır?

- **Bozuk indirme:** dosya yarım ya da hatalı inmişse özet farklı çıkar; kurulum hatası vermeden önce fark edersiniz.
- **Farklı dosya:** USB bellekle ya da başka bir yoldan getirdiğiniz dosyanın yayımlanan dosya olduğunu doğrularsınız.

Güncel özet değeri yalnız [indirme sayfasında](https://yoldas.io/indir) yayımlanır. Eski kalmasın diye bu rehberde yazmıyoruz.

## Adım adım

1. **Yayımlanan özeti bulun**

[İndirme sayfasındaki](https://yoldas.io/indir) "Dosya parmak izi (SHA-256)" kutusunda 64 karakterlik özet yazar. Kopyala düğmesiyle kopyalayabilirsiniz.
2. **APK'yı bilgisayarınıza indirin**

APK'yı yalnız aynı sayfadaki indirme düğmesiyle indirin ve dosyanın yerini not edin.
3. **Özeti hesaplayın**

Bilgisayarınıza uygun komutu çalıştırın (komutlar aşağıdaki tabloda). Komut 64 karakterlik bir değer yazar.
4. **İki değeri karşılaştırın**

Hesaplanan değer ile sayfadaki değer harfi harfine aynı olmalı. Bazı araçlar büyük harf yazar; harf büyüklüğünü yok sayın.
5. **Sonuca göre ilerleyin**

Değerler aynıysa dosyayı kurabilirsiniz. Farklıysa dosyayı silin, yeniden indirin ve yine farklıysa kurmayın; bize yazın.

## Özeti hesaplama komutları

Komutlardaki dosya adını kendi dosyanızın adıyla değiştirin. Komutu APK'nın bulunduğu klasörde çalıştırın.
SistemKomut Windows (PowerShell)`Get-FileHash .\indirdiğiniz-dosya.apk -Algorithm SHA256` Windows (Komut İstemi)`certutil -hashfile indirdiğiniz-dosya.apk SHA256` macOS`shasum -a 256 indirdiğiniz-dosya.apk` Linux`sha256sum indirdiğiniz-dosya.apk`

## Özet neyi gösterir, neyi göstermez?

- **Gösterir:** dosyanın, özetin yayımlandığı sayfadaki dosyayla aynı olduğunu.
- **Göstermez:** sayfanın kendisinin doğru olduğunu. Bu yüzden APK'yı ve özeti yalnız yoldas.io adresinden, HTTPS ile alın.

## Güncellemelerde ayrıca imza denetlenir

Yoldaş'ın bütün sürümleri aynı anahtarla imzalanır. Yoldaş kendini güncellerken kurmadan önce dosyanın bütünlüğünü, paket adını, sürüm numarasını ve imzasını denetler; eski bir sürümü yeniymiş gibi kurmaz. Ayrıntılar [güvenlik sayfasında](https://yoldas.io/guvenlik).

İsteyen ileri düzey kullanıcılar, Android SDK Build-Tools içindeki `apksigner verify --print-certs` komutuyla iki sürümün imza sertifikasını karşılaştırabilir; aynı anahtarla imzalandıkları için sertifika bilgisi aynı çıkmalıdır.

## Sonraki adım

Özet eşleştiyse dosyayı araca kurabilirsiniz: [USB bellekle APK yükleme](https://yoldas.io/rehber/byd-usb-ile-apk-yukleme) ya da [BYD'ye uygulama yükleme rehberi](https://yoldas.io/byd-uygulama-yukleme).

## Sık sorulan sorular

### SHA-256 özeti nedir?

Bir dosyanın içeriğinden hesaplanan 64 karakterlik parmak izidir. Dosyada tek bir bayt değişse özet tamamen değişir. Aynı dosya her zaman aynı özeti verir.

### Özetler eşleşmezse ne yapmalıyım?

Dosyayı kurmayın. Silip indirme sayfasından yeniden indirin. Yine eşleşmezse bağlantınızı ve adresin yoldas.io olduğunu kontrol edin; sorun sürerse bize yazın.

### Özeti araç ekranında doğrulayabilir miyim?

Rehberdeki komutlar bilgisayar içindir. En rahat yol, APK'yı bilgisayarda indirip doğrulamak ve sonra USB bellekle araca götürmektir.

### Telefon uygulaması için de özet var mı?

Hayır. Telefon tarafı bir web uygulamasıdır, kurulan bir dosyası yoktur. Özet yalnız araç APK'sı içindir.

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

### [BYD için araç uygulaması nasıl seçilir?](https://yoldas.io/rehber/byd-icin-arac-uygulamasi-secimi)

Kayıt güvenilirliği, verinin nerede durduğu, dil, kurulum ve güncelleme imzası için kontrol listesi.

### [Otomasyonlar: ne işe yarar, nasıl kullanılır](https://yoldas.io/rehber/otomasyonlar-nasil-kullanilir)

Tetik, koşul ve adımların ne demek olduğunu, ilk otomasyonun nasıl kurulacağını ve dosyadan nasıl alınacağını öğrenin.

### [Şarj fiyatı ve yolculuk maliyeti](https://yoldas.io/rehber/sarj-fiyati-ve-yolculuk-maliyeti)

Her şarja kendi fiyatını girin, yolculuk maliyetini şarj fiyatlarınıza göre görün.
