import telebot
import time
from telebot import types

bot = telebot.TeleBot(bot_token)

user_dict = {}
pm_dict = {}

class voterList:
    def __init__(self, voterId):
        self.voterId = voterId
        self.providerName = None
        self.first_question = None
        self.second_question = None
        self.third_question = None
        self.fourth_question = None
        self.fifth_question = None
        self.sixth_question = None

class Pm:
    def __init__(self, id):
        self.id = id
        self.textToUser = None
@bot.message_handler(commands=['sendpmtoallmembers'])
def send_pm_to_all(message):
    msg = bot.send_message(message.chat.id , "now send me a text")
    bot.register_next_step_handler(msg, send_message_to_all)

def send_message_to_all(message):
    userFiles = open("/home/allusers.txt", "r+")
    ids = userFiles.read()
    ids = ids.split(" ")
    for i in ids:
        bot.send_message(int(i) , text = message.text)
    userFiles.flush()
    userFiles.close()

@bot.message_handler(commands=['start'])
def first_step(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
    tables = types.KeyboardButton("زمان بندی کارگاه ها")
    introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
    vote = types.KeyboardButton("نظرسنجی")
    sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
    contact = types.KeyboardButton("ارتباط با ادمین")
    location = types.KeyboardButton("مکان دانشگاه")
    keyboard.add(location)
    keyboard.add(universityMap)
    keyboard.add(tables)
    keyboard.add(introduce)
    keyboard.add(vote)
    keyboard.add(contact)
    keyboard.add(sokhanraniTime)
    userFiles = open("/home/users.txt", "a+")
    users = userFiles.read()
    users = users.split(" ")
    if str(message.chat.id) not in users:
        userFiles.write(str(message.chat.id) + " ")
    userFiles.flush()
    userFiles.close()
    msg = bot.reply_to(message, 'خوش آمدید. چه کمکی از دست من برمیاد؟', reply_markup=keyboard)
    bot.register_next_step_handler(msg, choosing_one)


def choosing_one(message):
    try:
        if message.text == "راهنمایی مکان های دانشگاه":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            universityMap = types.KeyboardButton("نقشه دانشگاه")
            dareJonobBeDaneshkadeh = types.KeyboardButton("گیف در جنوبی به دانشکده")
            dareShomaliBeDaneshkade = types.KeyboardButton("گیف در شمالی به دانشکده")
            dareShomaliBeTalar = types.KeyboardButton("گیف در شمالی به تالارها")
            talarBeSelf = types.KeyboardButton("گیف تالارها به سلف")
            dareJonobiBeTalar = types.KeyboardButton("گیف در جنوبی به تالارها")
            talarBeMasjed = types.KeyboardButton("تالار به مسجد")
            back = types.KeyboardButton("بازگشت")
            keyboard.add(universityMap)
            keyboard.add(dareJonobBeDaneshkadeh)
            keyboard.add(dareShomaliBeDaneshkade)
            keyboard.add(dareShomaliBeTalar)
            keyboard.add(talarBeSelf)
            keyboard.add(dareJonobiBeTalar)
            keyboard.add(talarBeMasjed)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id,"بخش مورد نظر خود را انتخاب کنید",  reply_markup=keyboard)
            bot.register_next_step_handler(msg, guidance)
        elif message.text == "زمان بندی کارگاه ها":
            photo = open("/home/wssbot/kargahHa.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo)
            bot.register_next_step_handler(msg, choosing_one)


        elif message.text == "جدول زمانی سخنرانی ها":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            first_day = types.KeyboardButton("روز اول")
            second_day = types.KeyboardButton("روز دوم")
            back = types.KeyboardButton("بازگشت")
            keyboard.add(first_day)
            keyboard.add(second_day)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id,
                                   "لطفا روز مورد نظر خود را انتخاب کنید.",
                                   reply_markup=keyboard)
            bot.register_next_step_handler(msg, which_day)


        elif message.text == "آشنایی با ارائه دهنده ها":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            alirezaRezaei = types.KeyboardButton("علیرضا رضایی(کارگاه)")
            behzadMoshiri = types.KeyboardButton("دکتر بهزاد مشیری(ارائه + کارگاه)")
            ehsanEmamjomezadeh = types.KeyboardButton("دکتر احسان امام جمعه زاده")
            meysamRazavin = types.KeyboardButton("دکتر میثم رضویین(ارائه + کارگاه)")
            mohammadHeydari = types.KeyboardButton("محمد حیدری(کارگاه)")
            mohammadKhaloei = types.KeyboardButton("محمد خالوئی(کارگاه)")
            mohammadMahdian = types.KeyboardButton("دکتر محمد مهدیان")
            mortezaSaberi = types.KeyboardButton("دکتر مرتضی صابری")
            mozhganMirzaei = types.KeyboardButton("مژگان میرزایی(ارائه + کارگاه)")
            nedaSoltani = types.KeyboardButton("ندا سلطانی(کارگاه)")
            rezaMohammadi = types.KeyboardButton("رضا محمدی")
            salmanAbolfathbeigi = types.KeyboardButton("دکتر سلمان ابوالفتح بیگی")
            siminOreei = types.KeyboardButton("سیمین اورعی")
            zahraNazari = types.KeyboardButton("دکتر زهرا نظری")
            hamedSaleh =  types.KeyboardButton("حامد صالح")
            masodZamani = types.KeyboardButton("مسعود زمانی(کارگاه)")
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
            msg = bot.send_message(message.chat.id, "فردی را انتخاب کنید", reply_markup=keyboard)
            bot.register_next_step_handler(msg, choosing_providers)

        elif message.text == "نظرسنجی":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            seminarvote = types.KeyboardButton("نظرسنجی کلی رویداد")
            speakersvote = types.KeyboardButton( "نظرسنجی مربوط به هر ارائه")
            keyboard.add(seminarvote)
            keyboard.add(speakersvote)
            msg = bot.send_message(message.chat.id, " به بخش نظرسنجی خوش آمدید، لطفا یکی از انواع نظرسنجی را انتخاب کنید...", reply_markup=keyboard)
            bot.register_next_step_handler(msg, vote_part)
        elif message.text == "مکان دانشگاه":
            msg = bot.send_location(message.chat.id, 35.700413, 51.352248)
            bot.register_next_step_handler(msg, choosing_one)
        elif message.text == "ارتباط با ادمین":
            msg = bot.send_message(message.chat.id, "لطفا با @atenasaghi تماس بگیرید")
            bot.register_next_step_handler(msg, choosing_one)
        else:
            raise Exception
    except Exception:
        msg = bot.send_message(message.chat.id, "دستور شما جزء دستورات این بات نیست. مجددا تلاش کنید.")
        bot.register_next_step_handler(msg, choosing_one)


