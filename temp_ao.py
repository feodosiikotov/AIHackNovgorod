import telebot
from telebot import types
TOKEN = '1953421101:AAG_prDcNbeYqPRqYcxq_Rbwlb63ywBIZ_8'
bot = telebot.TeleBot(TOKEN)
from process_doc import process_doc

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """
    Поле content_types может принимать разные значения, и не только одно, например
    @bot.message_handler(content_types=['text', 'document', 'audio'])
    """
    if message.text == "/start":
        bot.send_message(message.from_user.id, """"Здравствуйте! 
Прикрепите к сообщению файл, который требуется проверить.
Если Вам требуется помощь, наберите "/help""")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, """"Данный бот предназначен для упрощения проверки законодательных актов и иных правовых документов на предмет наличия коррупциогенных факторов. Для того, чтобы программа могла совершить проверку, требуется прикрепить файл к пустому сообщению ("перетащить" в окошко чата Telegram) или активировать контекстный пункт меню и выбрать  во всплывшем окне проводника. Программа проверит документ, и если будут зафиксированы некоторые признаки, которые могут трактоваться как коррупциогенные факторы, она возвратит проверенный документ и выделит подозрительные места. Если же таких признаков не будет обнаружено, она отправит сообщение, что документ корректен - однако важно помнить,что любая компьютерная программа не дает стопроцентной эффективности, поэтому для наиболее четкой оценки требуется заключение квалифицированного действующего сотрудника Органов""")
  #  elif message.text == "Где":
  #      print ('done2')
  #      with open(file_route, "rb") as file:
  #          bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.from_user.id, """"Некорректная команда. Для помощи следует напечатать "Помощь" (без кавычек) или "/help"".""")
 
     
@bot.message_handler(content_types=['document'])   
def get_doc_messages(message):
    try:
        #try:
        save_dir = 'C:/Users/W/Documents/BotFiles'
        file_name = message.document.file_name
       # file_id = message.document.file_name
        file_id_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_id_info.file_path)
        src = file_name
        with open(save_dir + "/" + src, 'wb') as new_file:
            new_file.write(downloaded_file)
        # bot.send_message(message.chat.id, "[*] File added:\nFile name - {}\nFile directory - {}".format(str(file_name), str(save_dir)))
        file_route = 'C:/Users/W/Documents/BotFiles/Document.docx'
        text = process_doc(save_dir + "/" + src, file_route)
        bot.send_message(message.chat.id, text)
        with open(file_route, "rb") as file:
            bot.send_document(message.chat.id, file)
    except Exception as ex:
       bot.send_message(message.chat.id, "[!] error - {}".format(str(ex)))
"""
         
def load_docs(doc):
    # sendDocument
    doc = open('/tmp/file.txt', 'rb')
    bot.send_document (doc)
    bot.send_document("FILEID")    
"""

"""
@bot.message_handler(content_types = ['text'])
def send_file(message):
    print ('done')
    if message.text == "Где":
        print ('done2')
        with open(file_route, "rb") as file:
          #  files = {"document":filexlsx}
          #  title = "MarksSYAP.xlsx"
          #  chat_id = "1234567890"
            bot.send_document(message.chat.id, file)
"""  

bot.polling(none_stop=True, interval=0.3)


