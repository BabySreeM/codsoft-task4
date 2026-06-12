# RecoAI – Recommendation System

This project is a simple AI-based recommendation system built in Python. It suggests **movies**, **books**, or **products** to the user based on their ratings and preferences using two classic recommendation approaches.

## Features

- Three categories of items:
  - 🎬 Movies (58 items)
  - 📚 Books (50 items)
  - 🛒 Products (50 items)
- Two recommendation algorithms:
  - **Content-Based Filtering**
  - **Collaborative Filtering**
- Command-line interface for:
  - Selecting a category
  - Rating items from 1–5
  - Choosing the algorithm (`content` or `collaborative`)
  - Viewing top recommendations with scores and reasons

## Tech Stack

- **Language:** Python 3
- **Libraries Used:**  
  - Standard library only (`math`, `typing`)
- **Concepts Used:**
  - Cosine similarity
  - Tag-based item vectors
  - User–item rating profiles

## How It Works

### 1. Content-Based Filtering

- Each item (movie/book/product) has a list of tags.
- All unique tags form a feature vector space.
- A **user profile vector** is created by combining the tag vectors of items the user rated, weighted by their ratings.
- For each unrated item:
  - A tag vector is created.
  - Cosine similarity is computed between the item vector and the user profile.
  - Items are ranked based on similarity.
  - A short textual reason is shown (for example: `matches Sci-Fi, Drama`).

### 2. Collaborative Filtering

- A set of **synthetic users** with predefined ratings is used.
- The current user’s ratings are compared with each synthetic user using cosine similarity.
- Only positively similar users contribute to predictions.
- For each unrated item:
  - A predicted score is calculated from similar users’ ratings.
  - Scores are normalized to a percentage (0–100%).
  - A reason like `85% match with users like you` is displayed.

## Datasets

The project includes built-in datasets:

- **Movies:** Popular and classic films with tags like Action, Drama, Sci-Fi, etc.
- **Books:** Fiction, non-fiction, classics, fantasy, sci-fi, etc.
- **Products:** Common consumer products (electronics, fitness, home, etc.).

Each item includes:
- `id`
- `title`
- `tags`
- `year`
- `emoji`
- `subtitle` (director/author/brand)
- `image` (placeholder)

## Usage

1. Make sure Python 3 is installed.
2. Run the script:

```bash
python recoai.py
```

3. Follow the prompts:
   - Choose a category: `movies`, `books`, or `products`
   - Rate items from 1 to 5 (press Enter to skip any item)
   - Choose algorithm: `content` or `collaborative`
   - View the recommended items, along with scores and reasons.

## Example Flow

```text
RecoAI (Python-only, full datasets)
===================================
Categories: movies, books, products
Choose category: movies

Enter ratings 1–5 (or blank to skip):
Rate Inception (2010) [1-5, blank to skip]: 5
Rate Interstellar (2014) [1-5, blank to skip]: 4
...

Algorithm (content/collaborative): content

Recommendations:
#1 🦇 The Dark Knight (2008) [Action, Crime, Drama]
   Score: 92.3%  |  Reason: matches Action, Drama
```

## Learning Objectives

This project demonstrates:

- Implementation of **content-based** and **collaborative** filtering from scratch.
- Use of cosine similarity for comparing user preferences and items.
- Working with structured datasets and user interaction via CLI.
- Building an AI-powered recommendation system without external ML libraries.

## Credits

- Developed as part of an **Artificial Intelligence Internship** task.
- All datasets are synthetic and used for educational purposes.
