import pandas as pd

def evaluate_characteristics(recommendations_df, netflix_df):
    # Calculate average characteristics for recommendations and Netflix dataset
    avg_recommendations = recommendations_df[['averageRating', 'numVotes', 'golden_globe_wins', 
                                              'golden_globe_nominations', 'oscar_awards', 'oscar_nominations']].mean()
    avg_netflix = netflix_df[['averageRating', 'numVotes', 'golden_globe_wins', 
                              'golden_globe_nominations', 'oscar_awards', 'oscar_nominations']].mean()
    
    # Print out the average characteristics for comparison
    print("Average Characteristics for Recommendations:")
    print(avg_recommendations)
    print("\nAverage Characteristics for Netflix:")
    print(avg_netflix)
    
    # Compare the averages
    comparison = pd.DataFrame({'Recommendation': avg_recommendations, 'Netflix': avg_netflix})
    comparison['Difference'] = comparison['Recommendation'] - comparison['Netflix']
    
    print("\nComparison of Averages:")
    print(comparison)
