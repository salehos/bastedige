import telebot
import time
from telebot import types

bot = telebot.TeleBot(bot_token)

user_dict = {}
pm_dict = {}

class voteList:
    def __init__(self, voterId , providerName):
        self.voterId = voterId
        self.providerName = providerName
        self.first_question = None
        self.second_question = None
        self.thirth_question = None
        self.fourth_question = None
        self.fifth_question = None
        self.sixth_question0 = None

class Pm:
    def __init__(self, id):
        self.id = id
        self.textToUser = None

@bot.message_handler(commands=['start'])
def first_step(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    universityMap = types.KeyboardButton("نقشه دانشگاه")
    tables = types.KeyboardButton("جدول زمان بندی سمینار ها و کارگاه ها")
    introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
    vote = types.KeyboardButton("نظرسنجی")
    contact = types.KeyboardButton("ارتباط با ادمین")
    keyboard.add(universityMap)
    keyboard.add(tables)
    keyboard.add(introduce)
    keyboard.add(vote)
    keyboard.add(contact)
    msg = bot.reply_to(message, 'خوش آمدید. چه کمکی از دست من برمیاد؟', reply_markup=keyboard)
    bot.register_next_step_handler(msg, choosing_one)


def choosing_one(message):
    try:
        if message.text == "نقشه دانشگاه":
            keyboard = types.ReplyKeyboardMarkup()
            keyboard = types.ReplyKeyboardRemove(selective=False)
            photo = open("/home/wssbot/kuroky.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo)
            bot.register_next_step_handler(msg, choosing_one)
        elif message.text == "جدول زمان بندی سمینار ها و کارگاه ها":
            photo = open("/home/wssbot/kargahHa.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo , caption= "\n  ❄️معرفی کارگاه‌های پنجمین سری سمینارهای زمستانه شریف"
                                                             "📅۷ الی ۱۱ دی‌ماه\n"
                                                             "\n🏛دانشگاه صنعتی شریف"
                                                             "✨️تخفیف ویژه ثبت‌نام در کارگاه‌ها به همراه سمینار در پنجمین سری سمینار‌های زمستانه\n\n"
                                                             "🔹کسب اطلاعات بیشتر و ثبت‌نام کارگاه‌ها : \n"
                                                             "\nhttp://wss.ce.sharif.ir/go/WSS2019")
            bot.register_next_step_handler(msg, choosing_one)
        elif message.text == "آشنایی با ارائه دهنده ها":
            msg = bot.send_message(message.chat.id, "فردی را انتخاب کنید")
            bot.register_next_step_handler(msg, provider)

        elif message.text == "نظرسنجی":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            seminarvote = types.KeyboardButton("نظرسنجی کلی رویداد")
            speakersvote = types.KeyboardButton("نظرسنجی مربوط به هر سخنرانی")
            keyboard.add(seminarvote)
            keyboard.add(speakersvote)
            msg = bot.reply_to(message, " به بخش نظرسنجی خوش آمدید، لطفا یکی از انواع نظرسنجی را انتخاب کنید...", reply_markup=keyboard)
            bot.register_next_step_handler(msg, vote_part)

        elif message.text == "ارتباط با ادمین":
            msg = bot.send_message(message.chat.id, "لطفا با @TheMightyM تماس بگیرید")
            bot.register_next_step_handler(msg, choosing_one)
        else:
            raise Exception
    except Exception:
        msg = bot.reply_to(message, "دستور شما جزء دستورات این بات نیست. مجددا تلاش کنید.")
        bot.register_next_step_handler(msg, choosing_one)


def vote_part(message):
    try:
        if message.text == "نظرسنجی کلی رویداد" :
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            universityMap = types.KeyboardButton("نقشه دانشگاه")
            tables = types.KeyboardButton("جدول زمان بندی سمینار ها و کارگاه ها")
            introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
            vote = types.KeyboardButton("نظرسنجی")
            contact = types.KeyboardButton("ارتباط با ادمین")
            keyboard.add(universityMap)
            keyboard.add(tables)
            keyboard.add(introduce)
            keyboard.add(vote)
            keyboard.add(contact)
            msg = bot.reply_to(message, "این بخش در حال کامل شدن است، در حال بازگشت به منوی اصلی", reply_markup=keyboard)
            bot.register_next_step_handler(msg, choosing_one)
        elif message.text == "نظرسنجی مربوط به هر سخنران" :
            zahraNazari = types.KeyboardButton("دکتر زهرا نظری")
            behzadMoshiri = types.KeyboardButton("دکتر بهزاد مشیری")
            ehsanEmamjomezadeh = types.KeyboardButton("دکتر احسان امام جمعه زاده")
            mohammadHeydari = types.KeyboardButton("محمد حیدری")
            keyboard.add(behzadMoshiri)
            keyboard.add(ehsanEmamjomezadeh)
            keyboard.add(mohammadHeydari)
            keyboard.add(zahraNazari)
            msg = bot.reply_to(message, "لطفا فرد مورد نظر خود را انتخاب کنید", reply_markup=keyboard)
            bot.register_next_step_handler(msg, vote_for_speakers)

    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, vote_part)



def vote_for_speakers(message):
    try:
        chatId = message.chat.id
        providerName = message.text
        votelist = voteList(chatId, providerName)
        user_dict[chatId] = votelist
        if message.text == "دکتر زهرا نظری" :
            msg = bot.reply_to(message, "۱. ارائه کارگاه مناسب و قابل فهم")
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            bot.register_next_step_handler(msg, first_question)
        elif message.text == "دکتر بهزاد مشیری" :
            msg = bot.reply_to(message, "۱. ارائه کارگاه مناسب و قابل فهم")
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            bot.register_next_step_handler(msg, first_question)
        elif message.text == "دکتر احسان امام جمعه زاده" :
            msg = bot.reply_to(message, "۱. ارائه کارگاه مناسب و قابل فهم")
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            bot.register_next_step_handler(msg, first_question)
        elif message.text == "محمد حیدری" :
            msg = bot.reply_to(message, "۱. ارائه کارگاه مناسب و قابل فهم")
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            bot.register_next_step_handler(msg, first_question)

    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, vote_part)