def which_day(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        if message.text == "روز اول":
            photo = open("day1.jpg", 'rb')
            universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
            tables = types.KeyboardButton("زمان بندی کارگاه ها")
            introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
            vote = types.KeyboardButton("نظرسنجی")
            sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
            contact = types.KeyboardButton("ارتباط با ادمین")
            location = types.KeyboardButton("مکان دانشگاه")
            keyboard.add(location)
            keyboard.add(universityMap)
            keyboard.add(tables)
            keyboard.add(introduce)
            keyboard.add(vote)
            keyboard.add(contact)
            keyboard.add(sokhanraniTime)
            msg = bot.send_photo(message.chat.id, photo ,reply_markup = keyboard)
            bot.register_next_step_handler(msg , choosing_one)
        elif message.text == "روز دوم":
            photo = open("day2.jpg", 'rb')
            universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
            tables = types.KeyboardButton("زمان بندی کارگاه ها")
            introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
            vote = types.KeyboardButton("نظرسنجی")
            sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
            contact = types.KeyboardButton("ارتباط با ادمین")
            location = types.KeyboardButton("مکان دانشگاه")
            keyboard.add(location)
            keyboard.add(universityMap)
            keyboard.add(tables)
            keyboard.add(introduce)
            keyboard.add(vote)
            keyboard.add(contact)
            keyboard.add(sokhanraniTime)
            msg = bot.send_photo(message.chat.id, photo, reply_markup=keyboard)
            bot.register_next_step_handler(msg, choosing_one)
        elif message.text == "بازگشت" :
            universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
            tables = types.KeyboardButton("زمان بندی کارگاه ها")
            introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
            vote = types.KeyboardButton("نظرسنجی")
            sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
            contact = types.KeyboardButton("ارتباط با ادمین")
            location = types.KeyboardButton("مکان دانشگاه")
            keyboard.add(location)
            keyboard.add(universityMap)
            keyboard.add(tables)
            keyboard.add(introduce)
            keyboard.add(vote)
            keyboard.add(contact)
            keyboard.add(sokhanraniTime)
            msg = bot.send_message(message.chat.id, "شما در حال بازگشت به منوی اصلی هستید.", reply_markup=keyboard)
            bot.register_next_step_handler(msg, choosing_one)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, which_day)

