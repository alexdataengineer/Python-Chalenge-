import hashlib
import os
import time
from typing import Dict, Any, Generator, List

import requests
from dotenv import load_dotenv


def _build_auth_params(public_key: str, private_key: str) -> Dict[str, str]:
    ts = str(int(time.time()))
    to_hash = ts + private_key + public_key
    md5_hash = hashlib.md5(to_hash.encode("utf-8")).hexdigest()
    return {"ts": ts, "apikey": public_key, "hash": md5_hash}


def _get_keys() -> tuple[str, str]:
    # Hardcoded API keys for testing purposes
    public_key = "your_public_key_here"
    private_key = "your_private_key_here"
    
    # Alternative: try to load from environment first, fallback to hardcoded
    try:
        load_dotenv()
        env_public = os.getenv("PUBLIC_KEY")
        env_private = os.getenv("PRIVATE_KEY")
        if env_public and env_private:
            return env_public, env_private
    except:
        pass
    
    if public_key == "your_public_key_here" or private_key == "your_private_key_here":
        raise RuntimeError("Please replace 'your_public_key_here' and 'your_private_key_here' with your actual Marvel API keys")
    
    return public_key, private_key


def get_characters(limit: int = 5, name_starts_with: str | None = None, offset: int = 0) -> Dict[str, Any]:
    public_key, private_key = _get_keys()
    base_url = "https://gateway.marvel.com/v1/public/characters"
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if name_starts_with:
        params["nameStartsWith"] = name_starts_with
    params.update(_build_auth_params(public_key, private_key))

    response = requests.get(base_url, params=params, timeout=20)
    response.raise_for_status()
    return response.json()


def iter_all_characters(name_starts_with: str | None = None, page_size: int = 100, max_items: int | None = None) -> Generator[Dict[str, Any], None, None]:
    fetched = 0
    offset = 0
    while True:
        data = get_characters(limit=page_size, name_starts_with=name_starts_with, offset=offset)
        results: List[Dict[str, Any]] = data.get("data", {}).get("results", [])
        total = data.get("data", {}).get("total", 0)
        if not results:
            break
        for item in results:
            yield item
            fetched += 1
            if max_items is not None and fetched >= max_items:
                return
        offset += page_size
        if offset >= total:
            break


def get_character_comics(character_id: int, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    public_key, private_key = _get_keys()
    base_url = f"https://gateway.marvel.com/v1/public/characters/{character_id}/comics"
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    params.update(_build_auth_params(public_key, private_key))

    response = requests.get(base_url, params=params, timeout=20)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = get_characters(limit=3)
    for result in data.get("data", {}).get("results", []):
        print(f"- {result.get('name')}")


