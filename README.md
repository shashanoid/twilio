# Twitter for Asyncy

![Asyncy container](https://img.shields.io/badge/asyncy_container-ready-brightgreen.svg?style=for-the-badge)
[![Docker Build Status](https://img.shields.io/docker/build/asyncy/asyncy-twitter.svg?style=for-the-badge)](https://hub.docker.com/r/asyncy/asyncy-twitter/)
![Docker Stars](https://img.shields.io/docker/stars/asyncy/asyncy-twitter.svg?style=for-the-badge)

Do Twitter stuff from Asyncy!

This container adds Twitter support to Asyncy, so that you can write in story
things like:

```
twitter tweet 'What a wonderful world!'
```

To use this container properly you need Twitter OAuth tokens from the application
management center.

## Available commands

### Follow
```python
# follows an user
twitter follow "handle"
```

### Followers

```python
# list an user's followers
followers_list = twitter followers "handle"
```

### Retweet

```python
# retweet specified tweet
twitter retweet tweet_id
```

### Tweet

```python
# tweets a message
twitter tweet "message"
```

## Environment

Requires environment variables:

 - CONSUMER_KEY
 - CONSUMER_SECRET
 - ACCESS_TOKEN
 - ACCESS_TOKEN_SECRET
