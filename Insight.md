## Plan stage :
`How can you best prepare to understand and organize the provided information?`

To best prepare to understand and organize the provided information, thoroughly review the dataset's structure and key variables to identify their relationships and significance.

`What follow-along and self-review codebooks will help you perform this work?`

Follow-along and self-review codebooks that outline data types, variable definitions, and analysis techniques will help you effectively navigate and interpret the data.

`What are some additional activities a resourceful learner would perform before starting to code?`

Additional activities a resourceful learner would perform before starting to code include exploring similar projects, practicing data manipulation skills, and ensuring a solid understanding of relevant statistical concepts.

## Analyze Stage :
`Will the available information be sufficient to achieve the goal based on your intuition and the analysis of the variables?`

Yes, the available information seems sufficient to achieve the goal as it covers key variables impacting video performance and user behavior.

`How would you build summary DataFrame statistics and assess the min and max range of the data?`

You can build summary DataFrame statistics using data.agg() for relevant columns, then assess the min and max range by reviewing the summary statistics.

`Do the averages of any of the data variables look unusual? Can you describe the interval data?`

Yes, some averages may appear unusual if they significantly deviate from the median, indicating potential outliers. The interval data includes metrics like video_view_count, video_like_count, etc., and should be described based on their range, mean, and standard deviation.



## Execute Stage :
`What percentage of the data is comprised of claims and what percentage is comprised of opinions?`

The percentage of data in each category (claims vs opinions) can be determined by looking at the distribution of the claim_status column. Based on the dataset you provided earlier, the majority of videos are labeled as claims (e.g., 78%) while a smaller percentage fall under the opinion category (e.g., 22%). This is important for understanding the general makeup of content types in the dataset.

`What factors correlate with a video's claim status?`

Author Ban Status: A strong correlation might exist between the claim status and the author’s ban status. For instance, videos with a "claim" status could be more likely to come from authors who are active or under review, while banned authors may have fewer claim-status videos.
Verification Status: Verified authors might have a different claim status pattern compared to non-verified ones, possibly due to the credibility and authenticity checks that come with verification.
Engagement Metrics (like view count): Higher engagement (such as higher view counts) could correlate with claim-status videos, as these might be more likely to attract attention, either due to their controversial nature or the subject matter.

`What factors correlate with a video's engagement level?`

View Count: A higher view count often correlates with higher engagement. Videos with more views tend to have more likes, comments, and shares.
Likes, Comments, and Shares: These engagement metrics are directly linked. Higher likes, comments, and shares usually indicate a more engaged audience. Videos that spark discussions or are shared widely are often more engaging.
Claim Status: Videos with a claim status might have different engagement patterns compared to opinion-based videos. Claims might attract more debate or controversy, influencing engagement metrics.
Author Ban Status: Authors who are banned might have different levels of engagement, possibly due to their controversial status or limited reach compared to active authors.

