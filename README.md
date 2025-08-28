
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

The analysis script uses a comprehensive dictionary of themes, categories, and keywords to categorize crowdfunding stories. The taxonomy is presented below as single-column tables per category. Each table's first row is the Theme name, the second row is the Category name, and the remaining rows list one Keyword per row.

### Proximity — Close to the Heart

| Value |
| --- |
| Proximity |
| Close to the Heart |
| personal trauma |
| loss |
| memory of |
| dedicated to |
| personal connection |
| close to my heart |
| affected by |
| family |
| friend |
| loved one |
| in memory |
| because of my experience with |
| after losing |
| after experiencing |
| significant to me |
| means a lot to me |
| in honour of |
| in loving memory |
| tribute to |
| in memory of |

### Proximity — Close to Home

| Value |
| --- |
| Proximity |
| Close to Home |
| local |
| community |
| neighborhood |
| near me |
| close to home |
| in my area |
| local school |
| local hospital |
| supporting local |
| our town |
| our city |
| benefits my community |
| nearby |
| close by |
| local community |
| local cause |
| help our area |
| helping locally |
| our region |
| local initiative |

### Self-Gain — Social Standing

| Value |
| --- |
| Self-Gain |
| Social Standing |
| social status |
| social recognition |
| identity expression |
| social media |
| share |
| post |
| like |
| follow |
| support me |
| raise awareness |
| get the word out |
| trend |
| viral |
| identity |
| brand |
| followers |
| praise |
| reputation |
| public image |
| prestige |
| kudos |
| networking |
| visibility |
| social influence |
| popularity |

### Self-Gain — Personal Development

| Value |
| --- |
| Self-Gain |
| Personal Development |
| personal growth |
| learn |
| develop |
| improve myself |
| challenge myself |
| self-improvement |
| gain experience |
| skills |
| new abilities |
| transformative |
| journey |
| overcome |
| personal journey |
| self-discovery |
| grow as a person |
| better myself |
| achieve my goals |
| personal development |
| self-fulfillment |
| aspiration |

### Self-Gain — Seeking Experiences

| Value |
| --- |
| Self-Gain |
| Seeking Experiences |
| fun |
| enjoy |
| experience |
| exciting |
| adventure |
| challenge |
| marathon |
| hike |
| skydiving |
| activity |
| event |
| participate in |
| enjoyment |
| recreational |
| pleasure |
| once in a lifetime |
| exciting opportunity |
| thrill |
| fun run |
| recreational activity |
| enjoyable experience |
| memorable |
| leisure |
| festive |
| celebration |

### Empowerment — Stewardship

| Value |
| --- |
| Empowerment |
| Stewardship |
| control |
| direct impact |
| transparency |
| efficiency |
| effective altruism |
| manage |
| oversee |
| ensure |
| utilize resources effectively |
| stewardship |
| maximizing impact |
| evidence-based |
| make sure |
| responsibility |
| efficient use |
| accountability |
| ensure funds are used properly |
| allocate resources |
| direct involvement |
| trustworthy |
| responsible giving |
| efficient management |
| maximize effectiveness |

### Empowerment — Advocacy

| Value |
| --- |
| Empowerment |
| Advocacy |
| advocate |
| raise awareness |
| speak out |
| voice |
| visibility |
| marginalized |
| social movement |
| make a difference |
| change |
| policy |
| activism |
| fight for |
| supporting cause |
| urge |
| petition |
| social justice |
| stand up for |
| protest |
| equality |
| human rights |
| advocacy |
| take action |
| speak up |

### Moral Purpose — Religious Affiliation

| Value |
| --- |
| Moral Purpose |
| Religious Affiliation |
| faith |
| god |
| church |
| blessed |
| prayer |
| mission |
| ministry |
| religious |
| bible |
| spiritual |
| divine |
| grace |
| christian |
| islam |
| muslim |
| jewish |
| hindu |
| buddhist |
| religion |
| blessing |
| holy |
| worship |
| belief |
| devotion |
| religious duty |

### Moral Purpose — Moral Obligation

| Value |
| --- |
| Moral Purpose |
| Moral Obligation |
| duty |
| obligation |
| responsibility |
| ought to |
| moral |
| ethics |
| justice |
| empathy |
| altruism |
| help others |
| do the right thing |
| humanity |
| compassion |
| conscience |
| feel compelled |
| must help |
| moral duty |
| ethically |
| it's right |
| moral responsibility |
| obliged |
| commitment |
| moral imperative |
| sense of duty |

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