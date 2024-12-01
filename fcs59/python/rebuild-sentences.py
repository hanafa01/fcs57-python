def rebuild_sentence(words, lengths):
    
    for i in range(len(words)):
        print(words[i][:lengths[i]], end=" ")

rebuild_sentence(["the", "sky", "is", "blue"],[3,2,2,1])