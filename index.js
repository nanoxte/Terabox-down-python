async function main() {
  const { Telegraf, Markup } = require("telegraf");
  const { getDetails } = require("./api");
  const { sendFile } = require("./utils");

  const bot = new Telegraf(process.env.BOT_TOKEN);

  bot.start(async (ctx) => {
    try {
      ctx.reply(
        `Hi ${ctx.message.from.first_name},\n\nI can Download Files from Terabox.\n\nMade with ❤️ by [.𝖎𝖔𝖉𝖊𝖛𝖘](https://t.me/botio_devs)\n\nSend any terabox link to download.°°°° \n\n ⚠️spam is ban!!😒`,
        Markup.inlineKeyboard([
          Markup.button.url(" Channel", "https://t.me/botio_devs"),
        ]),
      );
    } catch (e) {
      console.error(e);
    }
  });

  bot.on("message", async (ctx) => {
    if (ctx.message && ctx.message.text) {
      const messageText = ctx.message.text;
      if (
        messageText.includes("terabox.com") ||
        messageText.includes("teraboxapp.com")
      ) {
        const details = await getDetails(messageText);
        if (details && details.direct_link) {
          try {
            ctx.reply(`Sending Files Please Wait.!!......✨`);
            sendFile(details.direct_link, ctx);
          } catch (e) {
            console.error(e); // Log the error for debugging
          }
        } else {
          ctx.reply('Something went wrong 🙃😒 \n  **contact admin for assistance**');
        }
        console.log(details);
      } else {
        ctx.reply("Please send a valid Terabox link.😕");
      }
    } else {
      //ctx.reply("No message text found.🤬");
    }
  });

  bot.launch();
}

main();