def guidance(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        if message.text == "نقشه دانشگاه" :
            photo = open("/home/wssbot/kuroky.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, reply_markup=keyboard)
            bot.register_next_step_handler(msg, guidance)
        elif message.text == "گیف در جنوبی به دانشکده" :
            audio = open("/home/wssbot/dareJonobiBeDaneshkade.gif.mp4", 'rb')
            msg = bot.send_video(message.chat.id, audio, reply_markup=keyboard)
            bot.register_next_step_handler(msg, guidance)
        elif message.text ==  "گیف در شمالی به دانشکده" :
            audio = open("/home/wssbot/dareShomaliBeDaneshkade.gif.mp4", 'rb')
            msg = bot.send_video(message.chat.id, audio, reply_markup=keyboard)
            bot.register_next_step_handler(msg, guidance)
        elif message.text == "گیف در شمالی به تالارها" :
            audio = open("/home/wssbot/dareShomaliBeTalar.gif.mp4", 'rb')
            msg = bot.send_video(message.chat.id, audio, reply_markup=keyboard)
            bot.register_next_step_handler(msg, guidance)
        elif message.text ==  "گیف تالارها به سلف":
            audio = open("/home/wssbot/talarBeSelf.gif.mp4", 'rb')
            msg = bot.send_video(message.chat.id, audio, reply_markup=keyboard)
            bot.register_next_step_handler(msg, guidance)
        elif message.text ==  "گیف در جنوبی به تالارها":
            audio = open("/home/wssbot/dareJonobiBeTalar.gif.mp4", 'rb')
            msg = bot.send_video(message.chat.id, audio, reply_markup=keyboard)
            bot.register_next_step_handler(msg, guidance)
        elif message.text == "تالار به مسجد":
            audio = open("/home/wssbot/talarBeMasjed.mp4", 'rb')
            msg = bot.send_video(message.chat.id, audio, reply_markup=keyboard)
            bot.register_next_step_handler(msg, guidance)
        elif message.text == "بازگشت":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
            tables = types.KeyboardButton("زمان بندی کارگاه ها")
            introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
            vote = types.KeyboardButton("نظرسنجی")
            contact = types.KeyboardButton("ارتباط با ادمین")
            sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
            location = types.KeyboardButton("مکان دانشگاه")
            keyboard.add(location)
            keyboard.add(sokhanraniTime)
            keyboard.add(universityMap)
            keyboard.add(tables)
            keyboard.add(introduce)
            keyboard.add(vote)
            keyboard.add(contact)
            msg = bot.reply_to(message, "این بخش در حال کامل شدن است، در حال بازگشت به منوی اصلی", reply_markup=keyboard)
            bot.register_next_step_handler(msg, choosing_one)

    except Exception :
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, choosing_one)


def vote_part(message):
    try:
        if message.text == "نظرسنجی کلی رویداد" :
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
            tables = types.KeyboardButton("زمان بندی کارگاه ها")
            introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
            vote = types.KeyboardButton("نظرسنجی")
            contact = types.KeyboardButton("ارتباط با ادمین")
            sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
            location = types.KeyboardButton("مکان دانشگاه")
            keyboard.add(location)
            keyboard.add(sokhanraniTime)
            keyboard.add(universityMap)
            keyboard.add(tables)
            keyboard.add(introduce)
            keyboard.add(vote)
            keyboard.add(contact)
            msg = bot.reply_to(message, "این بخش در حال کامل شدن است، در حال بازگشت به منوی اصلی", reply_markup=keyboard)
            bot.register_next_step_handler(msg, choosing_one)
        elif message.text == "نظرسنجی مربوط به هر ارائه" :
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            behzadMoshiri = types.KeyboardButton("Behzad Moshiri - Data Fusion” an AI approach for decision making")
            omidEtesami = types.KeyboardButton("Omid Etesami - Computational Concentration of Measure and Robust Learning")
            aminBabadi = types.KeyboardButton("Amin Babadi - Animation Synthesis using Machine Learning")
            siminOreei = types.KeyboardButton("Simin Oreei - Random testing of distributed systems with guarantees")
            afraAbnar = types.KeyboardButton("Afra Abnar - Microservice Architecture")
            mohammadMahdian = types.KeyboardButton("Mohammad Mahdian - Fairness in Clustering Algorithms")
            shahriyarEbrahimi = types.KeyboardButton("Shahriyar Ebrahimi - The Future of Cryptography: a Case-study of Lattice-based ones")
            ehsanEmamjomezadeh = types.KeyboardButton("Ehsan Emamjomeh-Zadeh - Online Learning")
            meysamAlizadeh = types.KeyboardButton("Meysam Alizadeh - Detecting Coordinated Influence Operation Content on Social Media")
            mohammadMahmodi = types.KeyboardButton("Mohammad Mahmoody - Registration-Based Encryption")
            moslemNoori = types.KeyboardButton("Moslem Noori - An application of quantum computing in chemistry")
            mozhganMirzaei = types.KeyboardButton("Mozhgan Mirzaei - Extremal Configurations in Point-Line Arrangements")
            salmanAbolfathbeigi = types.KeyboardButton("Salman Abolfath Beygi - Nonlocal Correlations in Networks")
            mohammadHosseinNoranian = types.KeyboardButton("Mohammad Hossein Noranian - Complexities in AI Commercialization")
            kerishaGomadi = types.KeyboardButton("Krishna Gummadi - Fairness in Machine Learning")
            hamedSaleh =  types.KeyboardButton("Hamed Saleh - Streaming and Massively Parellel Algorithms for Edge Coloring")
            mortezaSaberi = types.KeyboardButton("Morteza Saberi - Personalized Assortment Optimization for Online Retailer Considering Risk of Customers Churning")
            aliSharifiZarchi = types.KeyboardButton("Ali Sharifi Zarchi - Addressing several biomedical problems using deep learning")
            sinaDehghani = types.KeyboardButton("Sina Dehghani - Price of Competition and Dueling Games")
            rezaMohammadi = types.KeyboardButton("Reza Mohammadi - ‏A Journey into Media Studies from the Perspective of a Technical Person")
            amirNajjafi = types.KeyboardButton("Amir Najafi - Robustness to Adversarial Perturbations in Learning from Incomplete Data")
            mehdiSafarnenjad = types.KeyboardButton("Mahdi Safarnejad - Edit Distance and LCS: Beyond Worst Case")
            zahraNazari = types.KeyboardButton("Zahra Nazari - Recommender Systems Research: Advances, Pitfalls and Opportunities")
            mohammadSalehe = types.KeyboardButton("Mohammad Salehe - ‏Cloud Computing, Edge Computing and Beyond")
            arashPordamqani = types.KeyboardButton("Arash Pourdamghani - Algorithms and Games in Blockchain: Designing Verifable Systems")
            meysamRazavin = types.KeyboardButton("Meisam Razaviyayn - ‏Learning via Non-Convex Min-Max Games")


            back = types.KeyboardButton("انصراف")
            keyboard.add(behzadMoshiri)
            keyboard.add(omidEtesami)
            keyboard.add(aminBabadi)
            keyboard.add(siminOreei)
            keyboard.add(afraAbnar)
            keyboard.add(mohammadMahdian)
            keyboard.add(shahriyarEbrahimi)
            keyboard.add(ehsanEmamjomezadeh)
            keyboard.add(meysamAlizadeh)
            keyboard.add(mohammadMahmodi)
            keyboard.add(moslemNoori)
            keyboard.add(mozhganMirzaei)
            keyboard.add(salmanAbolfathbeigi)
            keyboard.add(mohammadHosseinNoranian)
            keyboard.add(kerishaGomadi)
            keyboard.add(hamedSaleh)
            keyboard.add(mortezaSaberi)
            keyboard.add(aliSharifiZarchi)
            keyboard.add(sinaDehghani)
            keyboard.add(rezaMohammadi)
            keyboard.add(amirNajjafi)
            keyboard.add(mehdiSafarnenjad)
            keyboard.add(zahraNazari)
            keyboard.add(mohammadSalehe)
            keyboard.add(arashPordamqani)
            keyboard.add(meysamRazavin)

            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "لطفا فرد مورد نظر خود را انتخاب کنید", reply_markup=keyboard)
            bot.register_next_step_handler(msg, vote_for_speakers)

    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, vote_part)



