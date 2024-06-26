from flask.cli import AppGroup
from .users import seed_users, undo_users
from .channels import seed_channels, undo_channels
from .reactions import seed_reactions, undo_reactions
from .servers import seed_servers, undo_servers
from .messages import seed_messages, undo_messages
from .server_memberships import seed_server_memberships, undo_server_memberships
from .channel_memberships import seed_channel_memberships, undo_channel_memberships
from app.models.db import environment

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup("seed")


# Creates the `flask seed all` command
@seed_commands.command("all")
def seed():
    if environment == "production":
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_reactions()
        undo_messages()
        undo_channel_memberships()
        undo_channels()
        undo_server_memberships()
        undo_servers()
        undo_users()
    seed_users()
    seed_servers()
    seed_server_memberships()
    seed_channels()
    seed_channel_memberships()
    seed_messages()
    seed_reactions()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command("undo")
def undo():
    undo_reactions()
    undo_messages()
    undo_channel_memberships()
    undo_channels()
    undo_server_memberships()
    undo_servers()
    undo_users()
