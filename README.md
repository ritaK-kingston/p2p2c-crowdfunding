
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

## 11. Keyword Contribution Tables

The following tables are generated from `analysis/keyword_contributions.txt`. They show, for each Category, the keyword-level contributions and their percentage share within the Category.

### Close to the Heart

| Keyword | Contribution | % of Category |
| --- | ---:| ---:|
| family | 1122.0747 | 73.61% |
| loss | 172.1247 | 11.29% |
| friend | 166.9906 | 10.95% |
| loved one | 46.6441 | 3.06% |
| personal experience | 11.6717 | 0.77% |
| personal connection | 4.0680 | 0.27% |
| directly touched | 0.7714 | 0.05% |
| significant to me | 0.0000 | 0.00% |
| affected by | 0.0000 | 0.00% |
| my parent | 0.0000 | 0.00% |
| memory of | 0.0000 | 0.00% |
| in loving memory | 0.0000 | 0.00% |
| after experiencing | 0.0000 | 0.00% |
| close to my heart | 0.0000 | 0.00% |
| my child | 0.0000 | 0.00% |
| because of my experience with | 0.0000 | 0.00% |
| means a lot to me | 0.0000 | 0.00% |
| first-hand | 0.0000 | 0.00% |
| tribute to | 0.0000 | 0.00% |
| after losing | 0.0000 | 0.00% |
| in memory | 0.0000 | 0.00% |
| dedicated to | 0.0000 | 0.00% |
| my partner | 0.0000 | 0.00% |
| personal trauma | 0.0000 | 0.00% |
| in honour of | 0.0000 | 0.00% |

### Close to Home

| Keyword | Contribution | % of Category |
| --- | ---:| ---:|
| community | 1200.9563 | 59.19% |
| local | 670.0934 | 33.02% |
| local community | 89.8661 | 4.43% |
| supporting local | 21.4111 | 1.06% |
| nearby | 14.4313 | 0.71% |
| neighborhood | 12.1724 | 0.60% |
| local hospital | 11.0015 | 0.54% |
| local school | 4.3726 | 0.22% |
| local cause | 2.7743 | 0.14% |
| local initiative | 2.0245 | 0.10% |
| close by | 0.0000 | 0.00% |
| help our area | 0.0000 | 0.00% |
| my neighborhood | 0.0000 | 0.00% |
| my community | 0.0000 | 0.00% |
| helping locally | 0.0000 | 0.00% |
| in my area | 0.0000 | 0.00% |
| my city | 0.0000 | 0.00% |
| near me | 0.0000 | 0.00% |
| our town | 0.0000 | 0.00% |
| our region | 0.0000 | 0.00% |
| my local area | 0.0000 | 0.00% |
| our city | 0.0000 | 0.00% |
| benefits my community | 0.0000 | 0.00% |
| my town | 0.0000 | 0.00% |
| close to home | 0.0000 | 0.00% |

### Social Standing

| Keyword | Contribution | % of Category |
| --- | ---:| ---:|
| like | 1144.7775 | 40.34% |
| friends | 552.8840 | 19.48% |
| share | 401.9820 | 14.17% |
| identity | 315.0816 | 11.10% |
| follow | 117.7026 | 4.15% |
| post | 113.8666 | 4.01% |
| social media | 98.9640 | 3.49% |
| brand | 41.1902 | 1.45% |
| praise | 8.2765 | 0.29% |
| networking | 7.0983 | 0.25% |
| followers | 6.4056 | 0.23% |
| viral | 6.0068 | 0.21% |
| reputation | 5.9809 | 0.21% |
| visibility | 5.7724 | 0.20% |
| trend | 2.8048 | 0.10% |
| prestige | 2.5974 | 0.09% |
| popularity | 2.1628 | 0.08% |
| identity expression | 1.6596 | 0.06% |
| social status | 1.4623 | 0.05% |
| kudos | 1.0000 | 0.04% |
| social influence | 0.0000 | 0.00% |
| public image | 0.0000 | 0.00% |
| social recognition | 0.0000 | 0.00% |
| get the word out | 0.0000 | 0.00% |
| support me | 0.0000 | 0.00% |

