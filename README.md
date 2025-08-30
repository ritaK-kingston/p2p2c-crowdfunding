
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

## 3. Sentiment Analysis Themes, Categories and Keywords

The analysis script uses a comprehensive dictionary of themes, categories, and keywords to categorize crowdfunding stories. The taxonomy is presented below as tables per theme. Each row shows the Category and a single Keyword.

### Proximity

| Category | Keyword |
| --- | --- |
| Close to the Heart | family |
| Close to the Heart | friend |
| Close to the Heart | loved one |
| Close to the Heart | loss |
| Close to the Heart | memory of |
| Close to the Heart | in memory |
| Close to the Heart | in loving memory |
| Close to the Heart | personal trauma |
| Close to the Heart | affected by |
| Close to the Heart | close to my heart |
| Close to the Heart | significant to me |
| Close to the Heart | means a lot to me |
| Close to the Heart | dedicated to |
| Close to the Heart | tribute to |
| Close to the Heart | because of my experience with |
| Close to the Heart | after losing |
| Close to the Heart | after experiencing |
| Close to the Heart | in honour of |
| Close to the Heart | personal connection |
| Close to the Heart | first-hand |
| Close to the Heart | directly touched |
| Close to the Heart | personal experience |
| Close to the Heart | my partner |
| Close to the Heart | my child |
| Close to the Heart | my parent |
| Close to Home | local |
| Close to Home | community |
| Close to Home | local community |
| Close to Home | neighborhood |
| Close to Home | nearby |
| Close to Home | close to home |
| Close to Home | in my area |
| Close to Home | our town |
| Close to Home | our city |
| Close to Home | our region |
| Close to Home | local school |
| Close to Home | local hospital |
| Close to Home | local cause |
| Close to Home | local initiative |
| Close to Home | supporting local |
| Close to Home | help our area |
| Close to Home | helping locally |
| Close to Home | benefits my community |
| Close to Home | near me |
| Close to Home | close by |
| Close to Home | my local area |
| Close to Home | my neighborhood |
| Close to Home | my community |
| Close to Home | my town |
| Close to Home | my city |

### Self-Gain

| Category | Keyword |
| --- | --- |
| Social Standing | identity |
| Social Standing | social media |
| Social Standing | share |
| Social Standing | post |
| Social Standing | like |
| Social Standing | follow |
| Social Standing | followers |
| Social Standing | trend |
| Social Standing | viral |
| Social Standing | brand |
| Social Standing | reputation |
| Social Standing | public image |
| Social Standing | social status |
| Social Standing | social recognition |
| Social Standing | identity expression |
| Social Standing | visibility |
| Social Standing | social influence |
| Social Standing | popularity |
| Social Standing | praise |
| Social Standing | kudos |
| Social Standing | networking |
| Social Standing | prestige |
| Social Standing | support me |
| Social Standing | get the word out |
| Social Standing | friends |
| Personal Development | learn |
| Personal Development | journey |
| Personal Development | skills |
| Personal Development | develop |
| Personal Development | overcome |
| Personal Development | transformative |
| Personal Development | personal development |
| Personal Development | personal journey |
| Personal Development | aspiration |
| Personal Development | gain experience |
| Personal Development | personal growth |
| Personal Development | self-improvement |
| Personal Development | challenge myself |
| Personal Development | comfort zone |
| Personal Development | dreams |
| Personal Development | fulfillment |
| Personal Development | joy |
| Personal Development | determined |
| Personal Development | growth |
| Personal Development | limits |
| Personal Development | healing |
| Personal Development | processing loss |
| Personal Development | new competencies |
| Personal Development | physicality |
| Personal Development | personal goal achievement |
| Seeking Experiences | challenge |
| Seeking Experiences | event |
| Seeking Experiences | experience |
| Seeking Experiences | fun |
| Seeking Experiences | enjoy |
| Seeking Experiences | activity |
| Seeking Experiences | marathon |
| Seeking Experiences | festive |
| Seeking Experiences | exciting |
| Seeking Experiences | adventure |
| Seeking Experiences | hike |
| Seeking Experiences | skydiving |
| Seeking Experiences | participate in |
| Seeking Experiences | enjoyment |
| Seeking Experiences | recreational |
| Seeking Experiences | pleasure |
| Seeking Experiences | once in a lifetime |
| Seeking Experiences | exciting opportunity |
| Seeking Experiences | thrill |
| Seeking Experiences | fun run |
| Seeking Experiences | recreational activity |
| Seeking Experiences | enjoyable experience |
| Seeking Experiences | memorable |
| Seeking Experiences | leisure |
| Seeking Experiences | celebration |

