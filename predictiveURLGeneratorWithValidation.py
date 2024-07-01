import base64
import re


def decode_id(encoded_id):
    try:
        return int(base64.b64decode(encoded_id).decode())
    except (base64.binascii.Error, ValueError) as e:
        print(f"Error decoding ID: {e}")
        return None


def encode_id(episode_id):
    try:
        return base64.b64encode(str(episode_id).encode()).decode()
    except Exception as e:
        print(f"Error encoding ID: {e}")
        return None


def extract_id(url):
    match = re.search(r'\?id=([^&]+)', url)
    if match:
        return match.group(1)
    return None


def generate_episode_urls(base_url, known_urls, start_episode, end_episode):
    # Validate inputs
    if not base_url:
        raise ValueError("Base URL is empty. Please provide a valid base URL.")
    if not known_urls or not all(known_urls):
        raise ValueError("One or more known URLs are empty. Please provide valid known URLs.")
    if start_episode <= 0 or end_episode <= 0 or end_episode < start_episode:
        raise ValueError("Invalid episode range. Please provide a valid start and end episode.")

    # Extract and decode the IDs from the known URLs
    decoded_ids = []
    for url in known_urls:
        encoded_id = extract_id(url)
        if encoded_id:
            decoded_id = decode_id(encoded_id)
            if decoded_id is not None:
                decoded_ids.append(decoded_id)
            else:
                raise ValueError(f"Failed to decode ID from URL: {url}")
        else:
            raise ValueError(f"Failed to extract ID from URL: {url}")

    if not decoded_ids:
        raise ValueError("No valid IDs found in known URLs.")

    # Calculate the base ID (assume the first known URL is for the first episode)
    base_id = decoded_ids[0] - known_urls.index(known_urls[0])

    urls = []
    for episode in range(start_episode, end_episode + 1):
        episode_id = base_id + (episode - 1)
        encoded_id = encode_id(episode_id)
        if encoded_id:
            url = f"{base_url}?id={encoded_id}"
            urls.append((episode, url))
        else:
            raise ValueError(f"Failed to encode ID for episode {episode}")

    return urls


# Base URL for the Link
base_url = ""

# Known URLs (example inputs)
known_urls = [
    "",  # 1
    "",  # Link 2
    "",  # Link 3
    ""  # Link 9
]

# Specify the range of episodes
start_episode = 1
end_episode = 12

try:
    # Generate the URLs
    episode_urls = generate_episode_urls(base_url, known_urls, start_episode, end_episode)

    # Print the URLs
    for episode, url in episode_urls:
        print(f"EPISODE {episode} URL: {url}")
except ValueError as e:
    print(f"Error: {e}")
