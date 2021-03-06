#!/usr/bin/env python
# -*- coding: utf-8 -*-

# special thanks to da3dsoul

version = 2  # increase with each push/edit

tagBlacklistAniDBHelpers = set([  # AniDB tags that don't help with anything
    "body and host",
    "breasts",
    "broadcast cropped to 4-3",
    "cast missing",
    "cast",
    "content indicators",
    "delayed 16-9 broadcast",
    "description missing",
    "development hell",  # :( God Eater
    "dialogue driven",  # anidb and their british spellings
    "dynamic",
    "earth",
    "elements",
    "ending",
    "ensemble cast",
    "family life",
    "fast-paced",
    "fictional world",
    "full hd version available",
    "jdrama adaptation",
    "meta tags",
    "motifs",
    "multi-anime projects",
    "noitamina",
    "origin",
    "past",
    "place",
    "present",
    "season",
    "sentai",
    "setting",
    "some weird shit goin` on",  # these are some grave accents in use...
    "storytelling",
    "tales",
    "target audience",
    "technical aspects",
    "television programme",
    "themes",
    "time",
    "translation convention",
    "tropes",
    "ungrouped",
    "unsorted"
])

tagBlackListSource = set([  # tags containing source of serie
    "4-koma",
    "action game",
    "erotic game",
    "fan-made",
    "game",
    "korean drama",
    "manga",
    "manhua",
    "manhwa",
    "movie",
    "new",
    "novel",
    "radio programme",
    "remake",
    "rpg",
    "television programme",
    "ultra jump",
    "visual novel"
])

tagBlackListArtStyle = set([  # tags that focus on art style
    "3d cg animation",
    "3d cg closing",
    "cel-shaded animation",
    "cgi",
    "chibi ed",
    "experimental animation",
    "flash animation",
    "live-action closing",
    "live-action imagery",
    "off-model animation",
    "photographic backgrounds",
    "product placement",
    "recycled animation",
    "slide show animation",
    "thick line animation",
    "vignette scenes",
    "watercolour style",
    "widescreen transition"
])

tagBlackListUsefulHelpers = set([  # tags that focus on episode attributes
    "ed variety",
    "half-length episodes",
    "long episodes",
    "multi-segment episodes",
    "op and ed sung by characters",
    "op variety",
    "post-credits scene",
    "recap in opening",
    "short episodes",
    "short movie",
    "stand-alone movie",
    "subtle op ed sequence change"
])

tagBlackListPlotSpoilers = set([  # tags that could contain story-line spoilers
    "branching story",
    "cliffhangers",
    "colour coded",
    "complex storyline",
    "drastic change in sequel",
    "fillers",
    "first girl wins",  # seriously a spoiler
    "incomplete story",
    "inconclusive",
    "inconclusive romantic plot",
    "non-linear",
    "open-ended",
    "room for sequel",
    "sudden change of pace",
    "tone changes",
    "unresolved",
    "unresolved romance"
])


def processTags(flags, string):

    """
        Filters tags based on settings specified in flags
    :param flags:
            0b00001 : Hide AniDB Internal Tags
            0b00010 : Hide Art Style Tags
            0b00100 : Hide Source Work Tags
            0b01000 : Hide Useful Miscellaneous Tags
            0b10000 : Hide Plot Spoiler Tags
    :param string: A list of strings [ 'meta tags', 'elements', 'comedy' ]
    :return: The list of strings after filtering
    """
    toRemove=set()
    readdOriginal=True

    string_set = set(string)
    for a in string_set:
        tag = a.strip().lower()
        if flags & 0b00010 == 0b00010:
            if tag in tagBlackListArtStyle:
                toRemove.add(a)
                continue
            if "censor" in tag:
                toRemove.add(a)
                continue
        if flags & 0b00100 == 0b00100:
            readdOriginal = False
            if tag in tagBlackListSource:
                toRemove.add(a)
                continue
            if "original work" == tag:
                toRemove.add(a)
                continue
        else:
            if tag in tagBlackListSource:
                readdOriginal=False
                continue
            if tag == "original work":
                toRemove.add(a)
                continue

        if flags & 0b01000 == 0b01000:
            if tag in tagBlackListUsefulHelpers:
                toRemove.add(a)
                continue
            if tag.startswith("preview"):
                toRemove.add(a)
                continue

        if flags & 0b10000 == 0b10000:
            if tag in tagBlackListPlotSpoilers:
                toRemove.add(a)
                continue
            if tag.startswith("plot"):
                toRemove.add(a)
                continue
            if tag.endswith(" dies"):
                toRemove.add(a)
                continue
            if tag.endswith(" end"):
                toRemove.add(a)
                continue
            if tag.endswith(" ending"):
                toRemove.add(a)
                continue

        if flags & 0b00001 == 0b00001:
            if tag in tagBlacklistAniDBHelpers:
                toRemove.add(a)
                continue
            if "to be" in tag:
                if "merged" in tag:
                    toRemove.add(a)
                    continue
                if "deleted" in tag:
                    toRemove.add(a)
                    continue
                if "split" in tag:
                    toRemove.add(a)
                    continue
                if "moved" in tag:
                    toRemove.add(a)
                    continue
                if "improved" in tag or "improving" in tag or "improvement" in tag:
                    toRemove.add(a)
                    continue
            if "need" in tag or "needs" in tag:
                if "merging" in tag or "merged" in tag:
                    toRemove.add(a)
                    continue
                if "deleting" in tag or "deleted" in tag:
                    toRemove.add(a)
                    continue
                if "moving" in tag or "moved" in tag:
                    toRemove.add(a)
                    continue
                if "improved" in tag or "improving" in tag or "improvement" in tag:
                    toRemove.add(a)
                    continue
            if "old animetags" in tag:
                toRemove.add(a)
                continue
            if "missing" in tag:
                toRemove.add(a)
                continue
            if tag.startswith("predominantly"):
                toRemove.add(a)
                continue
            if tag.startswith("weekly"):
                toRemove.add(a)
                continue

    for a in toRemove:
        if a in string_set:
            string.remove(a)

    if readdOriginal:
        if isinstance(string, set):
            string.add("Original Work")
        elif isinstance(string, list):
            string.append("Original Work")

    return string
