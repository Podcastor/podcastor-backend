# -*- coding: utf-8 -*-

from dateutil import parser

from app.core import background

@background.task(bind=True)
def create_episodes_from_podcast(self, podcast_id):
    from app.podcast.models import Podcast

    try:
        podcast = Podcast.objects.get(pk=podcast_id)
        feed_data = podcast.get_feed_data()

        for episode in feed_data['item']:
            create_episode.delay(podcast_id, episode)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=30)

@background.task(bind=True)
def create_episode(self, podcast_id, episode_data):
    from app.podcast.models import Podcast, Episode

    try:
        podcast = Podcast.objects.get(pk=podcast_id)
        episode = Episode.objects.create(
            podcast=podcast,
            title=episode_data['title'],
            description=episode_data['description'],
            audio_link=episode_data["enclosure"]["@url"],
            link=episode_data['link'],
            pub_date=parser.parse(episode_data['pubDate'])
        )
    except Exception as exc:
        raise self.retry(exc=exc, countdown=30)
