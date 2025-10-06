import time


def rate_limit_delay():
    time.sleep(1)


def validate_anime_search_result(result):
    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0
    
    for anime in result:
        validate_anime_search_item(anime)


def validate_anime_search_item(anime):
    assert isinstance(anime, dict)
    
    expected_keys = {'id', 'title', 'coverImage', 'averageScore', 'popularity', 'episodes', 'season', 'hashtag', 'isAdult'}
    actual_keys = set(anime.keys())
    assert actual_keys == expected_keys, f"Expected keys {expected_keys}, got {actual_keys}"
    
    assert isinstance(anime['title'], dict)
    title_keys = set(anime['title'].keys())
    assert title_keys == {'romaji', 'english'}, f"Title expected keys {{'romaji', 'english'}}, got {title_keys}"
    
    assert isinstance(anime['coverImage'], dict)
    cover_keys = set(anime['coverImage'].keys())
    assert cover_keys == {'large'}, f"CoverImage expected keys {{'large'}}, got {cover_keys}"


def validate_manga_search_result(result):
    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0
    
    for manga in result:
        validate_manga_search_item(manga)


def validate_manga_search_item(manga):
    assert isinstance(manga, dict)
    
    expected_keys = {'id', 'title', 'coverImage', 'averageScore', 'popularity', 'chapters', 'volumes', 'season', 'hashtag', 'isAdult'}
    actual_keys = set(manga.keys())
    assert actual_keys == expected_keys, f"Expected keys {expected_keys}, got {actual_keys}"
    
    assert isinstance(manga['title'], dict)
    title_keys = set(manga['title'].keys())
    assert title_keys == {'romaji', 'english'}, f"Title expected keys {{'romaji', 'english'}}, got {title_keys}"
    
    assert isinstance(manga['coverImage'], dict)
    cover_keys = set(manga['coverImage'].keys())
    assert cover_keys == {'large'}, f"CoverImage expected keys {{'large'}}, got {cover_keys}"


def validate_character_search_result(result):
    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0
    
    for character in result:
        validate_character_search_item(character)


def validate_character_search_item(character):
    assert isinstance(character, dict)
    
    expected_keys = {'id', 'name', 'image'}
    actual_keys = set(character.keys())
    assert actual_keys == expected_keys, f"Expected keys {expected_keys}, got {actual_keys}"
    
    assert isinstance(character['name'], dict)
    name_keys = set(character['name'].keys())
    assert name_keys == {'first', 'last'}, f"Name expected keys {{'first', 'last'}}, got {name_keys}"
    
    assert isinstance(character['image'], dict)
    image_keys = set(character['image'].keys())
    assert image_keys == {'large'}, f"Image expected keys {{'large'}}, got {image_keys}"


def validate_anime_by_id_result(result):
    assert result is not None
    assert isinstance(result, dict)
    
    expected_keys = {'name_romaji', 'name_english', 'starting_time', 'ending_time', 'cover_image', 'banner_image', 'airing_format', 'airing_status', 'airing_episodes', 'season', 'description', 'average_score', 'genres', 'next_airing_ep'}
    actual_keys = set(result.keys())
    assert actual_keys == expected_keys, f"Expected keys {expected_keys}, got {actual_keys}"


def validate_manga_by_id_result(result):
    assert result is not None
    assert isinstance(result, dict)
    
    expected_keys = {'name_romaji', 'name_english', 'starting_time', 'ending_time', 'cover_image', 'banner_image', 'release_format', 'release_status', 'chapters', 'volumes', 'desc', 'average_score', 'genres'}
    actual_keys = set(result.keys())
    assert actual_keys == expected_keys, f"Expected keys {expected_keys}, got {actual_keys}"


def validate_character_by_id_result(result):
    assert result is not None
    assert isinstance(result, dict)
    
    expected_keys = {'first_name', 'last_name', 'native_name', 'description', 'image'}
    actual_keys = set(result.keys())
    assert actual_keys == expected_keys, f"Expected keys {expected_keys}, got {actual_keys}"