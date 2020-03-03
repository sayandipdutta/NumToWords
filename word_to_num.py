# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:06:23 2020

@author: sayan
"""
from contextlib import suppress
from decimal import Decimal
import math
from typing import Union
from functools import lru_cache

x = 2


class WordFromNum:
	"""
	Converts words to num
	"""
	__common_prefix: dict = { 1_000_000_000_000: 'trillion', 1_000_000_000: 'billion', 1_000_000: 'million', 
						      1_000: 'thousand', 100: 'hundred', 90: 'ninety', 80: 'eighty', 70: 'seventy', 
							  60: 'sixty', 50: 'fifty', 40: 'forty', 30: 'thirty', 20: 'twenty', 19: 'nineteen', 
							  18: 'eighteen', 17: 'seventeen', 16: 'sixteen', 15: 'fifteen', 14: 'fourteen', 
							  13: 'thirteen', 12: 'twelve', 11: 'eleven', 10: 'ten', 9: 'nine', 8: 'eight', 
							  7: 'seven', 6: 'six', 5: 'Five', 4: 'four', 3: 'three', 2: 'two', 1: 'one', 0: 'zero'}
	__single_dict: dict = { 9: 'nine', 8: 'eight', 7: 'seven', 6: 'six', 5: 'Five', 
						    4: 'four', 3: 'three', 2: 'two', 1: 'one', 0: 'zero'}
	
	__double_dict: dict = { 90: 'ninety', 80: 'eighty', 70: 'seventy', 60: 'sixty', 50: 'fifty', 40: 'forty', 
					       30: 'thirty', 20: 'twenty', 19: 'nineteen', 18: 'eighteen', 17: 'seventeen', 16: 'sixteen', 
						   15: 'fifteen', 14: 'fourteen', 13: 'thirteen', 12: 'twelve', 11: 'eleven', 10: 'ten'}
	
	__poly_dict: dict = { 1_000_000_000_000: 'trillion', 1_000_000_000: 'billion', 1_000_000: 'million', 
					      1_000: 'thousand', 100: 'hundred'}
	
	def __init__(self):
		self.divisors = []
	   
	@classmethod
	def _process_num(num: Union[float, int, str]) -> Decimal:
		"""Converts input to correct form.
		
		If convertible, or already in correct form,
		returns num, else raised ValueError
		"""
		
		try:
			float(num)
		except ValueError as error:
			print(f'ValueError: {error}, expected num to be int or numeric string, got {num}')
		if isinstance(num, str):
			return Decimal(num)
		else:
			return Decimal(str(num))
	
	@staticmethod
	@lru_cache(maxsize=1000)
	def _construct_whole( num: int, sign: str, divisor: int,
					      remainder: Union[float, int] = float('inf'), result: str = '' ) -> str:

		"""
		turns whole part of the number into word(s)
		"""

		if num in WordFromNum.__common_prefix:
			return WordFromNum.__common_prefix[num]
		
		if remainder == 0:
			return result
		
		remainder, quotient = divmod(num, divisor)
		if not quotient:
			return WordFromNum._construct_word(num, sign, next(divisors))
		#TODO
	
	@staticmethod
	def wfm(num: str) -> str:
		"""
		converts fractional part, if any
		joins with the whole part
		"""
		num_str = num
		num = WordFromNum._process_num(num)
		whole, frac = (num_str[:num.exponent], num.digits[num.exponent:]) if num.exponent < 0 else (num_str, None)
		if frac:
			decimal_str = 'point ' + ' '.join(WordFromNum.__common_prefix[digit] for digit in frac)
			
		else:
			decimal_str = 'point zero'
			
		
		return WordFromNum._construct_whole(num, sign, divisor = next(divisors))
		
