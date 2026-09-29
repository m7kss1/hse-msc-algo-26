import random
import unittest
from collections import Counter

from anagrams import canonical, group_anagrams, solve


def brute(words: list[str]) -> list[list[str]]:
    groups = []
    for word in words:
        for group in groups:
            if Counter(group[0]) == Counter(word):
                group.append(word)
                break
        else:
            groups.append([word])
    return groups


class TestAnagrams(unittest.TestCase):
    def check(self, words: list[str], expected: list[list[str]]) -> None:
        self.assertEqual(canonical(group_anagrams(words)), canonical(expected))

    def test_example(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.assertEqual(
            canonical(group_anagrams(words)),
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        )

    def test_order_of_first_appearance(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.assertEqual(
            group_anagrams(words), [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        )

    def test_empty(self):
        self.assertEqual(group_anagrams([]), [])
        self.check([""], [[""]])
        self.check(["", "a", ""], [["", ""], ["a"]])

    def test_single(self):
        self.check(["a"], [["a"]])

    def test_duplicates_kept(self):
        self.check(["ab", "ba", "ab"], [["ab", "ab", "ba"]])

    def test_no_anagrams(self):
        self.check(["abc", "abd", "xyz"], [["abc"], ["abd"], ["xyz"]])

    def test_all_anagrams(self):
        self.check(["abc", "bca", "cab", "acb"], [["abc", "bca", "cab", "acb"]])

    def test_same_letters_different_counts(self):
        self.check(["ab", "aab", "abb"], [["ab"], ["aab"], ["abb"]])

    def test_case_sensitive(self):
        self.check(["Tea", "eat", "ate"], [["Tea"], ["eat", "ate"]])

    def test_unicode(self):
        self.check(["кот", "ток", "окт", "кит"], [["кот", "ток", "окт"], ["кит"]])

    def test_solve_text(self):
        self.assertEqual(
            solve("eat tea tan ate nat bat"),
            '[["bat"],["nat","tan"],["ate","eat","tea"]]',
        )
        self.assertEqual(solve(""), "[]")

    def test_big(self):
        words = ["".join(random.sample("abcdefgh", 8)) for _ in range(50_000)]
        groups = group_anagrams(words)
        self.assertEqual(len(groups), 1)
        self.assertEqual(len(groups[0]), 50_000)

    def test_against_brute(self):
        random.seed(0)
        for _ in range(500):
            words = [
                "".join(random.choices("abc", k=random.randint(0, 4)))
                for _ in range(random.randint(0, 12))
            ]
            self.assertEqual(group_anagrams(words), brute(words), words)


if __name__ == "__main__":
    unittest.main(verbosity=2)
