import psycopg2
import pandas as pd
import numpy as np
import nltk
import re
import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------------------------------------------------
# 1. NLTK setup (download stopwords/tokenizer if not already present)
# ------------------------------------------------------------------------
nltk.download('punkt')
nltk.download('stopwords')

# ------------------------------------------------------------------------
# 2. Database connection configuration
# ------------------------------------------------------------------------
DB_HOST = os.getenv("DB_HOST", "YOUR_HOST")
DB_NAME = os.getenv("DB_NAME", "YOUR_DATABASE_NAME")
DB_USER = os.getenv("DB_USER", "YOUR_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD", "YOUR_PASSWORD")


def get_db_connection():
    """
    Returns a psycopg2 connection to PostgreSQL.
    Adjust host/user/password to match your environment.
    """
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

# ------------------------------------------------------------------------
# 3. Themes, categories, and keywords dictionary
#    (Renamed 'Social Recognition' -> 'Social Standing')
# ------------------------------------------------------------------------
themes = {
    'Proximity': {
        'Close to the Heart': [
            'personal trauma', 'loss', 'memory of', 'dedicated to', 'personal connection',
            'close to my heart', 'affected by', 'family', 'friend', 'loved one', 'in memory',
            'because of my experience with', 'after losing', 'after experiencing', 'significant to me',
            'means a lot to me', 'in honour of', 'in loving memory', 'tribute to', 'in memory of'
        ],
        'Close to Home': [
            'local', 'community', 'neighborhood', 'near me', 'close to home', 'in my area',
            'local school', 'local hospital', 'supporting local', 'our town', 'our city',
            'benefits my community', 'nearby', 'close by', 'local community', 'local cause',
            'help our area', 'helping locally', 'our region', 'local initiative'
        ],
    },
    'Self-Gain': {
        'Social Standing': [  # <-- Renamed here
            'social status', 'social recognition', 'identity expression', 'social media', 'share',
            'post', 'like', 'follow', 'support me', 'raise awareness', 'get the word out', 'trend',
            'viral', 'identity', 'brand', 'followers', 'praise', 'reputation', 'public image',
            'prestige', 'kudos', 'networking', 'visibility', 'social influence', 'popularity'
        ],
        'Personal Development': [
            'personal growth', 'learn', 'develop', 'improve myself', 'challenge myself',
            'self-improvement', 'gain experience', 'skills', 'new abilities', 'transformative',
            'journey', 'overcome', 'personal journey', 'self-discovery', 'grow as a person',
            'better myself', 'achieve my goals', 'personal development', 'self-fulfillment', 'aspiration'
        ],
        'Seeking Experiences': [
            'fun', 'enjoy', 'experience', 'exciting', 'adventure', 'challenge', 'marathon', 'hike',
            'skydiving', 'activity', 'event', 'participate in', 'enjoyment', 'recreational', 'pleasure',
            'once in a lifetime', 'exciting opportunity', 'thrill', 'fun run', 'recreational activity',
            'enjoyable experience', 'memorable', 'leisure', 'festive', 'celebration'
        ],
    },
    'Empowerment': {
        'Stewardship': [
            'control', 'direct impact', 'transparency', 'efficiency', 'effective altruism', 'manage',
            'oversee', 'ensure', 'utilize resources effectively', 'stewardship', 'maximizing impact',
            'evidence-based', 'make sure', 'responsibility', 'efficient use', 'accountability',
            'ensure funds are used properly', 'allocate resources', 'direct involvement', 'trustworthy',
            'responsible giving', 'efficient management', 'maximize effectiveness'
        ],
        'Advocacy': [
            'advocate', 'raise awareness', 'speak out', 'voice', 'visibility',
            'marginalized', 'social movement', 'make a difference', 'change', 'policy', 'activism',
            'fight for', 'supporting cause', 'urge', 'petition', 'social justice', 'stand up for',
            'protest', 'equality', 'human rights', 'advocacy', 'take action', 'speak up'
        ],
    },
    'Moral Purpose': {
        'Religious Affiliation': [
            'faith', 'god', 'church', 'blessed', 'prayer', 'mission', 'ministry', 'religious',
            'bible', 'spiritual', 'divine', 'grace', 'christian', 'islam', 'muslim', 'jewish', 'hindu',
            'buddhist', 'religion', 'blessing', 'holy', 'worship', 'belief', 'devotion', 'religious duty'
        ],
        'Moral Obligation': [
            'duty', 'obligation', 'responsibility', 'ought to', 'moral', 'ethics', 'justice',
            'empathy', 'altruism', 'help others', 'do the right thing', 'humanity', 'compassion',
            'conscience', 'feel compelled', 'must help', 'moral duty', 'ethically', "it's right",
            'moral responsibility', 'obliged', 'commitment', 'moral imperative', 'sense of duty'
        ],
    },
}

