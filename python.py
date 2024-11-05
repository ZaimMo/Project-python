import pandas as pd
import numpy as np
data = pd.read_csv("tiktok_dataset.csv")

# Display and examine the first ten rows of the dataframe
(data.head(10))

# Get summary info
(data.info())

# Get summary statistics
(data.describe())

# Check the unique values in the claim_status column and count the occurrences of each
claim_status_counts = data['claim_status'].value_counts()
# Display the counts of each claim status
print(claim_status_counts)

# Calculate the average view count for videos with 'claim' status
average_claim_views = data[data['claim_status'] == 'claim']['video_view_count'].mean()
# Display the average view count for "claim" status
print("Average view count for 'claim' status:", average_claim_views)

# Calculate the average view count for videos with "opinion" status
average_opinion_views = data[data['claim_status'] == 'opinion']['video_view_count'].mean()
# Display the average view count for "opinion" status
print("Average view count for 'opinion' status:", average_opinion_views)

# Group by 'claim_status' and 'author_ban_status' and count the number of videos in each group
ban_status_counts = data.groupby(['claim_status', 'author_ban_status']).size().reset_index(name='video_count')
# Display the resulting counts
print(ban_status_counts)

# Calculate the median video share count for each author ban status
median_share_counts = data.groupby('author_ban_status')['video_share_count'].median().reset_index()
# Display the median video share counts for each author ban status
print(median_share_counts)

# Group by author_ban_status and calculate count, mean, and median for specified columns
engagement_stats = data.groupby('author_ban_status').agg(
    video_view_count_count=('video_view_count', 'count'),
    video_view_count_mean=('video_view_count', 'mean'),
    video_view_count_median=('video_view_count', 'median'),
    video_like_count_count=('video_like_count', 'count'),
    video_like_count_mean=('video_like_count', 'mean'),
    video_like_count_median=('video_like_count', 'median'),
    video_share_count_count=('video_share_count', 'count'),
    video_share_count_mean=('video_share_count', 'mean'),
    video_share_count_median=('video_share_count', 'median')
).reset_index()
# Display the engagement statistics for each author ban status
print(engagement_stats)

# Create a likes_per_view column
# Create a comments_per_view column
# Create a shares_per_view column
# Create new columns for engagement rates
data['likes_per_view'] = data['video_like_count'] / data['video_view_count']
data['comments_per_view'] = data['video_comment_count'] / data['video_view_count']
data['shares_per_view'] = data['video_share_count'] / data['video_view_count']

# Display the updated DataFrame with the new engagement rate columns
print(data[['author_ban_status', 'likes_per_view', 'comments_per_view', 'shares_per_view']].head())

# Group by 'claim_status' and 'author_ban_status', then aggregate the new engagement columns
engagement_summary = data.groupby(['claim_status', 'author_ban_status']).agg(
    count_likes_per_view=('likes_per_view', 'count'),
    mean_likes_per_view=('likes_per_view', 'mean'),
    median_likes_per_view=('likes_per_view', 'median'),
    count_comments_per_view=('comments_per_view', 'count'),
    mean_comments_per_view=('comments_per_view', 'mean'),
    median_comments_per_view=('comments_per_view', 'median'),
    count_shares_per_view=('shares_per_view', 'count'),
    mean_shares_per_view=('shares_per_view', 'mean'),
    median_shares_per_view=('shares_per_view', 'median')
).reset_index()

# Display the summary DataFrame
print(engagement_summary)


