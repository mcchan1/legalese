""" A function to iterate through a legal document and replace it with plain
	English
	Things to do: 
	-highlight legalese that is replaced with English
	-accept pdf and ms word docs
	-better way to make dictionary not case sensitive, as opposed to making the 
	search case insensitive. 
	"""
import re

# user inputs the document they want translated	
text = raw_input("Please type the full path of the document you want translated from legalese to plain english. >>>")

#text = '/Users/michaelchan/Desktop/legalsample.txt'

# document is read
text = open(text).read() 			
print "This is the original text..."
print text
print '\n'
print "Now, here is the new text with out legalese.."
print '\n'

#dictionary of useless legal terms
legal_dict = {'ab initio':'from the start',
'accord': 'give',
'afforded':'given',
'aforementioned':'this',
'aforesaid': 'this',
'albeit':'although' ,
'ambit':'scope',
'antecedent to':'before',
'as a means of': 'to',
'as prescribed by': 'under',
'aver':'state',
'bona fide': 'good faith',
'case at bar':'this case',
'case sub judice':'this case',
'cease':'stop',
'circa':'about',
'commence':	'start',
'defacto': 'in reality',
'envisage':	'see',
'ex post facto': 'retrospectively',
'hence': 'from now on',
'henceforth':'from now on',
'henceforward':	'from now on',
'herein': 'in this document/paragraph/sentence', 
'hereto': 'in this document/paragraph/sentence',
'heretofore':'until now',
'hitherto':	'until now',
'in a case in which':'when / where',
'in accordance with': 'under',
'in as much as':'because',
'in excess of':	'more than',
'in lieu of':'instead of',
'in order to':'to',
'in receipt of':'have',
'in reference to':	'about',
'in regard to':	'about',
'in the amount of':	'for',
'in the event of that' :'if',
'in the event that':'if',
'in the near future':'soon',
'inter alia':'among other things',
'inter partes':'between parties',
'inter se':	'among themselves',
'in toto': 'entirely',
'ipso facto':'therefore',
'it is apparent that':'clearly',
'mutatis mutandis': 'things that must be changed',
'notwithstanding':'despite',
'null and void':'void',
'pertaining to':'about/of',
'precis':'summary',
'prima facie':'on the face of it',
'on behalf of':	'for',
'on the part of':'by',
'post hoc':'after this',
'pursuant': 'required',
'remainder':'rest',
'requisite':'required',
'retain':'keep',
'simultaneously':'at the same time',
'subsequent':'later',
'subsequent to':'after',
'subsequently':	'afterwards', 
'substantiate':	'prove',
'take into consideration':'consider',
'the case at bar':'this case',
'the fact that':'that',
'the instant case':	'this case',
'the majority of':'most',
'the manner in which':'how',
'thereafter': 'from that',
'therein':'in there',
'thereof':	'of it',
'theretofore':'until then',
'thereupon':'then',
'thitherto':'until then',
'until such time as':'until',
'unto':	'to',
'upon':'on',
'utilize':'use',
'whence':'from where',
'whereas': 'This contract is made with reference to the following facts',
'whereat':'where',
'wherein':'where',
'with regard to':'about',
'with the exception of':'except for',
'witnesseth':'this agreement shows/between',
}

# Using a case insensitive search for legalese as opposed to a case insensitive dictionary.  Have to import regular expressions.  

def replace(legal_dict,text):
        keys = legal_dict.keys()
        for i in keys:
                exp = re.compile(i, re.I)
                text = re.sub(exp, legal_dict[i], text)
        return text

text = replace(legal_dict,text)
print text
	