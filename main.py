import asyncio
import sqlite3
from discord.ext import commands
import datetime as dt
# в data храниться только токен для удобного использования и сохранения секретности токена
from .data import TOKEN
SQL_FILE = ''


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


sql_adapter = SqlAdapter(SQL_FILE)
bot = commands.Bot(command_prefix='!!')
bot.add_cog(ToDo(bot, sql_adapter))
bot.run(TOKEN)