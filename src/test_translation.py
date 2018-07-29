'''
Created on Dec 17, 2017

'''
import unittest
from secret import consumer_key, access_token, consumer_secret,\
    access_token_secret
from tweet_translation import tweetTranslation, screenname, language,\
    translateTextFile, getTweets
from tweet_translation import api

class TestTranslation(unittest.TestCase):

# Test to make sure consumer_key is not NULL
# Passes
    def test_ConsumerKey(self):
        self.assertIsNotNone(consumer_key, msg=None)
       
# Test to make sure access_token is not NULL
# Passes
    def test_AccessToken(self):
        self.assertIsNotNone(access_token, msg=None)
   
# Test to make sure consumer_secret is not NULL
# Passes
    def test_ConsumerSecret(self):
        self.assertIsNotNone(consumer_secret, msg=None)
   
# Test to make sure access_token_secret is not NULL
# Passes
    def test_Access_Token_Secret(self):
        self.assertIsNotNone(access_token_secret, msg=None)
  
# Test to make sure screenname is not NULL
# Passes
    def test_Screenname(self):
        self.assertIsNotNone(screenname, msg=None)
         
# Test to make sure language is Spanish
# Passes
    def test_Langauge(self):
        self.assertIs(language, 'es')

# # Test to confirm that the translateTextFile function has no return value
# Passes
    def test_translateTextFile(self):
        result = translateTextFile("source-tweet.txt", 'es', "translation.txt")
        self.assertIsNone(result)
     
# Test to confirm that tweetTranslation function has no return value
# Passes
    def test_tweetTranslation(self):
        result = tweetTranslation("translation.txt")
        self.assertIsNone(result)
         
# Test to see if API works
    def test_IfAPIWorks(self):
        self.assertIsNotNone(api, "API should not be null")

# Test to see if getTweets is NULL 
    def testIfGetTweetsIsNone(self):
        self.assertIsNotNone(getTweets('justinbieber', 1, True), "Should not be null")
 
# Test to see if getTweets sends correct message       
    def testIfGetTweetsSendsCorrectMessage(self):
        message = "method worked properly"
        self.assertEquals(message, getTweets('ArianaGrande', 1, False), "Messages should be the same")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
