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

Python "star expression" can be used to address this problem. For example, suppose you run a course and decide at the end of the semester that you're going to drop the first and last homework grades, and only average the rest of them. If there are only four 
As another example, suppose you have user records that consist of a name and email address, followed by an arbitrary number of phone numbers. You could unpack the records like this: (see code #2)

It is worth nothing that the phone_numbers variabl will always be a list, regardsless of how many phone numbers are unpacked (including none). Thus, any code taht uses phone_numbers won't have to account for the possibility that it might not be a list or perform any kind of additional type checking. The starred variable can also be the first one in the list. FOr example, say you have a sequence of values representing your company's sales figures for the last eight quarters. If you want to see how the most recent quarter stacks up to the average of the first seven, you could do someting like this: (see code #3)

* Discussion
Extended iterable unpacking is tailor-made for unpacking iterables of unknown or arbirtrary length. **Oftentimes, these iterables have some known component or pattern to their construction _(e.g. "everything after element 1 is a phone number")_**
and star unpacking lets the developer leverage those patterns easily instead of perfroming acrobatics to get at the relevant elements in the iterable. 

It is worth nothing that the star syntax can be especially useful when iterating over a sequence of tuples of varying length. For example, perhaps a sequence of tagged tuples . (see code #4)

Star unpacking can also be useful when combined with certain kinds of string processing operations, such as splitting. For example: 
(see code #5)

Sometimes you might want to unpack values and throw them away. You can't just specify a bare* when unpacking, but you could use a common throway variable name, such as _ or ign (ignore). For example: (see code #6)

Star unpacking and list-processing features of various functional languages share certain similarities. For example, if you have a list, you can eeasily split it into head and tail components like this: (code #7)

One could imagine writing functions that perform such splitting in order to carry out some kind of cler recursive algorithm. For example (code #8)

_However_, be aware that recursion is not really a strong Python feature due to the inherent recursion limit. Thus, this last example might be nothing more than an academic curiosity in practice.

* End1.2 Unpacking Elements from Iterables of Arbitrary Length

---
