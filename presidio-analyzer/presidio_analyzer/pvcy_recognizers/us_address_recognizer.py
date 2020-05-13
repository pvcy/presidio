from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

# Parsed from https://pe.usps.com/text/pub28/28apc_002.htm
# See USPS.com: Postal Addressing Standards > Appendix C > C1 Street Suffix Abbreviations
# NB pprint(sorted([v.lower() for v in US_street_suffixes]), width=120, compact=True)
US_street_suffixes = [
    'allee', 'alley', 'ally', 'aly', 'anex', 'annex', 'annx', 'anx', 'arc', 'arcade', 'av', 'ave', 'aven', 'avenu',
    'avenue', 'avn', 'avnue', 'bayoo', 'bayou', 'bch', 'beach', 'bend', 'bg', 'bgs', 'blf', 'blfs', 'bluf', 'bluff',
    'bluffs', 'blvd', 'bnd', 'bot', 'bottm', 'bottom', 'boul', 'boulevard', 'boulv', 'br', 'branch', 'brdge', 'brg',
    'bridge', 'brk', 'brks', 'brnch', 'brook', 'brooks', 'btm', 'burg', 'burgs', 'byp', 'bypa', 'bypas', 'bypass', 'byps',
    'byu', 'camp', 'canyn', 'canyon', 'cape', 'causeway', 'causwa', 'cen', 'cent', 'center', 'centers', 'centr', 'centre',
    'cir', 'circ', 'circl', 'circle', 'circles', 'cirs', 'clb', 'clf', 'clfs', 'cliff', 'cliffs', 'club', 'cmn', 'cmns',
    'cmp', 'cnter', 'cntr', 'cnyn', 'common', 'commons', 'cor', 'corner', 'corners', 'cors', 'course', 'court', 'courts',
    'cove', 'coves', 'cp', 'cpe', 'crcl', 'crcle', 'creek', 'cres', 'crescent', 'crest', 'crk', 'crossing', 'crossroad',
    'crossroads', 'crse', 'crsent', 'crsnt', 'crssng', 'crst', 'cswy', 'ct', 'ctr', 'ctrs', 'cts', 'curv', 'curve', 'cv',
    'cvs', 'cyn', 'dale', 'dam', 'div', 'divide', 'dl', 'dm', 'dr', 'driv', 'drive', 'drives', 'drs', 'drv', 'dv', 'dvd',
    'est', 'estate', 'estates', 'ests', 'exp', 'expr', 'express', 'expressway', 'expw', 'expy', 'ext', 'extension',
    'extensions', 'extn', 'extnsn', 'exts', 'fall', 'falls', 'ferry', 'field', 'fields', 'flat', 'flats', 'fld', 'flds',
    'fls', 'flt', 'flts', 'ford', 'fords', 'forest', 'forests', 'forg', 'forge', 'forges', 'fork', 'forks', 'fort', 'frd',
    'frds', 'freeway', 'freewy', 'frg', 'frgs', 'frk', 'frks', 'frry', 'frst', 'frt', 'frway', 'frwy', 'fry', 'ft', 'fwy',
    'garden', 'gardens', 'gardn', 'gateway', 'gatewy', 'gatway', 'gdn', 'gdns', 'glen', 'glens', 'gln', 'glns', 'grden',
    'grdn', 'grdns', 'green', 'greens', 'grn', 'grns', 'grov', 'grove', 'groves', 'grv', 'grvs', 'gtway', 'gtwy', 'harb',
    'harbor', 'harbors', 'harbr', 'haven', 'hbr', 'hbrs', 'heights', 'highway', 'highwy', 'hill', 'hills', 'hiway', 'hiwy',
    'hl', 'hllw', 'hls', 'hollow', 'hollows', 'holw', 'holws', 'hrbor', 'ht', 'hts', 'hvn', 'hway', 'hwy', 'inlet', 'inlt',
    'is', 'island', 'islands', 'isle', 'isles', 'islnd', 'islnds', 'iss', 'jct', 'jction', 'jctn', 'jctns', 'jcts',
    'junction', 'junctions', 'junctn', 'juncton', 'key', 'keys', 'knl', 'knls', 'knol', 'knoll', 'knolls', 'ky', 'kys',
    'lake', 'lakes', 'land', 'landing', 'lane', 'lck', 'lcks', 'ldg', 'ldge', 'lf', 'lgt', 'lgts', 'light', 'lights', 'lk',
    'lks', 'ln', 'lndg', 'lndng', 'loaf', 'lock', 'locks', 'lodg', 'lodge', 'loop', 'loops', 'mall', 'manor', 'manors',
    'mdw', 'mdws', 'meadow', 'meadows', 'medows', 'mews', 'mill', 'mills', 'mission', 'missn', 'ml', 'mls', 'mnr', 'mnrs',
    'mnt', 'mntain', 'mntn', 'mntns', 'motorway', 'mount', 'mountain', 'mountains', 'mountin', 'msn', 'mssn', 'mt', 'mtin',
    'mtn', 'mtns', 'mtwy', 'nck', 'neck', 'opas', 'orch', 'orchard', 'orchrd', 'oval', 'overpass', 'ovl', 'park', 'parks',
    'parkway', 'parkways', 'parkwy', 'pass', 'passage', 'path', 'paths', 'pike', 'pikes', 'pine', 'pines', 'pkway', 'pkwy',
    'pkwys', 'pky', 'pl', 'place', 'plain', 'plains', 'plaza', 'pln', 'plns', 'plz', 'plza', 'pne', 'pnes', 'point',
    'points', 'port', 'ports', 'pr', 'prairie', 'prk', 'prr', 'prt', 'prts', 'psge', 'pt', 'pts', 'rad', 'radial',
    'radiel', 'radl', 'ramp', 'ranch', 'ranches', 'rapid', 'rapids', 'rd', 'rdg', 'rdge', 'rdgs', 'rds', 'rest', 'ridge',
    'ridges', 'riv', 'river', 'rivr', 'rnch', 'rnchs', 'road', 'roads', 'route', 'row', 'rpd', 'rpds', 'rst', 'rte', 'rue',
    'run', 'rvr', 'shl', 'shls', 'shoal', 'shoals', 'shoar', 'shoars', 'shore', 'shores', 'shr', 'shrs', 'skwy', 'skyway',
    'smt', 'spg', 'spgs', 'spng', 'spngs', 'spring', 'springs', 'sprng', 'sprngs', 'spur', 'spurs', 'sq', 'sqr', 'sqre',
    'sqrs', 'sqs', 'squ', 'square', 'squares', 'st', 'sta', 'station', 'statn', 'stn', 'str', 'stra', 'strav', 'straven',
    'stravenue', 'stravn', 'stream', 'street', 'streets', 'streme', 'strm', 'strt', 'strvn', 'strvnue', 'sts', 'sumit',
    'sumitt', 'summit', 'ter', 'terr', 'terrace', 'throughway', 'tpke', 'trace', 'traces', 'track', 'tracks', 'trafficway',
    'trail', 'trailer', 'trails', 'trak', 'trce', 'trfy', 'trk', 'trks', 'trl', 'trlr', 'trlrs', 'trls', 'trnpk', 'trwy',
    'tunel', 'tunl', 'tunls', 'tunnel', 'tunnels', 'tunnl', 'turnpike', 'turnpk', 'un', 'underpass', 'union', 'unions',
    'uns', 'upas', 'valley', 'valleys', 'vally', 'vdct', 'via', 'viadct', 'viaduct', 'view', 'views', 'vill', 'villag',
    'village', 'villages', 'ville', 'villg', 'villiage', 'vis', 'vist', 'vista', 'vl', 'vlg', 'vlgs', 'vlly', 'vly',
    'vlys', 'vst', 'vsta', 'vw', 'vws', 'walk', 'walks', 'wall', 'way', 'ways', 'well', 'wells', 'wl', 'wls', 'wy', 'xing',
    'xrd', 'xrds'
]

REGEX = r'\d{1,4}[\w\s]{1,20}(?:' + r"|".join(US_street_suffixes) + r')\W?(?=\s|$)'
CONTEXT = [] # TODO

class UsAddressRecognizer(PatternRecognizer):
    """
    TODO Handle P.O. Box
    """
    def __init__(self):
        patterns = [Pattern('US Address (medium)', REGEX, 0.4)]
        title_patterns = [Pattern('US Address Title(strong)',  # language=RegExp
                                  r'\b((?<!mac[\s_-])(address|addr)\d?)\b',
                                  0.7)]
        super().__init__(supported_entity="US_ADDRESS", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
