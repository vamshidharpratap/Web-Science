# Generative Models for the Web


Consider the following text of the entry "Simple English Wikipedia" in the Simple English Wikipedia (adapted to fit this exercise). The text file can be found in the zipball.

The Simple English Wikipedia is an English-language version of Wikipedia, an online encyclopedia, that is written in basic English. It was built on November 17, 2003. All of the articles in the Simple English Wikipedia need to use shorter sentences and easier words and grammar than the regular English Wikipedia. People with different needs use the Simple English Wikipedia. They include: students, children, adults, who might find it hard to learn or read. People who are learning English as a second language. Other people use the Simple English Wikipedia because the basic language helps them understand hard ideas or topics they do not know about. Many articles are shorter than the same articles in the English Wikipedia. Technical subjects use some terms which are not simple. Editors try to explain these terms in a simple way. This makes Simple English articles a good way to understand difficult articles from the ordinary English Wikipedia. If someone cannot understand an idea in complex English, they can read the Simple English article. When the Simple English Wikipedia began in 2003, the ordinary English Wikipedia already had 150,000 articles, and seven other Wikipedias in other languages had over 15,000 articles. Since the other Wikipedias already have so many articles, most Simple English articles take articles from other Wikipedias and make them simple; they are usually not new articles. Right now, the Simple English Wikipedia has 128,492 articles. As of December 2016, it was the 52nd largest Wikipedia.

1. Create a probabilistic generative model of text by sampling from the distribution of 1) word lengths 2) frequency of each character in the given text, similar to the one presented in the video slides'.<br/>

   Modelling choices:<br/>
     **•** Your model should generate one word at a time according to the distribution of the word lengths.<br/>
     **•** Within each word, generate characters according to the distribution of character
       frequencies. <br/>
     **•** Your model should only consider lowercase letters [az] and numbers [09]. <br/>
       All uppercase letters should be converted to lowercase. Other characters such as punctuations should be excluded.<br/>

Generate a text of 5,000 words with your model. Please upload your generated text as an individual file, but do not include it in the PDF document.

2. Plot the probability distribution of word lengths of 1) the original text 2) the text
you generated in one plot.


# Modelling the Web as a Graph Consider the following undirected graph G.


1. Write down the adjacency matrix A of the graph G. <br/>
2. The diameter of a graph is defined as the longest shortest path in the graph. The shortest path between two vertices u and u is defined as the distance between u and v: dist(u, v).<br/>
  
   Write the definition of the diameter as a mathematical formula, and give the diameter
d of the graph G. <br/>

3. Usually we do not store the adjacency matrix directly since it is too large. Instead,
we use one line: "u v" to represent an undirected edge between vertices u and v.<br/>

 * Write a function to read the file graph. dat and convert it to the adjacency matrix.<br/>

4. Write a function to compute the Gini coefficient g of the degrees of vertices in G. The function should have the adjacency matrix of G as its only parameter.<br/>
5. A triangle in an undirected graph G = (V,E) is defined as three vertices that are
adjacent to one another.<br/>

 Write the definition as a mathematical formula. <br/>

  * Write a function to compute the number of triangles t in the graph G. The function should have the adjacency matrix of G as its only parameter.<br/>