def first_question(message, theProvider):
    try:
        if message.text == "1" or "2" or "3" or "4" or "5":
            chatId = message.chat.id
            voterlist = user_dict[chatId]
            voterlist.first_question = message.text
            msg = bot.reply_to(message, "۲. تسلط ارائه دهنده بر موضوعم")
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            bot.register_next_step_handler(msg, second_question)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, first_question)

def second_question(message, theProvider):
    try:
        if message.text == "1" or "2" or "3" or "4" or "5":
            chatId = message.chat.id
            voterlist = user_dict[chatId]
            voterlist.second_question = message.text
            msg = bot.reply_to(message, "۳. مناسب بودن موضوع ارائه شده")
            yes = types.KeyboardButton("بله")
            second = types.KeyboardButton("خیر")
            bot.register_next_step_handler(msg, third_question)

    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, second_question)

def third_question(message, theProvider):
    try:
        if message.text == "1" or "2" or "3" or "4" or "5":
            chatId = message.chat.id
            voterlist = user_dict[chatId]
            voterlist.third_question = message.text
            msg = bot.reply_to(message, "۴. آیا موضوع گفته شده با محتوای کارگاه تناسب داشت؟")
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            bot.register_next_step_handler(msg, fourth_question)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, third_question)


def fourth_question(message, theProvider):
    try:
        if message.text == "بله" or "خیر":
            chatId = message.chat.id
            voterlist = user_dict[chatId]
            voterlist.forth_question = message.text
            msg = bot.reply_to(message, "۵. در کل به این کارگاه چه نمره ای را می‌دهید؟")
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            bot.register_next_step_handler(msg, fifth_question)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, fourth_question)



def fifth_question(message, theProvider):
    try:
        if message.text == "1" or "2" or "3" or "4" or "5":
            chatId = message.chat.id
            voterlist = user_dict[chatId]
            voterlist.fifth_question = message.text
            msg = bot.reply_to(message, "۶. اگر نظر دیگری درباره کارگاه دارید ذکر کنید. ")
            bot.register_next_step_handler(msg, sixth_question)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, fifth_question)

def sixth_question(message, theProvider):
    try:
        chatId = message.chat.id
        voterlist = user_dict[chatId]
        voterlist.sixth_question = message.text
        myFile = open("inputs.txt", "a+")
            myFile.write(
                "from chat Id:" + voterlist.voterId + "\tprovider:" + voterlist.provider + "\tfirst question:" + voterlist.port + "\tsecond_question:" + voterlist.username + "\tthird_question:" + voterlist.password + "\tforth_question:" + voterlist.hard + "\tfifth_question:" + voterlist.country + "\tsixth_question:" + voterlist.sixth_question +"\n")
            myFile.close()
        msg = bot.reply_to(message, "با تشکر از شما، نظر شما ثبت شد. ")
        bot.register_next_step_handler(msg, choosing_one)

    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, sixth_question)

