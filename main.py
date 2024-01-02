import os,telebot
from telebot import types
def create_and_start_bot(token,type,id):
    
    try:
        info = telebot.TeleBot(token).get_me()
    except telebot.apihelper.ApiException:
        return

    filepath = os.path.join("get_proxy", type)
    os.system(f"nohup python {filepath} {token} {id} & ")


main_bot_token = "6601528903:AAGspZfvyNHnON2Z-UzvY5ARyhWmlVOqQU0" #main bot factory token here.

bot = telebot.TeleBot(main_bot_token)

users_with_bots = set()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    fg = """
اهلأ بك في بوت استضافه : Python3
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
تعليمات لرفع بوتك :

ارسل ملف بوتك ثانيا ارجع اضغط [start]

ثم تضهر لك ايديات اختار ايدي حسابك

وثم ارسل توكن بوتك ومبروك تم الرفع بنجاح
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
المبرمج : @P_W_7
"""
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>{fg}</strong>",parse_mode="html",reply_markup=key)
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, "البوتات المرفوعه حالياً", reply_markup=keyboard)

@bot.message_handler(commands=['list'])
def list_bots(message):
    
    files = os.listdir("bots")

    
    bot.send_message(message.chat.id, "\n".join(files))

def create_keyboard():
   
    files = os.listdir("get_proxy")

    
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for file in files:
        button = telebot.types.InlineKeyboardButton(text=file, callback_data=file)
        buttons.append(button)
    keyboard.add(*buttons)
    return keyboard
@bot.callback_query_handler(func=lambda query: True)
def start_bot(query):
    
    file = query.data
    a = bot.edit_message_text(chat_id=query.message.chat.id, text="ارسـل تـوكن بـوتك ",message_id=query.message.id)
    bot.register_next_step_handler(a, rec,file)
def rec(message,file):
    try:
        infos = telebot.TeleBot(message.text).get_me()
    except telebot.apihelper.ApiException:
        bot.reply_to(message, "الـتوكن خطـأ او مـرتبط فـي بوت أخر")
        return
    bot.reply_to(message, "البـوت جـاهز: " + file+"\nأسـم البوت: "+str(infos.first_name)+"\nيـوزر الـبوت: @"+str(infos.username))
    create_and_start_bot(message.text,file,str(message.from_user.id))

#zzk=0
@bot.message_handler(content_types=['document'])
def inf(message):
		id2 = message.from_user.id
		#print('gg')
		try:
			filename = message.document.file_name
			file_info = bot.get_file(message.document.file_id)
			use = bot.download_file(file_info.file_path)
			with open(f"m/tool : {id2}.py","wb") as (zaidno):
				zaidno.write(use)
		except:
			key = types.InlineKeyboardMarkup()
			bot.send_message(message.chat.id, f"<strong>هنـاك خـطأ فـي الـملف</strong>",parse_mode="html",reply_markup=key)
		key = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id, f"<strong>تـم حفض ملفك في البوت اضغط start/ الان وختار ايديك وأكمل الخطوات المطلوبه</strong>",parse_mode="html",reply_markup=key)
		
while True:
	def zaid_ali():
		try:
			bot.infinity_polling()
		except:
			zaid_ali()
	zaid_ali()
