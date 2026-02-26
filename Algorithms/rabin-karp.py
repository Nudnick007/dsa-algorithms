# COPYRIGHT Nudnick007 2026

# In many data structures and algorithms (DSA) problems,
# one common task is to compare strings—whether it’s finding a word in a sentence,
# detecting duplicates, or checking for patterns inside a larger text.
# Think of this like trying to find a short phrase inside a big paragraph—manually checking every character would be tiring. 
# Computers do the same thing, and if we’re not careful, it can become very slow for long texts.

# it converts the strings into numbers (hashes) and compares those—just like how 
# barcodes are used in stores instead of reading the full product name.

# In short, Rabin-Karp is:

# A string matching algorithm
# Uses rolling hash to find all occurrences of a pattern in a text
# Optimized for cases where multiple patterns or repeated matching is required

# LEETCODE 1408 STRING MATCHING IN AN ARRAY IS ONE EXAMPLE
# Given an array of string words, return all strings in words that are a substring of another word. 
# You can return the answer in any order.

# Input words = ["leetcoder","leetcode","od","hamlet","am"]
# Expected ["leetcode","od","am"]

# For every pair of words:
# Treat the longer word as text
# Treat the shorter word as pattern
# Use Rabin–Karp to check if pattern exists in text

# Time Complexity:
# Worst case → O(n² · m)

class Solution:
	def stringMatching(self, words):
		
		# Rabin-Karp substring search
		def rabin_karp(text, pattern):
			n, m = len(text), len(pattern)
			if m > n:
				return False
			
			base = 256
			mod = 10**9 + 7
			
			pattern_hash = 0
			window_hash = 0
			highest_base = 1  # base^(m-1)

			# Precompute base^(m-1)
			for _ in range(m - 1):
				highest_base = (highest_base * base) % mod
			
			# Compute initial hash
			for i in range(m):
				pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
				window_hash = (window_hash * base + ord(text[i])) % mod
			
			# Slide window
			for i in range(n - m + 1):

				# Check hash match
				if pattern_hash == window_hash:
					# Double check to avoid collision
					if text[i:i+m] == pattern:
						return True

				# Compute next window hash
				if i < n - m:
					window_hash = (
						(window_hash - ord(text[i]) * highest_base) * base
						+ ord(text[i + m])
					) % mod
					
					# Avoid negative
					if window_hash < 0:
						window_hash += mod
			
			return False
		
		result = []
		
		for i in range(len(words)):
			for j in range(len(words)):
				if i != j:
					# Only check if words[i] is smaller or equal
					if len(words[i]) <= len(words[j]):
						if rabin_karp(words[j], words[i]):
							result.append(words[i])
							break
		
		return result