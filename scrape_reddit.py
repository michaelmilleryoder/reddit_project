import praw
import pdb

""" Script to scrape reddit data """

def init():
    credfile = 'reddit_cred.txt'
    with open(credfile) as f:
        lines = f.read().splitlines()
    client_id = lines[0]
    client_secret = lines[1]
    user_agent = lines[2]

    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent)

    return reddit

def scrape_subreddit(reddit, name):

    subs = []
    for submission in reddit.subreddit("MURICA").hot(limit=None):
        #print(submission.title)
        subs.append(submission)
    
    print(len(subs))

def main():
    reddit = init()
    scrape_subreddit(reddit, 'AmericanProblems')

if __name__ == '__main__':
    main()