def vote_for_speakers(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        chatId = message.chat.id
        providerName = message.text
        voterlist = voterList(chatId)
        user_dict[chatId] = voterlist
        voterlist.voterId = message.chat.id
        voterlist.providerName = providerName
        if message.text == "Behzad Moshiri - Data Fusion” an AI approach for decision making" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text =="Omid Etesami - Computational Concentration of Measure and Robust Learning" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Amin Babadi - Animation Synthesis using Machine Learning" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Simin Oreei - Random testing of distributed systems with guarantees" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Mohammad Mahdian - Fairness in Clustering Algorithms" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Shahriyar Ebrahimi - The Future of Cryptography: a Case-study of Lattice-based ones" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Ehsan Emamjomeh-Zadeh - Online Learning" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Meysam Alizadeh - Detecting Coordinated Influence Operation Content on Social Media" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Mohammad Mahmoody - Registration-Based Encryption":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text ==  "Moslem Noori - An application of quantum computing in chemistry":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Mozhgan Mirzaei - Extremal Configurations in Point-Line Arrangements":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text =="Salman Abolfath Beygi - Nonlocal Correlations in Networks" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Mohammad Hossein Noranian - Complexities in AI Commercialization":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Krishna Gummadi - Fairness in Machine Learning":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text =="Hamed Saleh - Streaming and Massively Parellel Algorithms for Edge Coloring" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Morteza Saberi - Personalized Assortment Optimization for Online Retailer Considering Risk of Customers Churning":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Ali Sharifi Zarchi - Addressing several biomedical problems using deep learning":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Sina Dehghani - Price of Competition and Dueling Games":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Reza Mohammadi - ‏A Journey into Media Studies from the Perspective of a Technical Person":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Amir Najafi - Robustness to Adversarial Perturbations in Learning from Incomplete Data":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Mahdi Safarnejad - Edit Distance and LCS: Beyond Worst Case" :
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Zahra Nazari - Recommender Systems Research: Advances, Pitfalls and Opportunities":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Mohammad Salehe - ‏Cloud Computing, Edge Computing and Beyond":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Arash Pourdamghani - Algorithms and Games in Blockchain: Designing Verifable Systems":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "Meisam Razaviyayn - ‏Learning via Non-Convex Min-Max Games":
            first = types.KeyboardButton("1")
            second = types.KeyboardButton("2")
            third = types.KeyboardButton("3")
            fourth = types.KeyboardButton("4")
            fifth = types.KeyboardButton("5")
            back = types.KeyboardButton("انصراف")
            keyboard.add(first)
            keyboard.add(second)
            keyboard.add(third)
            keyboard.add(fourth)
            keyboard.add(fifth)
            keyboard.add(back)
            msg = bot.send_message(message.chat.id, "۱. ارائه مناسب و قابل فهم", reply_markup=keyboard)
            bot.register_next_step_handler(msg, first_question)

        elif message.text == "انصراف" :
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
            tables = types.KeyboardButton("زمان بندی کارگاه ها")
            introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
            vote = types.KeyboardButton("نظرسنجی")
            contact = types.KeyboardButton("ارتباط با ادمین")
            sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
            location = types.KeyboardButton("مکان دانشگاه")
            keyboard.add(location)
            keyboard.add(sokhanraniTime)
            keyboard.add(universityMap)
            keyboard.add(tables)
            keyboard.add(introduce)
            keyboard.add(vote)
            keyboard.add(contact)
            msg = bot.send_message(message.chat.id , "شما در حال برگردانده شدن هستید.", reply_markup=keyboard)
            bot.register_next_step_handler(msg, choosing_one)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, vote_part)


