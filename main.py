import asyncio
import sqlite3
from discord.ext import commands
import schedule
import datetime as dt
# в data храниться только токен для удобного использования и сохранения секретности токена
from .data import TOKEN
SQL_FILE = ''


class Remainder:
    def __init__(self, bot):
        self.bot = bot

    async def remainding(self):
        schedule.every().minute.at(":00").do(self.bot.remind(date=dt.datetime.now().date(),
                                                               time=dt.datetime.now().time()))


class SqlAdapter:
    def __init__(self, sql_file):
        self.sql_file = sql_file
        self.con = sqlite3.connect(sql_file)

    async def take_object(self):
        pass

    async def take_objects(self):
        pass

    async def create_object(self):
        pass

    async def delete_object(self):
        pass

    async def change_object(self):
        pass

    async def create_user(self):
        pass

    async def take_unused_id(self):
        pass


class ToDo(commands.Cog):
    def __init__(self, bot, adapter):
        self.bot = bot
        self.adapter = adapter

    async def remind(self, date, time):
        pass

    @commands.command(name='help')
    async def set_problem(self, ctx, obj):
        pass

    @commands.command(name='set problem with deadline')
    async def set_problem(self, ctx, name, date):
        pass

    @commands.command(name='delete problem with deadline')
    async def delete_problem(self, ctx, name):
        pass

    @commands.command(name='change problem with deadline')
    async def delete_problem(self, ctx, name, field, value):
        pass

    @commands.command(name='set problem')
    async def set_problem(self, ctx, name):
        pass

    @commands.command(name='delete problem')
    async def delete_problem(self, ctx, name):
        pass

    @commands.command(name='change problem')
    async def delete_problem(self, ctx, name, field, value):
        pass

    @commands.command(name='set event')
    async def set_event(self, ctx, name, date):
        pass

    @commands.command(name='delete event')
    async def delete_event(self, ctx, name):
        pass

    @commands.command(name='change event')
    async def delete_problem(self, ctx, name, field, value):
        pass

    @commands.command(name='add description')
    async def delete_event(self, ctx, name, description):
        pass

    @commands.command(name='change description')
    async def delete_event(self, ctx, name, description):
        pass

    @commands.command(name='delete description')
    async def delete_event(self, ctx, name):
        pass

    @commands.command(name='get all')
    async def delete_event(self, ctx, typ):
        pass

    @commands.command(name='get all')
    async def delete_event(self, ctx, date):
        pass


async def bot_main(bot):
    bot.run(TOKEN)


async def reminder_main(remainder):
    await remainder.remainding()


async def main():
    sql_adapter = SqlAdapter(SQL_FILE)

    bot = commands.Bot(command_prefix='!!')
    main_bot = ToDo(bot, sql_adapter)

    remainder = Remainder(main_bot)

    main_bot = ToDo(bot, sql_adapter)
    bot.add_cog(main_bot)
    await asyncio.gather(
        bot_main(bot),
        reminder_main(remainder),
    )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
