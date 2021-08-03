MANAGE_MESSAGES_PERMISSION = 0x0000002000
ADMINISTRATOR_PERMISSION = 0x0000000008


def has_permission(permissions, permission):
    return permissions & permission == permission