def first_question(message):
    try:
        accepted = ["1", "2", "3", "4", "5", "انصراف"]
        if message.text in accepted:
            if message.text == "انصراف" :
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
                tables = types.KeyboardButton("زمان بندی کارگاه ها")
                introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
                vote = types.KeyboardButton("نظرسنجی")
                contact = types.KeyboardButton("ارتباط با ادمین")
                sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
                location = types.KeyboardButton("مکان دانشگاه")
                keyboard.add(location)
                keyboard.add(sokhanraniTime)
                keyboard.add(universityMap)
                keyboard.add(tables)
                keyboard.add(introduce)
                keyboard.add(vote)
                keyboard.add(contact)
                msg = bot.send_message(message.chat.id , "شما در حال برگردانده شدن هستید.", reply_markup=keyboard)
                bot.register_next_step_handler(msg, choosing_one)
            else:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                chatId = message.chat.id
                voterlist = user_dict[chatId]
                voterlist.first_question = message.text
                first = types.KeyboardButton("1")
                second = types.KeyboardButton("2")
                third = types.KeyboardButton("3")
                fourth = types.KeyboardButton("4")
                fifth = types.KeyboardButton("5")
                back = types.KeyboardButton("انصراف")
                keyboard.add(first)
                keyboard.add(second)
                keyboard.add(third)
                keyboard.add(fourth)
                keyboard.add(fifth)
                keyboard.add(back)
                msg = bot.send_message(message.chat.id, "۲. تسلط ارائه دهنده بر موضوع", reply_markup=keyboard)
                bot.register_next_step_handler(msg, second_question)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, first_question)

def second_question(message):
    try:
        accepted = ["1", "2", "3", "4", "5", "انصراف"]
        if message.text in accepted:
            if message.text == "انصراف" :
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
                tables = types.KeyboardButton("زمان بندی کارگاه ها")
                introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
                vote = types.KeyboardButton("نظرسنجی")
                contact = types.KeyboardButton("ارتباط با ادمین")
                sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
                location = types.KeyboardButton("مکان دانشگاه")
                keyboard.add(location)
                keyboard.add(sokhanraniTime)
                keyboard.add(universityMap)
                keyboard.add(tables)
                keyboard.add(introduce)
                keyboard.add(vote)
                keyboard.add(contact)
                msg = bot.send_message(message.chat.id , "شما در حال برگردانده شدن هستید.", reply_markup=keyboard)
                bot.register_next_step_handler(msg, choosing_one)
            else:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                chatId = message.chat.id
                voterlist = user_dict[chatId]
                voterlist.second_question = message.text
                first = types.KeyboardButton("1")
                second = types.KeyboardButton("2")
                third = types.KeyboardButton("3")
                fourth = types.KeyboardButton("4")
                fifth = types.KeyboardButton("5")
                back = types.KeyboardButton("انصراف")
                keyboard.add(first)
                keyboard.add(second)
                keyboard.add(third)
                keyboard.add(fourth)
                keyboard.add(fifth)
                keyboard.add(back)
                msg = bot.send_message(message.chat.id, "۳. مناسب بودن موضوع ارائه شده", reply_markup=keyboard)
                bot.register_next_step_handler(msg, third_question)

    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, second_question)

def third_question(message):
    try:
        accepted = ["1", "2", "3", "4", "5", "انصراف"]
        if message.text in accepted:
            if message.text == "انصراف" :
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
                tables = types.KeyboardButton("زمان بندی کارگاه ها")
                introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
                vote = types.KeyboardButton("نظرسنجی")
                contact = types.KeyboardButton("ارتباط با ادمین")
                sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
                location = types.KeyboardButton("مکان دانشگاه")
                keyboard.add(location)
                keyboard.add(sokhanraniTime)
                keyboard.add(universityMap)
                keyboard.add(tables)
                keyboard.add(introduce)
                keyboard.add(vote)
                keyboard.add(contact)
                msg = bot.send_message(message.chat.id , "شما در حال برگردانده شدن هستید.", reply_markup=keyboard)
                bot.register_next_step_handler(msg, choosing_one)
            else:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                chatId = message.chat.id
                voterlist = user_dict[chatId]
                voterlist.third_question = message.text
                yes = types.KeyboardButton("بله")
                no = types.KeyboardButton("خیر")
                back = types.KeyboardButton("انصراف")
                keyboard.add(yes)
                keyboard.add(no)
                keyboard.add(back)
                msg = bot.send_message(message.chat.id, "۴. آیا موضوع گفته شده با محتوای ارائه تناسب داشت؟", reply_markup=keyboard)
                bot.register_next_step_handler(msg, fourth_question)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, third_question)


def fourth_question(message):
    try:
        accepted = ["بله" , "خیر", "انصراف"]
        if message.text in accepted:
            if message.text == "انصراف" :
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
                tables = types.KeyboardButton("زمان بندی کارگاه ها")
                introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
                vote = types.KeyboardButton("نظرسنجی")
                contact = types.KeyboardButton("ارتباط با ادمین")
                sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
                location = types.KeyboardButton("مکان دانشگاه")
                keyboard.add(location)
                keyboard.add(sokhanraniTime)
                keyboard.add(universityMap)
                keyboard.add(tables)
                keyboard.add(introduce)
                keyboard.add(vote)
                keyboard.add(contact)
                msg = bot.send_message(message.chat.id , "شما در حال برگردانده شدن هستید.", reply_markup=keyboard)
                bot.register_next_step_handler(msg, choosing_one)
            else:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                chatId = message.chat.id
                voterlist = user_dict[chatId]
                voterlist.fourth_question = message.text
                first = types.KeyboardButton("1")
                second = types.KeyboardButton("2")
                third = types.KeyboardButton("3")
                fourth = types.KeyboardButton("4")
                fifth = types.KeyboardButton("5")
                back = types.KeyboardButton("انصراف")
                keyboard.add(first)
                keyboard.add(second)
                keyboard.add(third)
                keyboard.add(fourth)
                keyboard.add(fifth)
                keyboard.add(back)
                msg = bot.send_message(message.chat.id, "۵. در کل به این ارائه چه نمره ای را می‌دهید؟", reply_markup=keyboard)
                bot.register_next_step_handler(msg, fifth_question)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, fourth_question)



