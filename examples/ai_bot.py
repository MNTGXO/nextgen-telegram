from nextgen_telegram import HyperTelegramClient
from nextgen_telegram.ai.nlp import SmartReplyEngine

bot = HyperTelegramClient("ai_bot_session", config={
    "ai": {
        "enabled": True,
        "model_path": "models/telegram_nlp.onnx"
    },
    "routing": {
        "strategy": "auto"
    }
})

@bot.on_message()
async def handle_message(client, message):
    if message.text:
        reply = await client.ai.generate_reply(message)
        await message.reply(reply)

async def main():
    await bot.start()
    await bot.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
