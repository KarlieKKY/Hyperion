# CT2
# import libraries
import spacy
import pathlib
import math
nlp = spacy.load("en_core_web_md")


# create a function that print out the popular movie
def similar_movie(description):
    similar_index = -math.inf
    similar_title = ""
    compare_sentence = nlp(description)
    # open the movies,txt file
    file_name = "movies.txt"
    introduction_doc = nlp(pathlib.Path(file_name).read_text(encoding="utf-8"))
    list_ = introduction_doc.text.split("\n")
    # loop through the sentences of the movie list
    for ind, sentence in enumerate(list_):
        try:
            # assign variable of title
            title = sentence.split(" :")[0]
            # assign variable of movie description
            sentence = sentence.split(" :")[1]
            similarity = nlp(sentence).similarity(compare_sentence)
            # find out the most similar movie
            if similarity > similar_index:
                similar_index = similarity
                similar_title = title
        except:
            print(f"Empty description in line {ind}, the description is: {list_[ind]}")

    print(f"The similar title is {similar_title}")


# call the function and prompt the user for movie description
similar_movie(input("Enter a movie description: "))
