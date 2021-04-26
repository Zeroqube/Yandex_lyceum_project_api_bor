import asyncio
import sqlite3
from discord.ext import commands
import datetime as dt
# в data храниться только токен для удобного использования и сохранения секретности токена
from data import TOKEN
SQL_FILE = 'bot_db'


def normalize(a):
    res = []
    for line in a:
        res.append('\t'.join(str(item) for item in line))
    return res


bot = commands.Bot(command_prefix="!")

con = sqlite3.connect(SQL_FILE)
cur = con.cursor()


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        print(
            f'{bot.user} подключились к чату:\n'
            f'{guild.name}(id: {guild.id})')


@bot.command(name='set_task')
async def set_task(ctx, name):
    if len(name) > 10:
        await ctx.send('Название задачи не должно превышать 10 символов!')
        return
    channel_id = ctx.author.id
    if not cur.execute('SELECT id FROM channels WHERE id = ?', (channel_id, )).fetchone():
        cur.execute('INSERT INTO channels VALUES (?)', (channel_id, ))
    if cur.execute('SELECT task_name FROM todo WHERE channel_id = ? AND task_name = ?', (channel_id, name)).fetchone():
        await ctx.send(f'Задача с именнем {name} уже есть!')
        return
    cur.execute('INSERT INTO todo(channel_id, task_name) VALUES (?, ?)', (channel_id, name, ))
    con.commit()
    print(channel_id, name)


@bot.command(name='set_date')
async def set_date(ctx, name, date):
    channel_id = ctx.author.id
    if not cur.execute('SELECT id FROM channels WHERE id = ?', (channel_id,)).fetchone():
        await ctx.send('У вас ещё не было задач')
        return
    if not cur.execute('SELECT task_name FROM todo WHERE channel_id = ? AND task_name = ?',
                       (channel_id, name)).fetchone():
        await ctx.send(f'Задачи с именнем {name} ещё нет!')
        return
    day, month, year = map(int, date.split('.'))
    date = dt.date(year, month, day)
    cur.execute('''UPDATE todo
    SET date = ?
    WHERE channel_id = ? AND task_name = ?''', (date, channel_id, name))
    con.commit()


@bot.command(name='set_time')
async def set_time(ctx, name, time):
    channel_id = ctx.author.id
    if not cur.execute('SELECT id FROM channels WHERE id = ?', (channel_id,)).fetchone():
        await ctx.send('У вас ещё не было задач')
        return
    if not cur.execute('SELECT task_name FROM todo WHERE channel_id = ? AND task_name = ?',
                       (channel_id, name)).fetchone():
        await ctx.send(f'Задачи с именнем {name} ещё нет!')
        return
    hours, minutes = map(int, time.split(':'))
    print(hours, minutes)
    time = dt.time(hour=hours, minute=minutes)
    print(time)
    cur.execute('''UPDATE todo
    SET time = ?
    WHERE channel_id = ? AND task_name = ?''', (time, channel_id, name))
    con.commit()


@bot.command(name='set_description')
async def set_description(ctx, name, *description):
    channel_id = ctx.author.id
    if not cur.execute('SELECT id FROM channels WHERE id = ?', (channel_id,)).fetchone():
        await ctx.send('У вас ещё не было задач')
        return
    if not cur.execute('SELECT task_name FROM todo WHERE channel_id = ? AND task_name = ?',
                       (channel_id, name)).fetchone():
        await ctx.send(f'Задачи с именнем {name} ещё нет!')
        return
    description = ' '.join(description)
    cur.execute('''UPDATE todo
    SET description = ?
    WHERE channel_id = ? AND task_name = ?''', (description, channel_id, name))
    con.commit()


@bot.command(name='get_description')
async def get_description(ctx, name):
    channel_id = ctx.author.id
    if not cur.execute('SELECT id FROM channels WHERE id = ?', (channel_id,)).fetchone():
        await ctx.send('У вас ещё не было задач')
        return
    if not cur.execute('SELECT task_name FROM todo WHERE channel_id = ? AND task_name = ?',
                       (channel_id, name)).fetchone():
        await ctx.send(f'Задачи с именнем {name} ещё нет!')
        return
    res = cur.execute('SELECT date, time, description FROM todo WHERE channel_id = ?', (channel_id, )).fetchone()
    s = f'Вы описали задачу {name} {res[0]} {res[1]} так:\n' + res[2]
    await ctx.send(s)


@bot.command(name='get_tasks')
async def get_tasks(ctx):
    channel_id = ctx.author.id
    if not cur.execute('SELECT id FROM channels WHERE id = ?', (channel_id, )).fetchone():
        await ctx.send('У вас ещё не было задач')
        return
    if not cur.execute('SELECT task_name, date, time FROM todo WHERE channel_id = ?', (channel_id, )).fetchone():
        await ctx.send('У вас нет сейчас задач')
        return
    res = cur.execute('SELECT task_name, date, time FROM todo WHERE channel_id = ?', (channel_id, )).fetchall()
    s = 'Ваши задачи:\n' + '\n'.join(normalize(res))
    await ctx.send(s)


@bot.command(name='delete')
async def delete(ctx, name):
    channel_id = ctx.author.id
    if not cur.execute('SELECT id FROM channels WHERE id = ?', (channel_id,)).fetchone():
        await ctx.send('У вас ещё не было задач')
        return
    if not cur.execute('SELECT task_name FROM todo WHERE channel_id = ? AND task_name = ?',
                       (channel_id, name)).fetchone():
        await ctx.send(f'Задачи с именнем {name} ещё нет!')
        return
    cur.execute('''DELETE FROM todo
    WHERE channel_id = ? AND task_name = ?''', (channel_id, name, ))
    await ctx.send(f'Задача с именнем {name} успешно удалена')


@bot.command(name='delete_all')
async def delete_all(ctx):
    channel_id = ctx.author.id
    if not cur.execute('SELECT id FROM channels WHERE id = ?', (channel_id,)).fetchone():
        await ctx.send('У вас ещё не было задач')
        return
    if not cur.execute('SELECT task_name, date, time FROM todo WHERE channel_id = ?', (channel_id, )).fetchone():
        await ctx.send('У вас нет сейчас задач')
        return
    cur.execute('''DELETE FROM todo
    WHERE channel_id = ?''', (channel_id, ))
    await ctx.send('Все задачи успешно удалены')


bot.run(TOKEN)