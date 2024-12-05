function rebuild_sentence(words, lengths) {
    for (let i = 0; i < words.length; i++) {
        console.log(words[i].slice(0, lengths[i]))
    }
}
rebuild_sentence(["the", "sky", "is", "blue"], [3, 2, 2, 1]);
