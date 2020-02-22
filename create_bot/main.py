class CREATE_BOT:
    def __inti__(self,token):
        import discord
        self.client = discord.Client()
        self.token = token
    def create_event(self,tp="message"):
        if tp == "message":
            @self.client.event
            async def on_messsage(message):
                
    def run(self):
        self.client.run(token)