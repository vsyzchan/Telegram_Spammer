import time

from telethon import TelegramClient, events

api_id = api_id
api_hash = 'api_hash'

phone = '+62nomor hp'
session_file = 'nama sesi'
password = 'password, kalo gak ada kosongin aja'

message = "< Haha-hihi room chat > \n\nJoin sini terutama yang nolep, menerima semua golongan ⁄(⁄ ⁄•⁄-⁄•⁄ ⁄)⁄  \n\n@hahahihigroupchat ←(>▽<)ﾉ\n@hahahihigroupchat ←(>▽<)ﾉ\n@hahahihigroupchat ←(>▽<)ﾉ\n@hahahihigroupchat ←(>▽<)ﾉ\n@hahahihigroupchat ←(>▽<)ﾉ"

if __name__ == '__main__': 

    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
      if event.is_group:
        from_ = await event.client.get_entity(event.from_id)
        if not from_.bot:
          print(time.asctime(), '-', event.message)
          time.sleep(0.5)
          await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
