# DjangoRestApiwithMongoDB

Projemde python dili ile Django frameworkunu kullanarak bir web api projesi geliştirdim. Projeyi rest api servisini veritabanı olarak Nosql teknolojisi olan MongoDB ile
geliştirdim. MongoDB veritabanını remote ortamda MongoDB sayfasında bir cluster içinde oluşturdum. Böylelikle herhangi bir db ayarlaması yapmaksızın rest api projemiz db ye
bağlanacaktır. Projemde sadece ürün sepet ilişkisi kurarak küçük bir e-ticaret sitesi yaptım. 

Projemin backend kısmında;
 Product ve shopcart olmak üzere iki tablo oluşturdum ve birbirleri ile aralarındaki ilişkiyi kurdum. (tutorials/Models.py dosyamda görebilirsiniz.)
 Ürünleri listeleme, ekleme ve güncelleme methodlarını ürünü eğer stokta bulunuyorsa sepete eklemeyi bulunmuyorsa ürün stokta bulunmuyor mesajı veren fonksiyonlarımı 
 tutorials/views.py dosyamın içinde bulabilirsiniz.
 tutorials /urls.py dosyamın içinde bu fonksiyonlar için tanımladığım urller bulunmaktadır.
 settings.py  dosyamın içinde MongoDB ye bağlanmak için gerekli olan ayarlarımı görebilirsiniz
 Projemin Frontend kısmında;
 Hazır templateler kullanarak ve bu templatelere angularjs entegresi yaparak response request mantığı ile veritabanı verilerim ile crud işlemlerini gerçekleştirdim.
 Müşteri girişi (productlist ve addshopcart) için bir sayfa, admin kullanıcı girişi için ise(product crud işlemleri) iki ayrı html sayfa bulunmaktadır.
 Müşteri bir ürünü sepete eklediğinde eğer stokta yoksa backend servisinden dönen hata mesajını bir toast ile ön yüzümde görüntüledim.
 Müşteri girişi için tasarlanmış sayfanın yolu aşağıdaki gibidir;
   DjangoRestApiMongoDB\basic-opl\index.html 
Admin girişi için tasarlanmış sayfaların yolu;
  DjangoRestApiMongoDB\basic-opl\Admin\html\ProductList.html
   DjangoRestApiMongoDB\basic-opl\Admin\html\ProductUpdate.html
    DjangoRestApiMongoDB\basic-opl\Admin\html\ProductCreate.html
    
    Productlist sayfasına gittiğinizde Update ve create sayfalarına giden butonlar görebilirsiniz.
    
    Django Resp apinin çalışması için gerekli kurulumlar aşağıdadır;
    Python (yüklemek için installer kullandım)
    Django ;
    pip install Django
    
    Django Rest Framework ;
    pip install djangorestframework
    
    djongo ;
    pip install djongo
    
    django-cors-headers;
    pip install django-cors-headers
    
    Projeyi ayağa kaldırmak için gerekli komut;
    PS C:\DjangoRestApiMongoDB> dizininde: python manage.py runserver 8080
    NOT: Ben rest api projesini http://127.0.0.1:8080 portlu localhostum da ayağa kaldırdım. Eğer siz başka bir host veya port da ayağa kaldırısanız aşağıda belirtttiğim 
    dizinlerde bulunan controller.js scriptlerinde request urllerini ayağa kaldırdığınız Url ile değiştirmeniz gerekir.
    DjangoRestApiMongoDB\basic-opl\pageOneControler.js 
    DjangoRestApiMongoDB\basic-opl\Admin\html\SecondPageController.js
    DjangoRestApiMongoDB\basic-opl\Admin\html\updatePageController.js
    DjangoRestApiMongoDB\basic-opl\Admin\html\createPageController.js
    
    Eğer DB ye manuel bağlanıp verilerde değişiklik yapmak veya kontrol etmek isterseniz. MongoDB compass programını indirip connnect ekranında çıkan connection string hanesine 
    aşağıdaki stinge girerekremote DB bağlantısını gerçekleştireilirsiniz:
    mongodb+srv://user_betul:Zh121958@cluster0.llrr0.mongodb.net/test
    
    
