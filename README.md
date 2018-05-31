# Python Cookbook
## This repository is intended to practice and learn new recipes that are common and exceptional in 
## everyday Python programming. 
---
### Chapter 1 Data structures and algorithms

**Discussion**

Unpacking works with any object that happens to be iterable. Not just tuples or lists. This includes strings, files, iterators, and generators. When unpacking, you may sometimes want to discard certain values. Python has no special syntax for this, but you can just pick a throw away variable name. However, make sure the variable name you use is **NOT** in use already. 
* End 1.1 Unpacking a sequence into Seperate Variables
---

* 1.2 Unpacking elements from iterables of arbitrary length

* Problem:
You need to unpack N elements from an iterable ut the ierable may be longer than N elements, causing a "too many values to unpack" exception.
* Solution:
### 1.
Python "star expression" can be used to address this problem. For example, suppose you run a course and decide at the end of the semester that you're going to drop the first and last homework grades, and only average the rest of them. If there are only four assignments, maybe you simply unpack all four, but hwat if there are 24? A star expression makes it easy: (see code)
### 2.
As another example, suppose you have user records that consist of a name and email address, followed by an arbitrary number of phone numbers. You could unpack the records like this: (see code)
### 3.
It is worth nothing that the phone_numbers variabl will always be a list, regardsless of how many phone numbers are unpacked (including none). Thus, any code taht uses phone_numbers won't have to account for the possibility that it might not be a list or perform any kind of additional type checking. The starred variable can also be the first one in the list. FOr example, say you have a sequence of values representing your company's sales figures for the last eight quarters. If you want to see how the most recent quarter stacks up to the average of the first seven, you could do someting like this: (see code)
