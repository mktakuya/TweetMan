#!/usr/bin/env python
# coding:utf-8
import unittest
from datetime import datetime
from tweetman import TweetMan
import testsettings

tweet = """{0}
Tweet Man {1} test."""

class TweetManTest(unittest.TestCase):
    def setUp(self):
        self.tweetman = TweetMan(testsettings.CONSUMER_KEY,
                testsettings.CONSUMER_SECRET, testsettings.ACCESS_TOKEN,
                testsettings.ACCESS_TOKEN_SECRET)

    def create_tweetman_test(self):
        self.assertTrue(self.tweetman)

    def test_send_tweet(self):
        now = datetime.now()
        now = now.strftime('%Y/%m/%d %H:%M:%S')
        self.tweetman.send_tweet(tweet.format(now, 'send_tweet'))

if __name__ == '__main__':
    unittest.main()

