# -*- coding: utf-8 -*-

from disnake.ext import commands
import disnake

class Admin(commands.Cog):
    """Administrative command list"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', aliases=['k'], pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: disnake.Member, *, reason=None) -> None:
        """Kick a member from the server."""
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')


    @commands.command(name='ban', aliases=['b'], pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: disnake.Member, *, reason=None) -> None:
        """Ban a member from the server."""
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')


    @commands.command(name='unban', aliases=['ub'], pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member: disnake.Member) -> None:
        """Unban a member from the server."""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
            
        await ctx.send(f'Could not find {member} in the ban list.')


    @commands.command(name='clear', aliases=['c'], pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int=5) -> None:
        """Clear a certain amount of messages."""
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Cleared {amount} messages.')


    @commands.command(name='mute', aliases=['m'], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: disnake.Member, *, reason: str=None) -> None:
        """Mute a member from the server."""
        role = disnake.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(role, reason=reason)
        await ctx.send(f'Muted {member.mention}')


    @commands.command(name='unmute', aliases=['um'], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: disnake.Member, *, reason: str=None) -> None:
        """Unmute a member from the server."""
        role = disnake.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(role, reason=reason)
        await ctx.send(f'Unmuted {member.mention}')

    
    @commands.command(name='addrole', aliases=['ar'], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, member: disnake.Member, *, role: disnake.Role) -> None:
        """Add a role to a member."""
        await member.add_roles(role)
        await ctx.send(f'Added {role.name} to {member.mention}')


    @commands.command(name='removerole', aliases=['rr'], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: disnake.Member, *, role: disnake.Role) -> None:
        """Remove a role from a member."""
        await member.remove_roles(role)
        await ctx.send(f'Removed {role.name} from {member.mention}')

    
    @commands.command(name='guildid', aliases=['gid'], pass_context=True)
    async def guildid(self, ctx) -> None:
        """Get the guild id."""
        await ctx.send(f'The guild id is {ctx.guild.id}')

    
    @commands.command(name='invite', aliases=['i'], pass_context=True)
    async def invite(self, ctx) -> None:
        """Create an invite for the server."""
        invite = await ctx.channel.create_invite(max_age=0, max_uses=0)
        await ctx.send(f'{invite.url}')


    @commands.slash_command(name='clear', description='Clear a certain amount of messages.', pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, inter, amount: int=5) -> None:
        """Clear a certain amount of messages."""
        await inter.channel.purge(limit=amount)
    

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member) -> None:
        """On member join, assign the member the default role."""
        channel = member.guild.system_channel
        if channel is not None:
            role = disnake.utils.get(member.guild.roles, name='Member')
            await member.add_roles(role)
            await channel.send(f'Added {role.name} to {member.name}')


def setup(bot):
    bot.add_cog(Admin(bot))