def fifth_question(message):
    try:
        accepted = ["1", "2", "3", "4", "5", "انصراف"]
        if message.text in accepted:
            if message.text == "انصراف" :
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
                tables = types.KeyboardButton("زمان بندی کارگاه ها")
                introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
                vote = types.KeyboardButton("نظرسنجی")
                contact = types.KeyboardButton("ارتباط با ادمین")
                sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
                location = types.KeyboardButton("مکان دانشگاه")
                keyboard.add(location)
                keyboard.add(sokhanraniTime)
                keyboard.add(universityMap)
                keyboard.add(tables)
                keyboard.add(introduce)
                keyboard.add(vote)
                keyboard.add(contact)
                msg = bot.send_message(message.chat.id , "شما در حال برگردانده شدن هستید.", reply_markup=keyboard)
                bot.register_next_step_handler(msg, choosing_one)
            else:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                chatId = message.chat.id
                voterlist = user_dict[chatId]
                voterlist.fifth_question = message.text
                msg = bot.send_message(message.chat.id, "۶. اگر نظر دیگری درباره ارائه دهنده دارید ذکر کنید. ", reply_markup=keyboard)
                bot.register_next_step_handler(msg, sixth_question)
    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, fifth_question)

def sixth_question(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        chatId = message.chat.id
        voterlist = user_dict[chatId]
        sixthAnswer = message.text
        voterlist.sixth_question = sixthAnswer
        allAnswers = str("from chat Id:"+ str(voterlist.voterId) + "\tprovider:" +    str(voterlist.providerName)+ "\tfirst question:"
                         + str(voterlist.first_question) +"\tsecond_question:" + str(voterlist.second_question) +
                         "\tthird_question:" + str(voterlist.third_question) + "\tfourth_question:" + str(voterlist.fourth_question)
                         + "\tfifth_question:" + str(voterlist.fifth_question) + "\tsixth_question:" + str(voterlist.sixth_question) + "\n" )
        myFile = open("/home/seminarVotes.txt", "a+")
        myFile.write(allAnswers)
        myFile.flush()
        myFile.close()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
        tables = types.KeyboardButton("زمان بندی کارگاه ها")
        introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
        vote = types.KeyboardButton("نظرسنجی")
        contact = types.KeyboardButton("ارتباط با ادمین")
        sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
        location = types.KeyboardButton("مکان دانشگاه")
        keyboard.add(location)
        keyboard.add(sokhanraniTime)
        keyboard.add(universityMap)
        keyboard.add(tables)
        keyboard.add(introduce)
        keyboard.add(vote)
        keyboard.add(contact)
        msg = bot.send_message(message.chat.id, "با تشکر از شما، نظر شما ثبت شد. ", reply_markup=keyboard)
        bot.register_next_step_handler(msg, choosing_one)

    except Exception:
        msg = bot.reply_to(message, "دستور شما جز دستورات بات نیست. لطفا مجددا تلاش کنید")
        bot.register_next_step_handler(msg, sixth_question)



def choosing_providers(message):
    try:
        if message.text == "دکتر بهزاد مشیری(ارائه + کارگاه)" :
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
        elif message.text == "علیرضا رضایی(کارگاه)" :
            photo = open("/home/wssbot/alirezaRezaei.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌ـکارگاه‌ـ‌ها ❄️ \n"
                                                           "علیرضا رضایی \n"
                                                           "🔸دانشجوی دکتری دانشگاه واشنگتن\n"
                                                           " 🔹فعالیت در determinantal point processes and their applications in machine learning and spectral graph theory \n"
                                                           "🔸کارشناسی ریاضی و مهندسی کامپیوتر در دانشگاه شریف \n\n"
                                                           "🔺موضوع کارگاه \n"
                                                           "‌ Modeling Diversity in Machine Learning Using Determinantal Point Processes\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر میثم رضویین(ارائه + کارگاه)" :
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
        elif message.text == "محمد حیدری(کارگاه)" :
            photo = open("/home/wssbot/mohammadHeydari.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌ـکارگاه‌ـ‌ها\n"
                                                           " ❄️ محمد حیدری \n"
                                                           "🔸کارشناسی ارشد دانشگاه تربیت مدرس \n"
                                                           "🔹فعالیت در حوزه Big Data Analytics Techniques and their Application in Large Scale Social Networks \n"
                                                           "🔸کارشناسی مهندسی کامپیوتر دانشگاه فنی و حرفه‌ای \n"
                                                           "🔺موضوع کارگاه\n"
                                                           " ‌ Discovering Latent Patterns in Academic Collaboration Network based on Community Detection Approach\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "محمد خالوئی(کارگاه)" :
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
        elif message.text == "مژگان میرزایی(ارائه + کارگاه)" :
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
        elif message.text == "ندا سلطانی(کارگاه)" :
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
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                                 " ❄️ حامد صالح \n"
                                                                 "🔸دانشجوی دکتری در رشته علوم کامپیوتر دانشگاه مریلند \n"
                                                                 "🔹کارشناسی از دانشگاه صنعتی شریف \n"
                                                                 "🔸فعالیت در حوزه combinatorial problems in distributed/parallel models به طور ویژه models with sublinear memory \n\n"
                                                                 "❄️ موضوع ارائه \n"
                                                                 "Streaming and Massively Parellel Algorithms for Edge Coloring\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "مسعود زمانی(کارگاه)" :
            photo = open("/home/wssbot/masodZamani.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_کارگاه‌ـ‌ها\n"
                                                                 " ❄️ مسعود زمانی \n"
                                                                 "🔸کارشناسی ارشد امیرکبیر 🔹تحقیق و فعالیت در حوزه آینده‌پژوهی به ویژه \ntechnological singularity"
                                                                 " 🔸مطالعه و تحقیق future ethical و legal sides of technology \n"
                                                                 "🔹انجام پروژه های متنوع از ترکیب nanotech، biotech و cognitive scince و همینطور AI و Blockchain \n"
                                                                 "🔸مدیر آزمایشگاه فناوری‌های پیشرفته در فناپ\n\n"
                                                                 " 🔺موضوع کارگاه ‌\n"
                                                                 " Choose to be a Wizard or a Muggle? Journey towards an Exponential world.\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "افرا آبنار" :
            photo = open("/home/wssbot/afraAbnar.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                                 " ❄️ افرا آبنار \n"
                                                                 "🔸کارشناسی از دانشگاه صنعتی شریف\n"
                                                                 " 🔹کارشناسی ارشد در دانشگاه آلبرتا \n"
                                                                 "🔸توسعه دهنده نرم‌افزار ارشد در SAP \n"
                                                                 "🔹فعالیت و تحقیق در حوزه Data Mining\n\n"
                                                                 " ❄️ موضوع ارائه"
                                                                 " \nMicroservice Architecture")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "آرش پوردامغانی" :
            photo = open("/home/wssbot/arashPordamqani.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                                 " ❄️ آرش پوردامغانی \n"
                                                                 "🔸دانشجوی دکتری در دانشگاه نیویورک\n"
                                                                 " 🔹فعالیت و تحقیق در حوزه‌ی Algorithmic Game Theory و مسئله‌های الگوریتمی دیگر\n"
                                                                 " 🔸کارشناسی مهندسی کامپیوتر از دانشگاه شریف \n\n"
                                                                 "❄️ موضوع ارائه\n"
                                                                 " \nAlgorithms and Games in Blockchain: Designing Verifable Systems")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر امید اعتصامی" :
            photo = open("/home/wssbot/omidEtesami.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                                 " ❄️ دکتر امید اعتصامی \n"
                                                                 "🔸محقق در پژوهشگاه دانش‌های بنیادی\n"
                                                                 " 🔹کارشناسی و کراشناسی ارشد از دانشگاه شریف\n"
                                                                 " 🔸دکتر از دانشگاه  California, Berkeley \n"
                                                                 "🔹پسادکتر از  EPFL, Switzerland 🔸فعالیت در بخش تحقیقاتی مایکروسافت\n"
                                                                 " 🔹بهترین مقاله در علوم کامپیوتر سال ۲۰۱۴ از دیدگاه ACM Computing Reviews \n"
                                                                 "🔸فعالت در حوزه استفاده از probability and randomness در علوم کامپیوتر\n\n"
                                                                 " ❄️ موضوع ارائه\n"
                                                                 " Computational Concentration of Measure and Robust Learning\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر میثم علیزاده" :
            photo = open("/home/wssbot/meysamAlizadeh.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان \n"
                                                                 "️ آرش پوردامغانی \n"
                                                                 "🔸دانشجوی دکتری در دانشگاه نیویورک \n"
                                                                 "🔹فعالیت و تحقیق در حوزه‌ی Algorithmic Game Theory و مسئله‌های الگوریتمی دیگر \n"
                                                                 "🔸کارشناسی مهندسی کامپیوتر از دانشگاه شریف \n\n"
                                                                 "❄️ موضوع ارائه\n"
                                                                 " \nAlgorithms and Games in Blockchain: Designing Verifable Systems")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "امین بابادی" :
            photo = open("/home/wssbot/aminBabadi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                                 " ❄️ امین بابادی \n"
                                                                 "🔸دانشجوی دکتری علوم کامپیوتر در دانشگاه آلتو \n"
                                                                 "🔹پژوهشگر بازدیدکننده در آزمایشگاه Imager دانشگاه sity of British Columbia, Canada \n"
                                                                 "🔸فعالیت کنونی در حوزه Development of Efficient and Creative Movement AI for Physically/Biomechanically Simulated Game Characters in Multi-Agent Environments \n"
                                                                 "🔹۱۰سال تجربه در صنعت بازی‌سازی به ویژه در بخش‌های  AI, animation, gameplay, و physics \n\n"
                                                                 "❄️ موضوع ارائه\n"
                                                                 " Animation Synthesis using Machine Learning\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر سینا دهقانی" :
            photo = open("/home/wssbot/sinaDehghani.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان \n"
                                                                 "️❄ دکتر سینا دهقانی \n"
                                                                 "🔸پسادکتر در پژوهشگاه دانش‌های بنیادی \n"
                                                                 "🔹دکتر علوم کامپیوتر از دانشگاه مریلند\n"
                                                                 " 🔸فعالیت در حوزه Algorithmic Game Theory و Online Algorithms and Approximation Algorithms و Algorithmic Graph Theory and Social Networks \n\n"
                                                                 "❄️ موضوع ارائه\n"
                                                                 " Price of Competition and Dueling Games\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "دکتر محمد محمودی" :
            photo = open("/home/wssbot/mohammadMahmodi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان \n"
                                                                 "️❄ دکتر محمد محمودی \n"
                                                                 "🔸دکتری از دانشگاه پرینستون \n"
                                                                 "🔹کارشناسی مهندسی کامپیوتر از دانشگاه صنعتی شریف \n"
                                                                 "🔸فعالیت و تحقیق در حوزه‌ی foundations of Cryptography و تعامل آن با Computational Complexity و Adversarial Learning \n"
                                                                 "🔹پسادکتری در دانشگاه Cornell \n"
                                                                 "🔸استادیار در دانشگاه ویرجینیا \n\n"
                                                                 "❄️ موضوع ارائه\n"
                                                                 " Registration-Based Encryption\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "شهریار ابراهیمی" :
            photo = open("/home/wssbot/shahriyarEbrahimi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان \n"
                                                                 "❄️ شهریار ابراهیمی \n"
                                                                 "🔸کارشناسی و کارشناسی ارشد از دانشگاه صنعتی شریف \n"
                                                                 "🔹دانشجوی دکتری مهندسی کامپیوتر در دانشگاه صنعتی شریف \n"
                                                                 "🔸محقق تمام وقت در آزمایشگاه Secure and Smart Systems (3S) \n"
                                                                 "🔹محقق مهمان در دانشگاه‌های Mainz (ZDV center) و Hamburg (DKRZ center) \n"
                                                                 "🔸فعالیت و پژوهش در حوزه‌های Post-quantum cryptography, Lattice-based cryptography, Internet of Things (IoT) و Computer/Network Architecture and Security \n\n"
                                                                 "❄️ موضوع ارائه\n"
                                                                 " The Future of Cryptography: a Case-study of Lattice-based ones\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "مهدی صفرنژاد" :
            photo = open("/home/wssbot/mehdiSafarnenjad.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                                 " ❄️مهدی صفرنژاد \n"
                                                                 "🔸دانشجوی دکتری دانشگاه صنعتی شریف 🔹فعالیت و تحقیق در حوزه‌‌ی approximation algorithms for edit distance و مسئله‌های مشابه \n"
                                                                 "🔸کارشناسی و کارشناسی ارشد از دانشگاه صنعتی شریف \n\n"
                                                                 "❄️ موضوع ارائه\n"
                                                                 " \nEdit Distance and LCS: Beyond Worst Case")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "امیر نجفی" :
            photo = open("/home/wssbot/amirNajjafi.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان\n"
                                                                 " ❄️امیر نجفی \n"
                                                                 "🔸دانشجوی دکتری مهندسی کامپیوتر در دانشگاه صنعتی شریف \n"
                                                                 "🔹کارشناسی و کارشناسی ارشد مهندسی برق از دانشگاه صنعتی شریف \n"
                                                                 "🔸 محقق مهمان در دانشگاه‌های MIT، Harvard، Boston و MA \n"
                                                                 "🔹فعالیت در حوزه‌های machine learning theory, information theory و bioinformatics\n\n"
                                                                 " ❄️ موضوع ارائه\n"
                                                                 " Robustness to Adversarial Perturbations in Learning from Incomplete Data\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "مسلم نوری" :
            photo = open("/home/wssbot/moslemNoori.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان \n"
                                                                 "❄️دکتر  مسلم نوری\n "
                                                                 "🔸کارشناسی ارشد و دکتری از دانشگاه آلبرتا\n"
                                                                 " 🔹کارشناسی مهندسی برق و ریاضیات کاربردی از دانشگاه امیرکبیر\n"
                                                                 " 🔸 شرکت در دو دوره پسادکتری از دانشگاه‌های بریتیش کلمبیا و آلبرتا\n"
                                                                 " 🔹دوره بازدید از Nokia Bell Labs \n"
                                                                 "🔸محقق ارشد در 1QBit 🔹فعالیت در تیم  Microsoft Quantum در ردموند \n\n"
                                                                 "❄️ موضوع ارائه\n"
                                                                 " An application of quantum computing in chemistry\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "محمد صالحه" :
            photo = open("/home/wssbot/mohammadSalehe.jpg", 'rb')
            msg = bot.send_photo(message.chat.id, photo, caption="#معرفی‌_سخنرانان \n❄"
                                                                 "️ محمد صالحه \n"
                                                                 "🔸دانشجوی دکتر در دانشگاه تورنتو 🔹کارشناسی و کارشناسی ارشد از دانشگاه صنعتی شریف\n"
                                                                 " 🔸فعالیت در حوزه‌های Distributed Systems, Cloud Computing و Software Systems \n\n"
                                                                 "❄️ موضوع ارائه\n"
                                                                 " ‏Cloud Computing, Edge Computing and Beyond\n")
            bot.register_next_step_handler(msg, choosing_providers)
        elif message.text == "بازگشت" :
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            universityMap = types.KeyboardButton("راهنمایی مکان های دانشگاه")
            tables = types.KeyboardButton("زمان بندی کارگاه ها")
            introduce = types.KeyboardButton("آشنایی با ارائه دهنده ها")
            vote = types.KeyboardButton("نظرسنجی")
            sokhanraniTime = types.KeyboardButton("جدول زمانی سخنرانی ها")
            contact = types.KeyboardButton("ارتباط با ادمین")
            location = types.KeyboardButton("مکان دانشگاه")
            keyboard.add(location)
            keyboard.add(universityMap)
            keyboard.add(tables)
            keyboard.add(introduce)
            keyboard.add(vote)
            keyboard.add(contact)
            keyboard.add(sokhanraniTime)
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
