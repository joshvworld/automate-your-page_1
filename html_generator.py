


LESSON_CONCEPTS = [['World Wide Web','The web is the way computers interact with the internet via HTTP, or hypertext transfer protocol. The webpages we see are transmitted via this protocol and are written in HTML, hypertext markup language. '], ['HTML','HTML documents are written using markup language, or tags, to alter plain text and present the multimedia experiences that we know as webpages. Different tags have different behaviors. Some must be accompanied by a closing tag, while others are void tags. Some tags are block tags and segregate content into invisible boxes, while others are inline and simply affect the text without blocking it off.'], ['Stupid Computers','We say that computers are stupid because they cannot detect and fix mistakes that a reasonably intelligent human would be able to. They can only interpret instructions literally and cannot guess context.'], ['The Importance of Remembering Everything','Programming has too many rules and details to remember everything. Programmers should focus on learning big, important details and rely on their ability to search for and find the rest. If you are stressed over remembering every little detail of code which will invariably change in the future, please click here to destress, then resume your studies.']]

def generate_html(notes):
    for item in notes:
	    title = item[0]
	    concept = item[1]
	    concept_number_integer = notes.index(item) + 1
	    concept_number_string = str(concept_number_integer)
	    print '''<div class="concept" id="lesson-1-''' + concept_number_string + '''">
	<h4 class="concept-title">
		''' + title + '''
	</h4>
	<div class="concept-description">
		''' + concept + '''
	</div>
</div>'''

print generate_html(LESSON_CONCEPTS)