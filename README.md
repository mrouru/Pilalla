# PilallaBot
Twitter bot for selecting a random Finnish noun from a text file and adding " on pilalla" (is ruined) to it. I swore that I won't program anything in the summer, but as my friend Atte had this great idea I had to. Luckily many things were the same as in LyricsBot, so this took only a few hours to complete.
Inspiration comes from this Finnish rapper's DJ Ibusal song, "Pilalla", where everything is basically ruined: https://genius.com/Dj-ibusal-pilalla-lyrics

Bot running at https://twitter.com/kaikkipilalla on my Raspberry Pi.

The word list is from http://www.palomaki.info/apps/genetiivi/subs.txt (some words removed from the list, as it might produce problematic results)

# Features
  - Uses a text file to find a random noun and tweeting it "*noun* on pilalla"
  - Adds the noun to a pickle file, so it could not be used for second time
  
 # What did I do/learn?
  - More to love Python!
  - Little about Twitter API
  - Pickle files revised
  - Cron jobs revised
