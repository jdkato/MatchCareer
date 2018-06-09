import numpy as np

from .attributes import attributes, ordered_keys
from .index import player_index


def inches_to_label(height):
    if height >= 84:
        return "7'{0}".format(height - 84)
    else:
        return "6'{0}".format(height - 72)


def find(name, fix=['Height']):
    """Find the most similar NBA 2K18 MyCareer archetype to `name`.

    TODO: Add a `method` argument that uses either Ln norm or a new
    method altogether.

    Arguments:
        `fix` (list[str]): A list of attributes that should be fixed.

    Returns:
        A dictionary of the following form:

        ```json
        {
            "MyCareer": {
                "primary": "...",
                "secondary": "...",
                "height": "6'8",
                "position": "...",
                "attributes": [...]
            },
            "exact": {
                "height": "6'8",
                "position": "...",
                "attributes": [...]
            }
        }
        ```
    """
    match = None
    best = 0

    player = player_index.get(name)
    # TODO: Use difflib for name-matching?
    if player is None:
        return {}

    attrs = np.array([player['attributes'][k] for k in ordered_keys])
    for archetype in attributes:
        if not all(player[k] == archetype[k] for k in fix):
            continue
        values = [archetype[k] for k in ordered_keys]
        score = np.linalg.norm((attrs - np.array(values)), ord=1)
        if match is None or score < best:
            match = [archetype, values]
            best = score

    ret = {'attributes': match[1]}
    for k, v in match[0].items():
        if k not in ordered_keys + ['ContactDunk', 'SpeedwithBall']:
            # HACK: Why aren't `ContactDunk` and `SpeedwithBall`
            # included?
            if k == 'Height':
                ret[k] = inches_to_label(v)
            else:
                ret[k] = v

    return {"MyCareer": ret, "exact": player, "score": round(best, 3)}
