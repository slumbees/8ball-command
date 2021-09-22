

@client.command(aliases='8ball')
async def _8ball(ctx):
    responses = ['123',
                '456',
                '789',
                '10 11 12',
                '13 14 15'
await ctx.send(f'\nChoice: {random.choice(responses)}')





@client.command(aliases=['food'])
async def _food(ctx):
    responses = ['cereal',
                'yogurt',
                'pizza',
                'fast food'
await ctx.send(f'\nChoice: {random.choice(responses)}')


client.run('')
