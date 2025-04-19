In text processing, particularly when dealing with large documents or long pieces of text, it can be useful to split the text into smaller, 
more manageable pieces, called chunks. Here’s what the terms chunk size and chunk overlap mean, along with an example:

Chunk Size: This refers to the length of each chunk. It can be defined in terms of the number of 
            characters, words, sentences, or tokens, depending on the context and requirements of the text processing task.

Chunk Overlap: This refers to the number of characters, words, sentences, or tokens that are shared between consecutive
               chunks. Overlap ensures that important information that might be at the boundary of one chunk is not missed in the next chunk.



Embeddings create a vector representation of a piece of text. This is useful because it means we can think about text in the vector space, and do 
things like semantic search where we look for pieces of text that are most similar in the vector space.

The base Embeddings class in LangChain provides two methods: one for embedding documents and one for embedding a query. The former takes as input
multiple texts, while the latter takes a single text. The reason for having these as two separate methods is that some embedding providers 
have different embedding methods for documents (to be searched over) vs queries (the search query itself).