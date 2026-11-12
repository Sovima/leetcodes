class Solution:
    def score(self, cards: List[str], x: str) -> int:
        from collections import defaultdict
        
        first = defaultdict(int)
        second = defaultdict(int)
        both = defaultdict(int)
        for card in cards:
            if card[0] == x and card[1] == x:
                both[card] += 1
            elif card[0] == x:
                first[card] += 1
            elif card[1] == x:
                second[card] += 1
        
        # Make up pairs
        fm = 0 if not first else max(first.values())
        ft = 0 if not first else sum(first.values())
        first_pairs = ft // 2 if fm <= ft / 2 else ft - fm

        sm = 0 if not second else max(second.values())
        st = 0 if not second else sum(second.values())
        second_pairs = st // 2 if sm <= st / 2 else st - sm


        # Distribute the middles
        first_remains = ft - first_pairs * 2
        second_remains = st - second_pairs * 2
        both_total = 0 if not both else sum(both.values())
        both_total_remains = both_total
        both_total_remains = max(0, both_total_remains - first_remains)
        both_total_remains = max(0, both_total_remains - second_remains)
        matched_middles = both_total - both_total_remains

        # See if unmatched can be distributed too
        next_both_total = both_total_remains
        distributed_pairs = 0
        odd = both_total_remains % 2
        both_total_remains = max(odd, both_total_remains - 2 * second_pairs)
        odd = both_total_remains % 2
        both_total_remains = max(odd, both_total_remains - 2 * first_pairs)
        distribtued_pairs = (next_both_total - both_total_remains) // 2

        
        return second_pairs + first_pairs + matched_middles + distribtued_pairs
