# BYD'ye uygulama yükleme (APK): adım adım rehber

BYD'nin DiLink multimedya ekranı Android ile çalışır. Yoldaş gibi uygulamalar APK dosyasıyla kurulur. Bu rehberde iki kurulum yolunu ve kurulumdan sonraki ilk ayarları anlatıyoruz.

Son güncelleme: 19 Kasım 2026

[Debug modu ve Yoldaş yardımcısı](#debug-kurulumu)

## Başlamadan önce

- **Yazılım sürümünüzü öğrenin.** Araç ayarlarının sistem bilgisi bölümünde multimedya yazılım sürümü yazar (ör. 13.1.33.2606100.1). Sürüm numarasının ne anlama geldiğini [DiLink 3, 4 ve 5 rehberinde](https://yoldas.io/rehber/byd-dilink-3-4-5) bulursunuz.
- **Aracı P'de park edin.** Kurulum sırasında ekrana dokunmanız gerekir.
- **Aracı Wi-Fi'ye bağlayın.** APK'yı indirmek ve Yoldaş'ın telefonunuza veri göndermesi için internet gerekir.
- **Dosyayı Yoldaş'tan alın.** APK'nın güncel sürümü her zaman [yoldas.io/indir](https://yoldas.io/indir) adresindedir. Dosyanın özetini doğrulamak isterseniz [SHA-256 rehberine](https://yoldas.io/rehber/apk-sha256-dogrulama) bakın.

## Yol 1: APK'yı araç ekranında açmak

1. **APK'yı araca getirin**

Araç tarayıcısıyla [indirme sayfasını](https://yoldas.io/indir) açın ya da APK'yı bilgisayarda bir USB belleğe kopyalayıp araca takın.
2. **Dosyayı açın**

Araç ekranındaki dosya yöneticisinde (Dosyalar) APK'ya dokunun.
3. **Kuruluma izin verin**

"Bilinmeyen kaynaklardan yüklemeye izin ver" sorusu çıkarsa izin verin, sonra "Yükle"ye dokunun.

Bu yolun kısa ve ayrı bir rehberi var: [USB bellekle APK yükleme](https://yoldas.io/rehber/byd-usb-ile-apk-yukleme). "Yükle" düğmesi çıkmazsa ikinci yolu kullanın.

## Yol 2: Bilgisayardan ADB ile kurmak

Bir bilgisayar ve aynı Wi-Fi ağı gerekir. ADB, Android'in resmî geliştirici aracıdır (Android SDK Platform Tools).

1. **Geliştirici seçeneklerini açın**

Araç ayarlarında geliştirici seçeneklerini açın; ardından "USB hata ayıklama" ve ağ üzerinden hata ayıklamayı açın.
2. **Bilgisayardan araca bağlanın**

Aracın ağdaki adresini öğrenin ve bilgisayarda `adb connect ARAÇ-ADRESİ:5555` yazın. Araç ekranında "Hata ayıklamaya izin verilsin mi?" sorusu çıkarsa onaylayın.
3. **APK'yı kurun**

`adb install -r indirdiğiniz-dosya.apk` komutunu çalıştırın. "Success" yazısını görünce kurulum bitmiştir.

## Kurulumdan sonra

1. **İlk açılış izinleri**

Yoldaş ilk açılışta kamera ve ses izinlerini ayrı ayrı sorar. Kullanacağınız özelliklerin izinlerini verin.
2. **Arka planda çalışma**

Yoldaş'ta **Sistem › Arka planda çalışma** kartından "Pil kısıtlaması dışında" ve "Otomatik başlatma desteği" ayarlarını açın. Güncelleme sonrası BYD otomatik başlatma iznini sıfırlarsa Yoldaş bunu kendiliğinden düzeltmeye çalışır; düzelmezse bu kartı kontrol edin. Böylece veriler kesintisiz gelir.
3. **Telefonu eşleyin**

Telefonda app.yoldas.io adresini açın, ana ekrana ekleyin ve araç ekranındaki karekodu okutun.

## Yoldaş yardımcısı

Kadrana aktarım, özel alt çubuk, nöbet ekran uyarısı ve park hâlinde bağlantı desteği Yoldaş yardımcısı ile çalışır. Kurulumu araç ekranından, bilgisayarsız yapılır:

1. **Başlatın**

Yoldaş'ta **Sistem › Yoldaş yardımcısı** sayfasında "Başlat"a dokunun.
2. **İzin verin**

Android'in izin penceresi açılınca bir kez "Her zaman izin ver"i seçin. Bağlantı kurulunca sayfada "Bağlı" yazar.
3. **Kullanın**

Yardımcı bir kez açıldıktan sonra bağlantı koparsa kendiliğinden yeniden denenir. "Bağlantıyı kes" ile istediğiniz an kapatırsınız.

Yardımcı yalnız Yoldaş'ın sabit, izinli komut listesiyle çalışır; dışarıdan genel komut kabul etmez. Yoldaş durursa ya da kaldırılırsa yaptığı sistem ayarlarını geri alır.

### Park hâlinde ve araç kapanınca bağlantı

Telefondan kontrol ve Yoldaş yardımcısı açıkken, araç P'deyken ve kontak kapandıktan sonra da telefonla bağlantının sürmesi için Yoldaş CPU ve Wi-Fi desteğini kendiliğinden sağlar. Varsayılan olarak pil ve 12 V akü için sınır yoktur ("Sınır yok"). İsterseniz Yoldaş'taki "Araç kapalıyken bağlı kal" bölümünden alt sınır koyabilirsiniz: pil için %10 ile %60 arası, 12 V akü için 11 ile 13 V arası. Değer sınırın altına inince bağlantı kendiliğinden durur. Şarj kablosu takılıyken sınır aranmaz.

Bağlantı şu durumlarda da durur: vites P değilse ya da hız sıfır değilse, sistem çok ısındıysa, araç verisi okunamıyorsa. Durma nedeni Yoldaş'ta yazılır. Araç internetsiz kalırsa Yoldaş aracı uyandırmayı dener: ilk 10 dakikada 30 saniyede bir, sonra 2 dakikada bir, en çok 6 saat boyunca.

Uygulama beklenmedik biçimde kapanırsa Yoldaş yardımcısı onu yeniden başlatmayı dener; araç açıkken ve sürüşte de bu geçerlidir, 10 dakikada en çok 6 deneme yapılır. Uygulamayı zorla durdursanız bile yardımcı bağlıysa uygulamayı yeniden başlatır. Yeniden başlatılmayan durumlar: "Bağlantıyı kes" demeniz, uygulamanın kaldırılması ya da güncellenmesi.

## Sık karşılaşılan sorunlar

### "Uygulama yüklenmedi" hatası

Dosya yarım inmiş olabilir; APK'yı [indirme sayfasından](https://yoldas.io/indir) yeniden indirin. Daha önce başka bir kaynaktan kurulmuş aynı adlı bir uygulama varsa önce onu kaldırın.

### "Yükle" düğmesi çıkmıyor

Bilgisayardan ADB ile kurun (Yol 2).

### Telefonda veriler güncellenmiyor

Yukarıdaki "Arka planda çalışma" adımını yapın ve aracın internete bağlı olduğunu kontrol edin. Yoldaş'ta **Sistem › Bağlantı** kartındaki "Bağlantı testi" Wi-Fi'yi ve mobil veriyi ayrı ayrı sınar.

### BYD güncellemesinden sonra uygulama kayboldu

Yoldaş'ı yeniden kurup telefonunuzla yeniden eşleyin. Sunucuya yedeklenen geçmişiniz ve tercihleriniz yerinde durur. Güncellemeden önce ve sonra yapılacaklar: [BYD güncellemesi rehberi](https://yoldas.io/rehber/byd-yazilim-guncellemesi).

Aracınızla ilgili bir sorunuz olursa [iletisim@yoldas.io](mailto:iletisim@yoldas.io) adresine yazın.

## Sık sorulan sorular

### BYD'de Google Play var mı?

Türkiye'de satılan BYD'lerin multimedya ekranında Google Play yoktur. Uygulamalar APK dosyası olarak kurulur.

### BYD güncellemesinden sonra Yoldaş'ı yeniden kurmam gerekir mi?

Bazı BYD güncellemeleri sonradan kurulan uygulamaları kaldırır. Böyle olursa Yoldaş'ı yeniden kurup telefonunuzla eşleyin. Sunucuya yedeklenen geçmişiniz ve tercihleriniz yerinde durur. Yoldaş güncellenince BYD'nin otomatik başlatma izni sıfırlanabilir; Yoldaş bunu kendiliğinden düzeltmeye çalışır.

### Yoldaş güncellemeleri nasıl gelir?

Yoldaş yeni sürümü Wi-Fi'de ya da aracın kendi mobil verisinde kendisi indirir ve imzasını denetler; dolaşımdayken mobil veriyle indirmez. "Onay sormadan kur" açıksa dokunmanız gerekmez, kapalıysa araç ekranında "Yükle"ye bir kez dokunursunuz. Sonrasında Yoldaş kendiliğinden yeniden başlar; güncelleme otomatik başlatma iznini sıfırlarsa Yoldaş bunu kendiliğinden düzeltmeye çalışır.

### Kurulum ne kadar sürer?

Araç ekranından kurulum birkaç dakika sürer. Telefonla eşleme dahil yaklaşık 10 dakikada bitirirsiniz.

## Debug modu ve Yoldaş yardımcısı

Yoldaş 0.12.67 ve sonrasında, desteklenen BYD ekranında şifre araç içinde hesaplanıp girilebilir. Bu adımlar Yoldaş kurulduktan sonra uygulanır. Kurulum sırasında aracı park edin.

1.

Yoldaş’ta Sistem → Yoldaş yardımcısı bölümünü açın ve Bağlantıyı hazırla düğmesine dokunun.
2.

İzin ekranı açılırsa Yoldaş bağlantı kurulumu anahtarını açın. Yoldaş’a geri dönüp Bağlantıyı hazırla düğmesine tekrar dokunun. Bu izin, yalnız sizin başlattığınız BYD kurulumunda ekranı okumak ve şifreyi girmek içindir.
3.

BYD doğrulama ekranında IMEI okunur, şifre araç içinde üretilir ve giriş denenir. IMEI ve şifre sunucuya gönderilmez. Şifre reddedilirse arka arkaya deneme yapılmaz.
4.

TestTools açılınca Wireless adb debug switch açık olmalı. Debug mode when USB is connected anahtarını da açın; Android bir onay sorarsa okuyup onaylayın. İlk bağlantıda Her zaman izin ver seçeneğini işaretleyip izin verin.
5.

Yoldaş’a dönün. Yardımcıda Bağlı yazdığını kontrol edin. Gerekirse Başlat veya Yeniden bağlan düğmesine dokunun. Yoldaş otomatik başlatma ayrı bir servistir; yardımcı bağlandıktan sonra yönetilir.

### Otomatik giriş olmazsa

Yoldaş yardımcısındaki Şifre üret düğmesine dokunun. BYD ekranındaki IMEI’nin son 6 hanesini girin; Şimdi kodunu BYD’nin şifre alanına yazıp giriş yapın. Araç saati doğru olmalı. Şifre reddedilirse tekrar tekrar denemeyin; destek ekibine yazın. Ekran ve anahtar adları araç yazılımına göre değişebilir.

### İzni kaldırma

BYD Ayarlar → Erişilebilirlik hizmetleri bölümünde Yoldaş bağlantı kurulumu anahtarını kapatabilirsiniz. Bu, debug anahtarını kapatmaz. Liste araçta kurulu diğer uygulamaları da gösterir; onlara dokunmanız gerekmez.