### Personal Development

| Keyword | Contribution | % of Category |
| --- | ---:| ---:|
| learn | 201.8220 | 18.24% |
| skills | 187.3744 | 16.93% |
| journey | 184.3733 | 16.66% |
| develop | 115.4633 | 10.43% |
| joy | 106.8362 | 9.66% |
| determined | 73.3550 | 6.63% |
| overcome | 55.6843 | 5.03% |
| dreams | 47.5276 | 4.30% |
| growth | 35.0851 | 3.17% |
| healing | 29.9895 | 2.71% |
| limits | 25.7540 | 2.33% |
| transformative | 16.2777 | 1.47% |
| comfort zone | 14.7245 | 1.33% |
| personal development | 3.3886 | 0.31% |
| fulfillment | 2.3788 | 0.21% |
| personal journey | 2.2165 | 0.20% |
| aspiration | 1.7976 | 0.16% |
| gain experience | 1.1485 | 0.10% |
| personal growth | 0.8391 | 0.08% |
| processing loss | 0.4709 | 0.04% |
| challenge myself | 0.0000 | 0.00% |
| self-improvement | 0.0000 | 0.00% |
| physicality | 0.0000 | 0.00% |
| personal goal achievement | 0.0000 | 0.00% |
| new competencies | 0.0000 | 0.00% |

### Seeking Experiences

| Keyword | Contribution | % of Category |
| --- | ---:| ---:|
| challenge | 766.9622 | 32.87% |
| event | 394.4266 | 16.90% |
| experience | 266.3748 | 11.42% |
| fun | 245.0585 | 10.50% |
| enjoy | 172.6691 | 7.40% |
| activity | 85.7914 | 3.68% |
| festive | 84.3246 | 3.61% |
| marathon | 83.8230 | 3.59% |
| exciting | 55.2520 | 2.37% |
| celebration | 41.6725 | 1.79% |
| pleasure | 33.2758 | 1.43% |
| adventure | 31.6170 | 1.35% |
| hike | 21.4099 | 0.92% |
| leisure | 12.2634 | 0.53% |
| recreational | 10.9433 | 0.47% |
| enjoyment | 8.2449 | 0.35% |
| memorable | 7.8472 | 0.34% |
| fun run | 4.8223 | 0.21% |
| exciting opportunity | 2.9225 | 0.13% |
| skydiving | 1.7119 | 0.07% |
| thrill | 1.6419 | 0.07% |
| recreational activity | 0.4042 | 0.02% |
| participate in | 0.0000 | 0.00% |
| once in a lifetime | 0.0000 | 0.00% |
| enjoyable experience | 0.0000 | 0.00% |

### Stewardship

| Keyword | Contribution | % of Category |
| --- | ---:| ---:|
| ensure | 435.3811 | 55.07% |
| make sure | 164.4619 | 20.80% |
| control | 59.8499 | 7.57% |
| manage | 50.0695 | 6.33% |
| responsibility | 48.5360 | 6.14% |
| oversee | 7.7467 | 0.98% |
| direct impact | 6.3044 | 0.80% |
| transparency | 5.0207 | 0.64% |
| trustworthy | 3.1356 | 0.40% |
| allocate resources | 2.8795 | 0.36% |
| efficiency | 2.5672 | 0.32% |
| stewardship | 2.3153 | 0.29% |
| accountability | 1.3871 | 0.18% |
| maximum impact | 0.9651 | 0.12% |
| efficient management | 0.0000 | 0.00% |
| direct involvement | 0.0000 | 0.00% |
| effective altruism | 0.0000 | 0.00% |
| personally overseeing | 0.0000 | 0.00% |
| utilize resources effectively | 0.0000 | 0.00% |
| responsible giving | 0.0000 | 0.00% |
| maximize effectiveness | 0.0000 | 0.00% |
| ensure funds are used properly | 0.0000 | 0.00% |
| maximizing impact | 0.0000 | 0.00% |
| evidence-based | 0.0000 | 0.00% |
| efficient use | 0.0000 | 0.00% |

