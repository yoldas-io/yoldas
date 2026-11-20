# Otomasyonlar: ne işe yarar, nasıl kullanılır

Otomasyon, "şu olunca, şu koşullarda, şunları sırayla yap" diyen kendi kuralınızdır. Klimayı sabahları kendiliğinden açtırabilir, yokuşta bataryayı korumaya alabilir ya da şarj bitince haber alabilirsiniz. Bu rehber ilk otomasyonu kurmayı ve ekrandaki her seçeneğin ne demek olduğunu anlatır. Seçenek adları uygulamadakiyle aynıdır.

Son güncelleme: 19 Kasım 2026

## Otomasyon ne işe yarar?

Sık yaptığınız işleri bir kez tanımlarsınız, sonrasında Yoldaş sizin yerinize yapar. Otomasyonlar telefonda ya da araç ekranında kurulur ve **araçta çalışır**. Üç parçadan oluşur: **Ne zaman** (tetik), **Hangi koşulda** (isteğe bağlı) ve **Ne yapsın** (adımlar).

### Soğuk havada klima

- **Ne zaman** Araç açılınca.
- **Hangi koşulda:** Pil en az %25 ve Dış sıcaklık altında 5 °C.
- **Ne yapsın:** Klimayı aç, Sürücü sıcaklığı 22 °C, Ön buz çözme açık.

Bu akış araç açıkken çalışır. Araç tamamen kapalıyken yalnız "Klimayı aç" adımı çalışır; sıcaklık ve buz çözme adımları reddedilir. Sabah kapalı araçta klima için belirli saatte tetiklenen, tek adımlı ("Klimayı aç") bir akış kurun. Hazır şablonlarda benzer bir **Sabah hazırlığı** da bulunur.

### Yokuşta batarya koruma ve mod

- **Ne zaman** Eğim şu değere ulaşınca, eşik 6.
- **Hangi koşulda:** Eğim, En az, 6.
- **Ne yapsın:** Batarya koruma Açık ve hedef %55, sonra Sürüş modu Normal mod.

İnişe geçince ayrı bir akış kurabilirsiniz: **Eğim şu değerin altına inince**, eşik -5. Adımlar: Batarya koruma Açık, hedef %70, Rejenerasyon seviyesi Yüksek, Sürüş modu Eco modu.

### 120 km/sa üstünde spor mod

- **Ne zaman** Hız şu değere ulaşınca, eşik 120.
- **Ne yapsın:** Sürüş modu Spor modu.

### Şarj bitince bildirim

- **Ne zaman** Pil %100 olunca.
- **Ne yapsın:** Araçta bildirim göster. Telefonda da haber almak için Telefona bildirim ekleyin.

## Nerede bulunur?

- **Telefonda:Hesap** › **Otomasyonlar** (Yoldaş temasında) ya da **Tüm özellikler** › **Otomasyonlar**.
- **Araç ekranında:Yoldaş › Sistem › Otomasyonlar**.

