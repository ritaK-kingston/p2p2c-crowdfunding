
---

# Crowdfunding Data Collection & Sentiment Analysis

This repository contains two main scripts designed to interface with the [JustGiving](https://www.justgiving.com/) API. The **search** script fetches active crowdfunding project data and stores it in a PostgreSQL database. The **analysis** script then reads this database and applies a thematic/categorical sentiment analysis to the fetched stories.

> **Note**: According to JustGiving’s API documentation and permissions, only **currently active** crowdfunding projects are returned. Historical (closed) projects are **not** accessible via the JustGiving APIs.

---

## 1. Prerequisites

- **Python**: 3.12.7  
  (Other 3.x versions may work, but the code is tested on 3.12.7.)
- **PostgreSQL**: 15.10  
  (Older versions may work, but it has been tested on 15.10.)
- **Git**: Optional, for cloning the repository.

### 1.1 Python Dependencies

Each script folder (`search` and `analysis`) contains its own `requirements.txt` file to specify needed Python packages. Refer to the [Installation](#installation) section below on how to install them.

---

## 2. Repository Structure

```
.
├── search
│   ├── justgiving_search.py
│   └── requirements.txt
├── analysis
│   ├── sentiment_analysis.py
│   └── requirements.txt
└── README.md
```

1. **search/**  
   - **justgiving_search.py**  
     Fetches crowdfunding pages from JustGiving using their REST API and saves the data into PostgreSQL.

2. **analysis/**  
   - **sentiment_analysis.py**  
     Reads the data from PostgreSQL, cleans/preprocesses the text, applies TF-IDF-based analysis, then categorizes the stories according to a predefined set of themes and categories. Outputs charts, ranking files, and a CSV of weighted results.

---

## 3. Sentiment Analysis Themes and Keywords

The analysis script uses a comprehensive dictionary of themes, categories, and keywords to categorize crowdfunding stories. The taxonomy is presented below as tables, one per theme. Each row repeats the theme and category for a single keyword.

### Proximity

| Theme | Category | Keyword |
| --- | --- | --- |
| Proximity | Close to the Heart | personal trauma |
| Proximity | Close to the Heart | loss |
| Proximity | Close to the Heart | memory of |
| Proximity | Close to the Heart | dedicated to |
| Proximity | Close to the Heart | personal connection |
| Proximity | Close to the Heart | close to my heart |
| Proximity | Close to the Heart | affected by |
| Proximity | Close to the Heart | family |
| Proximity | Close to the Heart | friend |
| Proximity | Close to the Heart | loved one |
| Proximity | Close to the Heart | in memory |
| Proximity | Close to the Heart | because of my experience with |
| Proximity | Close to the Heart | after losing |
| Proximity | Close to the Heart | after experiencing |
| Proximity | Close to the Heart | significant to me |
| Proximity | Close to the Heart | means a lot to me |
| Proximity | Close to the Heart | in honour of |
| Proximity | Close to the Heart | in loving memory |
| Proximity | Close to the Heart | tribute to |
| Proximity | Close to the Heart | in memory of |
| Proximity | Close to Home | local |
| Proximity | Close to Home | community |
| Proximity | Close to Home | neighborhood |
| Proximity | Close to Home | near me |
| Proximity | Close to Home | close to home |
| Proximity | Close to Home | in my area |
| Proximity | Close to Home | local school |
| Proximity | Close to Home | local hospital |
| Proximity | Close to Home | supporting local |
| Proximity | Close to Home | our town |
| Proximity | Close to Home | our city |
| Proximity | Close to Home | benefits my community |
| Proximity | Close to Home | nearby |
| Proximity | Close to Home | close by |
| Proximity | Close to Home | local community |
| Proximity | Close to Home | local cause |
| Proximity | Close to Home | help our area |
| Proximity | Close to Home | helping locally |
| Proximity | Close to Home | our region |
| Proximity | Close to Home | local initiative |

### Self-Gain

| Theme | Category | Keyword |
| --- | --- | --- |
| Self-Gain | Social Standing | social status |
| Self-Gain | Social Standing | social recognition |
| Self-Gain | Social Standing | identity expression |
| Self-Gain | Social Standing | social media |
| Self-Gain | Social Standing | share |
| Self-Gain | Social Standing | post |
| Self-Gain | Social Standing | like |
| Self-Gain | Social Standing | follow |
| Self-Gain | Social Standing | support me |
| Self-Gain | Social Standing | raise awareness |
| Self-Gain | Social Standing | get the word out |
| Self-Gain | Social Standing | trend |
| Self-Gain | Social Standing | viral |
| Self-Gain | Social Standing | identity |
| Self-Gain | Social Standing | brand |
| Self-Gain | Social Standing | followers |
| Self-Gain | Social Standing | praise |
| Self-Gain | Social Standing | reputation |
| Self-Gain | Social Standing | public image |
| Self-Gain | Social Standing | prestige |
| Self-Gain | Social Standing | kudos |
| Self-Gain | Social Standing | networking |
| Self-Gain | Social Standing | visibility |
| Self-Gain | Social Standing | social influence |
| Self-Gain | Social Standing | popularity |
| Self-Gain | Personal Development | personal growth |
| Self-Gain | Personal Development | learn |
| Self-Gain | Personal Development | develop |
| Self-Gain | Personal Development | improve myself |
| Self-Gain | Personal Development | challenge myself |
| Self-Gain | Personal Development | self-improvement |
| Self-Gain | Personal Development | gain experience |
| Self-Gain | Personal Development | skills |
| Self-Gain | Personal Development | new abilities |
| Self-Gain | Personal Development | transformative |
| Self-Gain | Personal Development | journey |
| Self-Gain | Personal Development | overcome |
| Self-Gain | Personal Development | personal journey |
| Self-Gain | Personal Development | self-discovery |
| Self-Gain | Personal Development | grow as a person |
| Self-Gain | Personal Development | better myself |
| Self-Gain | Personal Development | achieve my goals |
| Self-Gain | Personal Development | personal development |
| Self-Gain | Personal Development | self-fulfillment |
| Self-Gain | Personal Development | aspiration |
| Self-Gain | Seeking Experiences | fun |
| Self-Gain | Seeking Experiences | enjoy |
| Self-Gain | Seeking Experiences | experience |
| Self-Gain | Seeking Experiences | exciting |
| Self-Gain | Seeking Experiences | adventure |
| Self-Gain | Seeking Experiences | challenge |
| Self-Gain | Seeking Experiences | marathon |
| Self-Gain | Seeking Experiences | hike |
| Self-Gain | Seeking Experiences | skydiving |
| Self-Gain | Seeking Experiences | activity |
| Self-Gain | Seeking Experiences | event |
| Self-Gain | Seeking Experiences | participate in |
| Self-Gain | Seeking Experiences | enjoyment |
| Self-Gain | Seeking Experiences | recreational |
| Self-Gain | Seeking Experiences | pleasure |
| Self-Gain | Seeking Experiences | once in a lifetime |
| Self-Gain | Seeking Experiences | exciting opportunity |
| Self-Gain | Seeking Experiences | thrill |
| Self-Gain | Seeking Experiences | fun run |
| Self-Gain | Seeking Experiences | recreational activity |
| Self-Gain | Seeking Experiences | enjoyable experience |
| Self-Gain | Seeking Experiences | memorable |
| Self-Gain | Seeking Experiences | leisure |
| Self-Gain | Seeking Experiences | festive |
| Self-Gain | Seeking Experiences | celebration |

### Empowerment

| Theme | Category | Keyword |
| --- | --- | --- |
| Empowerment | Stewardship | control |
| Empowerment | Stewardship | direct impact |
| Empowerment | Stewardship | transparency |
| Empowerment | Stewardship | efficiency |
| Empowerment | Stewardship | effective altruism |
| Empowerment | Stewardship | manage |
| Empowerment | Stewardship | oversee |
| Empowerment | Stewardship | ensure |
| Empowerment | Stewardship | utilize resources effectively |
| Empowerment | Stewardship | stewardship |
| Empowerment | Stewardship | maximizing impact |
| Empowerment | Stewardship | evidence-based |
| Empowerment | Stewardship | make sure |
| Empowerment | Stewardship | responsibility |
| Empowerment | Stewardship | efficient use |
| Empowerment | Stewardship | accountability |
| Empowerment | Stewardship | ensure funds are used properly |
| Empowerment | Stewardship | allocate resources |
| Empowerment | Stewardship | direct involvement |
| Empowerment | Stewardship | trustworthy |
| Empowerment | Stewardship | responsible giving |
| Empowerment | Stewardship | efficient management |
| Empowerment | Stewardship | maximize effectiveness |
| Empowerment | Advocacy | advocate |
| Empowerment | Advocacy | raise awareness |
| Empowerment | Advocacy | speak out |
| Empowerment | Advocacy | voice |
| Empowerment | Advocacy | visibility |
| Empowerment | Advocacy | marginalized |
| Empowerment | Advocacy | social movement |
| Empowerment | Advocacy | make a difference |
| Empowerment | Advocacy | change |
| Empowerment | Advocacy | policy |
| Empowerment | Advocacy | activism |
| Empowerment | Advocacy | fight for |
| Empowerment | Advocacy | supporting cause |
| Empowerment | Advocacy | urge |
| Empowerment | Advocacy | petition |
| Empowerment | Advocacy | social justice |
| Empowerment | Advocacy | stand up for |
| Empowerment | Advocacy | protest |
| Empowerment | Advocacy | equality |
| Empowerment | Advocacy | human rights |
| Empowerment | Advocacy | advocacy |
| Empowerment | Advocacy | take action |
| Empowerment | Advocacy | speak up |

### Moral Purpose

| Theme | Category | Keyword |
| --- | --- | --- |
| Moral Purpose | Religious Affiliation | faith |
| Moral Purpose | Religious Affiliation | god |
| Moral Purpose | Religious Affiliation | church |
| Moral Purpose | Religious Affiliation | blessed |
| Moral Purpose | Religious Affiliation | prayer |
| Moral Purpose | Religious Affiliation | mission |
| Moral Purpose | Religious Affiliation | ministry |
| Moral Purpose | Religious Affiliation | religious |
| Moral Purpose | Religious Affiliation | bible |
| Moral Purpose | Religious Affiliation | spiritual |
| Moral Purpose | Religious Affiliation | divine |
| Moral Purpose | Religious Affiliation | grace |
| Moral Purpose | Religious Affiliation | christian |
| Moral Purpose | Religious Affiliation | islam |
| Moral Purpose | Religious Affiliation | muslim |
| Moral Purpose | Religious Affiliation | jewish |
| Moral Purpose | Religious Affiliation | hindu |
| Moral Purpose | Religious Affiliation | buddhist |
| Moral Purpose | Religious Affiliation | religion |
| Moral Purpose | Religious Affiliation | blessing |
| Moral Purpose | Religious Affiliation | holy |
| Moral Purpose | Religious Affiliation | worship |
| Moral Purpose | Religious Affiliation | belief |
| Moral Purpose | Religious Affiliation | devotion |
| Moral Purpose | Religious Affiliation | religious duty |
| Moral Purpose | Moral Obligation | duty |
| Moral Purpose | Moral Obligation | obligation |
| Moral Purpose | Moral Obligation | responsibility |
| Moral Purpose | Moral Obligation | ought to |
| Moral Purpose | Moral Obligation | moral |
| Moral Purpose | Moral Obligation | ethics |
| Moral Purpose | Moral Obligation | justice |
| Moral Purpose | Moral Obligation | empathy |
| Moral Purpose | Moral Obligation | altruism |
| Moral Purpose | Moral Obligation | help others |
| Moral Purpose | Moral Obligation | do the right thing |
| Moral Purpose | Moral Obligation | humanity |
| Moral Purpose | Moral Obligation | compassion |
| Moral Purpose | Moral Obligation | conscience |
| Moral Purpose | Moral Obligation | feel compelled |
| Moral Purpose | Moral Obligation | must help |
| Moral Purpose | Moral Obligation | moral duty |
| Moral Purpose | Moral Obligation | ethically |
| Moral Purpose | Moral Obligation | it's right |
| Moral Purpose | Moral Obligation | moral responsibility |
| Moral Purpose | Moral Obligation | obliged |
| Moral Purpose | Moral Obligation | commitment |
| Moral Purpose | Moral Obligation | moral imperative |
| Moral Purpose | Moral Obligation | sense of duty |

## 4. How the Scripts Work

### 4.1 The Search Script (justgiving_search.py)

1. **Setup**:  
   - Connects to the PostgreSQL database (`justgivingdb` by default).  
   - Ensures two tables exist:  
     - `query_state` for storing partial/resume data about ongoing queries.  
     - `crowdfunding` for storing the actual project details (in JSONB).  
2. **Queries the JustGiving API** using small letter or user-defined queries to find fundraising pages (crowdfunding projects).  
3. **Paginates** through results (up to a max page limit or total pages found).  
4. **Stores** each found page’s details by “short_name” as a unique key in `crowdfunding` table.  
5. **Resumes** seamlessly if interrupted, by checking `query_state`. If the script is re-run, it continues where it left off or starts fresh if needed.  

> **Important**: You must supply a valid **JustGiving App ID** (and possibly a personal access token if required) via environment variables or direct script configuration. The search script will only return **active** crowdfunding pages, since JustGiving’s API does not expose closed campaigns.

### 4.2 The Analysis Script (sentiment_analysis.py)

1. **Fetches** data from the `crowdfunding` table (using conditions like `activityCharityCreated=false` and `activityType=CharityAppeal`).  
2. **Cleans** each story (removing HTML, URLs, etc.).  
3. **Preprocesses** the text (tokenization, lowercasing, stopword removal).  
4. **Applies TF-IDF** vectorization to find relevant keywords based on a dictionary of themes and categories (e.g., “Proximity,” “Self-Gain,” etc.).  
5. **Aggregates** scores at both the category and theme level.  
6. **Normalizes** scores for clearer comparisons.  
7. **Generates** a variety of outputs:  
   - **Rankings** of themes and categories based on average TF-IDF weights.  
   - **Plots** (bar charts, heatmaps, etc.).  
   - **CSV** file containing the final dataset with normalized scores.  
   - **Text files** for top stories per category.  

---

## 5. Creating the PostgreSQL Database & Schema

### 5.1 Database Creation

1. **Install PostgreSQL** 15.10 on your system (if not already installed).
2. **Create a database**. For example, open a terminal and run:
   ```bash
   createdb justgivingdb
   ```
   or use `psql`:
   ```bash
   psql
   CREATE DATABASE justgivingdb;
   ```

3. **Create a user** (if you prefer a separate user from `postgres`):
   ```sql
   CREATE USER justgiving WITH PASSWORD 'some_secure_password';
   ```
   Then grant privileges:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE justgivingdb TO justgiving;
   ```

### 5.2 Creating Tables

Both scripts will automatically create tables if they don’t exist. However, you can pre-create them in `psql`:

```sql
\c justgivingdb;

-- Table to store partial query results (search script state)
CREATE TABLE IF NOT EXISTS query_state (
    query TEXT PRIMARY KEY,
    depth INT,
    current_page INT,
    fully_processed BOOLEAN DEFAULT FALSE
);

-- Table to store fetched crowdfunding project data
CREATE TABLE IF NOT EXISTS crowdfunding (
    short_name TEXT PRIMARY KEY,
    details JSONB
);
```

---

## 6. Installation

1. **Clone the repository** (or download the source):
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/p2p2c-crowdfunding.git
   cd p2p2c-crowdfunding
   ```
   *(Replace `<YOUR_USERNAME>` with your actual GitHub handle.)*

2. **Set environment variables** (preferred) for your DB credentials and JustGiving API key:
   ```bash
   export DB_HOST="localhost"
   export DB_NAME="justgivingdb"
   export DB_USER="justgiving"
   export DB_PASSWORD="some_secure_password"
   export JUSTGIVING_APP_ID="YOUR_JUSTGIVING_APP_ID"
   ```
   Alternatively, you can edit the scripts directly in `justgiving_search.py` or `sentiment_analysis.py` to hard-code credentials, but that is **less secure**.

3. **Install Python dependencies**.

   - For the **Search** script:
     ```bash
     cd search
     pip install -r requirements.txt
     cd ..
     ```

   - For the **Analysis** script:
     ```bash
     cd analysis
     pip install -r requirements.txt
     cd ..
     ```

---

## 7. Usage

### 7.1 Running the Search Script

```bash
cd search
python justgiving_search.py
```

This will:

1. Create (or update) the required tables in `justgivingdb`.
2. Start searching for active crowdfunding projects on JustGiving.
3. Store each project record in the `crowdfunding` table in JSONB format.

**Optional** arguments:
- `--reset-state`: Clears only the `query_state` table, allowing you to restart the search from scratch without losing the existing project data.

### 7.2 Running the Analysis Script

```bash
cd ../analysis
python sentiment_analysis.py
```

This will:

1. Read relevant crowdfunding data from the `crowdfunding` table.
2. Clean and preprocess the story text.
3. Apply a TF-IDF-based thematic/categorical analysis.
4. Output:
   - **theme_ranking.txt** and **category_ranking.txt**  
   - **plots/** folder containing bar charts and heatmaps  
   - **stories_with_theme_and_category_weights.csv** (final dataset)  
   - **top_stories_by_category** folder with top 2 stories per category

---

## 8. Notes & Limitations

- **Active Campaigns Only**: JustGiving’s API does not provide historical (closed) crowdfunding projects, so this workflow **cannot retrieve** data for ended/expired campaigns.
- **Customization**:  
  - You can modify the thematic dictionary in `sentiment_analysis.py` to suit your own taxonomy of themes, categories, and keywords.  
  - Adjust your PostgreSQL credentials or host as needed if you’re using a remote or containerized DB server.
- **Performance**:  
  - TF-IDF vectorization on large datasets might require more memory or performance tuning.  
  - For extremely large datasets, consider chunked loading or more advanced data pipeline strategies.

---

## 9. Contributing

1. Fork the repo and create a new branch for your feature or bugfix.
2. Submit a pull request with a clear explanation of changes.

---

## 10. License

This project is licensed under the [Apache License 2.0](LICENSE).

You are free to use, modify, and distribute this project in accordance with the terms of the license.

**Please note:** This source code and description was created with the assistance of ChatGPT o1. 

---

**Happy coding!** If you encounter any issues or have feature requests, please open an issue in the repository.