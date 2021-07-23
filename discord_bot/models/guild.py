class Guild(object):
    def __init__(self, id, name, nsfw=None, topic=None, approximate_member_count=None, approximate_presence_count=None,
                 rate_limit_per_user=None, afk_channel_id=None, afk_timeout=None, application_id=None, banner=None,
                 default_message_notifications=None, description=None, discovery_splash=None, emojis=None,
                 explicit_content_filter=None, features=None, icon=None, max_members=None, max_presences=None,
                 max_video_channel_users=None, mfa_level=None, nsfw_level=None, owner_id=None, preferred_locale=None,
                 premium_subscription_count=None, premium_tier=None, public_updates_channel_id=None, region=None,
                 roles=None, rules_channel_id=None, splash=None, stickers=None, system_channel_flags=None,
                 system_channel_id=None, vanity_url_code=None, verification_level=None, widget_channel_id=None,
                 widget_enabled=None, **kwargs):
        self.id = id
        self.name = name
        self.nsfw = nsfw
        self.topic = topic
        self.approximate_member_count = approximate_member_count
        self.approximate_presence_count = approximate_presence_count
        self.rate_limit_per_user = rate_limit_per_user
        self.afk_channel_id = afk_channel_id
        self.afk_timeout = afk_timeout
        self.application_id = application_id
        self.banner = banner
        self.default_message_notifications = default_message_notifications
        self.description = description
        self.discovery_splash = discovery_splash
        self.emojis = emojis
        self.explicit_content_filter = explicit_content_filter
        self.features = features
        self.icon = icon
        self.max_members = max_members
        self.max_presences = max_presences
        self.max_video_channel_users = max_video_channel_users
        self.mfa_level = mfa_level
        self.nsfw_level = nsfw_level
        self.owner_id = owner_id
        self.preferred_locale = preferred_locale
        self.premium_subscription_count = premium_subscription_count
        self.premium_tier = premium_tier
        self.public_updates_channel_id = public_updates_channel_id
        self.region = region
        self.roles = roles
        self.rules_channel_id = rules_channel_id
        self.splash = splash
        self.stickers = stickers
        self.system_channel_flags = system_channel_flags
        self.system_channel_id = system_channel_id
        self.vanity_url_code = vanity_url_code
        self.verification_level = verification_level
        self.widget_channel_id = widget_channel_id
        self.widget_enabled = widget_enabled

        self.__dict__.update(**kwargs)
