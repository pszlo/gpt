import openai
import telebot

openai.api_key = "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"
bot = telebot.TeleBot("5876607430:AAFcMgFdDZ4RJM8-PoFtAMb6rTxvbZBG4tE")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response["choices"][0]["text"])

bot.polling()