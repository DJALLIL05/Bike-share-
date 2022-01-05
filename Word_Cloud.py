def calculate_frequencies(file_contents):
  # Here is a list of punctuations and uninteresting words you can use to process your text
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
  # Opening and reading the text file
  # link to the article https://www.ibm.com/cloud/learn/what-is-artificial-intelligence
  with open('/content/AI.txt', 'r') as f_handel:
    f = f_handel.read()
  #Making all characters lower case and removing any spaces at the begening and the end of the text
  text = f.replace('\n', ' ').lower().strip()
  # Removing all the unnevessary punctuations
  d = {}
  for i in punctuations+'“”‘’':
    d[i] = None
  table = text.maketrans(d)
  new_text = text.translate(table).replace('—', '  ')
  #splitting the text file into a list of words
  words = new_text.split()
  #counting the words in the list and ignoring all uninteresting words and words that do not contain all alphabets
  count = dict()
  for word in words:
    if (word not in uninteresting_words) and (word.isalpha()):
      count[word] = count.get(word, 0) + 1
  cloud = wordcloud.WordCloud()
  cloud.generate_from_frequencies(count)
  return cloud.to_array()

# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
