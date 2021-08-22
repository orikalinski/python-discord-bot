class DiscordMissingAccess(Exception):
    pass


class DiscordUnknownChannel(Exception):
    pass


CODE_TO_EXCEPTION = {
    50001: DiscordMissingAccess,
    10003: DiscordUnknownChannel
}