def provider(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    alirezaRezaei = types.KeyboardButton("علیرضا رضایی")
    behzadMoshiri = types.KeyboardButton("دکتر بهزاد مشیری")
    ehsanEmamjomezadeh = types.KeyboardButton("دکتر احسان امام جمعه زاده")
    meysamRazavin = types.KeyboardButton("دکتر میثم رضویین")
    mohammadHeydari = types.KeyboardButton("محمد حیدری")
    mohammadKhaloei = types.KeyboardButton("محمد خالوئی")
    mohammadMahdian = types.KeyboardButton("دکتر محمد مهدیان")
    mortezaSaberi = types.KeyboardButton("دکتر مرتضی صابری")
    mozhganMirzaei = types.KeyboardButton("مژگان میرزایی")
    nedaSoltani = types.KeyboardButton("ندا سلطانی")
    rezaMohammadi = types.KeyboardButton("رضا محمدی")
    salmanAbolfathbeigi = types.KeyboardButton("دکتر سلمان ابوالفتح بیگی")
    siminOreei = types.KeyboardButton("سیمین اورعی")
    zahraNazari = types.KeyboardButton("دکتر زهرا نظری")

    hamedSaleh =  types.KeyboardButton("حامد صالح")
    masodZamani = types.KeyboardButton("مسعود زمانی")
    afraAbnar = types.KeyboardButton("افرا آبنار")
    arashPordamqani = types.KeyboardButton("آرش پوردامغانی")
    omidEtesami = types.KeyboardButton("دکتر امید اعتصامی")
    meysamAlizadeh = types.KeyboardButton("دکتر میثم علیزاده")
    aminBabadi = types.KeyboardButton("امین بابادی")
    sinaDehghani = types.KeyboardButton("دکتر سینا دهقانی")
    mohammadMahmodi = types.KeyboardButton("دکتر محمد محمودی")
    shahriyarEbrahimi = types.KeyboardButton("شهریار ابراهیمی")
    mehdiSafarnenjad = types.KeyboardButton("مهدی صفرنژاد")
    amirNajjafi = types.KeyboardButton("امیر نجفی")
    moslemNoori = types.KeyboardButton("مسلم نوری")
    mohammadSalehe = types.KeyboardButton("محمد صالحه")


    back = types.KeyboardButton("بازگشت")
    keyboard.add(kargahHa)
    keyboard.add(alirezaRezaei)
    keyboard.add(behzadMoshiri)
    keyboard.add(ehsanEmamjomezadeh)
    keyboard.add(meysamRazavin)
    keyboard.add(mohammadHeydari)
    keyboard.add(mohammadKhaloei)
    keyboard.add(mohammadMahdian)
    keyboard.add(mortezaSaberi)
    keyboard.add(mozhganMirzaei)
    keyboard.add(nedaSoltani)
    keyboard.add(rezaMohammadi)
    keyboard.add(salmanAbolfathbeigi)
    keyboard.add(siminOreei)
    keyboard.add(zahraNazari)

    keyboard.add(hamedSaleh)
    keyboard.add(masodZamani)
    keyboard.add(afraAbnar)
    keyboard.add(arashPordamqani)
    keyboard.add(omidEtesami)
    keyboard.add(meysamAlizadeh)
    keyboard.add(aminBabadi)
    keyboard.add(sinaDehghani)
    keyboard.add(mohammadMahmodi)
    keyboard.add(shahriyarEbrahimi)
    keyboard.add(mehdiSafarnenjad)
    keyboard.add(amirNajjafi)
    keyboard.add(moslemNoori)
    keyboard.add(mohammadSalehe)
    keyboard.add(back)






    msg = bot.reply_to(message, 'یکی از گزینه ها را انتخاب کنید.', reply_markup=keyboard)
    bot.register_next_step_handler(msg, choosing_providers)

def choosing_providers(message):
    try:
        if message.text == "دکتر بهزاد مشیری" :
            photo = open("/home/wssbot/behzadMoshiri.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption= "#معرفی‌_سخنرانان \n"
                                                            "#معرفی‌ـکارگاه‌ـ‌ها\n"
                                                            " ❄️ دکتر بهزاد مشیری \n"
                                                            "🔸لیسانس مهندسی مکانیک دانشگاه علم و صنعت 🔹\n"
                                                            "فوق‌لیسانس و دکتری گرایش مهندسی سیستم‌های کنترل از دانشگاه Manchester Institute of Science and Technology \n"
                                                            "🔸پروفسور مهندسی کنترل در دانشگاه تهران 🔹از اعضای International Society of Information Fusion \n"
                                                            "🔸عضو ارشد موسسه  مهندسان برق و الکترونیک آمریکا (IEEE) \n"
                                                            "🔹استاد وابسته دانشگاه های Waterloo و York \n"
                                                            "🔸محقق ارشد موسسه تحقیقاتی WISE, Waterloo Institute for Sustainable Energy \n"
                                                            "🔹چاپ بیش از ۳۶۰ مقاله در مجلات معتبر علمی، پژوهشی و کنفرانس‌های ملی و بین‌المللی.\n"
                                                            " 🔸چاپ ۲۱ فصل کتاب در ۲۱ کتاب تالیف یافته توسط ناشران بین المللی.\n"
                                                            " 🔹رئیس مجمع سیستم های کنترل Control Systems Chapter, IEEE Iran Section ❄\n"
                                                            "️ موضوع ارائه ‏Data Fusion” an AI approach for decision making \n\n"
                                                            "🔺موضوع کارگاه \n"
                                                            "‌ ‏Sensor / Data Fusion, Theoretical and Practical issues\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر احسان امام جمعه زاده" :
            photo = open("/home/wssbot/ehsanEmamjomezadeh.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان \n"
                                                           "❄️ دکتر احسان امام جمعه زاده \n"
                                                           "🔸دکتری علوم کامپیوتر از دانشگاه Southern California \n"
                                                           "🔹 کارشناسی مهندسی کامپیوتر دانشگاه صنعتی شریف \n"
                                                           "🔸تحقیق در حوزه theoretical computer science \n"
                                                           "🔹تحقیق در حوزه‌های game theory و online learning \n"
                                                           "🔸محقق در Facebook \n\n"
                                                           "❄️ موضوع ارائه \n"
                                                           "\nOnline Learning")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "علیرضا رضایی" :
            photo = open("/home/wssbot/alirezaRezaei.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌ـکارگاه‌ـ‌ها ❄️ \n"
                                                           "علیرضا رضایی \n"
                                                           "🔸دانشجوی دکتری دانشگاه واشنگتن\n"
                                                           " 🔹فعالیت در determinantal point processes and their applications in machine learning and spectral graph theory \n"
                                                           "🔸کارشناسی ریاضی و مهندسی کامپیوتر در دانشگاه شریف \n\n"
                                                           "🔺موضوع کارگاه \n"
                                                           "‌ Modeling Diversity in Machine Learning Using Determinantal Point Processes\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر میثم رضویین" :
            photo = open("/home/wssbot/meysamRazavin.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان ❄️ \n"
                                                           "دکتر میثم رضویین \n"
                                                           "🔸استادیار مهندسی سامانه‌ها، صنایع و علوم کامپیوتر در دانشگاه کالیفورنیا جنوبی \n"
                                                           "🔹فوق‌دکتری در دانشگاه استنفورد \n"
                                                           "🔸دکتری در مهندسی برق و علوم کامپیوتر در دانشگاه Minnesota \n"
                                                           "🔹برنده بهترین مقاله سال ۲۰۱۹ و ۲۰۱۴ در کارگاه علوم‌داده موسسه  مهندسان برق و الکترونیک آمریکا (IEEE) \n"
                                                           "🔸فینالیست جایزه بهترین مقاله برای محقق جوان در بهینه‌سازی مداوم سال ۲۰۱۳ و ۲۰۱۶ \n\n"
                                                           "❄️ موضوع ارائه\n"
                                                           " ‏Learning via Non-Convex Min-Max Games\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "محمد حیدری" :
            photo = open("/home/wssbot/mohammadHeydari.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌ـکارگاه‌ـ‌ها\n"
                                                           " ❄️ محمد حیدری \n"
                                                           "🔸کارشناسی ارشد دانشگاه تربیت مدرس \n"
                                                           "🔹فعالیت در حوزه Big Data Analytics Techniques and their Application in Large Scale Social Networks \n"
                                                           "🔸کارشناسی مهندسی کامپیوتر دانشگاه فنی و حرفه‌ای \n"
                                                           "🔺موضوع کارگاه\n"
                                                           " ‌ Discovering Latent Patterns in Academic Collaboration Network based on Community Detection Approach\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "محمد خالوئی" :
            photo = open("/home/wssbot/mohammadKhaloei.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌ـکارگاه‌ـ‌ها \n"
                                                           "❄️ محمد خالوئی \n"
                                                           "🔸دانشجوی دکتری دانشگاه امیرکبیر 🔹فعالیت در آزمایشگاه Intelligence and Multimedia Processing \n"
                                                           "🔸فعالیت در حوزه artificial intelligence \n"
                                                           "🔹در حال کار بر روی vulnerability of deep neural network, adversarial machine learning and unsupervised learning \n"
                                                           "🔸مشاور استفاده از deep neural networks برای پردازش داده و پروژه‌های بین‌المللی\n\n"
                                                           " 🔺موضوع کارگاه\n"
                                                           " ‌ Robustness of Deep Neural Networks\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر محمد مهدیان" :
            photo = open("/home/wssbot/mohammadMahdian.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان ❄️ دکتر محمد مهدیان\n"
                                                           " 🔸دکتری از دانشگاه MIT \n"
                                                           "🔹کارشناسی ارشد از دانشگاه تورنتو \n"
                                                           "🔸کارشناسی از دانشگاه صنعتی شریف \n"
                                                           "🔹محقق در آزمایشگاه تحقیقاتی Google \n"
                                                           "🔸متخصص Market algorithms \n"
                                                           "🔹سابقه کار در بخش تحقیقاتی Yahoo و Microsoft \n\n"
                                                           "❄️ موضوع ارائه\n"
                                                           " Fairness in Clustering Algorithms\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر مرتضی صابری" :
            photo = open("/home/wssbot/mortezaSaberi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                           " ❄️ دکتر مرتضی صابری\n"
                                                           " 🔸استادیار University of Technology Sydney 🔹مدرس در University of New South Wales \n"
                                                           "🔸فعال در حوزه‌های هوش‌تجاری، داده‌کاوی و یادگیری ماشین \n"
                                                           "🔹چاپ بیش از ۱۸۰ مقاله در مجلات و کنفرانس‌های معتبر علمی\n"
                                                           " 🔸رئیس محسابات تکاملی در استرالیا \n"
                                                           "🔹برنده جایزه نفر اول مسابقات مقالات از ششمین کنفرانس بین‌المللی IEOM \n\n"
                                                           "️❄ موضوع ارائه\n"
                                                           " \nPersonalized Assortment Optimization for Online Retailer Considering Risk of Customers Churning")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "مژگان میرزایی" :
            photo = open("/home/wssbot/mozhganMirzaei.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان #معرفی‌ـکارگاه‌ـ‌ها\n"
                                                           " ❄️ مژگان میرزایی \n"
                                                           "🔸دانشجوی دکتری دانشگاه کالیفرنیا، سن دیگو\n"
                                                           " 🔹لیسانس ریاضی از دانشگاه صنعتی شریف \n"
                                                           "🔸فعالیت در حوزه‌های ترکیبیات و هندسه ترکیبیاتی\n"
                                                           " ❄️ موضوع ارائه Extremal Configurations in Point-Line Arrangements \n\n"
                                                           "🔺موضوع کارگاه \n"
                                                           "‌ \nIncidence Theorem and Its Applications")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "ندا سلطانی" :
            photo = open("/home/wssbot/nedaSoltani.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌ـکارگاه‌ـ‌ها\n"
                                                           " ❄️ ندا سلطانی \n"
                                                           "🔸دانشجوی دکتری دانشگاه امیرکبیر \n"
                                                           "🔹فعالیت بر روی Quality of Experience in a Pervasive Computing Environment \n"
                                                           "🔸فعالیت در حوزه Data Science \n"
                                                           "🔹فعالیت در حوزه SNA \n\n"
                                                           "🔺موضوع کارگاه\n"
                                                           " ‌ Social Network Analysis with Gephi\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "رضا محمدی":
            photo = open("/home/wssbot/rezaMohammadi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                           " ❄️ رضا محمدی \n"
                                                           "🔸لیسانس علوم کامپیوتر دانشگاه صنعتی شریف \n"
                                                           "🔹از بنیان‌گذاران کافه بازار \n"
                                                           "🔸از بنیان‌گذاران دیوار \n"
                                                           "🔹مالک محصول (Product Owner) در شرکت Machine2Learn واقع در آمستردام\n"
                                                           " 🔸مشغول مطالعه New Media and Digital Culture در دانشگاه آمستردام\\nn"
                                                           " ❄️ موضوع ارائه\n"
                                                           " ‏A Journey into Media Studies from the Perspective of a Technical Person\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر سلمان ابوالفتح بیگی" :
            photo = open("/home/wssbot/salmanAbolfathbeigi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                           " ❄️ دکتر سلمان ابوالفتح بیگی \n"
                                                           "🔸لیسانس علوم ریاضی دانشگاه صنعتی شریف\n"
                                                           " 🔹دکتری ریاضی دانشگاه MIT \n"
                                                           "🔸فوق دکترا در Institute for Quantum Information at Caltech \n"
                                                           "🔹عضو هیئت علمی پژوهشکده‌ی ریاضیات در پژوهشگاه دانش‌های بنیادی (IPM) \n"
                                                           "🔸عضو هیئت تحریریه مجله Mathematical Physics 🔹مدال طلای المپیاد جهانی ریاضی\n\n"
                                                           " ❄️ موضوع ارائه\n"
                                                           " ‏Nonlocal Correlations in Networks\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "سیمین اورعی" :
            photo = open("/home/wssbot/siminOreei.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                           " ❄️ سیمین اورعی \n"
                                                           "🔸دانشجوی دکتری در Max Planck \n"
                                                           "🔹فعالیت در حوزه Testing and model checking of distributed and concurrent systems \n"
                                                           "🔸کارآموزی symbolic model checking of reactive systems در IST Austria \n\n"
                                                           "❄️ موضوع ارائه\n"
                                                           " Random testing of distributed systems with guarantees\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر زهرا نظری" :
            photo = open("/home/wssbot/zahraNazari.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption=" #معرفی‌_سخنرانان \n"
                                                           "❄️ دکتر زهرا نظری 🔸دکتری علوم کامپیوتر از دانشگاه Southern California \n"
                                                           "🔹محقق در Spotify \n"
                                                           "🔸فعالیت در حوزه درک و مدل کردن رفتار انسان در وضعیت‌های پیچیده به ویژه برای استفاده در جست‌و‌جو و سیستم‌ها توصیه دهنده\n"
                                                           "🔹کارشناسی علوم کامپیوتر از دانشگاه امیرکبیر\n"
                                                           "🔸کارشناسی ارشد از دانشگاه لوئیزیانا\n\n"
                                                           "❄️ موضوع ارائه\n"
                                                           "\nRecommender Systems Research: Advances, Pitfalls and Opportunities")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "حامد صالح" :
            photo = open("/home/wssbot/hamedSaleh.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "مسعود زمانی" :
            photo = open("/home/wssbot/masodZamani.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "افرا آبنار" :
            photo = open("/home/wssbot/afraAbnar.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "آرش پوردامغانی" :
            photo = open("/home/wssbot/arashPordamqani.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر امید اعتصامی" :
            photo = open("/home/wssbot/omidEtesami.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر میثم علیزاده" :
            photo = open("/home/wssbot/meysamAlizadeh.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "امین بابادی" :
            photo = open("/home/wssbot/aminBabadi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر سینا دهقانی" :
            photo = open("/home/wssbot/sinaDehghani.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر محمد محمودی" :
            photo = open("/home/wssbot/mohammadMahmodi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "شهریار ابراهیمی" :
            photo = open("/home/wssbot/shahriyarEbrahimi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "مهدی صفرنژاد" :
            photo = open("/home/wssbot/mehdiSafarnenjad.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "امیر نجفی" :
            photo = open("/home/wssbot/amirNajjafi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "مسلم نوری" :
            photo = open("/home/wssbot/moslemNoori.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "محمد صالحه" :
            photo = open("/home/wssbot/mohammadSalehe.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "بازگشت" :
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            universityMap = types.KeyboardButton("نقشه دانشگاه")
            tables = types.KeyboardButton("جدول زمان بندی سمینار ها و کارگاه ها")
            introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
            vote = types.KeyboardButton("نظرسنجی")
            contact = types.KeyboardButton("ارتباط با ادمین")
            keyboard.add(universityMap)
            keyboard.add(tables)
            keyboard.add(introduce)
            keyboard.add(vote)
            keyboard.add(contact)
            msg = bot.reply_to(message, 'در حال بازگشت به منوی اصلی.', reply_markup=keyboard)
            bot.register_next_step_handler(msg, choosing_one)
        else:
            raise Exeption
    except Exception:
        msg = bot.reply_to(message, "فرد مورد نظر شما داخل لیست نیست. لطفا فرد دیگری را انتخاب کنید")
        bot.register_next_step_handler(msg, choosing_providers)



while True:
    try:
        bot.polling()
    except:
        time.sleep(15)
