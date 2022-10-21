from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
import my_infos

token = my_infos.token
############################### Bot ############################################

def start(update, context):
  update.message.reply_text(main_menu_message(),
                        reply_markup=main_menu_keyboard())

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

# and so on for every callback_data option
def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Listas', callback_data='m1')],
              [InlineKeyboardButton('Provas', callback_data='m2')],
              [InlineKeyboardButton('Matrícula', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Exercicios', callback_data='m1_1')],
              [InlineKeyboardButton('Notas', callback_data='m1_2')],
              [InlineKeyboardButton('Menu inicial', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Notas', callback_data='m2_1')],
              [InlineKeyboardButton('Medias', callback_data='m2_2')],
              [InlineKeyboardButton('Menu inicial', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Escolha uma opção no menu: '

def first_menu_message():
  return 'Escolha uma opção: '

def second_menu_message():
  return 'Escolha uma opção: '

############################# Handlers #########################################
updater = Updater(token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu,
                                                    pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu,
                                                    pattern='m2_1'))

updater.start_polling()