### Advocacy

| Keyword | Contribution | % of Category |
| --- | ---:| ---:|
| raise awareness | 220.3063 | 37.75% |
| policy | 88.0214 | 15.08% |
| voice | 48.5761 | 8.32% |
| advocacy | 40.4141 | 6.93% |
| equality | 32.5197 | 5.57% |
| advocate | 30.4755 | 5.22% |
| human rights | 25.6932 | 4.40% |
| urge | 23.9690 | 4.11% |
| take action | 16.2814 | 2.79% |
| reform | 13.3183 | 2.28% |
| social justice | 11.3549 | 1.95% |
| supporting cause | 11.1250 | 1.91% |
| visibility | 5.7724 | 0.99% |
| activism | 4.2091 | 0.72% |
| marginalized | 4.0075 | 0.69% |
| protest | 3.4013 | 0.58% |
| petition | 1.7198 | 0.29% |
| educate others | 1.4090 | 0.24% |
| social movement | 0.9651 | 0.17% |
| fight for | 0.0000 | 0.00% |
| speak up | 0.0000 | 0.00% |
| speak out | 0.0000 | 0.00% |
| stand up for | 0.0000 | 0.00% |
| make a difference | 0.0000 | 0.00% |
| campaign for | 0.0000 | 0.00% |

### Altruism and Empathy

| Keyword | Contribution | % of Category |
| --- | ---:| ---:|
| save lives | 174.7705 | 38.69% |
| change lives | 101.2748 | 22.42% |
| kindness | 77.5274 | 17.16% |
| give hope | 31.7277 | 7.02% |
| selfless | 24.5356 | 5.43% |
| bring hope | 19.9420 | 4.41% |
| stand together | 7.6747 | 1.70% |
| better lives | 4.8404 | 1.07% |
| selflessness | 4.7221 | 1.05% |
| relieve suffering | 4.7075 | 1.04% |
| ease their pain | 0.0000 | 0.00% |
| lend a hand | 0.0000 | 0.00% |
| act of kindness | 0.0000 | 0.00% |
| stand with them | 0.0000 | 0.00% |
| care for others | 0.0000 | 0.00% |
| for their sake | 0.0000 | 0.00% |
| support those in need | 0.0000 | 0.00% |
| no recognition | 0.0000 | 0.00% |
| caring for others | 0.0000 | 0.00% |
| pure giving | 0.0000 | 0.00% |
| anonymous giving | 0.0000 | 0.00% |
| be kind | 0.0000 | 0.00% |
| empathic concern | 0.0000 | 0.00% |

### Moral Obligation

| Keyword | Contribution | % of Category |
| --- | ---:| ---:|
| humanity | 80.9857 | 18.69% |
| help others | 65.3039 | 15.07% |
| commitment | 60.3806 | 13.94% |
| justice | 56.1240 | 12.95% |
| compassion | 55.8916 | 12.90% |
| compassionate | 38.5734 | 8.90% |
| duty | 37.5465 | 8.67% |
| moral | 15.4490 | 3.57% |
| obligation | 7.0826 | 1.63% |
| feel compelled | 4.7639 | 1.10% |
| obliged | 4.4387 | 1.02% |
| ethics | 3.2301 | 0.75% |
| ethically | 3.0529 | 0.70% |
| moral responsibility | 0.4624 | 0.11% |
| faith-based duty | 0.0000 | 0.00% |
| moral imperative | 0.0000 | 0.00% |
| altruism | 0.0000 | 0.00% |
| do the right thing | 0.0000 | 0.00% |
| sense of duty | 0.0000 | 0.00% |
| guided by faith | 0.0000 | 0.00% |
| conscience | 0.0000 | 0.00% |
| moral duty | 0.0000 | 0.00% |