# ------------------------------------------------------------------------
# 4. Fetch relevant data from the PostgreSQL database
# ------------------------------------------------------------------------
def fetch_data_from_db():
    """
    Fetch rows from the 'crowdfunding' table that match:
       details->>'activityCharityCreated' = 'false'
       details->>'activityType' = 'CharityAppeal'
    Returns a pandas DataFrame with columns: short_name, story, activityCharityCreated, activityType.
    """
    query = """
        SELECT 
            short_name,
            details->>'activityCharityCreated' AS activityCharityCreated,
            details->>'activityType' AS activityType,
            details->>'story' AS story
        FROM crowdfunding
        WHERE details->>'activityCharityCreated' = 'false'
          AND details->>'activityType' = 'CharityAppeal';
    """
    conn = get_db_connection()
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()
    return df

# ------------------------------------------------------------------------
# 5. Clean and preprocess
# ------------------------------------------------------------------------
def clean_text(text):
    """
    Removes HTML tags, character entities, URLs, extra spaces, etc.
    """
    if not isinstance(text, str):
        text = str(text) if text is not None else ''
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove HTML character entities
    text = re.sub(r'&\w+;', '', text)
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """
    Tokenize, remove stopwords/punctuation, lowercase, rejoin.
    """
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)

# ------------------------------------------------------------------------
# 6. Main analysis function
# ------------------------------------------------------------------------
def main_analysis():
    # 1) Fetch from DB
    df = fetch_data_from_db()
    matching_count = len(df)
    print(f"\nNumber of rows matched in DB (activityCharityCreated=false, activityType=CharityAppeal): {matching_count}")

    # 2) Basic cleaning of 'story'
    df['story'] = df['story'].fillna('').astype(str)
    df['clean_story'] = df['story'].apply(clean_text)

    # 3) Remove duplicates or empty stories
    df = df.drop_duplicates(subset='clean_story')
    df = df[df['clean_story'].str.strip() != '']
    df['story_id'] = df.index  # assign unique ID

    # 4) Preprocess for TF-IDF
    df['preprocessed_story'] = df['clean_story'].apply(preprocess_text)

    # 5) Prepare all keywords
    all_keywords = set()
    keyword_to_categories = {}
    category_to_theme = {}

    for theme, categories in themes.items():
        for category, keywords in categories.items():
            for keyword in keywords:
                all_keywords.add(keyword)
                if keyword in keyword_to_categories:
                    keyword_to_categories[keyword].append(category)
                else:
                    keyword_to_categories[keyword] = [category]
            category_to_theme[category] = theme

    all_keywords = list(all_keywords)  # convert to list for TfidfVectorizer

    # 6) TF-IDF vectorization
    tfidf_vectorizer = TfidfVectorizer(vocabulary=all_keywords, ngram_range=(1,3))
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['preprocessed_story'])
    feature_names = tfidf_vectorizer.get_feature_names_out()

    # 7) Build TF-IDF DataFrame
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
    tfidf_df['story_id'] = df['story_id']

    # 8) Map keywords -> categories -> themes
    def map_keywords_to_categories(row):
        category_scores = {cat: 0 for cat in category_to_theme.keys()}
        for kw in feature_names:
            score = row[kw]
            cats = keyword_to_categories[kw]
            for c in cats:
                category_scores[c] += score
        return category_scores

    tfidf_df['category_scores'] = tfidf_df.apply(map_keywords_to_categories, axis=1)

    def aggregate_category_to_theme_scores(cat_scores):
        theme_scores = {t: 0 for t in themes.keys()}
        for cat, sc in cat_scores.items():
            theme = category_to_theme[cat]
            theme_scores[theme] += sc
        return theme_scores

    tfidf_df['theme_scores'] = tfidf_df['category_scores'].apply(aggregate_category_to_theme_scores)

    # 9) Normalize
    def normalize_scores(scores_dict):
        total = sum(scores_dict.values())
        if total > 0:
            return {k: v / total for k, v in scores_dict.items()}
        else:
            return {k: 0 for k in scores_dict.keys()}

    tfidf_df['normalized_category_scores'] = tfidf_df['category_scores'].apply(normalize_scores)
    tfidf_df['normalized_theme_scores'] = tfidf_df['theme_scores'].apply(normalize_scores)

    # 10) Merge back to main df
    df = df.merge(tfidf_df[['story_id', 'normalized_category_scores', 'normalized_theme_scores']], on='story_id')

    # 11) Analyze & visualize
    # Category & theme DF
    normalized_category_scores_df = pd.DataFrame(df['normalized_category_scores'].tolist())
    normalized_category_scores_df['story_id'] = df['story_id']

    normalized_theme_scores_df = pd.DataFrame(df['normalized_theme_scores'].tolist())
    normalized_theme_scores_df['story_id'] = df['story_id']

    # Averages
    average_category_weights = normalized_category_scores_df.drop('story_id', axis=1).mean().fillna(0)
    average_category_weights_sorted = average_category_weights.sort_values(ascending=False)

    average_theme_weights = normalized_theme_scores_df.drop('story_id', axis=1).mean().fillna(0)
    average_theme_weights_sorted = average_theme_weights.sort_values(ascending=False)

    # -----------------------
    # Print ranking in console
    # -----------------------
    print("\nRanking of Themes from Most to Least Important:")
    for idx, (theme, weight) in enumerate(average_theme_weights_sorted.items(), start=1):
        print(f"{idx}. {theme}: {weight:.4f}")

    print("\nRanking of Categories from Most to Least Important:")
    for idx, (category, weight) in enumerate(average_category_weights_sorted.items(), start=1):
        print(f"{idx}. {category}: {weight:.4f}")

    # -----------------------
    # Print the raw data used by the plots in console
    # -----------------------

    # Theme weights data (for 'Average Weights of Themes' bar chart)
    print("\nTheme Weights (Data for the 'Average Weights of Themes' chart):")
    print(average_theme_weights_sorted)

    # Category weights data (for 'Average Weights of Categories' bar chart)
    print("\nCategory Weights (Data for the 'Average Weights of Categories' chart):")
    print(average_category_weights_sorted)

    # Save the rankings
    with open('theme_ranking.txt', 'w') as f:
        f.write("Ranking of Themes from Most to Least Important:\n")
        for idx, (theme, weight) in enumerate(average_theme_weights_sorted.items(), start=1):
            f.write(f"{idx}. {theme}: {weight:.4f}\n")

    with open('category_ranking.txt', 'w') as f:
        f.write("Ranking of Categories from Most to Least Important:\n")
        for idx, (cat, weight) in enumerate(average_category_weights_sorted.items(), start=1):
            f.write(f"{idx}. {cat}: {weight:.4f}\n")

    print("\nRankings saved to 'theme_ranking.txt' and 'category_ranking.txt'.")

    # 12) Visualizations
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # Themes bar chart
    plt.figure(figsize=(10,6), dpi=600)  # 600 DPI for high resolution
    average_theme_weights_sorted.sort_values(ascending=True).plot(kind='barh', color='skyblue')
    plt.xlabel('Average Normalized Weight')
    plt.title('Average Weights of Themes')
    plt.tight_layout()
    plt.savefig('plots/theme_weights_bar_chart.png', dpi=600)
    plt.show()

    print("Theme weights bar chart saved as 'plots/theme_weights_bar_chart.png'.")

    # Categories bar chart
    plt.figure(figsize=(10,8), dpi=600)  # 600 DPI for high resolution
    average_category_weights_sorted.sort_values(ascending=True).plot(kind='barh', color='lightgreen')
    plt.xlabel('Average Normalized Weight')
    plt.title('Average Weights of Categories')
    plt.tight_layout()
    plt.savefig('plots/category_weights_bar_chart.png', dpi=600)
    plt.show()

    print("Category weights bar chart saved as 'plots/category_weights_bar_chart.png'.")

    # Correlation heatmaps
    corr_cat = normalized_category_scores_df.drop('story_id', axis=1).corr()
    corr_theme = normalized_theme_scores_df.drop('story_id', axis=1).corr()

    # Print correlation data (tables) in console
    print("\nCategory Correlation Table (Data for 'Correlation Between Categories' heatmap):")
    print(corr_cat)

    print("\nTheme Correlation Table (Data for 'Correlation Between Themes' heatmap):")
    print(corr_theme)

    # Category correlation heatmap
    plt.figure(figsize=(12,10), dpi=600)
    sns.heatmap(corr_cat, annot=True, cmap='coolwarm')
    plt.title('Correlation Between Categories')
    plt.tight_layout()
    plt.savefig('plots/category_correlation_heatmap.png', dpi=600)
    plt.show()
    print("Category correlation heatmap saved as 'plots/category_correlation_heatmap.png'.")

    # Theme correlation heatmap
    plt.figure(figsize=(8,6), dpi=600)
    sns.heatmap(corr_theme, annot=True, cmap='coolwarm')
    plt.title('Correlation Between Themes')
    plt.tight_layout()
    plt.savefig('plots/theme_correlation_heatmap.png', dpi=600)
    plt.show()
    print("Theme correlation heatmap saved as 'plots/theme_correlation_heatmap.png'.")

    # 13) Save final DataFrame
    df.to_csv('stories_with_theme_and_category_weights.csv', index=False)
    print("\nResults saved to 'stories_with_theme_and_category_weights.csv'.")

    # 14) Top 2 stories per category
    if not os.path.exists('top_stories_by_category'):
        os.makedirs('top_stories_by_category')

    for category in category_to_theme.keys():
        # Stories that have a non-zero score for this category
        stories_with_cat = df[df['normalized_category_scores'].apply(lambda x: x[category] > 0)]
        if stories_with_cat.empty:
            continue

        # Add the category score as a column
        stories_with_cat = stories_with_cat.copy()
        stories_with_cat['category_score'] = stories_with_cat['normalized_category_scores'].apply(lambda x: x[category])

        # Sort descending
        stories_with_cat = stories_with_cat.sort_values('category_score', ascending=False)

        # Top 2
        top_stories = stories_with_cat.head(2)

        safe_cat_name = re.sub(r'[\\/*?:"<>|]', "_", category)
        file_path = f'top_stories_by_category/{safe_cat_name}_top_stories.txt'
        top_stories['story'].to_csv(file_path, index=False, header=False)

    print("Top 2 stories for each category saved in 'top_stories_by_category' directory.")

# ------------------------------------------------------------------------
# 7. Main Entry
# ------------------------------------------------------------------------
if __name__ == "__main__":
    main_analysis()
