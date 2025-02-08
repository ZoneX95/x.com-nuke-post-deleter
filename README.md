# x.com-nuke-post-deleter
A Python script to delete all tweets from a specified X (Twitter) account utilizing multithreading for faster operation.

## Features

- **Multithreading**: Deletes tweets at a rate of 30-50 per second.
- **Python 3 Compatibility**: Uses Python 3 syntax and libraries.
- **Rate Limit Consideration**: Small delay to mitigate hitting API rate limits.

## Requirements

- Python 3.13+
- [Tweepy](https://github.com/tweepy/tweepy) (`pip install tweepy`)

## Usage

1. **Set Up API Credentials**:
   - Replace the placeholder API keys in the script with your own Twitter Developer API credentials. Remember, for security, it's better to use environment variables or a separate configuration file.

2. **Run the Script**:
   - Execute the script from your command line:
     ```bash
     python x.com_nuke.py
     ```

3. **Confirmation Prompt**:
   - The script will ask for confirmation before deleting any tweets. Type 'yes' to proceed.

**Note**: You might need to manually load more tweets on the X web interface if the script stops prematurely due to how X loads content.
