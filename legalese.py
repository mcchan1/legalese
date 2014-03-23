""" A function to iterate through a legal document and replace it with plain
	English
	Things to do: 
	-highlight replaced words
	-accept pdf and ms word docs
	-better way to make dictionary not case sensitive
	"""

# user inputs the document they want translated	
fin = raw_input("Please type the full path of the document you want translated from legalese to plain english. >>>")

#fin = '/Users/michaelchan/Desktop/legalsample.txt'

# document is read
fin = open(fin).read() 			
print "This is the original text..."
print fin
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

#a function to iterate through the user inputed document
def replace_legalese(text, legal_dict):	
		
	for key, value in legal_dict.iteritems(): 
		# is there a better way to make legal_dict not case sensitive??
		text = text.lower() 
		text = text.replace(key,value)
		
	return text

#inputs the user's document and run it through the function
new_text = replace_legalese(fin, legal_dict)

print new_text

# where to implement this class???
# class CaseInsensitiveDict(legal_dict):
# 	def __setitem__(self, key, value):
# 		super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)
# 		
# 	def __getitem__(self, key):
# 		return super(CaseInsensitiveDict, self).__getitem__(key.lower())
	