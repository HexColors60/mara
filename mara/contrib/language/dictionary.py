"""
Dictionary of socials and verbs
"""
from __future__ import unicode_literals

# Social verbs with default prepositions
SOCIAL_PREPOSITIONS = {
    'agree': 'with',
    'apologise': 'to',
    'argue': 'with',
    'bark': 'at',
    'beam': 'at',
    'beckon': 'to',
    'beep': 'at',
    'bing': 'at',
    'bingle': 'at',
    'bleep': 'at',
    'blink': 'at',
    'blush': 'at',
    'bow': 'to',
    'bouce': 'around',
    'cackle': 'at',
    'caper': 'around',
    'chuckle': 'at',
    'chortle': 'at',
    'complain': 'to',
    'confess': 'to',
    'cough': 'at',
    'cower': 'behind',
    'crash': 'into',
    'cringe': 'at',
    'croak': 'at',
    'croon': 'at',
    'cuddle': 'up with',
    'curl': 'up with',
    'curse': 'at',
    'curtsey': 'to',
    'dance': 'with',
    'disagree': 'with',
    'discriminate': 'against',
    'dribble': 'on',
    'drool': 'on',
    'eek': 'at',
    'eep': 'at',
    'fart': 'on',
    'fib': 'to',
    'fiddle': 'with',
    'flirt': 'with',
    'flutter': 'around',
    'frolic': 'around',
    'frown': 'at',
    'gape': 'at',
    'gasp': 'at',
    'gawk': 'at',
    'gaze': 'at',
    'gesticulate': 'to',
    'gesture': 'to',
    'giggle': 'at',
    'glare': 'at',
    'gloat': 'at',
    'glower': 'at',
    'grin': 'at',
    'grimace': 'at',
    'grind': 'with',
    'groan': 'at',
    'grovel': 'before',
    'growl': 'at',
    'grumble': 'at',
    'grunt': 'at',
    'guffaw': 'at',
    'gulp': 'at',
    'hiccup': 'at',
    'hiss': 'at',
    'hoot': 'at',
    'hop': 'around',
    'howl': 'at',
    'hrmph': 'at',
    'hmm': 'at',
    'hrm': 'at',
    'hum': 'to',
    'jump': 'on',
    'laugh': 'at',
    'lecture': 'to',
    'leer': 'at',
    'listen': 'to',
    'loom': 'over',
    'meep': 'at',
    'meow': 'at',
    'mime': 'to',
    'moan': 'at',
    'moo': 'at',
    'moose': 'at',
    'mope': 'at',
    'mumble': 'at',
    'mutter': 'at',
    'neigh': 'at',
    'nestle': 'up to',
    'nod': 'at',
    'ook': 'at',
    'ping': 'at',
    'plead': 'to',
    'point': 'at',
    'pose': 'for',
    'pounce': 'on',
    'pout': 'at',
    'prance': 'around',
    'propose': 'to',
    'puke': 'all over',
    'purr': 'at',
    'quack': 'at',
    'rant': 'at',
    'roar': 'at',
    'scamper': 'around',
    'scoff': 'at',
    'scowl': 'at',
    'scream': 'at',
    'screech': 'at',
    'shrug': 'at',
    'shiver': 'at',
    'shriek': 'at',
    'shudder': 'at',
    'sigh': 'at',
    'sing': 'to',
    'sit': 'on',
    'slobber': 'on',
    'smile': 'at',
    'smirk': 'at',
    'snap': 'at',
    'snarl': 'at',
    'sneer': 'at',
    'sneeze': 'at',
    'snicker': 'at',
    'sniff': 'at',
    'sniffle': 'at',
    'snigger': 'at',
    'snore': 'at',
    'snort': 'at',
    'snortle': 'at',
    'snore': 'at',
    'sob': 'at',
    'somersault': 'at',
    'sparkle': 'at',
    'spit': 'at',
    'spy': 'on',
    'squeak': 'at',
    'squeal': 'at',
    'squint': 'at',
    'stare': 'at',
    'sulk': 'at',
    'swagger': 'at',
    'swear': 'at',
    'sympathise': 'with',
    'tango': 'with',
    'tattle': 'on',
    'think': 'about',
    'tremble': 'at',
    'tut': 'at',
    'twinkle': 'at',
    'twirl': 'at',
    'twitch': 'at',
    'vomit': 'at',
    'wail': 'at',
    'wait': 'for',
    'waltz': 'with',
    'wave': 'at',
    'weep': 'at',
    'whimper': 'at',
    'whine': 'at',
    'whinge': 'at',
    'whinny': 'at',
    'whistle': 'to',
    'wibble': 'at',
    'wince': 'at',
    'wiggle': 'at',
    'wink': 'at',
    'wobble': 'at',
    'worry': 'about',
    'yawn': 'at',
    'yodel': 'at',
    'yelp': 'at',
}


# All social verbs
SOCIAL_VERBS = list(SOCIAL_PREPOSITIONS.keys()) + [
    # Simple socials
    'accuse', 'annoy', 'bite', 'blame', 'bribe', 'caress', 'chase', 'chastise',
    'comfort', 'compliment', 'condemn', 'congratulate', 'defenestrate',
    'distract', 'educate', 'elbow', 'encourage', 'envy', 'embarrass',
    'embrace', 'flash', 'flatter', 'fondle', 'forgive', 'glomp', 'grab',
    'greet', 'grope', 'hassle', 'headbutt', 'highfive', 'hit', 'hug', 'hush',
    'kick', 'kiss', 'lick', 'love', 'lynch', 'massage', 'mesmerise', 'moon',
    'mourn', 'nag', 'nudge', 'obey', 'ogle', 'pat', 'patronise', 'pinch',
    'pity', 'pamper', 'pester', 'pet', 'poke', 'prod', 'praise', 'preen',
    'promise', 'punch', 'punish', 'push', 'ram', 'ravish', 'rub', 'remind',
    'salute', 'satisfy', 'scare', 'scold', 'scratch', 'sedate', 'seduce',
    'sentence', 'serenade', 'shake', 'shoo', 'shove', 'shun', 'shush', 'slap',
    'smack', 'smooch', 'snog', 'soothe', 'spam', 'spank', 'squeeze', 'stalk',
    'strangle', 'stroke', 'sue', 'surprise', 'tackle', 'taunt', 'tease',
    'tempt', 'thank', 'threaten', 'tickle', 'toast', 'tongue', 'touch',
    'trust', 'warn', 'welcome',

    # These will often have adjectives
    'applaud', 'boo', 'bleat', 'bleed', 'breakdance', 'breathe', 'burp',
    'cheer', 'chew', 'clap', 'code', 'collapse', 'cry', 'daydream', 'declare',
    'duck', 'explode', 'faint', 'fall', 'feel', 'fidget', 'glow', 'gurgle',
    'hate', 'idle', 'melt', 'nap', 'panic', 'pant', 'ponder', 'protest',
    'prepare', 'quote', 'relax', 'sleep', 'spin', 'squirm', 'stagger',
    'stumble', 'suck', 'sweat', 'volunteer', 'win', 'wobble', 'wonder',
]


# All known verbs
VERBS = SOCIAL_VERBS
