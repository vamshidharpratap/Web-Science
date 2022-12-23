# Simple Crawler


Your task in this exercise is to "crawl" all the pages of http://quotes.toscrape.com.
Please keep in mind the following points to complete this assignment: <br/>
 •  Please have a look at the next exercise before you start this one. <br/>
 •  Your crawler should crawl all the quotes, their author (if mentioned), the tags associated with the quotes and form a comprehensive dataframe. <br/>
 •  Your crawling should stop when you encounter a page that no longer contains any quotes. <br/>
 •  You must provide the time taken crawl the above mentioned website. <br/>

You may use **Beautifulsoup, urllib/urllib2, pandas** but not Scrapy. Your final data frame post crawling should have the following columns;

| Page |  Quote        | Author       | Tags         |
|------|---------------|--------------|--------------|
|  1   | The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking. | Albert Einstein | change, deep-thoughts, thinking, world |


You may use the following functions

  1. def check_module: A function that checks the response code of the page along with the presence of quotes.
  2. def crawl module: To crawl the pages and extract information

# Descriptive Statistics

If you have successfully completed the above exercise of this assignment, then please provide the following details. You may have to tweak your code in the above exercise for some of the results.

1. What is the total count of **valid pages** in the aforementioned website that you could crawl?
2. Provide a frequency distribution of the number of **quotes** per author 
3. Provide a frequency distribution of the **tags**
4. Plot the average **length of quotes** (no. of words) per author..
