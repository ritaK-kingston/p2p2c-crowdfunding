# p2p2c-crowdfunding
Peer to Peer to Charity Crowdfunding 
# JustGiving Data Collection and Sentiment Analysis

This project contains two main components:

1. **Search**: A script that queries the [JustGiving API](https://api.justgiving.com) to find active crowdfunding pages, then stores the data in a PostgreSQL database.
2. **Analysis**: A sentiment/rubric analysis script that reads the stored page data from PostgreSQL, applies a thematic/categorical analysis using TF-IDF, and outputs reports, charts, and top stories for each category.

## Project Structure
- **search/**  
  Contains the script (`justgiving_search.py`) to pull data from JustGiving.

- **analysis/**  
  Contains the script (`sentiment_analysis.py`) to perform the TF-IDF-based analysis.

## Requirements

- Python 3.9+ (tested; older versions may work but not guaranteed)
- PostgreSQL (tested with version 13+; older versions may also work)
- A valid [JustGiving API key](https://api.justgiving.com/docs)

## Setup Instructions

1. **Clone this repository** (or download the ZIP).

   ```bash
   git clone https://github.com/your-username/justgiving-project.git
   cd justgiving-project
