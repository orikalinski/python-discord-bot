CDN_URL = "https://cdn.discordapp.com"
BASE_URL = "https://discord.com/api/v9"

ICONS = "/icons"
GUILD_ICON = CDN_URL + ICONS + "/{}" + "/{}.png"

OAUTH_TOKEN_URL = "/oauth2/token"

GET_ME = "/users/@me"
GET_USER = "/users/{}"
GET_USER_CONNECTIONS = GET_ME + "/connections"
CHANNELS = "/channels"
DM_URL = GET_ME + CHANNELS
GET_CHANNEL = CHANNELS + "/{}"
CHANNEL_MESSAGE = GET_CHANNEL + "/messages" + "/{}"
CHANNEL_MESSAGES = GET_CHANNEL + "/messages"
GUILDS = "/guilds"
GET_GUILD = GUILDS + "/{}"
GET_GUILD_PREVIEW = GET_GUILD + "/preview"
GET_GUILD_ROLES = GET_GUILD + "/roles"
GET_GUILD_MEMBERS = GET_GUILD + "/members"
