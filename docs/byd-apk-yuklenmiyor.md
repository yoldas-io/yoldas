# BYD'ye APK yüklenmiyor: nedenleri ve çözümleri

BYD ekranına uygulama kurarken "yükleme engellendi" türünden bir mesaj mı aldınız? Bu rehber mesajların ne anlama geldiğini, hangi yazılım sürümünde neyin değiştiğini ve BYD sahiplerinin kilitli ekrana uygulamayı hangi yollarla kurduğunu anlatır.

Son güncelleme: 20 Kasım 2026

## Kısaca: sorun dosyada değil, yazılım sürümünde

BYD, 2023 sonunda yayımladığı 2310 yazılımından beri DiLink ekranına dışarıdan uygulama kurmayı kısıtlıyor. 2307 ve öncesinde APK dosya yöneticisinden açılıp doğrudan kurulur. Sonraki sürümlerde BYD'nin yükleyicisi kurulumu reddeder; dosya sağlam olsa da başka bir yol gerekir.

Önce multimedya yazılım sürümünüzü öğrenin: araç ayarlarının sistem bilgisi bölümündeki uzun numara, örneğin `13.1.33.2606100.1`. Dördüncü kümenin ilk dört hanesi (burada 2606) yazılımın tarihidir. Ayrıntı [DiLink 3, 4 ve 5 rehberinde](https://yoldas.io/rehber/byd-dilink-3-4-5). Yazılımınız 51 ile başlıyorsa [Sealion 7 ve DiLink 5 rehberine](https://yoldas.io/rehber/sealion-7-dilink-5-uygulama-kurma) geçin.

## Gördüğünüz mesaja göre

### "For your driving safety and system stability, please do not install third party apps"

Türkçe arayüzde aynı anlamda bir uyarı çıkar. BYD'nin kendi yükleyicisi kurulumu reddediyor. Dosyada bir sorun yok; yazılımınız dışarıdan kurulumu kapatmış. Aşağıdaki "Kilitli ekrana kurulum yolları" bölümüne geçin.

### "Uygulama yüklenmedi"

Dosya yarım inmiş olabilir ya da aynı adlı ama farklı imzalı bir uygulama zaten kuruludur. APK'yı [indirme sayfasından](https://yoldas.io/indir) yeniden indirin, [SHA-256 özetini doğrulayın](https://yoldas.io/rehber/apk-sha256-dogrulama), başka bir kaynaktan kurulmuş eski kopya varsa önce onu kaldırın.

### USB klasörüyle denerken "izin listesinde uygulama yok"

Şifre kabul edildi ama ülkenizin izin listesi bu uygulamayı içermiyor. BYD sahiplerinin bildirdiğine göre yeni DiLink 3 sürümlerinde USB klasörü yolu çoğunlukla buna takılıyor. Bu durumda servis menüsü yoluna geçin.

### Araç tarayıcısında indirme başlamıyor

Bazı sürümlerde (bildirilen örnek: 2507 grubu) araç tarayıcısından indirilen dosyalar sessizce engelleniyor. APK'yı bilgisayarda bir USB belleğe kopyalayın.

### "Yükle" düğmesi yok ya da soluk

Bu da yükleyicinin kurulumu reddettiğini gösterir. Kilitli ekrana kurulum yollarına geçin.

## Yazılım sürümüne göre ne çalışıyor?

BYD bu konuda resmî bir tablo yayımlamıyor. Aşağıdaki tablo BYD sahiplerinin forumlarda ve rehberlerde bildirdiklerinden derlendi; aracınızda farklı olabilir.
Yazılım (DiLink 3/4)USB bellek, dosya yöneticisiUSB klasörü ve şifreServis menüsünden ADB 2307 ve öncesiÇalışırGerekmezGerekmez 2310 – 2501ReddedilirÇoğunlukla çalışırÇalışır 2503 ve sonrasıReddedilirPazara göre değişir, çoğunlukla izin listesine takılırÇalışır; bazı araçlarda QR onayı ister

## Kilitli ekrana kurulum yolları

### 1. USB klasörü ve şifre

USB belleğin kökünde, ülke kodunuzla adlandırılmış bir klasör açılır (Türkiye için "Third Party Apps 90") ve APK içine konur. Bellek takılınca araç bir şifre sorar ve klasördeki uygulamaları kurar. Şifre BYD'nin servis bilgisidir; sitede yazmıyoruz. Yeni sürümlerde bu yol izin listesine takılabilir.

### 2. Servis menüsünden kablosuz hata ayıklama (ADB)

BYD sahiplerinin en çok kullandığı yol budur:

1. **Servis menüsünü açın**

Aracın telefon tuş takımına girilen bir servis koduyla BYD'nin geliştirici araçları açılır.
2. **Şifreyi girin**

Menü, aracın IMEI numarasına ve saatine bağlı bir şifre ister. Araç saati doğru olmalıdır. Bazı araçlarda (çoğunlukla Çin pazarı) şifre yerine ekranda QR kodu çıkar ve uzaktan onay gerekir.
3. **Kablosuz ADB'yi açın**

Açılan Test Tools ekranında kablosuz ADB ve USB hata ayıklama anahtarlarını açın.
4. **Bilgisayardan kurun**

Bilgisayar ve araç aynı Wi-Fi'deyken `adb connect ARAÇ-ADRESİ:5555` ve `adb install yoldas-arac.apk` komutlarını çalıştırın. Ayrıntı [kurulum rehberinde](https://yoldas.io/byd-uygulama-yukleme).

IMEI'nizi tanımadığınız kişilere ve sitelere vermeyin. Yoldaş kurulduktan sonra bu şifreyi aracın içinde kendisi üretir ve yardımcı bağlantısını hazırlar; IMEI ve şifre hiçbir yere gönderilmez ([Debug modu ve Yoldaş yardımcısı](https://yoldas.io/byd-uygulama-yukleme#debug-kurulumu)).

### 3. Sürüm düşürme

BYD sahiplerinin bir kısmı aracı USB'den eski bir yazılıma döndürüp uygulamaları kuruyor, sonra yeniden güncelliyor. Bu işlemde ekran açılmayabilir ve multimedya ayarları sıfırlanır; bazı USB bellekler yeni sürümlerden geri dönüşü başlatamıyor. Yoldaş bu yolu önermez. Diğer yollar olmadıysa önce bize yazın.
**Bir kez kurun, gerisini Yoldaş yapsın**

Yoldaş kurulduktan sonra yeni sürümlerini kendisi indirir ve kurar; her güncellemede bu yollarla uğraşmazsınız. Ana ekran, nöbetçi, dört kameralı kayıt ve telefon uygulaması tek uygulamada.

[Yoldaş'ı indir](https://yoldas.io/indir/yoldas-arac-321.apk) [Bütün özellikler](https://yoldas.io/ozellikler)

## Kurulduktan sonra

- BYD ayarlarında Yoldaş için arka planda çalışmayı ve otomatik başlatmayı engelleyen ayarlar kapalı olmalı; Yoldaş bunu çoğu araçta kendisi düzeltir.
- BYD güncellemeleri kurulu uygulamaları çoğunlukla bırakır ama kurulum yolunu kapatabilir. Güncellemeden önce ne yapacağınız [BYD güncellemesi rehberinde](https://yoldas.io/rehber/byd-yazilim-guncellemesi).
- Yoldaş sonraki sürümlerini kendisi indirir ve kurar; her güncellemede bu yolları yeniden yapmanız gerekmez.

Takıldıysanız [iletisim@yoldas.io](mailto:iletisim@yoldas.io) adresine multimedya yazılım sürümünüzü ve gördüğünüz mesajı yazın.

## Kaynaklar

- BYD Club Italia kurulum kılavuzu (2307/2310 sınırı): [byd-club-italia.github.io](https://byd-club-italia.github.io/byd-club-italia-guides/generale.html)
- Dolphin multimedya ünitesi teknik incelemesi (tarayıcı engeli, izin listesi): [github.com/wheregoes/byd-dolphin-hacking](https://github.com/wheregoes/byd-dolphin-hacking)
- BYD sahiplerinin forumu (Sealion 7 ve DiLink 5 kurulumu): [byd.forum](https://byd.forum/topic/8-sealion-7-installing-apps/)

## Sık sorulan sorular

### BYD'ye neden APK yüklenmiyor?

BYD, 2310 yazılımından beri DiLink ekranına dışarıdan uygulama kurmayı kısıtlıyor. 2307 ve öncesinde APK dosya yöneticisinden doğrudan kurulur; sonraki sürümlerde BYD'nin yükleyicisi kurulumu reddeder ve başka bir yol gerekir.

### "sha256 is invalid" bir BYD hatası mı?

BYD'nin yükleyicisinde böyle bir mesaj bildirilmedi; bu ifade internette başka cihazların yükleme araçlarında geçiyor. İndirdiğiniz Yoldaş dosyasının bozuk olmadığından emin olmak için SHA-256 rehberindeki gibi özetini doğrulayın.

### Kurulum için aracın yazılımını eski sürüme düşürmem gerekir mi?

Çoğu zaman gerekmez. BYD sahiplerinin bir kısmı sürüm düşürüyor ama bu işlemde ekran kilitlenebilir ve multimedya ayarları sıfırlanır. Yoldaş bu yolu önermez; önce aşağıdaki diğer yolları deneyin ya da bize yazın.

### BYD güncellemesinden sonra kurduğum uygulamalar kalır mı?

BYD sahiplerinin bildirdiğine göre olağan güncellemelerde kurulu uygulamalar çoğunlukla kalır; büyük sürüm geçişlerinde ve bayide yapılan yüklemelerde silinebilir. Kurulum yolu da kapanabilir. Ayrıntı BYD güncellemesi rehberinde.

### IMEI'mi başkasına vermem güvenli mi?

Servis menüsünün şifresi IMEI'ye bağlıdır. IMEI'nizi tanımadığınız kişilere ve sitelere vermeyin. Yoldaş kurulduktan sonra bu şifreyi aracın içinde kendisi üretir; IMEI ve şifre hiçbir yere gönderilmez.

## Diğer rehberler

### [BYD kameraları kayıt yapıyor mu?](https://yoldas.io/rehber/byd-kamera-kayit-yapiyor-mu)

BYD'nin kendi kayıt cihazı hangi modelde var, 360° kameralar neden kaydetmiyor ve ek dashcam almadan dört kamerayla kayıt.

### [BYD'de YouTube, Netflix, Google Maps](https://yoldas.io/rehber/byd-youtube-netflix-google-maps)

BYD ekranında hangi uygulamalar yerleşik, hangileri kurulur; Google Maps'i göstergeye almak, şarjda YouTube izlemek.

### [BYD CarPlay ve Android Auto](https://yoldas.io/rehber/byd-carplay-android-auto)

Hangi BYD'de kablolu ya da kablosuz, nasıl bağlanır ve CarPlay haritasını direksiyonun arkasındaki göstergeye almak.

### [BYD'de nöbetçi modu var mı?](https://yoldas.io/rehber/byd-nobetci-modu-var-mi)

BYD'nin kendi nöbetçi modu hangi pazarda var, hangisinde yok; park hâlindeki aracı Yoldaş'la izlemek.

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

### [BYD için araç uygulaması nasıl seçilir?](https://yoldas.io/rehber/byd-icin-arac-uygulamasi-secimi)

Kayıt güvenilirliği, verinin nerede durduğu, dil, kurulum ve güncelleme imzası için kontrol listesi.

### [Otomasyonlar: ne işe yarar, nasıl kullanılır](https://yoldas.io/rehber/otomasyonlar-nasil-kullanilir)

Tetik, koşul ve adımların ne demek olduğunu, ilk otomasyonun nasıl kurulacağını ve dosyadan nasıl alınacağını öğrenin.

### [Şarj fiyatı ve yolculuk maliyeti](https://yoldas.io/rehber/sarj-fiyati-ve-yolculuk-maliyeti)

Her şarja kendi fiyatını girin, yolculuk maliyetini şarj fiyatlarınıza göre görün.