### Empowerment

| Category | Keyword |
| --- | --- |
| Stewardship | ensure |
| Stewardship | make sure |
| Stewardship | control |
| Stewardship | manage |
| Stewardship | oversee |
| Stewardship | responsibility |
| Stewardship | direct impact |
| Stewardship | transparency |
| Stewardship | efficiency |
| Stewardship | effective altruism |
| Stewardship | utilize resources effectively |
| Stewardship | stewardship |
| Stewardship | maximizing impact |
| Stewardship | evidence-based |
| Stewardship | efficient use |
| Stewardship | accountability |
| Stewardship | ensure funds are used properly |
| Stewardship | allocate resources |
| Stewardship | direct involvement |
| Stewardship | trustworthy |
| Stewardship | responsible giving |
| Stewardship | efficient management |
| Stewardship | maximize effectiveness |
| Stewardship | personally overseeing |
| Stewardship | maximum impact |
| Advocacy | advocate |
| Advocacy | raise awareness |
| Advocacy | speak out |
| Advocacy | voice |
| Advocacy | visibility |
| Advocacy | marginalized |
| Advocacy | social movement |
| Advocacy | make a difference |
| Advocacy | reform |
| Advocacy | policy |
| Advocacy | activism |
| Advocacy | fight for |
| Advocacy | supporting cause |
| Advocacy | urge |
| Advocacy | petition |
| Advocacy | social justice |
| Advocacy | stand up for |
| Advocacy | protest |
| Advocacy | equality |
| Advocacy | human rights |
| Advocacy | advocacy |
| Advocacy | take action |
| Advocacy | speak up |
| Advocacy | campaign for |
| Advocacy | educate others |

### Moral Purpose

| Category | Keyword |
| --- | --- |
| Altruism and Empathy | selfless |
| Altruism and Empathy | selflessness |
| Altruism and Empathy | for their sake |
| Altruism and Empathy | no recognition |
| Altruism and Empathy | anonymous giving |
| Altruism and Empathy | pure giving |
| Altruism and Empathy | kindness |
| Altruism and Empathy | act of kindness |
| Altruism and Empathy | be kind |
| Altruism and Empathy | empathic concern |
| Altruism and Empathy | care for others |
| Altruism and Empathy | caring for others |
| Altruism and Empathy | lend a hand |
| Altruism and Empathy | support those in need |
| Altruism and Empathy | relieve suffering |
| Altruism and Empathy | ease their pain |
| Altruism and Empathy | save lives |
| Altruism and Empathy | change lives |
| Altruism and Empathy | better lives |
| Altruism and Empathy | give hope |
| Altruism and Empathy | bring hope |
| Altruism and Empathy | stand with them |
| Altruism and Empathy | stand together |
| Moral Obligation | duty |
| Moral Obligation | obligation |
| Moral Obligation | obliged |
| Moral Obligation | moral |
| Moral Obligation | ethics |
| Moral Obligation | justice |
| Moral Obligation | compassionate |
| Moral Obligation | altruism |
| Moral Obligation | help others |
| Moral Obligation | do the right thing |
| Moral Obligation | humanity |
| Moral Obligation | compassion |
| Moral Obligation | conscience |
| Moral Obligation | feel compelled |
| Moral Obligation | moral duty |
| Moral Obligation | ethically |
| Moral Obligation | moral responsibility |
| Moral Obligation | obliged |
| Moral Obligation | commitment |
| Moral Obligation | moral imperative |
| Moral Obligation | sense of duty |
| Moral Obligation | faith-based duty |
| Moral Obligation | guided by faith |

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
3. Apply a TF-IDF-based thematic/categorical analysis using the following keyword taxonomy:

#### **Theme 1: Proximity**
- **Close to the Heart**: family, friend, loved one, loss, memory of, in memory, in loving memory, personal trauma, affected by, close to my heart, significant to me, means a lot to me, dedicated to, tribute to, because of my experience with, after losing, after experiencing, in honour of, personal connection, first-hand, directly touched, personal experience, my partner, my child, my parent
- **Close to Home**: local, community, local community, neighborhood, nearby, close to home, in my area, our town, our city, our region, local school, local hospital, local cause, local initiative, supporting local, help our area, helping locally, benefits my community, near me, close by, my local area, my neighborhood, my community, my town, my city

#### **Theme 2: Self-Gain**
- **Social Standing**: identity, social media, share, post, like, follow, followers, trend, viral, brand, reputation, public image, social status, social recognition, identity expression, visibility, social influence, popularity, praise, kudos, networking, prestige, support me, get the word out, friends
- **Personal Development**: learn, journey, skills, develop, overcome, transformative, personal development, personal journey, aspiration, gain experience, personal growth, self-improvement, challenge myself, comfort zone, dreams, fulfillment, joy, determined, growth, limits, healing, processing loss, new competencies, physicality, personal goal achievement
- **Seeking Experiences**: challenge, event, experience, fun, enjoy, activity, marathon, festive, exciting, adventure, hike, skydiving, participate in, enjoyment, recreational, pleasure, once in a lifetime, exciting opportunity, thrill, fun run, recreational activity, enjoyable experience, memorable, leisure, celebration

#### **Theme 3: Empowerment**
- **Stewardship**: ensure, make sure, control, manage, oversee, responsibility, direct impact, transparency, efficiency, effective altruism, utilize resources effectively, stewardship, maximizing impact, evidence-based, efficient use, accountability, ensure funds are used properly, allocate resources, direct involvement, trustworthy, responsible giving, efficient management, maximize effectiveness, personally overseeing, maximum impact
- **Advocacy**: advocate, raise awareness, speak out, voice, visibility, marginalized, social movement, make a difference, reform, policy, activism, fight for, supporting cause, urge, petition, social justice, stand up for, protest, equality, human rights, advocacy, take action, speak up, campaign for, educate others

#### **Theme 4: Moral Purpose**
- **Altruism and Empathy**: selfless, selflessness, for their sake, no recognition, anonymous giving, pure giving, kindness, act of kindness, be kind, empathic concern, care for others, caring for others, lend a hand, support those in need, relieve suffering, ease their pain, save lives, change lives, better lives, give hope, bring hope, stand with them, stand together
- **Moral Obligation**: duty, obligation, obliged, moral, ethics, justice, compassionate, altruism, help others, do the right thing, humanity, compassion, conscience, feel compelled, moral duty, ethically, moral responsibility, commitment, moral imperative, sense of duty, faith-based duty, guided by faith

4. **Output**:
   - **theme_ranking.txt** and **category_ranking.txt** - Detailed rankings of themes and categories
   - **keyword_contributions.txt** - Analysis showing which keywords drive the weights in each category
   - **plots/** folder containing bar charts and heatmaps  
   - **stories_with_theme_and_category_weights.csv** (final dataset)  
   - **top_stories_by_category** folder with top 2 stories per category

#### **Keyword Contribution Analysis**
The script now includes a comprehensive keyword contribution analysis that shows:
- Which specific keywords contribute most to each category's weight
- The percentage contribution of each keyword within its category
- Whether categories are driven by a few dominant keywords or distributed more evenly
- This helps identify if the thematic analysis is balanced or overly reliant on specific terms

---

## 8. Notes & Limitations

- **Active Campaigns Only**: JustGiving’s API does not provide historical (closed) crowdfunding projects, so this workflow **cannot retrieve** data for ended/expired campaigns.
- **Customization**:  
  - You can modify the thematic dictionary in `sentiment_analysis.py` to suit your own taxonomy of themes, categories, and keywords.  
  - Adjust your PostgreSQL credentials or host as needed if you’re using a remote or containerized DB server.
- **Performance**:  
  - TF-IDF vectorization on large datasets might require more memory or performance tuning.  
  - For extremely large datasets, consider chunked loading or more advanced data pipeline strategies.
- **Keyword Analysis**:  
  - The keyword contribution analysis provides insights into which terms drive each category's weight.
  - Categories with highly concentrated keyword distributions may need refinement for more balanced analysis.

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