Telefon ve araç aynı listeyi paylaşır; birkaç dakika içinde eşitlenir. Yeni özellikler araçtaki Yoldaş sürümüne bağlıdır: hız, eğim ve fren tetikleri **0.12.56**, araç bilgisi tetikleri, gölge kip, internet isteği ve hazır şablonlar **0.13.21**, yeni düzenleyici, direksiyon tuşu tetikleri ve koşul grupları **0.13.29**, yeni araç komutları **0.13.40** ya da üstünü ister. Sürüm eskiyse ilgili tetikler araca ulaşmaz ve telefon "Araçtaki Yoldaş güncellenince çalışır" notunu gösterir. Güncelleme için [indirme sayfasına](https://yoldas.io/indir) bakın.

## İlk otomasyonunuzu kurun

1. **Otomasyonlar ekranını açın**

Telefonda **Hesap › Otomasyonlar**'a (Yoldaş temasında) ya da **Tüm özellikler › Otomasyonlar**'a gidin. Araç ekranında **Yoldaş › Sistem › Otomasyonlar**'ı açın.
2. **Yeni otomasyon başlatınYeni otomasyon**'a dokunun ya da **Hazır şablonlar**'dan birini seçin. Sihirbaz beş adımda ilerler: Ne zaman, Hangi koşulda, Ne yapsın, Ayarlar, Özet.
3. **Ne zaman çalışacağını seçinNe zaman** adımında bir ya da birkaç tetik seçin. Hız, eğim ve fren gibi eşikli tetiklerde çıkan kutuya eşik değerini yazın; saat tetiğinde saati ve günleri seçin.
4. **İsterseniz koşul ekleyinHangi koşulda** adımında pil, dış sıcaklık, hız, eğim, fren pedalı ya da aracın başka bir bilgisi için koşul seçin. Koşulları **Hepsi doğruysa** ya da **Biri doğruysa** gruplarında toplayabilirsiniz.
5. **Adımları sırayla ekleyinNe yapsın** adımında araç eylemini, beklemeyi, bildirimi ya da başka bir adımı kategoriden seçip ekleyin. Sırayı yukarı taşıyarak değiştirebilirsiniz.
6. **Ayarları yapınAyarlar** adımında aynı otomasyonun iki çalışması arasında geçmesi gereken en kısa süreyi (yeniden çalışma aralığı) ve istiyorsanız gölge kipi seçin.
7. **Özeti okuyup kaydedinÖzet** adımında kuralın okunur cümlesini kontrol edin, bir ad verin (en çok 60 karakter) ve kaydedin. Otomasyon araca iletilir; araç bağlı değilse bağlanınca uygulanır.
8. **Park halindeyken deneyin**

Otomasyonun ayrıntı sayfasındaki **Şimdi çalıştır** düğmesiyle adımları gerçekten uygulatıp sonucu görün. **Geçmişte dene** son 7 günde ne olacağını gösterir. Sonra otomasyonu etkinleştirin.

Ayrıntılı seçenekler aşağıdaki sözlüktedir. Telefondan başka komutlar için [telefondan kontrol](https://yoldas.io/ozellikler/telefondan-kontrol) sayfasına bakın.

## Sözlük: her seçenek ne demek?

### Tetikler: Ne zaman

Otomasyonu neyin başlattığını seçersiniz. Birden fazla tetik seçebilirsiniz; biri gerçekleşince otomasyon başlar.
SeçenekNe zaman çalışır? Düğmeye basıncaSiz başlatınca: telefondan ya da araç ekranından. Araç açılıncaAraç açıldığında. Pil %100 oluncaBatarya tam dolduğunda. Belirli saatteSeçtiğiniz saatte ve seçtiğiniz günlerde. Konuma girinceAraç, belirlediğiniz bölgenin içine girdiğinde. Bölgeye **Konum adı** verir, **Alan yarıçapı (m)** yazarsınız (100–5000 m). **Aracın şu anki konumunu kullan** düğmesi bölgeyi aracın bulunduğu yere koyar. Konumdan çıkıncaAraç, belirlediğiniz bölgenin dışına çıktığında. Hız şu değere ulaşıncaHız, yazdığınız **Hız eşiği (km/sa)** değerine ulaştığında. Hız şu değerin altına ininceHız, eşiğin altına indiğinde. Eğim şu değere ulaşıncaYol eğimi, yazdığınız **Eğim eşiği (°; + yokuş yukarı)** değerine ulaştığında. Artı değer yokuş yukarı, eksi değer yokuş aşağıdır. Eğim şu değerin altına ininceEğim, eşiğin altına indiğinde. Fren pedalı şu kadar basılıncaFren pedalı, yazdığınız **Fren eşiği (%)** değerine ulaştığında. Fren pedalı şunun altına ininceFren pedalı, eşiğin altına indiğinde. Vites P'ye alınıncaVites P konumuna getirildiğinde. Aracın bir bilgisi eşiği geçince ya da değişincePil ve şarj, lastikler, 12 V akü, kapılar, bağlantı gibi yaklaşık 60 araç bilgisinden birini seçersiniz. Sayısal bilgide eşiği, durum bilgisinde (ör. kapı açık) yeni durumu yazarsınız. Direksiyon tuşuna basıncaDireksiyondaki seçtiğiniz tuşa basıldığında. Tuşun adını **Sistem › Tanılama › Tuş keşfi** ekranında (60 saniye, yalnız araçta) basarak öğrenirsiniz. Tuşun kendi işlevi bozulmaz.

**Konum tetikleri için:** konum paylaşımı açık ve GPS verisi güncel olmalıdır. Bölge sınırında konum belirsizse tetik çalışmaz.

**Geçişte bir kez çalışır.** Hız, eğim ve fren tetikleri sürekli değil, eşiği geçtikleri anda çalışır. "Ulaşınca" tetiği, değer eşiğin altındayken eşiğe ulaşınca çalışır. "Altına inince" tetiği, değer eşikte ya da üstündeyken eşiğin altına inince çalışır. Değer zaten eşiğin üstündeyse tekrar tekrar çalışmaz.

**Fren pedalı hakkında:** pedal yalnız basılı (%100) ya da bırakılmış (%0) olarak okunur. %25 ile %35 eşiği bu yüzden aynı davranır.

### Koşullar: Hangi koşulda

Koşullar isteğe bağlıdır. Varsayılan olarak hepsi birlikte doğru olduğunda otomasyon çalışır. **Hepsi doğruysa** ve **Biri doğruysa** gruplarını en çok üç kat iç içe kullanabilirsiniz; örneğin "pil azsa ve (hız sıfırsa ya da vites P ise)".
SeçenekAnlamı Pil en az (%)Batarya doluluğu yazdığınız yüzdeye eşit ya da daha yüksek olmalı. Dış sıcaklık altında (°C)Dış sıcaklık yazdığınız değerin altında olmalı. Hız (km/sa)Hız, yazdığınız değere göre **En az** ya da **Altında** olmalı. Eğim (°; + yokuş yukarı)Eğim, yazdığınız değere göre **En az** ya da **Altında** olmalı. Fren pedalı (%)Fren pedalı, yazdığınız değere göre **En az** ya da **Altında** olmalı. Pedal basılıysa %100, bırakılmışsa %0 sayılır. Aracın başka bir bilgisiKapı, lastik, 12 V akü, bağlantı gibi katalogdaki bir bilgi, seçtiğiniz değerde ya da durumda olmalı. Sayısal bilgide ayrıca "eşit", "eşit değil", "en fazla" ve "üstünde" seçenekleri vardır. Sadece bu konumdaykenAraç, belirlediğiniz bölgenin içinde olmalı.

**En az** değer yazdığınız sayıya eşit ya da ondan büyük olmalı demektir. **Altında** değer o sayıdan küçük olmalı demektir. Hız, eğim ve fren koşullarında ikisinden birini seçersiniz; pil ve dış sıcaklık koşullarında anlam adın içindedir.

**Veri eskiyse koşul sağlanmaz.** İlgili araç verisi güncel değilse koşul sağlanmış sayılmaz ve otomasyon durur; çalışma geçmişinde nedeni yazar.

### Adımlar: Ne yapsın

Adımlar yukarıdan aşağıya sırayla çalışır. **Adım ekle** ile eklersiniz.
AdımNe yapar? Araç eylemiAracı kontrol eder. Seçenekleri aşağıdaki tabloda. Bekle (saniye)Yazdığınız süre kadar bekler (1–7200 saniye), sonra sıradaki adıma geçer. MedyaÇalan medyanın sesini kapatır (ya da eski seviyeye döndürür), oynatır, duraklatır veya sesi ayarlar. Kaydı durdurKaydı durdurur. Kaydı işaretleKaydı şimdi işaretler; klip korunur. Kayıt moduSürüş kaydı modunu Kapalı, Park, Sürüş ya da Sürekli yapar. Nöbetçiyi aç / kapatPark için nöbetçiyi açar ya da kapatır. Başka otomasyonu aç / kapatSeçtiğiniz başka bir otomasyonu etkinleştirir ya da kapatır. İnternet isteğiBir adrese istek gönderir. İsterseniz gizli bir anahtarla imzalanır; başarısız olursa 0–6 kez yeniden denenir ve istek en çok 24 saat kuyrukta bekler. Gizli anahtarı kimseyle paylaşmayın. Uygulama açSeçtiğiniz uygulamayı araç ekranında açar. Araçta bildirim gösterYazdığınız mesajı (en çok 160 karakter) araç ekranında gösterir. Araç ekranı mesajıYazdığınız kısa mesajı (en çok 140 karakter) araç ekranında gösterir. Telefona bildirimTelefonunuza bildirim gönderir (en çok 160 karakter). Telefonda Hesap › Bildirimler bölümünde otomasyon bildirimlerini açmanız gerekir. Bildirimin ulaşması her zaman kesin değildir; sürüşte bekletilir ve 10 dakika sonra silinir. EğerSeçtiğiniz koşul doğruysa, **Değilse** ya da **Koşulun sonu** adımına kadar olan adımları çalıştırır. En çok 3 koşul iç içe olabilir. Değilseİsteğe bağlıdır. Eğer koşulu doğru değilse çalışacak adımları başlatır. Koşulun sonuHer Eğer adımını bununla kapatın. Koşula kadar bekleSeçtiğiniz koşul doğru olana kadar bekler. **En fazla bekleme (saniye)** kutusuna yazdığınız süre dolarsa beklemeyi bırakır.

### Araç eylemleri

Araç eylemi adımında şunlardan birini seçersiniz:
EylemSeçenekler ve anlamı KlimaKlimayı aç, Klimayı kapat, Sürücü sıcaklığı, Yolcu sıcaklığı ve Fan. Ön buz çözmeAç ya da Kapat. Ön camdaki buğu ve buzu çözer. Arka buz çözmeAç ya da Kapat. Arka camdaki buğu ve buzu çözer. Hava dolaşımıİç ya da Dış. Kabin havasını içeride döndürür ya da dışarıdan alır. Camları kapat / Camları aralaCamları kapatır ya da havalandırma için hafifçe aralar. Bagajı aç / Bagajı kapatBagajı açar ya da kapatır. Açmak için araç duruyor ve sürücü kapısının kilidi açık olmalıdır. Sürüş moduEco modu, Normal mod, Spor modu ya da Kar modu. Rejenerasyon seviyesiStandart ya da Yüksek. Aracın yavaşlarken enerjiyi bataryaya ne kadar geri kazandıracağını belirler. Fren hissiKonfor ya da Spor. Fren pedalının hissini değiştirir. Güç moduEV ya da HEV. Batarya korumaKapalı ya da Açık. Açık seçerseniz **Hedef doluluk (%, 15–70)** değerini yazarsınız. Yeni komutlar (0.13.40)Kablosuz şarj, direksiyon ısıtma, koltuk ısıtma ve havalandırma, ortam ışığı parlaklığı ve rengi, gündüz farı (yalnız açma), bagaj açılma yüksekliği ve HUD. Kablosuz şarj ve bagaj yüksekliği için araç P'de ve duruyor olmalıdır. Araç bir komutu desteklemiyorsa adım reddedilir.

**Araç kapalıyken:** yalnız klimayı açma ve kapatma çalışır. Bunun için vites P, hız 0, sürücü kapısı kapalı ve kilitli olmalı; pil %20'nin, 12 V akü 12,0 V'un üstünde olmalıdır (şarj kablosu takılıysa pil ve akü sınırı aranmaz). Kapalı araçta sıcaklık, fan, buz çözme, hava dolaşımı, camlar ve sürüş modu adımları reddedilir.

### Diğer ayarlar ve düğmeler
SeçenekAnlamı Yeniden çalışma aralığı (saniye)Aynı otomasyonun iki çalışması arasında geçmesi gereken en kısa süre. Varsayılan 60 saniyedir; 1 saniye ile 1 gün arasında seçebilirsiniz. Gölge kipAçıkken otomasyon tetiklenir ama hiçbir şey yapmaz; yalnız "yapardı" diye kaydeder. Birkaç gün izleyip doğru çalıştığını görünce kapatın. Geçmişte deneAyrıntı sayfasında son 7 günde otomasyonun kaç kez çalışacağını, atlanacağını ya da yalnız izleneceğini gösterir. Şimdi çalıştırOtomasyonu hemen çalıştırır ve adımları gerçekten uygular. Otomasyon kapalı olsa da çalışır. EtkinListede her otomasyonun yanındaki anahtardır. Açıkken tetikler otomasyonu başlatır. Kapalıyken otomasyon kendiliğinden çalışmaz. Hazır şablonlarOndan fazla hazır otomasyon vardır (ör. Sabah hazırlığı, Pil %100 olunca, Şarj kablosunu takmayı unutma, Düşük lastik basıncı, 12 V akü düşük). Seçip düzenlersiniz. Karmaşık olanlar kapalı ve gölge kipte başlar. Son çalışmalarOtomasyonların son durumlarını gösterir: Çalışıyor, Tamamlandı, Durduruldu, Tamamlanamadı, Atlandı (nedeniyle birlikte) ya da gölge kipte Yapardı.

### Sınırlar

- Bir otomasyonda en çok **20 adım** olabilir.
- En çok **50 otomasyon** kaydedebilirsiniz.
- Bir otomasyondaki toplam bekleme süresi en çok **2 saat** olabilir.
- İç içe Eğer en çok **3** kat olabilir.
- Bir otomasyonda en çok **6 tetik** olabilir.
- Otomasyon adı en çok 60, telefon bildirimi 160, araç ekranı mesajı 140 karakter olabilir.
- Aynı anda yalnız bir otomasyon çalışır.

## Başka uygulamadan otomasyon alma

Başka bir uygulamadan dışa aktarılmış otomasyon dosyasını Yoldaş'a alabilirsiniz. Alma kapsamı dardır: yalnız hız, eğim ve fren tetikleri ile sürüş modu, rejenerasyon, fren hissi, güç modu ve batarya koruma eylemleri tanınır; gerisi atlanır.

1. **Dosyayı seçin**

Telefonda **Otomasyonlar** › **Dosyadan al**'a dokunun ve dışa aktarılmış .json dosyasını seçin. Dosya en çok 250 KB olabilir ve en çok 50 otomasyon içerebilir.
2. **İçe aktarma raporunu okuyun**

Rapor kaç otomasyonun alındığını gösterir. Her otomasyon için **Tamamı alındı**, **Kısmen alındı** ya da **Alınmadı** yazar; nedeni de belirtilir.
3. **Kontrol edip açın**

Alınan otomasyonlar **kapalı** gelir. Her birinin adımlarına bakın, uygun olanı açın ya da hepsini birden açmak için **Hepsini etkinleştir**'e dokunun.

Yoldaş'ın desteklemediği bir tetik, koşul ya da eylem varsa o kısım **atlanır**; yerine tahmini bir karşılık uydurulmaz. Koşulu uygulanamayan bir blok bütünüyle atlanır, böylece içindeki eylemler koşulsuz çalışmaz. "Eşit" ve "veya" koşulları desteklenmez. "Büyük eşit" ve "küçük eşit" koşulları yaklaşık olarak çevrilir ve raporda yazar.

## Dikkat edilecekler

- **Sürüşte otomatik mod değişimi** (sürüş modu, rejenerasyon, fren hissi, güç modu) aracın davranışını değiştirir. Yeni bir otomasyonu önce park halindeyken **Şimdi çalıştır** ile deneyin, sonra etkinleştirin.
- **Sonuç bazen "doğrulanamadı" görünür.** Yeni komutların sonucu araçtan her zaman geri okunamaz. Bu durumda komut yine de gönderilmiştir ve araçtaki komut günlüğüne yazılır; otomasyon devam eder.
- **Aynı anda tek otomasyon çalışır.** Biri çalışırken başka bir otomasyon tetiklenirse "Başka bir akış çalışıyor" denir ve ikincisi geçilir. Hız ve fren gibi sık tetiklenen otomasyonları kısa tutun.
- **Eski araç sürümü.** Araçtaki Yoldaş sürümü, kullandığınız özelliğin gerektirdiği sürümden eskiyse (yukarıdaki sürüm listesine bakın) o tetik ya da adım çalışmaz.
- **Kapalı araç.** Araç tamamen kapalıyken yalnız klima aç/kapat adımı çalışır.

Bunlara ek olarak [Otomasyonlar özellik sayfasına](https://yoldas.io/ozellikler/otomasyonlar), [alt çubuk kısayollarına](https://yoldas.io/ozellikler/alt-cubuk) ve [sürüm notlarına](https://yoldas.io/surum-notlari) göz atabilirsiniz.

## Sık sorulan sorular

### Otomasyon nedir, ne işe yarar?

"Şu olunca, şu koşullarda, şunları sırayla yap" diyen bir kuraldır. Örneğin araç açılınca klimayı 22 °C'ye ayarlayabilir ya da pil %100 olunca araç ekranında bildirim gösterebilirsiniz. Otomasyonlar araçta çalışır.

### Otomasyonları nerede bulurum?

Telefonda Hesap › Otomasyonlar (Yoldaş temasında) ya da Tüm özellikler › Otomasyonlar. Araç ekranında Yoldaş › Sistem › Otomasyonlar. Telefon ve araç aynı listeyi paylaşır; değişiklikler birkaç dakika içinde eşitlenir.

### Bazı tetikler ya da adımlar neden aracıma ulaşmıyor?

Yeni özellikler araçtaki Yoldaş sürümüne bağlıdır. Hız, eğim ve fren tetikleri için 0.12.56; araç bilgisi tetikleri, gölge kip, internet isteği ve hazır şablonlar için 0.13.21; yeni düzenleyici, direksiyon tuşu tetikleri ve koşul grupları için 0.13.29; yeni araç komutları için 0.13.40 ya da üstü gerekir. Sürüm eskiyse telefon "Araçtaki Yoldaş güncellenince çalışır" notunu gösterir.

### Kapalı araçta otomasyon çalışır mı?

Araç tamamen kapalıyken yalnız klimayı açıp kapatan adım çalışır. Sıcaklık, fan, buz çözme, hava dolaşımı, camlar ve sürüş modu adımları reddedilir; bunlar için araç açık olmalıdır.

### Koşullar sağlanıyor ama otomasyon çalışmadı. Neden?

Dört neden olabilir. İlgili araç verisi güncel değilse koşul sağlanmış sayılmaz. Yeniden çalışma aralığı dolmamış olabilir. Başka bir otomasyon çalışıyorsa yenisi geçilir. Hız, eğim ve fren tetikleri yalnız eşiği geçerken çalışır; değer zaten eşiğin üstündeyse tekrar tetiklenmez.

### Etkin anahtarı kapalıysa ne olur?

Tetikler çalışmaz, yani otomasyon kendiliğinden başlamaz. "Şimdi çalıştır" ise yine çalışır.

### Sonuç "doğrulanamadı" diyorsa komut gitmemiş mi?

Hayır. Yeni sürüş ve enerji komutlarının sonucu araçtan her zaman geri okunamaz. Komut yine de gönderilmiştir ve araçtaki komut günlüğüne yazılır; otomasyon da devam eder. Sürüş modunu araç göstergesinden kontrol edebilirsiniz.

### Fren pedalı eşiğini %25 ya da %35 yapmam fark eder mi?

Hayır. Fren pedalı yalnız basılı (%100) ya da bırakılmış (%0) olarak okunur. Bu yüzden %25 ile %35 eşiği aynı davranır.

### Başka bir uygulamadaki otomasyonlarımı alabilir miyim?

Kısmen. Otomasyonlar › Dosyadan al ile dışa aktarılmış .json dosyasını seçin. Yalnız hız, eğim ve fren tetikleri ile sürüş modu, rejenerasyon, fren hissi, güç modu ve batarya koruma eylemleri alınır. Alınan otomasyonlar kapalı gelir; desteklenmeyen kısımlar atlanır ve içe aktarma raporunda yazar.

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

### [BYD için araç uygulaması nasıl seçilir?](https://yoldas.io/rehber/byd-icin-arac-uygulamasi-secimi)

Kayıt güvenilirliği, verinin nerede durduğu, dil, kurulum ve güncelleme imzası için kontrol listesi.

### [Şarj fiyatı ve yolculuk maliyeti](https://yoldas.io/rehber/sarj-fiyati-ve-yolculuk-maliyeti)

Her şarja kendi fiyatını girin, yolculuk maliyetini şarj fiyatlarınıza göre görün.
