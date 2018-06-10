# MatchCareer

`MatchCareer` is a Python library that determines the best NBA 2K18 archetype to replicate an existing NBA player's skill set.

The idea is simple: if we treat a given player's attributes as an array, we can then calculate the sum of the [absolute differences](https://en.wikipedia.org/wiki/Sum_of_absolute_difference) at each index to determine the most similar archetype.

For exmaple, let `P1 = [1, 4, 6]`, `P2 = [1, 3, 6]`, and `P3 = [1, 9, 2]`. Then we have,

```
S(P1 - P2) = |1 - 1| + |4 - 3| + |6 - 6| = 1
S(P1 - P3) = |1 - 1| + |4 - 9| + |6 - 2| = 9
```

which indicates that `P1` is more similar to `P2` than `P3`.

## Usage

```python
>>> from match import find
>>> results = find('Klay Thompson')
>>> results['MyCareer']
{'Position': 'SG', 'Primary': 'Playmaker', 'Secondary': 'Sharpshooter', 'Height': "6'7", 'Weight': 'Default', 'Wingspan': 'Default', 'attributes': [83, 85, 85, 79, 88, 88, 82, 83, 79, 63, 66, 86, 88, 66, 66, 66, 67, 67, 65, 73, 73, 64, 64, 76, 82, 83, 69, 65],}
```

You can also try out the [demo website](https://jdkato.github.io/MatchCareer/).

## Adding Players

I haven't been able to find an online source for 2K's in-game attributes&mdash;so, I've had to add them one-by-one from the game itself. If you'd like to add a player, you need to update the [index](https://github.com/jdkato/MatchCareer/blob/master/match/index.py).
