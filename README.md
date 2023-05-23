# Songify


1. Introduction



In this report, we present the details and findings of our project on song recommendation using machine learning techniques. The objective of this project is to develop a system that can recommend songs to users based on their preferences and similarities between songs.



2. Methodology



Our approach for song recommendation involves the following key steps:

Vectorization and similarity based on angle: We utilize vectorization techniques to represent songs as vectors. The angle between vectors is used to measure the similarity between songs. If two vectors have a small angle between them, it indicates that the two songs are close to each other in terms of their characteristics.

Natural Language Processing (NLP): We employ NLP techniques to process the song data. This includes data formatting, creating tags, and performing word replacement using NLTK library to ensure consistency and improve accuracy in similarity calculations.



3. Data Formatting



The song data is obtained from a CSV file. We extract the relevant columns containing useful information for song recommendation. To prepare the data for further processing, we create tags based on the important column information. The tags are then transformed to lowercase and any spaces between individual words are removed. Additionally, we use NLTK to replace words that have similar meanings, reducing redundancy in the dataset.



4. Vectorization



We employ vectorization to represent songs as numerical vectors. By creating vectors based on the tags, we capture the essential characteristics of each song. A stop_words function is applied to remove common words such as "the," "and," and "are," which do not contribute significantly to the differentiation of songs. The vector representation of each song consists of coordinates in the "x" dimension. We have chosen x = 2000 to balance the trade-off between underfitting and overfitting of the model.



5. Song Recommendation



The cosine_similarity function is utilized to calculate the angle between each pair of song vectors. The smaller the angle, the closer the songs are in terms of their characteristics. Based on this, an array is constructed with the cosine(angle) values, arranged in descending order. The indexes of the cosine(angle) values are used to recommend songs to users, as songs with smaller angles have larger cosine(angle) values.



6. User Interface and Deployment



To provide a user-friendly interface, we have implemented the song recommendation system using the Streamlit framework. The deployed website allows users to easily navigate and explore the recommended songs. We have integrated YouTube links for quick access to the recommended songs, enhancing the user experience.



7. Conclusion



In conclusion, our project successfully developed a song recommendation system using machine learning techniques. By employing vectorization, similarity calculation, and natural language processing, we were able to recommend songs based on user preferences and similarities between songs. The system demonstrated promising results and effectively provided relevant song recommendations to users.



8. Potential Future Improvements or Expansions



While our project achieved its objectives, there are several potential areas for improvement and expansion. Some suggestions for future work include:

  1. Incorporating user feedback and ratings to personalize recommendations further.

  2. Exploring additional feature extraction techniques to capture more comprehensive song characteristics.

  3. Evaluating and fine-tuning the recommendation system using performance evaluation metrics and user satisfaction surveys.

  4. Scaling up the system to handle larger datasets and increasing the diversity of recommended songs.




9.Liabraries used



pandas,
 numpy,
 ast, 
 sklearn.feature_extraction.text, 
 sklearn.metrics.pairwise, 
 nltk.stem.porter, 
 streamlit, 
 pickle


website Link - https://radit242-songify-app-zp1njp.streamlit.app/
