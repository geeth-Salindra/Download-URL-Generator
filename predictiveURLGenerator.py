import base64
import re

def decode_id(encoded_id):
    return int(base64.b64decode(encoded_id).decode())

def encode_id(episode_id):
    return base64.b64encode(str(episode_id).encode()).decode()

def extract_id(url):
    match = re.search(r'\?id=([^&]+)', url)
    if match:
        return match.group(1)
    return None

def generate_episode_urls(base_url, known_urls, start_episode, end_episode):
    # Extract and decode the IDs from the known URLs
    decoded_ids = [decode_id(extract_id(url)) for url in known_urls]
    # Calculate the base ID (assume the first known URL is for the first episode)
    base_id = decoded_ids[0] - (known_urls.index(known_urls[0]))

    urls = []
    for episode in range(start_episode, end_episode + 1):
        episode_id = base_id + (episode - 1)
        encoded_id = encode_id(episode_id)
        url = f"{base_url}?id={encoded_id}"
        urls.append((episode, url))
    return urls

# Base URL for the link
base_url = "link"

# Known URLs (example inputs)
known_urls = [
    "", # link 1
    "", # link 2
    "", # linke 3
    ""  # link 9
]

# Specify the range of episodes
start_episode = 1
end_episode = 12

# Generate the URLs
episode_urls = generate_episode_urls(base_url, known_urls, start_episode, end_episode)

# Print the URLs
for episode, url in episode_urls:
    print(f" EPISODE {episode} URL: {url}")
