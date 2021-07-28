from discord.ext import commands
import asyncpraw
import random
import datetime
import giphy_client
from urllib.request import urlopen
from urllib import parse as par
import re
from discord import Embed

class WebBrowse(commands.Cog):
    """
    Search the internet
    """

    @commands.command(name='video', aliases=['youtube', 'yt', 'vid'], case_insensitive=True, help='look for a video on Youtube')
    async def video(ctx, *, query):
        lookUpURL = 'http://www.youtube.com/results?' + par.urlencode({'search_query': query})
        html_content = urlopen(lookUpURL).read().decode()
        search_results = re.findall(r"watch\?v=(\S{11})", html_content)

        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

    @commands.command(name='gif', aliases=['giphy'], case_insensitive=True, help='look for a gif on Giphy')
    async def gif(ctx, *, query = None):
        if query == None:
            query = "random"

        api_instance = giphy_client.DefaultApi()
        api_key="T71TU2iOoWoLbK5lcij6wjRKuWystotB"

        try:             
            api_response = api_instance.gifs_search_get(api_key, query, limit=5, rating='g')

            gifs = list(api_response.data)
            gif = random.choice(gifs)

            gifEmbed = Embed(title=query, timestamp=datetime.datetime.utcnow())
            gifEmbed.set_image(url = f'https://media.giphy.com/media/{gif.id}/giphy.gif')
            await ctx.send(embed=gifEmbed)
        
        except giphy_client.rest.ApiException as e:
            pass

    @commands.command(name='image', aliases=['img'], case_insensitive=True, help='look for a image on didnt get api yet ;-;')
    async def image(ctx, *, query):
        imageEmbed = Embed(title=query, colour=0xadd8e6, timestamp=datetime.datetime.utcnow())

        imageEmbed.set_image(url=f'https://source.unsplash.com/1600x900/?{query.replace(" ", "-")}')

        await ctx.send(embed=imageEmbed)

    @commands.command(name='reddit', aliases=['meme'], case_insensitive=True, help='look for top gifs on Reddit, default u/memes')
    async def meme(ctx, *, subreddit='memes'):
        reddit = asyncpraw.Reddit(client_id="R_R7sefdBIXlYw",
                            client_secret="DBYtiqczDUxIXQCOb7d6GDwk_q1rMw",
                            user_agent="EzIntel:v1.0.0 by u/EzClappr" "At <GIT LINK>")

        subreddit = await reddit.subreddit(subreddit)
        submissions = []

        top = subreddit.top(limit=50)

        async for submission in top:
            submissions.append(submission)

        submission = random.choice(submissions)

        name = submission.title
        url = submission.url

        memeEmbed = Embed(title=name, timestamp=datetime.datetime.utcnow())
        memeEmbed.set_image(url=url)
        await ctx.send(embed=memeEmbed)

def setup(bot):
    bot.add_cog(WebBrowse(bot))