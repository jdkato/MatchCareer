"""
"""
import numpy as np

from .attributes import attributes, ordered_keys
from .index import player_index


def find(name, fix=['Height']):
    """
    """
    match = None
    best = 0

    player = player_index.get(name)
    if player is None:
        return {'match': '{0} not found.'.format(name), 'attrs': []}

    attrs = np.array(player['attributes'])
    for archetype in attributes:
        if not all(player[k] == archetype[k] for k in fix):
            continue
        values = [archetype[k] for k in ordered_keys]
        score = np.linalg.norm((attrs - np.array(values)), ord=2)
        if match is None or score < best:
            match = archetype
            best = score

    return match
